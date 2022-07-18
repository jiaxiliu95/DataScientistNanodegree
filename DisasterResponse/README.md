# Disaster Response Classification

## Table of Contents
- [Installation](#Installation)
- [Project Motivation](#ProjectMotivation)
- [File Descriptions](#FileDescriptions)
- [Instructions](#Instructions)
- [Acknowledgments](#Acknowledgments)
## Installation
The project used Python and HTML. The necessary libraries to run the code can be found in the requirements.txt file.
## Project Motivation
Disaster organizations need to filter and pull out the relevant and most important messages from millions of messages following a disaster. Then the reflected problems are assigned to different professionals/organizations to take care of, such as water, medical and so on. 

The project trained a classifier using the historical messages taken after disasters and the categories that the messages belong to. The classifier can predict the categories that a new message most likely belongs to for disaster response.
## File Descriptions
The structure of the project and the file descriptions are as follows.
- [app](app)
	- [template](app/template)
		- [master.html](app/template/master.html) : main page of web app
		- [go.html](app/template/go.html) : classification result page of web app
	- [run.py](app/run.py) : Flask file that runs the app
	- [img](app/img) : include the images shown on the web page
- [data](data)
	- [disaster_categories.csv](data/disaster_categories.csv) : categories data to process
	- [disaster_messages.csv](data/disaster_messages.csv) : messages data to process
	- [process_data.py](data/process_data.py) : file that processes the data
	- [DisasterResponse.db](data/DisasterResponse.db) : database that stores clean data
- [models](models)
	- [train_classifier.py](models/train_classifier.py) : file that trains the classifier using cleaned data
- [ETL Pipeline Preparation.ipynb](ETLPipelinePreparation.ipynb) : development process of process_data.py
- [ML Pipeline Preparation.ipynb](MLPipelinePreparation.ipynb) : development process of train_classifier.py
- [requirements.txt](requirements.txt) : All  required libraries to run the code for this project
- [README.md](README.md)

## Instructions
1. To process the data and train the model, run the following commands in the project's root directory.
	- Run the ETL pipeline to process the data and store the cleaned data in the Sqlite database: `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
	- Run the ML pipeline to train and save the classifier: `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
2. To run the web app, run the following command in the `app` directory: `python run.py`

## Screenshot of the Web App
1. Before typing in anything, the main page shows three visualizations that provides an overview of the training dataset.

<img src="app/img/overview1.png" alt="drawing" width="700"/>

<img src="app/img/overview2.png" alt="drawing" width="700"/>

<img src="app/img/overview3.png" alt="drawing" width="700"/>

2. To classify a new message, type in search box and click the "Classify Message" button. 

<img src="app/img/predict.png" alt="drawing" width="700"/>

The predicted categories are highlighted.

<img src="app/img/results.png" alt="drawing" width="700"/>

## Acknowledgments
The disaster data are from [Appen](https://appen.com/#data_for_ai). The skeleton code for this web app is provided by [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).
