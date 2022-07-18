import sys
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'stopwords'])

import re
import numpy as np
import pandas as pd
import pickle
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def load_data(database_filepath):
    """
    Load data from database

    Args:
        database_filepath: path of the database

    Returns:
        X: input text data, messages
        Y: output variable, categories
        categories: category names
    """

    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql('SELECT * FROM DisasterResponse', engine)
    X = df['message'].values
    Y = df.iloc[:, 4:].values
    categories = df.columns[4:]

    return X, Y, categories


def tokenize(text):
    """process text data"""

     # normalization
    text = text.lower() # capitalization removal
    text = re.sub(r"[^a-z0-9]", " ", text) # punctuation removal

    # tokenization

    tokens = word_tokenize(text)
    # lemmatization
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok)
        clean_tokens.append(clean_tok)
    return clean_tokens


def build_model():
    """Build and return a machine learning model"""

    # pipeline
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer = tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    # grid of parameters to tune
    parameters = {'clf__estimator__n_estimators': [50, 100],
             'clf__estimator__min_samples_split': [2, 5, 10]}

    cv = GridSearchCV(pipeline, param_grid = parameters, scoring = 'f1_micro')
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    """Evaluate the model on the test data and print the results"""

    y_pred = cv.predict(X_test)
    print(classification_report(y_test, y_pred, target_names = categories))

def save_model(model, model_filepath):
    """Export the trained model as a pickle file"""

    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
