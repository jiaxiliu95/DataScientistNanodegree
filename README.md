## Table of Contents

- [Installation](#Installation)

- [Project Motivation](#ProjectMotivation)

- [File Descriptions](#FileDescriptions)

- [Results](#Results)

- [Acknowledgments](#Acknowledgments)

## Installation

The necessary libraries to run the code are:

- geopandas
- shapely
- geoplot
- statsmodels.api
- wordcloud

With the above libraries installed, the code in the Jupyter Notebook should be able to work without any issue using Python version 3.*.

## Project Motivation

The target of this project is to provide takeaways we can learn from the data to the Airbnb hosts so that they can better understand the market and their business. This project focused on three questions the Airbnb hosts may be interested in:

1. What does the market look like across neighborhoods in Seattle?
2. What are the best months for the hosts in Seattle?
3. What features of a property/listing may attract more bookings?

Ideas and code for further exploration are also discussed at the end of the project. 

## File Descriptions

There is a notebook file, named "Airbnb-Seattle.ipynb", that includes the whole data analysis process following the guideline of CRISP-DM. You can find the answers to the above three questions following the section titles. The results are reproducible by running the code cells. The markdown cells are used to explain the individual steps and interpret the results.

There is another folder named image. Files in the folder are the visualizations obtained from the code.

## Results

The main findings and detailed discussion can be found at the post here.

## Acknowledgments

The data used in this project is credited to Airbnb. You can find the Licensing for the data and other descriptive information of the dataset at [Kaggle](https://www.kaggle.com/datasets/airbnb/seattle). The shape data that was used to draw the Seattle map is credited to the Seattle government. You can find the data public [here](https://data.seattle.gov/dataset/Census-Tracts-2010/m35x-4p25).