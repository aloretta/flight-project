# Download files
# exec(open('00_download_market_data.py').read())

# Source: https://stackoverflow.com/questions/8814813/saving-a-downloaded-zip-file-w-python

#zip_url = 'https://transtats.bts.gov/PREZIP/Origin_and_Destination_Survey_DB1BMarket_2017_1.zip'

import urllib.request, urllib.parse, urllib.error
import numpy as np

# Create the file names
main_url = 'https://transtats.bts.gov/PREZIP'
stem = 'Origin_and_Destination_Survey_DB1BMarket'

year = np.array(range(2000,2006))
quarter = np.array(range(1,5))
filetype = '.zip'

for yr in year:
    for qtr in quarter:
        mylist = []
        mylist.append(stem)
        mylist.append(str(yr))
        mylist.append(str(qtr))
        zip_filename = '_'.join(mylist) + filetype
        zip_url = '/'.join([main_url, zip_filename])
        print(zip_url)
        # Download and save
        print("Downloading: " + zip_filename)
        f = urllib.request.urlopen(zip_url)
        data = f.read()
        with open(zip_filename, "wb") as code:
            code.write(data)
            
            f.close()

# End of downloads

