# Read in the CSV files for different BTS data.
# Process them and save a smaller version to reduce memory usuage
# Not all columns in the table are useful, so we'll only keep the
# columns we need for our project.

# Directories used to save the CSV files:
# 'DB1BCoupon', 'DB1BMarket', 'DB1BTicket' and 'OnTimePerformance'

# Loretta Au, Sept. 23, 2017

# exec(open('00_process_data.py').read())

import csv
import glob
import os
import pandas as pd

# Change 'main_dir' to the file where your original tables are saved
main_dir = '/media/loretta/My Passport/Datasets/Aviation_Data/'
folders = ['DB1BCoupon', 'DB1BMarket', 'DB1BTicket', 'OnTimePerformance']
sub_dirs = [os.path.join(main_dir, dir) for dir in folders if os.path.isdir(os.path.join(main_dir, dir))]

coupon_csv = []
market_csv = []
ticket_csv = []
perf_csv = []

# Get the CSV file names
for dir in folders:
    sub_dir = os.path.join(main_dir,dir) 
    print(sub_dir);
    if dir == 'DB1BCoupon':
        coupon_csv = [os.path.join(sub_dir +'/'+csv) for csv in os.listdir(sub_dir) 
                      if os.path.isfile(os.path.join(sub_dir, csv)) and csv.endswith('.csv')]
    elif dir == 'DB1BMarket':
        market_csv = [os.path.join(sub_dir + '/'+ csv) for csv in os.listdir(sub_dir) 
                      if os.path.isfile(os.path.join(sub_dir, csv)) and csv.endswith('.csv')]
    elif dir == 'DB1BTicket':
        ticket_csv = [os.path.join(sub_dir +'/'+csv) for csv in os.listdir(sub_dir) 
                      if os.path.isfile(os.path.join(sub_dir, csv)) and csv.endswith('.csv')]
    elif dir == 'OnTimePerformance':
        perf_csv = [os.path.join(sub_dir + '/' + csv) for csv in os.listdir(sub_dir) 
                    if os.path.isfile(os.path.join(sub_dir, csv)) and csv.endswith('.csv')]

# Set up variables for assigning table to each list
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
quarter = [range(1,5)] #'Q1', 'Q2', 'Q3', 'Q4']
coupon_list = ['coupon_' + str(qtr) for qtr in quarter] 
market_list = ['market_' + str(qtr) for qtr in quarter]
ticket_list = ['ticket_' + str(qtr) for qtr in quarter]


data_dict = {}


def origin_dest(table):
    origin = table['Origin'];
    dest = table['Dest'];
    # Put in a check point where you have actual values
    route = origin.str.cat(dest, sep=':')
    table['Route'] = route
    return(table)

print('Working on Market tables');
for i in range(0,len(market_csv)):
    print("Table ", i+1, "of ", str(len(market_csv)))
    market_df = pd.read_csv(market_csv[i], header=0)
    new_market_df = market_df[['Origin', 'Dest', 'MktFare', 'MktDistance', 'NonStopMiles',
                               'RPCarrier', 'TkCarrier', 'OpCarrier', 'MktDistanceGroup', 'MktCoupons',
                               'Passengers']].copy()
    new_market_df = origin_dest(new_market_df)
    file_info = market_csv[i].split("/")
    new_info = file_info[-1].split("_")
    new_info = new_info[-3:] # Data type, year and quarter
    new_info.insert(0, 'reduced')
    new_filename = '_'.join(new_info)
    new_subdir = main_dir + 'small_DB1BMarket/'
    new_market_df.to_csv(new_subdir + new_filename, header=True)
    del market_df # Clear the memory
    del new_market_df


print('Working on Monthly tables');
for i in range(0,len(perf_csv)):
    print("Table ", i+1, "of ", str(len(perf_csv)))
    perf_df = pd.read_csv(perf_csv[i], header=0)
    new_perf_df = perf_df[['FlightDate', 'DayofMonth', 'DayOfWeek',
                           'Origin', 'Dest',
                           'Quarter', 'AirlineID', 'UniqueCarrier', #'UniqueCarrierName', #'UniqCarrierEntity',
                           'DepDelay', 'ArrDelay', 'Cancelled', 'Diverted',
                           'CRSElapsedTime', 'ActualElapsedTime', 'AirTime', 'Flights', 'Distance',
                           'CarrierDelay', 'WeatherDelay', 'NASDelay', 
                           'SecurityDelay', 'LateAircraftDelay',
                           'FirstDepTime', 'TotalAddGTime', 'LongestAddGTime']].copy()
    new_perf_df = origin_dest(new_perf_df)
    file_info = perf_csv[i].split("/")
    new_info = file_info[-1].split("_")
    new_info = new_info[-3:] # Data type, year and quarter
    new_info.insert(0, 'reduced_OnTime')
    new_filename = '_'.join(new_info)
    new_subdir = main_dir + 'small_OnTimePerformance/'
    new_perf_df.to_csv(new_subdir + new_filename, header=True)
    del perf_df # Clear the memory
    del new_perf_df

# LA: commented out bc ended up not needing Coupon tables
# Read in CSV, slice it, and save it as a smaller file.
#for i in range(0,len(coupon_csv)):
#    print("Table ", i+1, "of ", str(len(coupon_csv)))
#    coupon_df = pd.read_csv(coupon_csv[i], header=0)
#    new_coupon_df = coupon_df[['Origin', 'Dest', 'Break', 'TkCarrier', 'OpCarrier', 'RPCarrier', 'FareClass']].copy() 
#    new_coupon_df = origin_dest(new_coupon_df)
#    file_info = coupon_csv[i].split("/")
#    new_info = file_info[-1].split("_")
#    new_info = new_info[-3:] # Data type, year and quarter
#    new_info.insert(0, 'reduced')
#    new_filename = '_'.join(new_info)
#    new_subdir = main_dir + 'small_DB1BCoupon/'
#    new_coupon_df.to_csv(new_subdir + new_filename, header=True)
#    del coupon_df # Clear the memory
#    del new_coupon_df
