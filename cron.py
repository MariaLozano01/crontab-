import pandas as pd 
import requests as rs 
import json
import os
import sys
import time 

response_API_json= rs.get('https://healthdata.gov/resource/vbjv-rh5z.json')
#this code allows us to get the data from the API link

#print(response_API.status_code)

data = response_API_json.text #pulls the data from the API
json.loads(data) #parses the data into a json file 

#One should pull down data from an API once a day (don’t care about what time) 


#One should pull down data every Sunday night at 10:00pm 


#And another one (?) should pull down data at the end of every quarter  
