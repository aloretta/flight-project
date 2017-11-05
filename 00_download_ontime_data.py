# Download files
# exec(open('00_download_ontime_data.py').read())

# Source code template: 
# https://stackoverflow.com/questions/8814813/saving-a-downloaded-zip-file-w-python

# Example: zip_url = 'https://transtats.bts.gov/PREZIP/On_Time_On_Time_Performance_2015_1.zip' 

import urllib.request, urllib.parse, urllib.error
import numpy as np


# Create the file names
main_url = 'https://transtats.bts.gov/PREZIP'
stem = 'On_Time_On_Time_Performance'
year = np.array(range(2000, 2017))
month = np.array(range(1,13))
filetype = '.zip'


for yr in year:
    for mo in month:
        mylist = []
        mylist.append(stem)
        mylist.append(str(yr))
        mylist.append(str(mo))
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


