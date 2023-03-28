import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml as lxml

list_index = []
list_name = []
list_district = []
list_houses = []

# Define URL
url = 'https://postbox.uz/indexes/default/index'

# Ask hosting server to fetch url
r = requests.get(url)
# print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

index = soup.find_all('td', class_='col-sm-2')
names = soup.find_all('td', class_='col-sm-4')
district = soup.find_all('td', class_='col-sm-3')

# Create list_index, list_name, list_district 
for name in index:
    list_index.append(name.text)
for name in names:
    list_name.append(name.text)
for name in district:
    list_district.append(name.text)

# Split list and Create list_houses
for i in range(0, len(list_district)):
    if i % 2:
        list_houses.append(list_district[i])


# Сделать цикл удаления элементов из list_district






