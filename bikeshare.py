import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def choice(prompt, choices=('y', 'n')):
    """Return a valid input from the user given an array of possible answers. Additional Changes for GITHUB project
    """

    while True:
        choice = input(prompt).lower().strip()
        # terminate the program if the input is end
        if choice == 'end':
            raise SystemExit
        # triggers if the input has only one name
        elif ',' not in choice:
            if choice in choices:
                break
        # triggers if the input has more than one name
        elif ',' in choice:
            choice = [i.strip().lower() for i in choice.split(',')]
            if list(filter(lambda x: x in choices, choice)) == choice:
                break

        prompt = ("\nSomething is not right. Please mind the formatting and "
                  "be sure to enter a valid option:\n>")

    return choice

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
    cities = ["Chicago", "New York City", "Washington"]
    months = ["January", "February", "March", "April", "May", "June", "All"]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"]
    
    while True:
        city = input("Which city you would like to explore the bikeshare data for: chicago, new york city, or washington ?")
        if city.title() in cities:
            print("Great !!")
            break
        else:
            print("Sorry, please select again from the following cities: chicago, new york city, washington")
                   

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input("Which month you would like to explore the bikeshare data for: january, february, march, april, may, june or all ?")
        if month.title() in months:
            print("Great !!")
            break
        else:
            print("Sorry, please select again from the following options: january, february, march, april, may, june or all")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week you would like to explore the bikeshare data for: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ?")
        if day.title() in days_of_week:
            print("Great !!")
            break
        else:
            print("Sorry, please select again from the following: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all")

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
    # data loaded into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert start time into datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # separate columns for month, day of the week and hour
    df['months'] = df['Start Time'].dt.month
    df['days_of_week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['months'].mode()[0]
    print("The most common month is", most_common_month)

    # TO DO: display the most common day of week
    most_common_week = df['days_of_week'].mode()[0]
    print("The most common week is", most_common_week)

    # TO DO: display the most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print("The most common hour is", most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print("The most commonly used start station is", Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].mode()[0]
    print("The most commonly used end station is", End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination = df['Start Station'] + ' to ' + df['End Station']
    print('The most common start and end station is', Combination.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User_Type' in df.columns:
        counts_user_types = df['User Type'].value_counts()
        print("The counts of user types is: ")
        for i in range(len(counts_user_types.index.values)):
            print(counts_user_types.index.values[i], ' : ', list(counts_user_types)[i])
    else:
        print("User Type Data is not available")


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print("The counts of gender is: ")
        for i in range(len(counts_gender.index.values)):
            print(counts_gender.index.values[i], ' : ', list(counts_gender)[i])
    else:
        print("Gender data is not available")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        
        earliest_year = df['Birth Year'].min()
        print("The earliest year of birth is", int(earliest_year))
        
        most_recent_year = df['Birth Year'].max()
        print("The most recent year of birth is", int(most_recent_year))
        
        most_common_year = df['Birth Year'].mode()
        print("The most common year of birth is", int(most_common_year))
        
    else:
        print("Birth Year Data is not available")

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df, mark_place):
    """Display 5 line of sorted raw data each time."""

    print("\nYou opted to view raw data.")

    # this variable holds where the user last stopped
    if mark_place > 0:
        last_place = choice("\nWould you like to continue from where you "
                            "stopped last time? \n [y] Yes\n [n] No\n\n>")
        if last_place == 'n':
            mark_place = 0

    # sort data by column
    if mark_place == 0:
        sort_df = choice("\nHow would you like to sort the way the data is "
                         "displayed in the dataframe? Hit Enter to view "
                         "unsorted.\n \n [st] Start Time\n [et] End Time\n "
                         "[td] Trip Duration\n [ss] Start Station\n "
                         "[es] End Station\n\n>",
                         ('st', 'et', 'td', 'ss', 'es', ''))

        asc_or_desc = choice("\nWould you like it to be sorted ascending or "
                             "descending? \n [a] Ascending\n [d] Descending"
                             "\n\n>",
                             ('a', 'd'))

        if asc_or_desc == 'a':
            asc_or_desc = True
        elif asc_or_desc == 'd':
            asc_or_desc = False

        if sort_df == 'st':
            df = df.sort_values(['Start Time'], ascending=asc_or_desc)
        elif sort_df == 'et':
            df = df.sort_values(['End Time'], ascending=asc_or_desc)
        elif sort_df == 'td':
            df = df.sort_values(['Trip Duration'], ascending=asc_or_desc)
        elif sort_df == 'ss':
            df = df.sort_values(['Start Station'], ascending=asc_or_desc)
        elif sort_df == 'es':
            df = df.sort_values(['End Station'], ascending=asc_or_desc)
        elif sort_df == '':
            pass

    # each loop displays 5 lines of raw data
    while True:
        for i in range(mark_place, len(df.index)):
            print("\n")
            print(df.iloc[mark_place:mark_place+5].to_string())
            print("\n")
            mark_place += 5

            if choice("Do you want to keep printing raw data?"
                      "\n\n[y]Yes\n[n]No\n\n>") == 'y':
                continue
            else:
                break
        break

    return mark_place
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        mark_place = 0

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        mark_place = raw_data(df, mark_place)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
