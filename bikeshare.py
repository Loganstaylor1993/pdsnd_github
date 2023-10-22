import time
import calendar
import pandas as pd

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ""
    valid_cities = CITY_DATA.keys()
    month = ""
    valid_months = ["all", "january", "february", "march", "april", "may", "june"]
    day = ""
    valid_days = [
        "all",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    print("Hello! Let's explore some US bikeshare data!")

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in valid_cities:
        city = str(
            input("Please select a city (chicago, new york city, washington): ")
        ).lower()
        if city not in valid_cities:
            print("Invalid input")

    # get user input for month (all, january, february, ... , june)
    while month not in valid_months:
        month = str(
            input(
                "Please select a month (january - june). Enter 'all' to include all months: "
            )
        ).lower()
        if month not in valid_months:
            print("Invalid input")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in valid_days:
        day = str(
            input("Please select day of the week. Enter 'all' to include all days: ")
        ).lower()
        if day not in valid_days:
            print("Invalid input")

    print("You've selected:", city, month, day)
    print("-" * 40)
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
    df = pd.read_csv(CITY_DATA[city], parse_dates=["Start Time"])

    # Filter data based on selected month and day
    if month == "all" and day == "all":
        filtered_data = df

    if month == "all" and day != "all":
        day_filter = list(calendar.day_name).index(day.capitalize())
        filtered_data = df[(df["Start Time"].dt.dayofweek == day_filter)]

    if month != "all" and day == "all":
        month_filter = list(calendar.month_name).index(month.capitalize())
        filtered_data = df[df["Start Time"].dt.month == month_filter]

    if month != "all" and day != "all":
        day_filter = list(calendar.day_name).index(day.capitalize())
        month_filter = list(calendar.month_name).index(month.capitalize())
        filtered_data = df[
            (df["Start Time"].dt.month == month_filter)
            & (df["Start Time"].dt.dayofweek == day_filter)
        ]
    return filtered_data


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month formatted
    df["month"] = df["Start Time"].dt.strftime("%B")
    most_common_month = df["month"].value_counts().idxmax()
    print("Most common month:", most_common_month)

    # display the most common day of week formatted
    df["day"] = df["Start Time"].dt.strftime("%A")
    most_common_day = df["day"].value_counts().idxmax()
    print("Most common day:", most_common_day)

    # display the most common start hour formatted
    df["hour"] = df["Start Time"].dt.strftime("%I %p")
    most_common_start_hour = df["hour"].value_counts().idxmax()
    print("Most common start hour:", most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df["Start Station"].value_counts().idxmax()
    print("Most common start station:", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df["End Station"].value_counts().idxmax()
    print("Most common end station:", most_common_end_station)

    # display most frequent combination of start station and end station trip
    df["trip"] = df["Start Station"] + " to " + df["End Station"]
    most_common_trip = df["trip"].value_counts().idxmax()
    print("Most common trip:", most_common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    def days_hours_minutes_seconds(total_seconds):
        days, remainder = divmod(total_seconds, 24 * 60 * 60)
        hours, remainder = divmod(remainder, 60 * 60)
        minutes, seconds = divmod(remainder, 60)
        return int(days), int(hours), int(minutes), int(seconds)
        # print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    average_travel_time = int(df["Trip Duration"].mean())
    days, hours, minutes, seconds = days_hours_minutes_seconds(total_travel_time)
    print(
        "Total travel time:",
        days,
        "Days",
        hours,
        "Hours",
        minutes,
        "Minutes",
        seconds,
        "Seconds",
    )
    # display mean travel time
    minutes, seconds = divmod(average_travel_time, 60)
    print("Average travel time:", minutes, "Minutes", seconds, "Seconds")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_count = df["User Type"].value_counts()
    subscriber_count = user_count["Subscriber"]
    customer_count = user_count["Customer"]
    print("Number of subscribers:", subscriber_count)
    print("Number of non-subscribers:", customer_count)

    # Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        male_count = gender_count["Male"]
        female_count = gender_count["Female"]
        none_count = df["Gender"].isnull().sum()
        print("Male Count:", male_count)
        print("Female Count:", female_count)
        print("None Count:", none_count)
    except KeyError:
        print("No gender data for selected city.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df["Birth Year"].min())
        most_recent_year = int(df["Birth Year"].max())
        most_common_year = int(df["Birth Year"].value_counts().idxmax())
        print("Earliest Birth Year:", earliest_year)
        print("Most Recent Birth Year:", most_recent_year)
        print("Most Common Birth Year:", most_common_year)
    except KeyError:
        print("No birth year data for selected city.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def raw_data(df):
    """Prompts user and displays five rows of raw data."""
    # Prompt the user if they want to see raw data
    raw_data_prompt = input("\nWould you like to see the raw data? Enter yes or no: ")

    # Display raw data if the user wants to see it
    if raw_data_prompt.lower() == "yes":
        # Set initial row index
        row_index = 0

        # Loop until the user doesn't want to see more rows
        while True:
            # Display 5 rows of raw data
            print("\n", df.iloc[row_index : row_index + 5])

            # Update row index
            row_index += 5

            # Prompt the user if they want to see more rows
            show_more = input("\nWould you like to see more rows? Enter yes or no: ")

            # Break the loop if the user doesn't want to see more rows
            if show_more.lower() != "yes":
                if show_more.lower() != "y":
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no: ")
        if restart.lower() != "yes":
            if restart.lower() != "y":
                break


if __name__ == "__main__":
    main()
