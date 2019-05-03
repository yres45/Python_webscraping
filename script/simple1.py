# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:44:00 2019

@author: Yres
"""
import requests
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from pandas.io.json import json_normalize
from selenium.webdriver.chrome.options import Options
from langdetect import detect


options = Options()
options.headless = True
driver = webdriver.Chrome("C:\\Users\\Yres\\Downloads\\chromedriver_win32\\chromedriver.exe", chrome_options=options)

driver.get('http://zakaz-ali.ru/login.php')

s = requests.Session()

username = driver.find_element_by_name("login")
password = driver.find_element_by_name("password")

username.send_keys("Терешкин")
password.send_keys("юра")

driver.find_element_by_name("do_login").click()

source = driver.page_source
driver.quit() 

result_finish = ''
conn = sqlite3.connect("prob1.db")
conn.text_factory = str

cursor = conn.cursor()
# delete 
cursor.execute("""DROP TABLE yres_package;""")
sql_command = """
CREATE TABLE yres_package ( 
id     INTEGER PRIMARY KEY AUTOINCREMENT,
name   VARCHAR(100), 
track  VARCHAR(100), 
number VARCHAR(100),
point  VARCHAR(100));"""
cursor.execute(sql_command)


soup = BeautifulSoup(source, "html.parser")
target = soup.findAll("tr", class_="normal")
targer_a = soup.findAll("a", href=lambda href: href and "1track" in href)

grades = {}
track1 = []
p = ''
cursor.execute("Delete  FROM yres_package  ")
for tr in soup.find_all("tr",class_="normal"):
    td_text = [td.text.strip() for td in tr.find_all("td")]
    grades[td_text[0]] = td_text[1]
    trek = targer_a[3].text
    #if td_text[2]=='-' or td_text[5]=='-' or td_text[6]=='-':
#    if(td_text[5]==''):
#         td_text[5]='нету'
    #print(td_text[6])   
    
    url = 'https://1track.ru/ajax/tracking2'              
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    if td_text[5]==0:
         continue
    else:
         

         payload = {'tracks[0][track]': ''+ str(td_text[5]) +''}          
         data = requests.post(url, headers=headers, data=payload).json()   
         if data['status']=='ok':
                  jsonObj = data['JSON']      
         else :
              continue      
     #    
         df = json_normalize(jsonObj['data']['events']['data'])      
     #     
     #  
     #    #print (td_text[2]+" "+td_text[5]+" "+td_text[6]+" "+df['attribute.name'][0])  
         if(df['attribute.name'][0]=='Вручение адресату' or df['attribute.name'][0]=='Доставлено'):
              continue
         else:
              cursor.execute ("INSERT INTO yres_package ( name, track, number, point) VALUES (?, ?, ?, ?)",(str(td_text[1]),str(td_text[5]),str(td_text[6]),str(df['attribute.name'][0])))
         conn.commit()    
#    
#    

result = list()
#def get_posts(test): 
#    with conn:
#cursor.execute("SELECT * FROM yres_package  ")
       # track1[0] = cursor.execute("SELECT track FROM yres limit 1 ")
        #p = cursor.fetchone()
#        print(cursor.fetchall())   
#        p = cursor.fetchall()        
#result = cursor.fetchall()                  
#        print(result)
#        print(result)
#        print (type(result)) 
        #return result
  

        
#get_posts()     

conn.close()

#print(track1)
#print (result)
#def track(return1):


#url = 'https://1track.ru/ajax/tracking2'
#          
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#payload = {'tracks[0][track]': ''+ str(result) +''}
#          
#data = requests.post(url, headers=headers, data=payload).json()
#          
#jsonObj = data['JSON']
#df = json_normalize(jsonObj['data']['events']['data'])
#          
#print(grades.values())
#print (td_text[2]+" "+td_text[5]+" "+td_text[6]+" "+df['attribute.name'][0])
#
#
#conn = sqlite3.connect("bgg1.db")
#cursor = conn.cursor()
#cursor.execute ("INSERT INTO yres (point) VALUES (?)",(df['attribute.name'][0]))
#conn.commit() 
#cursor.execute("SELECT point FROM yres limit 1  ")
#conn.close()  
#track(get_posts())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SQL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#connection = sqlite3.connect("bgg1.db")
#cursor = connection.cursor()
## delete 
#cursor.execute("""DROP TABLE yres;""")
#sql_command = """
#CREATE TABLE yres ( 
#name   VARCHAR(100), 
#track  VARCHAR(100), 
#number VARCHAR(100),
#point  VARCHAR(100));"""
#
#cursor.execute(sql_command)
#
#sql_command = """INSERT INTO yres (name, track, number, point)
#    VALUES (?,?,?,?);""",(str(td_text[1]),str(td_text[5]),str(td_text[6]),str(df['attribute.name'][0]))
#cursor.execute(str(sql_command))
#
#connection.commit()
#
#connection.close()


#trek = targer_a[3].text
#print(trek)
#os.system('python create_db.py')





#links = soup.find_all("a")  # Look for all anchor tags
#tags = soup.find_all("li", "search-result") #Look for all tags with a specific class attribute
#tag = soup.find("div", id="title_page").find("h1",itemprop ="name") # Look for the tag with a specific ID attribute
#tags = soup.find("div", id="search-results").find_all("a", "external-links") #Look for nested patterns of tags (useful for finding generic elements, but only within a specific section of the page)

#print (r.status_code)
#print(r.text)
#if "blocked" in r.text:
#    print ("we've been blocked")
#print (r.headers.get("content-type", "unknown"))
#print(re.findall(r'\$[0-9,.]+', r.text))

#print(tag)
#text1 = tag.find("h1",itemprop ="name")
#mydivs = soup.findAll("div", {"class": "wsection wdata"})
#
#print(mydivs)




#inner_contents = soup.find("h1", itemprop="name").contents
#inner_text = soup.find("div", id="title_page").text.strip()
#inner_text = soup.find("div", id="title_page").text.strip().encode("utf-8")
#anchor_href = soup.find("a")["href"]


#for product in soup.find_all("div", "g-i-tile g-i-tile-catalog"):
#    product_title = product.find("a").text
#    product_price = product.find("div", "price") text
#    product_url = product.find("a")["href"]
#    print ("{} is selling for {} at {}".format(product_title, product_price, product_url))
