from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from datetime import datetime, timezone

from pytz import timezone
import pytz

date_format='%m/%d/%Y %H:%M:%S %Z'
date = datetime.now(tz=pytz.utc)

date = date.astimezone(timezone('US/Pacific'))

update_time = date.strftime(date_format)


#Headers to parse url
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gec...: ko) Chrome/83.0.4103.97 Safari/537.36"}
url = 'https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/date/product/101397570845/lang/en'

#Url Vs
url_match = 'https://www.roadtrips.com/world-cup/2022-world-cup-packages/schedule/'




#Send page and headers
page = requests.get(url,headers=headers)
page_team_1 = requests.get(url_match,headers=headers)
page_team_2 = requests.get(url_match,headers=headers)


#Parse html
soup = BeautifulSoup(page.content, 'html.parser')
soup_matche_team_1 = BeautifulSoup(page_team_1.content, 'html.parser')
soup_matche_team_2 = BeautifulSoup(page_team_2.content, 'html.parser')

#Set the class that contains all the match information and its parent tag
all_data = soup.find_all('div', class_='performance_container') 
data_team1_from_page = soup_matche_team_1.find_all('td', class_='column-2')
data_team2_from_page = soup_matche_team_2.find_all('td', class_='column-4')
 
count=0
data_into_alist  = list()
data_list = []
team1_data_list = []
team2_data_list = []
list_index = []
final_list= []

#For to add team 1 to list
for i in data_team1_from_page:
    team1_data_list.append(i.text)

#For to add team 2 to list
for i in data_team2_from_page:
    team2_data_list.append(i.text)

#For to add items to a list
for i in all_data:
    data_into_alist.append(i.text)
   
#Remove all garbage
special_char = '@_!#$%^&*()<>?/\|}{~:;.[]\n\r\t'
out_list = [''.join(filter(lambda i: i not in special_char, string)) for string in data_into_alist]
string_clean = ''.join(map(str, out_list))
new_list_clean = string_clean.split()
data_list = ','.join(map(str, new_list_clean))

#Final clean list
lista = data_list.split(',')

#Find a string that is repeated in all matches
#To take it as a reference and work
#The list starting from that element
#And generate the index of the list to iterate
for i in range(0,len(lista)):
    if('Stadium' in lista[i] ):
        list_index.append(i)

#Iterating the indexes to find available tickets
for i in range(len(list_index)):      
    for j in range(list_index[i],list_index[i]+1):
         if lista[j+3] == 'Limited' or lista[j+3] == 'availability':
            state = 'Not available'
         else:
            state = 'Available'
         count += 1
         id_tikect = 101437163854+count   
         matchesV = {'Match': 'M'+str(count) ,'HomeTeam': team1_data_list[i] ,'AwayTeam': team2_data_list[i] , 'Status': state, 'Buy': 'https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/seat/performance/'+str(id_tikect)+'/lang/en', 'UpdateAt': update_time}
         final_list.append(matchesV)

#Conver into json

json_dump = json.dumps(final_list)
with open('fifa.json', 'w') as f:
    f.write(json_dump)
    print("The json file is created")
print(json_dump)
