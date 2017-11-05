# flight-project

<p>
Have you ever had your flight delayed and wondered if you were just 
having bad luck or if the carrier has a growing reputation for being late?
</p>


<p>
In this project, we perform time series analysis on flight delay data provided by the Bureau of Transportation Statistics from 2000-2016, and evaluate the on-time performance for all current airline carriers. Additionally, we identify the factors that influence ticket pricing the most, and how these may be correlated with overall airline performance.
</p>


<b>Getting started</b>

Data files can be downloaded from the BTS website directly.
An example of how to get all the <a href = 'https://www.transtats.bts.gov/DatabaseInfo.asp?DB_ID=125'>On-Time Performance</a> tables is provided. 
Although BTS has data for the different 
<a href="https://www.transtats.bts.gov/tables.asp?db_id=125&DB_Name=Airline%20Origin%20and%20Destination%20Survey%20%28DB1B%29#">Tickets</a> and <a href="https://www.transtats.bts.gov/tables.asp?db_id=125&DB_Name=Airline%20Origin%20and%20Destination%20Survey%20%28DB1B%29#">Coupons</a>, we mostly utilized the 
<a href="https://www.transtats.bts.gov/tables.asp?db_id=125&DB_Name=Airline%20Origin%20and%20Destination%20Survey%20%28DB1B%29#">Market</a> data, and the
source code for getting those files is also included. 
<ul>
  <li><code>00_download_ontime_data.py</code></li>
  <li><code>00_download_market_data.py</code></li>
</li>

