import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# create a data frame from the csv file.
dataframe = pd.read_csv('Zomato-data-.csv')
print(dataframe.head())

# taking the rating, splitting it into a list based on the / character, returning first index of the list as a float. 
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

#applying the handleRate function to all the items in the rate column and reassigning the rate column to these new values. 
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

# displays info about the datafram including data types of the columns and the non-null count of each column. 
dataframe.info()
# shows there are no null items in any column. 
print(dataframe.isnull().sum())


#EXPLORATORY DATA ANALYSIS (creating graphs)

#this section uses seaborn to create a count plot which shows the amount of restauraunts in each type in the listed_in(type) column. 
#'Figure_1.png'
sns.countplot(x = dataframe['listed_in(type)'])
plt.xlabel("Type of Restaurant")
plt.show()


#this section uses mat plot lib and pandas to create a new data frame, grouping each type of restaurant and summing their votes. 
#it then makes a line plot to show the differnce in votes between types
#'Figure_2.png'
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker = 'o')
plt.xlabel('Type of restauruant')
plt.ylabel('Votes')
plt.show()

#create a max_votes dataframe from the votes column and gets the maximum value. 
max_votes = dataframe['votes'].max()
# a variable containing the position in the csv file and name of restauruant with max_votes
restauruant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print(max_votes)
print('Restaurant(s) with the maxiumum votes: ')
print(restauruant_with_max_votes)


#this graph, 'Figure_3.png',  shows the amount of restauruants that take online orders vs those that dont. 
sns.countplot(x=dataframe['online_order'], color='orange')
plt.show()

#this code creates a histogram that shows the distribution of ratings across the restuarants. 
#'Figure_4.png"
plt.hist(dataframe['rate'], bins =5)
plt.title('Ratings Distribution')
plt.show()

#this code shows the approximate cost for two people (in rupees which the data set was collected in)
#'Figure_5.png'
plt.figure()
couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()

#this code creates a box plot that show the ratings for restaurants that have online orders versus offline orders. 
#'Figure_6.png'
plt.figure(figsize=(6,6))
sns.boxplot(x= 'online_order', y='rate', data = dataframe)
plt.show()

#this code creates a pivot table and turns it into a heat map of the frequency of online orders at each type of restaurants
#'Figure_7.png'
plt.figure()
pivot_table = dataframe.pivot_table(index = 'listed_in(type)', columns = 'online_order', aggfunc='size', fill_value = 0)
sns.heatmap(pivot_table, annot = True, cmap = 'YlGnBu', fmt = 'd')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()