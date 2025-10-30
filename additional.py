import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#preprocessing / cleaning the data for additional use / figures. 
#Taken from main.py file and the tutorial. 
dataframe = pd.read_csv('Zomato-data-.csv')


def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)

#print(dataframe.head())
#dataframe.info()
#print(dataframe.isnull().sum())

# New Questions:
# - How many restaurants allow you to book a table?
# - What types of restaurants allow you to book a table?
# - Do restaurants that allow you to book tables have higher ratings?
# - Is there a correlation between higher ratings and restaurants that allow you to book a table?

# How many restaurats allow you to book a table?

plt.figure(1)
sns.countplot(x = dataframe['book_table'], color='green')
plt.title("Restaurants that allow reservations")
plt.xlabel("Allows Reservations")
plt.ylabel('')

#function to change the book_table values from 'Yes' to 1 and 'No' to 0. 
def handleBooking(value):
    if(value == 'Yes'):
        value = 1
    elif(value == 'No'):
        value = 0
    return int(value)

dataframe['book_table']=dataframe['book_table'].apply(handleBooking)

# What types of restaurants allow you to book a table?
plt.figure(2)

#I want to get just the restauruants where 'book_table' is 1. 
restAndBooking = dataframe[["listed_in(type)","book_table"]]
rest_allow_booking = restAndBooking[restAndBooking["book_table"] == 1]

sns.countplot(data = rest_allow_booking, x='listed_in(type)')
plt.title('# of restaurant types that allow booking')
plt.ylabel('# of restaurants')
plt.xlabel('types of restaurants')

# - Do restaurants that allow you to book tables have higher ratings?
# Now we are oging to look at rest_allow_booking and examine their ratings, then we will compare it to restaurants that dont allow bookings. 

rest_disallow_booking = restAndBooking[restAndBooking["book_table"] == 0]

plt.figure(3)
sns.countplot(data = rest_disallow_booking, x='listed_in(type)')
plt.title('# of restaurant types that dont allow booking')
plt.ylabel('# of restaurants')
plt.xlabel('types of restaurants')

plt.show()