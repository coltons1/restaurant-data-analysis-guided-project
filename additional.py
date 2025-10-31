import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

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
# Now we are going to look at rest_allow_booking and examine their ratings, then we will compare it to restaurants that dont allow bookings. 

rest_disallow_booking = restAndBooking[restAndBooking["book_table"] == 0]

plt.figure(3)
sns.countplot(data = rest_disallow_booking, x='listed_in(type)')
plt.title('# of restaurant types that dont allow booking')
plt.ylabel('# of restaurants')
plt.xlabel('types of restaurants')

type_booking_rating = dataframe[["listed_in(type)", "book_table", "rate"]]
allow_booking_and_ratings = type_booking_rating[type_booking_rating["book_table"] == 1]
#print(allow_booking_and_ratings)

#box plot showing the range of ratings that DO allow bookings
plt.figure(4)
sns.boxplot(data=allow_booking_and_ratings, x=allow_booking_and_ratings["listed_in(type)"], y=allow_booking_and_ratings["rate"])
plt.title('ratings of restaurants that accept bookings')
plt.xlabel('types of restaurants')
plt.ylabel('ratings')

#box plot showing the range of ratings for those that DO NOT allow bookings
disallow_booking_and_ratings = type_booking_rating[type_booking_rating["book_table"] == 0]
plt.figure(5)
sns.boxplot(data=disallow_booking_and_ratings, x=disallow_booking_and_ratings["listed_in(type)"], y=disallow_booking_and_ratings["rate"])
plt.title('ratings of restaurants that dont accept bookings')
plt.xlabel('types of restaurants')
plt.ylabel('ratings')

#next we will show the means between the different ranges broken down by category. 

#means of types of restaurants that allow booking
cafesThatBook_ratings = allow_booking_and_ratings[allow_booking_and_ratings['listed_in(type)'] == "Cafes"]
buffetThatBook_ratings = allow_booking_and_ratings[allow_booking_and_ratings['listed_in(type)'] == "Buffet"]
diningThatBook_ratings = allow_booking_and_ratings[allow_booking_and_ratings['listed_in(type)'] == "Dining"]
otherThatBook_ratings = allow_booking_and_ratings[allow_booking_and_ratings['listed_in(type)'] == "other"]

cafeBookMean = cafesThatBook_ratings['rate'].mean()
buffetBookMean = buffetThatBook_ratings['rate'].mean()
diningBookMean = diningThatBook_ratings['rate'].mean()
otherBookMean = otherThatBook_ratings['rate'].mean()

cafesNoBooking_ratings = disallow_booking_and_ratings[disallow_booking_and_ratings['listed_in(type)'] == "Cafes"]
buffetNoBooking_ratings = disallow_booking_and_ratings[disallow_booking_and_ratings['listed_in(type)'] == "Buffet"]
diningNoBooking_ratings = disallow_booking_and_ratings[disallow_booking_and_ratings['listed_in(type)'] == "Dining"]
otherNoBooking_ratings = disallow_booking_and_ratings[disallow_booking_and_ratings['listed_in(type)'] == "other"]

cafeNoBookMean = cafesNoBooking_ratings['rate'].mean()
buffetNoBookMean = buffetNoBooking_ratings['rate'].mean()
diningNoBookMean = diningNoBooking_ratings['rate'].mean()
otherNoBookMean = otherNoBooking_ratings['rate'].mean()

BookingMeanData = {
    'Cafes' : [cafeBookMean, cafeNoBookMean],
    'Buffet': [buffetBookMean, buffetNoBookMean],
    'Dining': [diningBookMean, diningNoBookMean],
    'Other' : [otherBookMean, otherNoBookMean]
}

bMD = pd.DataFrame(BookingMeanData)
bMD = bMD.rename(index={0: 'Allows Booking Means'})
bMD = bMD.rename(index={1: 'Disallows Booking Means'})
bMD = bMD.round(3)
print(bMD)

plt.show()