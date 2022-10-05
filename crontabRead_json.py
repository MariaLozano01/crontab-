import pandas as pd 
import airflow #pip install apache-airflow and #airflow db init
import requests as rs 
import json
import os
import sys
import time 
import csv

#this code allows us to get the data from the API link as a dataset itself
#not just a string

response_API_json= pd.read_json('https://healthdata.gov/resource/vbjv-rh5z.json')
response_API_json

#save data locally
response_API_json.to_csv('/Users/marialozano/Documents/GitHub/crontab-/data/Socialdt.csv', index=None)

######################## CRONTAB CODE STARTS ####################################

#get current working directory
cwd= os.getcwd()

#print cwd
print(cwd)

#create a new dictionary with data 
#this code allows us to get the data from the API link

#print(response_API.status_code)
#parses the data into a json file 

#get current time
now = time.time()

timestart = time.strftime("%Y-%m-%D_%H:%M:%S", time.localtime(now))
print('Time program started running: ', timestart)

#Create a new file in the current working directory
with open(cwd + '/testFile_' + timestart + '.csv', 'w') as f:
    f.write(str(response_API_json))


#One should pull down data from an API once a day (don’t care about what time) 


#One should pull down data every Sunday night at 10:00pm 


#And another one (?) should pull down data at the end of every quarter  
