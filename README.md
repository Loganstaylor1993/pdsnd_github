>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
10/21/2023

### Project Title
Explore US Bikeshare Data

### Description
In this project, Python is used to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. Interesting questions are answered about the data by computing descriptive statistics. A script takes in raw input to create an interactive experience in the terminal to present these statistics.

### Functions
get_filters
load_data
time_stats
station_stats
trip_duration_stats
user_stats
raw_data

### Example
Hello! Let's explore some US bikeshare data!
Please select a city (chicago, new york city, washington): chicago
Please select a month (january - june). Enter 'all' to include all months: all
Please select day of the week. Enter 'all' to include all days: all
You've selected: chicago all all
----------------------------------------

Calculating The Most Frequent Times of Travel...

Most common month: June
Most common day: Tuesday
Most common start hour: 05 PM

This took 8.28998064994812 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

Most common start station: Streeter Dr & Grand Ave
Most common end station: Streeter Dr & Grand Ave
Most common trip: Lake Shore Dr & Monroe St to Streeter Dr & Grand Ave

This took 0.18169140815734863 seconds.
----------------------------------------

Calculating Trip Duration...

Total travel time: 3250 Days 19 Hours 56 Minutes 27 Seconds
Average travel time: 15 Minutes 36 Seconds

This took 0.002112865447998047 seconds.
----------------------------------------

Calculating User Stats...

Number of subscribers: 238889
Number of non-subscribers: 61110
Male Count: 181190
Female Count: 57758
None Count: 61052
Earliest Birth Year: 1899
Most Recent Birth Year: 2016
Most Common Birth Year: 1989

This took 0.06149411201477051 seconds.
----------------------------------------

Would you like to see the raw data? Enter yes or no: no

Would you like to restart? Enter yes or no: no

### Files used
bikeshare.py
chicago.csv
new_york_city.csv
washington.csv

### Credits
https://pandas.pydata.org/docs/reference/frame.html
https://docs.python.org/3/library/calendar.html

