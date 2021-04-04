
# coding: utf-8

# In[16]:


"""
Code to scrap headlines and corresponding url from "https://www.noaa.gov/"
"""

import urllib.request as ul
from bs4 import BeautifulSoup as soup
import csv

class Harvester:
    def  __init__(self,keyword):
        self.keyword = keyword

        # Accessing the url with  the specified location as search query
        
        url = 'https://search.usa.gov/search?utf8=%E2%9C%93&affiliate=noaa.gov&query='+keyword+'&commit='
        req = ul.Request(url, headers={'User-Agent': 'Chrome/87.0.4280.141'})
        client = ul.urlopen(req)
        htmldata = client.read()
        client.close()

        # Accessing the data
        
        pagesoup = soup(htmldata, "html.parser")
        itemlocator = pagesoup.findAll('div', {"class":"content-block-item result"})

        # Saving the data into  output.csv file
        
        filename = "output.csv"
        f = open(filename, "w", encoding="utf-8")
        writer = csv.writer(f)
        headers = "Headlines And Url\n"
        f.write(headers)

       

        # Adding the data to news.csv

        news=[]
        for items in itemlocator:   
            headlines = items.findAll('h4',{"class":"title"})
            url = items.findAll('div',{"class":"url"})
            for i in range(0,len(headlines)): 
                    news = headlines[i].text
                    url1 = url[i].text
                    f.write(news.replace(",", " "))
                    f.write(url1)
            print(news) 

        f.close()
        
keyword = input("Enter the location to search:")

data = Harvester(keyword)

