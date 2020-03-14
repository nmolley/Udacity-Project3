# Import the Python Data Analysis Library (PANDAS)

import pandas as pd

# Read the city data files using the read.csv function into dataframes
# Note that data files and this code are on removable media SANDISKNAM
# Path /Volumes/SANDISKNAM/bikeshare-2
#
df_chicago = pd.read_csv ('chicago.csv')
df_ny      = pd.read_csv ('new_york_city.csv')
df_washington = pd.read_csv ('washington.csv')
#
# Convert the Start Time column to datatype datetime then parse
#
df_chicago ['Start Time'] = pd.to_datetime (df_chicago['Start Time'])
df_ny ['Start Time']      = pd.to_datetime (df_ny['Start Time'])
df_washington ['Start Time'] = pd.to_datetime (df_washington['Start Time'])
#
df_chicago ['Hour']          = df_chicago['Start Time'].dt.hour
df_ny ['Hour']               = df_ny['Start Time'].dt.hour
df_washington ['Hour']       = df_washington['Start Time'].dt.hour
#
df_chicago['DoW'] = df_chicago['Start Time'].dt.weekday_name
df_chicago['DoW'].mode()[0]
df_ny['DoW'] = df_ny['Start Time'].dt.weekday_name
df_ny['DoW'].mode()[0]
df_washington['DoW'] = df_washington['Start Time'].dt.weekday_name
df_washington['DoW'].mode()[0]
#
df_chicago['Month'] = df_chicago['Start Time'].dt.month
most_freq_month_chicago = df_chicago['Month'].mode()[0]
df_ny['Month'] = df_ny['Start Time'].dt.month
most_freq_month_ny =df_ny['Month'].mode()[0]
df_washington['Month'] = df_washington['Start Time'].dt.month
most_freq_month_washington = df_washington['Month'].mode()[0]
#
# Compute basic descriptive statistics for all data in all files
# Start with measures of central tendency, frequency distributions
#       then compute measures of dispersion
#
# Some measures of central tendency (mean, median, mode)
#
avg_trip_duration_chicago = df_chicago['Trip Duration'].mean()
avg_trip_duration_ny      = df_ny['Trip Duration'].mean()
avg_trip_duration_washington = df_washington['Trip Duration'].mean()
median_trip_duration_chicago = df_chicago['Trip Duration'].median()
median_trip_duration_ny      = df_ny['Trip Duration'].median()
median_trip_duration_washington = df_washington['Trip Duration'].median()
most_freq_hour_chicago          = df_chicago['Hour'].mode()[0]
most_freq_hour_ny               = df_ny['Hour'].mode()[0]
most_freq_hour_washington       = df_washington['Hour'].mode()[0]
most_freq_start_station_chicago = df_chicago['Start Station'].mode()[0]
most_freq_start_station_ny      = df_ny['Start Station'].mode()[0]
most_freq_start_station_washington  = df_washington['Start Station'].mode()[0]
#
# Frequency counts
#
Gender_count_chicago = df_chicago['Gender'].value_counts()      #Provides frequency of Male and Female
Gender_count_ny      = df_ny['Gender'].value_counts()           #Same here for NY data
User_type_count_washington = df_washington['User Type'].value_counts() #Frequency counts Sub vs. Cust.
Chicago_null_count         = df_chicago.isnull().sum(axis=0)           #Number of NULL values Chicago
NY_null_count              = df_ny.isnull().sum(axis=0)                #Number of NULL values NY
Year_count_chicago         = df_chicago['Birth Year'].value_counts()
Year_count_ny              = df_ny['Birth Year'].value_counts()
#
# Some measures of dispersion (standard deviation, variance)
#
std_trip_duration_chicago = df_chicago['Trip Duration'].std()
std_trip_duration_ny      = df_ny['Trip Duration'].std()
std_trip_duration_washington = df_washington['Trip Duration'].std()
#
#new
print ('Mean trip duration for Chicago: ',round(avg_trip_duration_chicago))
print ('Mean trip duration for NY :',round(avg_trip_duration_ny))
print ('Mean trip duration for Washington: ',round(avg_trip_duration_washington))
print ('Median trip duration for Chicago: ',round(median_trip_duration_chicago))
print ('Median trip duration for NY :',round(median_trip_duration_ny))
print ('Median trip duration for Washington: ',round(median_trip_duration_washington))
print ('Most frequent starting hour for Chicago: ',most_freq_hour_chicago)
print ('Most frequent starting hour for NY: ',most_freq_hour_ny)
print ('Most frequent starting hour for Washington: ',most_freq_hour_washington)
print ("St.Dev. Chicago: " , round(std_trip_duration_chicago) , " seconds")
print ("St.Dev. New York: " , round(std_trip_duration_ny) , " seconds")
print ("St. Dev.Washington: " , round(std_trip_duration_washington) , " seconds")



