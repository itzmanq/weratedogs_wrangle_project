import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    
    while True:
        city = input('Would you like to analyze data for Chicago, New York City or Washington?: ').lower()
        if city in cities:
            break
        else:
            print('\nPlease enter a valid city\n')
       
        
         # get user input for month (all, january, february, ... , june)
            
    while True:
        month = input('Would you like to analyze data by month? Enter January, February, March, April, May, June\n You can enter "All" to analyze all months: ').lower()
        if month in months:
            break 
        else:
            print('\nPlease enter a valid month')
        
         # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to analyze data by day? Enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n You can enter "All" to analyze all days: ').lower()
        if day in days:
            break
        else:
            print('\nPlease enter a valid day')

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
    
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['Month']==month]
        
    if day != 'all':
        df = df[df['Day_of_Week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month = months[most_common_month - 1]
    print('The most common month is {}'.format(most_common_month).title())


    # display the most common day of week
    most_common_day = df['Day_of_Week'].mode()[0]
    print('The most common day is {}'.format(most_common_day).title())

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Hour'].mode()[0]
    print('The most common Hour is {}'.format(most_common_hour).title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(most_common_start_station))


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(most_common_end_station))


    # display most frequent combination of start station and end station trip
    df['Start to End Station'] = df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
    most_common_ste_station = df['Start to End Station'].mode()[0]
    print('The most frequent combination of start to end station is {}'.format(most_common_ste_station).title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum().sum().round(2)
    print('The total travel time is {}'.format(total_travel_time).title())


    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('The average travel time is {}'.format(avg_travel_time).title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('the number of sunscribers and customers are: \n{}'.format(user_type_count).title())
    
    
    print('-'*40)

    # Display counts of gender
    city = ['Chicago', 'New York City', 'Washington']
    try:
        if city != 'Washington':
            gender_count = df['Gender'].value_counts()
            print('The number of males and females are:\n {}'.format(gender_count).title())
        else:
            print('The city you are analyzing has no gender')
    except:
        print('The city you are analyzing has no gender')


    # Display earliest, most recent, and most common year of birth
    try:
        if city != 'Washington':
            earliest_birth_year = df['Birth Year'].min()
            print('The earliest birth year is {}'.format(earliest_birth_year).title())
            most_recent_birth_year = df['Birth Year'].max()
            print('\nThe most recent birth year is {}'.format(earliest_birth_year).title())
            most_common_birth_year = df['Birth Year'].mode()
            print('\nThe most common birth year is {}'.format(earliest_birth_year).title())
       
        else:
            print('The city you are analyzing has no birth year')
    except:
        print('The city you are analyzing has no birth year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    """Displays 5 rows of bikeshare data at a time."""
    
    print('\nDisplaying 5 rows of data...\n')
    start_time = time.time()
    
    while True:
        input_data = input('Would you like to view raw data?\n Please enter "yes" or "no": ').lower()
        if input_data == 'yes':
            data_length = len(df.index)
            start_loc = 0
            end_loc = 5
            
            while start_loc < 5:
                row_data = df.iloc[0:5]
                print(row_data)
                start_loc += 5
                end_loc += 5
                view_display = input("Do you wish to continue?: ").lower()
                if view_display == 'yes':
                    start_loc += 5
                    end_loc += 5
                    next_row_data = df.iloc[start_loc:end_loc]
                    print(next_row_data)
                    view_display = input("Do you wish to continue?: ").lower()
                elif view_display == 'no':
                    print('Thank you')
                    break
                else:
                    print('\nPlease enter a valid response')
                
                        
        elif input_data == 'no':
            break
        else:
            print('\nPlease enter a valid response')
            
            
            
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
