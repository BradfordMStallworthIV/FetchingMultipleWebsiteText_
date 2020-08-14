#fetch multiple website test
#Bradford

import requests
from bs4 import BeautifulSoup
import csv
import time

#open csv file that contains lower cased state names
with open('50_us_states_lowercased.csv', newline= '') as f:
    reader = csv.reader(f)
    csv_states = list(reader)

#importing the csv file and creating a list caused a minor issue
# example [[ohio],[florida],[chicago]]
#figured out a way to remove the brackets inside the list by nesting list comprehension

states = []
for sublist in csv_states:
    for val in sublist:
        states.append(val)



#with the flattened data state names
# concatenate "state" part of the url


for s in states:
    url = 'https://www.attractionsofamerica.com/attractions/'+s+'.php'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    with open(s+'-attraction2.html','w', encoding = 'utf-8') as file:
        file.write(str(soup))
    time.sleep(5)

        








