import pandas as pd 
import airflow #pip install apache-airflow and #airflow db init
import requests as rs
import json
import os
import sys
import time 
import csv

#pulls the data from the API
response_API = rs.get('https://healthdata.gov/resource/vbjv-rh5z.json')
data = response_API.text #parses the data into a readable modum (string of text)
data #print readable string of data from API

json.loads(data) #print string of data as well

######################## CRONTAB CODE STARTS ####################################

#get current working directory
cwd= os.getcwd()

#print cwd
print(cwd)

#create a new dictionary with data 
response_API_json= rs.get('https://healthdata.gov/resource/vbjv-rh5z.json')
#this code allows us to get the data from the API link

data = response_API_json.text #pulls the data from the API
json.loads(data) #parses the data into a json file 

#get current time
now = time.time()
timestart = time.strftime("%Y-%m-%D_%H:%M:%S", time.localtime(now))
print('Time program started running: ', timestart)

#Create a new file in the current working directory
with open(cwd + '/testFile_' + timestart + '.txt', 'w') as f:
    f.write(str(data))
