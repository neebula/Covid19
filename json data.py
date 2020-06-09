# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 05:51:10 2020

@author: swetagupta110
"""

import json
import csv

# Opening JSON file 
# loading the data 
# into the variable data 
with open('covid19.json') as json_file: 
    data = json.load(json_file) 
  
covid_data = data['raw_data'] 
  
# now we will open a file for writing 
covid_data_file = open('covid_data_file.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(covid_data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for patient in covid_data: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = patient.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(patient.values()) 
  
covid_data_file.close() 
