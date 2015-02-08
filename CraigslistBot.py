##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : Engine
#Version: 0.1
##########################

from emailSender import EmailSender
from bs4 import BeautifulSoup
import urllib.request

    
url = "http://seattle.craigslist.org/search/sss?sort=pricedsc&minAsk=10&maxAsk=10&query=gay"

request = urllib.request.urlopen(url)

soup = BeautifulSoup(request.read())

x = soup.find_all("a href")
print(x)

