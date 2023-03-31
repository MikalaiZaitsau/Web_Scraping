import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml as lxml

list_index = []
list_name = []
list_district_temp = []
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

# Create list_index, list_name, list_district_temp
for name in index:
    list_index.append(name.text)
for name in names:
    list_name.append(name.text)
for name in district:
    list_district_temp.append(name.text)

# Split list and Create list_houses and list_district
for i in range(0, len(list_district_temp)):
    if i % 2:
        list_houses.append(list_district_temp[i])
    else:
        list_district.append(list_district_temp[i])

# Dict for pandas DataFrame
dict_for_pandas = {'Postal Index': list_index[1:], 'Index Name': list_name[1:], 
                   'District Name': list_district[1:], 'House': list_houses[1:]}

df = pd.DataFrame(dict_for_pandas)

#export to csv
#df.to_csv('out_postal_index', index=False)

#export to Excel
#df.to_excel('out_postal_index.xlsx', sheet_name='Postal_Index')
