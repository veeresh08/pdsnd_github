import time
import pandas as pd
import numpy as np


CityData = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    """
    
    invalid_inputs = "Input is invalid try again" 
    
    print(' Hey !! Lets Explore US Bikeshare data')
    # get's  user input for city .
    while 1 == 1 :
        city = raw_input("\nplease Enter the name of as Follows\nchicago,\nnew york,\nwashington. \n").lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print(invalid_inputs)
    
    # Get's user input for month (all, january, february, ... , june)
    while 1 == 1 :
        month = raw_input("\nPlease Enter Name of month as follow \njanuary,\nfebruary,\nmarch,"
            "\napril,\nmay,\njune\nto filter by, or \"all\" to apply no month filter\n").lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print(invalid_inputs)

    # It gets user input in day of week (all, monday, tuesday, ... sunday)
    while 1 == 1 :
        day = raw_input("\nPlease enter Name of day\nmonday,\ntuesday,\nwednesday,\nthursday,"
            "\nfriday,\nsaturday,\nsunday\nof week to filter by, or \"all\" to apply no day filter\n").lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print(invalid_inputs)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    TO Do: Loading data for the specific city and filter it in month and day if applied 
    
    """
    file_name = CityData[city]
    print ("Accessgn data from: " + file_name)
    df = pd.read_csv(file_name)

    # It converts start time colum to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

    # filter's in month if applied
    if month != 'all':
        # Extracting month and day of week 
        df['month'] = df['Start Time'].dt.month

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filtering by month
        df = df.loc[df['month'] == month]

    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # Filtering by day of the week to create the new DF(dataframe)
        df = df.loc[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Display's Statestic's on most frequent time"""

    print('\n The Most Frequent Times of traveling . . . \n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

    month = df['Start Time'].dt.month
    weekday_name = df['Start Time'].dt.weekday_name
    hour = df['Start Time'].dt.hour
   
    most_common_month = month.mode()[0]
    print('The Most Common Month is : ', most_common_month)

     most_common_day_of_week = weekday_name.mode()[0]
    print(' The Most Common Day Of Week: is ', most_common_day_of_week)

    common_start_hour = hour.mode()[0]
    print('Most frequent start hour: ', common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displaying stat's on most popular stations and trip."""

    print('\n The Popular Station and Trip...\n')
    start_time = time.time()

    print('Most commonly used start station:', df['Start Station'].value_counts().idxmax())

    print('Most commonly used end station:', df['End Station'].value_counts().idxmax())

    combine_stations = df['Start Station'] + "*" + df['End Station']
    common_station = combine_stations.value_counts().idxmax()
    print('Frequent combinations is"\n{} \nto\n{}'.format(common_station.split('*')[0], common_station.split('*')[1]))
    print('-'*40)

def trip_duration_stats(df):
    """Displaying stat's  on total and average trip duration."""
    print('\n Calculating Duration\n')
    start_time = time.time()
    # Convert seconds to readable time format converting seconds in understandable Format
    def secs_to_readable_time(seconds):
        m, s = divmod(seconds,60)
        h, m = divmod(m,60)
        d, h = divmod(h,24)
        y, d = divmod(d,365)
        print('Years: {}, Days: {}, Hours: {}, Mins: {}, Secs: {}'.format(y,d,h,m,s))
 
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:\n')
    secs_to_readable_time(total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: {} seconds'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displaing stat's of bike sharing users ."""

    print('\nCalculating.... \n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)
   
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\n earliest year of birth: " + str(earliest_birth_year))
        print("\n most recent year of birth: " + str(most_recent_birth_year))
        print("\n most common year of birth: " + str(common_birth_year))

    print("\ntime %s second took." % (time.time() - start_time))    
    print('-'*40)

def raw_data(df):
    user_input = raw_input('Do you like  to see  data? Enter [yes] or [no].\n')
    line_number = 0

    while 1 == 1 :
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = raw_input('\n Do you like to see more data? Enter [yes] or [no] .\n')
        else:
            break    

def main():
    while 1 == 1 :
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = raw_input('\n Do you want to restart? Enter [yes] or [no] .\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
