# Analysis of Customer Response to Starbucks Offers

## Table of Contents
- [Installation](#Installation)
- [Project Motivation](#ProjectMotivation)
- [File Descriptions](#FileDescriptions)
- [Instructions](#Instructions)
- [Acknowledgments](#Acknowledgments)
## Installation
The Jupyter Notebook in the repository should be able to work without any issue using Python version 3.. with following libraries installed:
- NumPy
- Pandas
- matplotlib
- scikit-learn
- seaborn
The requirements.txt can be used to set up the environment.
## Project Motivation
Starbucks sends out offers to customers through various media channels to encourage buying. The offers can be discount coupons or  merely advertisements for specific drinks. However, only a proportion of the sent-out offers are viewed and used by the customers before expiration. 

To explore a smarter way to send out offers that gains a higher response rate, a simulation is conducted to mimic customer behavior on the Starbucks offers. The objective is of this project is to analyze the how the demographic characteristics of a customer, as well as the features of the received offer, may affect the way that they react to the offer.
## File Descriptions
The structure of the project and the file descriptions are as follows.
- [data](data)
	- [portfolio.json](data/portfolio.json) : contains meta data about the offers (duration, type, rewards, etc.)
	- [profile.json](data/profile.json) : contains demographic data of the customers (age, gender, income, etc.)
	- [transcript.json](data/transcript.json) : contains all transactions the customers made, all offers that the customers received, viewed and completed.
- [img](img) : contains the visulization results
- [Analysis_of_Customer_Response_to_Starbucks_Offers.ipynb](Analysis_of_Customer_Response_to_Starbucks_Offers.ipynb) : the Jupyter Notebook that performs the analysis
- [requirements.txt](requirements.txt) : All  required libraries to run the code for this project
- [README.md](README.md)
## Results
The project conducts qualitative and quantitative analysis of the customer's response to BOGO, discount and informational offers. The main takeaways are
- BOGO and discount offers are likely to get more response/completion from customers with longer membership, customers with higher income, and older customer groups. 
- Informational offers tend to get more response/completion from customers with longer membership, customers with lower income, and younger customer groups.
- The marginal improvement of the amount spent at Starbucks promoted by the offers is higher for the customers with lower income.

The main findings and the detailed discussion can be found in [this post](https://medium.com/@jiaxi_liu/is-there-a-better-strategy-to-send-out-starbucks-offer-57838bba32c3).

## Acknowledgments
The data for this project is provided by Udacity: [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).
