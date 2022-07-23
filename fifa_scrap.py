from itertools import count
from ntpath import join
from bs4 import BeautifulSoup
from numpy import true_divide
import requests
import pandas as pd
import json
from datetime import datetime, timezone
from pytz import timezone
import pytz

#Only When needs time
date_format='%m/%d/%Y %H:%M:%S %Z'
date = datetime.now(tz=pytz.utc)
date = date.astimezone(timezone('US/Pacific'))
update_time = date.strftime(date_format)
#Headers
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gec...: ko) Chrome/83.0.4103.97 Safari/537.36"}

#list
tags = []
classes = []
count=0
list_v_color =[]
list_index = []

#Url Vs
url_match = 'https://www.roadtrips.com/world-cup/2022-world-cup-packages/schedule/'


url = 'https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/date/product/101397570845/lang/en'


#Send page and headers
page = requests.get(url,headers=headers)
page_with_display_none = requests.get(url,headers=headers)
page_team_1 = requests.get(url_match,headers=headers)
page_team_2 = requests.get(url_match,headers=headers)


#Parse html
soup = BeautifulSoup(page.content, 'html.parser')
soup_find_display_none = BeautifulSoup(page_with_display_none.content, 'html.parser')
soup_matche_team_1 = BeautifulSoup(page_team_1.content, 'html.parser')
soup_matche_team_2 = BeautifulSoup(page_team_2.content, 'html.parser')

#Set the class that contains all the match information and its parent tag
all_data = soup.find_all('div', class_='performance_container') 
all_data_display_none = soup_find_display_none.find_all('div', class_='limited') 
data_team1_from_page = soup_matche_team_1.find_all('td', class_='column-2')
data_team2_from_page = soup_matche_team_2.find_all('td', class_='column-4')

stateStr=""
count=0
data_into_alist  = list()
data_display_none_into_alist = list()
data_category = list() 
data_list = []
data_list_none = []
data_list_display_none = []
team1_data_list = []
team2_data_list = []

final_list= []
list_v_color =[]
#For to add team 1 to list
for i in data_team1_from_page:
    team1_data_list.append(i.text)


#For to add display none to alist
for i in all_data_display_none:
    data_list_display_none.append(i.text)


#For to add team 2 to list
for i in data_team2_from_page:
    team2_data_list.append(i.text)

#For to add items to a list
for i in all_data:
    data_into_alist.append(i.text)


#print(data_list_display_none)   

#Remove all garbage
special_char = '@_!#$%^&*()<>?/\|}{~:;.[]\n\r\t'
#General
out_list = [''.join(filter(lambda i: i not in special_char, string)) for string in data_into_alist]
#Display none
out_list_none = [''.join(filter(lambda i: i not in special_char, string)) for string in data_list_display_none]

#general
string_clean = ''.join(map(str, out_list))
new_list_clean = string_clean.split()
data_list = ','.join(map(str, new_list_clean))


#none
string_clean_none = ''.join(map(str, out_list_none))
new_list_clean_none = string_clean_none.split()
data_list_none = ','.join(map(str, new_list_clean_none))
#print(data_list_none)

#Final clean list
lista = data_list.split(',')


#Final clean list none
lista_none_parse = data_list_none.split(',')

#print(lista_none)


def getAllDataTikects(url):
    
    page = requests.get(url,headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
   
   
    #Set the class that contains all the match information and its parent tag
    all_data1 = soup.find_all('span', class_='color') 
    select1 = soup.find(id='eventFormData[0].quantity') 
    select2 = soup.find(id='eventFormData[1].quantity') 
    select3 = soup.find(id='eventFormData[2].quantity') 
    #all_data = soup.find_all('class', class_='color') 
    #print(all_data1)

    
    color= str(all_data1)
    tikect1 = str(select1)
    tikect2 = str(select2)
    tikect3 = str(select3)

    
    if '#0000FF' in color:
        varesita = "true"
    
        list_v_color.append("Not available") 
        list_v_color.append("Not available") 
        list_v_color.append("Not available") 
        
    else:
        if '#C78800' in color:
            varesita = "true"
            if 'option' in tikect1:
                category1 = "true"
               
                list_v_color.append("Available") 
            else:
                category1 = "false"
                list_v_color.append("Not available")  
                      
    
                    
        if '#AD0000' in color:
            varesita = "true"
            if 'option' in tikect2:
                category2 = "true"
               
                list_v_color.append("Available")
            else:
                category2 = "false"
                list_v_color.append("Not available")
               
           
        if '#006BD6' in color:
            varesita = "true"
            if 'option' in tikect3:
                category3 = "true"
              
                list_v_color.append("Available") 
            else:
                category3 = "false"
                list_v_color.append("Not available")  
               
           
    print(list_v_color)
    #print(list_v_color)

for i in range(0,64):
    count += 1       
    id_tikect = 101437163854+count  
    getAllDataTikects('https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/seat/performance/'+str(id_tikect)+'/lang/en')





for i in range(0,len(lista)):
    if('Stadium' in lista[i] ):
        list_index.append(i)
        count += 1
        id_tikect = 101437163854+count  
        url_tikect = 'https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/seat/performance/'+str(id_tikect)+'/lang/en'
        #Send page and headers
        page = requests.get(url_tikect,headers=headers)
        #Parse html
        soup = BeautifulSoup(page.content, 'html.parser')

        #Set the class that contains all the match information and its parent tag
        all_data = soup.find_all('span', class_='text') 


cuenta = 0
boletos =-1
#Iterating the indexes to find available tickets
for i in range(len(list_index)):      
    for j in range(list_index[i],list_index[i]+1):
        if lista[j+3] == 'Limited' or lista[j+3] == 'availability' or  lista[j+3] == 'Low' or lista[j+3] == 'Currently' or lista[j+3]== 'unavailable' or lista[j+3]=='This':
            state = 'Not available'
            cat1='Not available'
            cat2='Not available'
            cat3='Not available' 
        else:
            state = 'Available'
         
        cuenta += 1
        boletos +=1
        id_tikect = 101437163854+cuenta
         



        if(i==0):
            match_index = str(i+1)
        else:
            match_index = str(i)


        if(list_index[i] > len(lista_none_parse) ):
            lista_none_parse.append('Not visble match')
       
                                    
        if(lista_none_parse[i]== 'Low'):
            state_des = 'Low availability'    
            #lista_none_parse.append('Low availability')
           
           
        if(lista_none_parse[i]== 'availability'):
            state_des = 'Low availability'
           
              
            #lista_none_parse.append('Low availability')
        if(list_v_color[boletos]=='Available' or list_v_color[boletos+1]=='Available' or list_v_color[boletos+2]=='Available'):
            state ='Available'
        matchesV = {'Match': 'M'+str(cuenta) ,'HomeTeam': team1_data_list[i] ,'AwayTeam': team2_data_list[i] , 'Status': state, 'StateDesc': state_des, 'Category1': list_v_color[boletos], 'Category2': list_v_color[boletos+1], 'Category3': list_v_color[boletos+2], 'Buy': 'https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/seat/performance/'+str(id_tikect)+'/lang/en'}
        final_list.append(matchesV)
        del list_v_color[0:2]  
#Conver into json

json_dump = json.dumps(final_list)
with open('fifa.json', 'w') as f:
    f.write(json_dump)
    print("The json file is created")
print(json_dump)
