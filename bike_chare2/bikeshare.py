import time
import pandas as pd
import numpy as np 
import os

#for change working directory to in this file 
os.chdir(os.path.dirname(os.path.abspath(__file__)))


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

list_city=["chicago","washington","new york city"]
list_month = ['january', 'february', 'march', 'april', 'may', 'june']
list_day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']
filter_by=["both","month","day","non"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city=input("would you like to see data for => 'chicago' , 'new york city' , 'washington' \n ").lower()
        if city in list_city :
            break
        else:        
            print("Invalid inputs try again...!")
            continue
            
    #filter dateby month,day,both,or not at all
    while True:
        filt=input("whould you like filter the date by month,day,both,or non ? \n").lower()
        if filt in filter_by:
            break
        else:
            print("Invalid inputs try again...!")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)

    if filt == "month" or filt=="both":
        while True:
            month=input("which month? january,february,march,april,may,or june \n ").lower()
            if month in list_month:
                break
            else:
                print("Invalid inputs try again...!")
                continue

    if filt == "day" :
        month="all"



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    if filt == "day" or filt=="both":
        while True:
            day=input("which day ? please your response like monday, tuesday, ... sunday \n").lower()
            if day in list_day:
                break
            else:
                print("Invalid inputs try again...!")
                continue

    if filt == "month" :
        day="all"



    #no filter the data 
    if  filt=="non" :
        day="all"
        month="all"

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]


    # filter by day of week if applicable
    if day != 'all':

        # use the index of day list to get the corresponding int
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print("the most common month : ",df["month"].mode()[0] ,"\n")

    # TO DO: display the most common day of week

    print("the most common day of week : ",df["day_of_week"].mode()[0],"\n")

    # TO DO: display the most common start hour

    print("the most common start hour: ",df['hour'].mode()[0],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("most commonly used start station: ",df["Start Station"].mode()[0],"\n")

    # TO DO: display most commonly used end station

    print("most commonly used end station: ",df["End Station"].mode()[0],"\n")

    # TO DO: display most frequent combination of start station and end station trip

    print("most frequent combination of start station and end station : from ",(df["Start Station"] + "to" + df["End Station"]).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print("total travel time [",df["Trip Duration"].sum(),"] seconds \n")

    # TO DO: display mean travel time

    print("total travel time [",df["Trip Duration"].mean(),"] seconds \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if "Birth day" in df.columns :
        # TO DO: Display counts of user types
        print("counts of user types : ",df["User Type"].value_counts(),"\n")
        # TO DO: Display counts of gender
        print("counts of gender : ",df["Gender"].value_counts(),"\n")
    else:
        print("sorry column is not exist \n")


    if "Gender" in df.columns :
        # TO DO: Display earliest, most recent, and most common year of birth
        print("most earliest : ",df["Birth Year"].max(),"\n")
        print("most recent : ",df["Birth Year"].min(),"\n")
        print("most popular year : ",df["Birth Year"].mode()[0],"\n")
    else:
        print("sorry column is not exist \n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def loop_data(df):

    """print 5 row of date"""

    sum=0
    while True:
        trip_data=input("would you like to view individual trip data ? yes or no \n").lower()
        if trip_data =="yes":
            print(df.iloc[sum:sum+5])
            sum=sum+5
            continue
        elif trip_data=="no":
            break
        else:
            print("Invalid inputs try again...! \n ")
            continue
                

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        loop_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":

	main()



