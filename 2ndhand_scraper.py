#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import urllib.request
import sys
import requests
import math
import pandas as pd
import re
import numpy as np
import schedule
import datetime
import time
from IPython.display import display, Image


# In[ ]:


for i in range(0,100): #number of pages
#for i in range(0,10):# for test purpose
   
    i += 1  #page increment +1 
    url = ":::::URL::::::"+str(i)+"&page_size=50"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tag=soup.findAll("article", {"class":"listing"}) #find all tag under Article and class listing
    pricetag=soup.findAll("div", {"class":"listing__price"}) #find all tag under Article and class listing
    
    #retrieved all information under tag name article
    for getall in tag:
        getallurl=getall.get('data-url')
        getallmake= getall.get('data-make')
        getallmodel=getall.get('data-model')
        getallyear=getall.get('data-year')
        getallmileage=getall.get('data-mileage')
        getalltransmission=getall.get('data-transmission')
        getallinstallment=getall.get('data-installment')
        #getallprice=getall.get_text('data-price')
        
        #Append string into list
        model.append(getallmodel)
        make.append(getallmake)
        year.append(getallyear)
        installment.append(getallinstallment)
        mileage.append(getallmileage)
        transmission.append(getalltransmission)
        dataurl.append(getallurl)
    
#     #retrieved all price stored under listing__price
    for getprice in soup.findAll("div", {"class":"listing__price"}):
        if ("div", {"class":"listing__price"}):
            getallprice=getprice.get_text()
        else:
            getallprice="no value"
        price.append(getallprice) 
print(url)




#     for getprice in pricetag:
#         getallprice=getprice.get_text()
#         #Append string into list
#         price.append(getallprice)

# #print(price) #test print
df = pd.DataFrame({'make':make,'model':model,'year':year,'mileage':mileage
                    ,'transmission':transmission,'installment':installment})#,'price':price})
#df2 = pd.DataFrame({'price':price})
df.count()
df


# In[9]:


### this is how the html looklike


# In[10]:


display(Image(filename='/screenshot.png'))


# In[ ]:


df2.to_csv("carprice.csv",encoding='utf-8')
df.to_csv("cardetail.csv",encoding='utf-8')

