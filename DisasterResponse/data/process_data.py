import sys
import pandas as pd
import numpy as np
import re
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    load the message data and the catetoreis data,
    merge the two dataset

    Args:
        messages_filepath: file path of message.csv
        categories_filepath: file path of categories.csv

    Returns:
        A DataFrame that merges the message data and the category data
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, on = 'id')
    return df


def clean_data(df):
    """
    split categories into separate category columns, each of which
    is a category variable with 0 and 1

    Args:
        df: a dataframe with all categories in one column

    Returns:
        A dataframe in which each category has one column representing
        if the message belongs to the category or not
    """

    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand = True)
    row = categories.iloc[0, :]
    category_colnames = row.str.replace("-[0-9]", "", regex = True)
    categories.columns = category_colnames

    # convert category values to 0 and 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x[-1])
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column], errors = 'ignore')

    # replace categories column in df with the new category columns
    df.drop(labels = 'categories', axis = 1, inplace = True)
    df = pd.concat([df, categories], axis = 1)

    # drop the data that have "related" category value equal 2
    df = df[df['related'] != 2]
    # drop duplicates
    df.drop_duplicates(inplace = True)

    return df



def save_data(df, database_filename):
    """Save the cleaned dataset into an sqlite database"""
    engine = create_engine('sqlite:///' + database_filename)
    table = database_filename.replace(".db", "").replace("data/", "")
    df.to_sql(table, engine, index=False, if_exists = 'replace')

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
