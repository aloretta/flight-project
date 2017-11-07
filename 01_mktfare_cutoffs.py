# Process the condensed DB1B_Market CSV tables for outliers
# Keep in mind that these are quarterly data

# Loretta Au, Oct. 2, 2017

# exec(open('01_mktfare_cutoffs.py').read())

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# Read in the functions
exec(open('99_functions.py').read()) 

path =  '/media/loretta/My Passport/Datasets/Aviation_Data/small_DB1BMarket/'
years = np.array(range(2000,2017))
quarters = np.array(range(1,5)) 

stem = 'reduced_DB1BMarket' # year_quarter.csv

# ====================================================
years= np.array(range(2000, 2017))
qtr_names = ['Q1', 'Q2', 'Q3', 'Q4']
# Remember to change this path to match your directories
path = "/media/loretta/My Passport/Datasets/Aviation_Data/small_DB1BMarket/"

cutoffs = {}
lower = range(0,16)
upper = range(85,101)
all_cuts = np.append(lower, upper)

for year in years:
    print('Processing data for:', year)
    market_df = {}
    market_routes = []
    market_fares = []
    for i in range(len(qtr_names)):
        file_name = path + 'reduced_DB1BMarket_' + str(year) + '_' + str(i+1) + '.csv'
        market_df[qtr_names[i]] = pd.read_csv(file_name, header=0, index_col=0)
        if (year == years[-1]):
            market_fares.extend(market_df[qtr_names[i]]['MktFare'])
    cutoffs[year]= fare_cdf(market_df, all_cuts)
    del market_df

# Plot the ECDF
market_fares = np.array(market_fares)
market_fares = market_fares[market_fares < 5000]
x,y = ecdf(market_fares)
plt.figure(figsize=[7,5])
plt.plot(x,y)
plt.title('Market Fare Distribution in 2016 Sample')
plt.xlabel('Price')
plt.ylabel('Proportion')
plt.savefig('figures/full_ecdf.png')

cutoffs = pd.DataFrame(cutoffs)
cutoffs['percentile'] = all_cuts

# Optional: save to a CSV file to avoid re-running calculations for cutoffs
cutoffs.to_csv('/home/loretta/capstone_data/flight_project/processed/price_cutoffs.csv')
cutoffs = pd.read_csv('/home/loretta/capstone_data/flight_project/processed/price_cutoffs.csv')
cutoffs.mean(axis=1)

years = [str(x) for x in years]
lower_df = cutoffs.loc[cutoffs['percentile'].isin(lower)]
upper_df = cutoffs[cutoffs['percentile'].isin(upper)]


plt.figure(figsize=[7,5])
axes = lower_df[years].plot(legend=False)
_ = plt.xticks(range(len(lower)), lower)
plt.title('Cutoffs for Market Fare Data')
plt.xlabel('Percentiles')
plt.ylabel('Price')
plt.ylim([-500,200])
plt.hlines(y=700,xmin= 0,xmax=100, color='k', linestyle='dashed')
plt.hlines(y=50, xmin=0,xmax=100, color='k', linestyle='dashed')
plt.margins(0.02)
plt.savefig('figures/fare_lower.png')

plt.figure(figsize=[7,5])
axes2 = upper_df[years].plot(legend=False)
_ = plt.xticks(range(len(lower), len(lower)+len(upper)), upper)
plt.title('Cutoffs for Market Fare Data')
plt.xlabel('Percentiles')
plt.ylabel('Price')
plt.ylim([0,1000])
plt.hlines(y=700,xmin= 0,xmax=100, color='k', linestyle='dashed')
plt.hlines(y=50, xmin=0,xmax=100, color='k', linestyle='dashed')
plt.margins(0.02)
plt.savefig('figures/fare_upper.png')

# Reprocess the data tables to remove outliers
upper_cutoff = 700
lower_cutoff = 50

# Remove outliers and save the data tables with new file names
years = np.array(range(2000,2017))
new_stem = 'rm_outliers_DB1BMarket'
for year in years:
    print('Processing year', year)
    for quarter in range(1,5):
        file_name = path + stem + '_' + str(year) + '_' + str(quarter) + '.csv'
        df = pd.read_csv(file_name, header=0)
        applied_cutoffs = df[(df.MktFare > lower_cutoff) & (df.MktFare < upper_cutoff)]
        new_file = path + new_stem + '_' + str(year) +'_' + str(quarter) + '.csv'
        applied_cutoffs.to_csv(new_file)
