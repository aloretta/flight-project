# Check of departure time outliers

# Loretta Au, Oct. 30, 2017

# exec(open('01_depdelay_cutoffs.py').read())

# Note that a few airlines started at a different time
# F9 2005 :
#Int64Index([5, 6, 7, 8, 9, 10, 11, 12], dtype='int64', name='FlightDate')
#HA 2003 :
#Int64Index([11, 12], dtype='int64', name='FlightDate')

# Load the data

exec(open('99_functions.py').read())

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import datetime as dt
from pathlib import Path

path = "/media/loretta/My Passport/Datasets/Aviation_Data/small_OnTimePerformance/"

airlines_2016 = ['AA', 'AS', 'B6', 'DL', 'EV', 'F9', 'HA', 'OO', 'UA', 'WN', 'NK', 'VX']
years = np.array(range(2000,2017))
file_stem = 'OnTime_Performance.pkl'
years = np.arange(2000, 2017)

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
days = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun'];

delay_negative = {}
for company in airlines_2016:
    file_info = ()
    delay_times = []
    year_count = 0
    for year in years:
        file_info = [company, str(year), file_stem]
        pkl_filename = path + '_'.join(file_info)
        if Path(pkl_filename).is_file():
            print(company, str(year))
            flight_data = pd.read_pickle(pkl_filename)
            flight_data = flight_data.fillna(0)
            time_index = pd.DatetimeIndex(flight_data['FlightDate'])
            delays_in_minutes = flight_data['DepDelay'].tolist()
            delay_times.extend(delays_in_minutes)
            year_count += 1
    delay_times = np.array(delay_times)
    delay_negative[company] = delay_times[delay_times < 0]
    del delay_times
    

plt.figure(figsize=[7,5])
for key, value in delay_negative.items():
    value = value[value < -15]
    x, y = ecdf(value)
    plt.plot(x,y, label=key)

plt.title('Departures Ahead of Schedule')
plt.xlabel('Time (minutes)')
plt.ylabel('Proportion of Flights')
plt.tight_layout()
plt.savefig('figures/early_dep.png')
#plt.show()
# Set lower-bound for DepDelay to be -15
