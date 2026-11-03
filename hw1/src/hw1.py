from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).parent / "bicycle_data.csv"

df = pd.read_csv(DATA_FILE)

# Making the column names workable and changing the types, step 2 in HW

df = df.rename(columns={
    'Fremont Bridge Sidewalks, south of N 34th St Total': 'bikes_total', 
    'Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk': 'bikes_west',
    'Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk': 'bikes_east'})
df = df.convert_dtypes()
df['Date'] = pd.to_datetime(df['Date'])
## Column # / Name / abreviated name / (type)
# 0 / Date / (datetime64[us]) 
# 1 / Fremont Bridge Sidewalk Total Cyclists / bikes_total / (int64) 
# 2 / Fremont Bridge West Sidewalk Cyclists / bikes_west / (int64) 
# 3 / Fremont Bridge East Sidewalk Cyclists / bikes_east / (int64) 

# Adding columns as directed in step 3 of HW

df['bikes_east+bikes_west'] = df['bikes_east'] + df['bikes_west']
df['hour'] = df['Date'].dt.hour
df['year'] = df['Date'].dt.year

# Part 4, 2016 df

df_2016 = df[df['year'] == 2016]

# Part 5, Filtering any nulls or na out

df_2016 = pd.DataFrame.dropna(df_2016)

# Part 6, all the 12pms are the same I guess. 
# I disagree with noon in winter being lumped in with noon in summer, but that's what the instructions seem to be asking for.

df_2016_plot = df.groupby(df_2016['hour']).agg(hourly_total=('bikes_total', 'sum'))
df_2016_plot['hour'] = range(0, len(df_2016_plot))
df_2016_plot = df_2016_plot.convert_dtypes()

plt.title('Counts by Hour')
plt.xlabel('Hour')
plt.ylabel('Total Bike Counts')
plt.bar(df_2016_plot['hour'], df_2016_plot['hourly_total'], color='orange')
plt.plot()
# plt.savefig('counts_by_hour.png')

# Part 7, averages!

df_2016_mean = df.groupby(df_2016['hour']).agg(hourly_total=('bikes_total', 'mean'))
df_2016_mean['hour'] = range(0, len(df_2016_plot))

print(df_2016_mean)

# This says that 17 aka 5pm is the busiest on average

# Part 8, the making of. It's in the README!


