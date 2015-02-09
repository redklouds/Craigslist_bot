##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : Engine
#Version: 0.1
##########################

from emailSender import EmailSender
from bs4 import BeautifulSoup
import urllib.request

    
url = "http://seattle.craigslist.org/search/sss?sort=pricedsc&minAsk=10&maxAsk=30&query=gay"


request = urllib.request.urlopen(url)

soup = BeautifulSoup(request.read())

x = soup('p',{"class":"row"})#access all p tags with attribute class = "row"

title = soup.title.contents[0]#get title of the Doc


#link = soup.find("link",{"href"})
IdOfListing = x[0].find('a', {"data-id"})
print(IdOfListing)
#print(link)
nameOfListing = x[0].find('a',{"class":"hdrlnk"}).contents[0]#contends shows all but the tags, and puts the information into a list,
#calling the list by the index shows what the tagsg AND the commands were wrapping
priceOfListing = x[0].find("span", {"class":"price"}).contents[0]
print("Title Of this search result: %s \nName Of listing: %s \nPrice Of the Listing: %s "%(title,nameOfListing, priceOfListing))#contents removes all the tags and attributes to give what they
#were wraping

print()
