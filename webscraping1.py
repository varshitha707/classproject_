import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(bright_stars_url)
print(page)

Soup=bs(page.text,'html.parser')
startable=Soup.find('table')
print(startable)

templist=[]
tablerows=startable.find_all('tr')
print(tablerows)

for tr in tablerows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td ]
    templist.append(row)
print(templist)

starnames=[]
distance=[]
mass=[]
radius=[]
lum=[]

for i in range(1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])
    
df2=pd.DataFrame(list(zip(starnames,distance,mass,radius,lum)),columns=['starname','mass','distance','radius','lum'])
print(df2)
df2.to_csv('brightstars.csv')  