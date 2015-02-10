##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : Engine
#Version: 0.1
##########################
"""

I left off at searching how to print a list of objects the pythonic way
"""
from emailSender import EmailSender
from bs4 import BeautifulSoup
import urllib.request, time
from craiglistsPostObj import CraigslistPostObj


from craigslistStack import CraigslistStack

class CraigslistBot():

    """
    NOTES: BUGS#######################
    1)when passing s url without giving price perameters, it will crash


    NOTES: Still needs development################
    1)
    """

    def __init__(self,URL, notifyAddr, explicitKeywords = None):
        """URL: craigslist link including price parameters entered.
           notifyAddr: Passed as an list if there are 2 or more recipiants, else accepts a string
           explicitKeywords: if there are specific keywords to include in the title of the posting list them here as a list if two or more

    
        """
        #####   Variables
        self.url = URL
        self.notifyAddr = notifyAddr
        self.explicitKeywords = explicitKeywords

        self.mailMan = EmailSender() #create the instance of EmailSender to send notifications to email

        self.request = urllib.request.urlopen(self.url)
        
        self.DBListing = CraigslistStack()

        self.stack = list()
    
    def start(self):
        """Just using this function as a entry/starting point for program run """

        soupGetDom = BeautifulSoup(self.request.read())#reads from the URL and gets the document online into DOM

        soup = soupGetDom('p', {"class": "row"}) # finds p tags (paragraph) with attribute "class: row" attached to them


        searchKeyWord = soupGetDom.title.contents[0] # using BeautifulSoup find command to find the DOC title and gets its contents
        ## Contents gets all the text that the tags are wrapping

        print("key word for this Search: %s"%(searchKeyWord))
        
        for posting in range(0, len(soup)-1):
            
            timeOfListing = soup[posting].find("time").contents[0]
            
            listingID = soup[posting]['data-pid']
            
            nameOfListing = soup[posting].find('a',{"class":"hdrlnk"}).contents[0]
            
            priceOfListing = soup[posting].find("span", {"class":"price"}).contents[0]
            
            #print("\nName Of listing: %s \nPrice Of the Listing: %s\nTime Of Listing: %s \nListing ID: %s "%(nameOfListing, priceOfListing, timeOfListing, listingID))#contents removes all the tags and attributes to give what they
            listingObj = CraigslistPostObj(listingID,nameOfListing,priceOfListing,timeOfListing)

            #self.DBListing.push(listingObj)
            self.stack.append(listingObj)

            
    def run(self):
        
        request = urllib.request.urlopen(self.url)
        
        soupGetDom = BeautifulSoup(request.read())#reads from the URL and gets the document online into DOM

        soup = soupGetDom('p', {"class": "row"}) # finds p tags (paragraph) with attribute "class: row" attached to them

        while(True):

            
            timeOfListing = soup[0].find("time").contents[0]
            
            listingID = soup[0]['data-pid']
            
            nameOfListing = soup[0].find('a',{"class":"hdrlnk"}).contents[0]
            
            priceOfListing = soup[0].find("span", {"class":"price"}).contents[0]
            


            #print("\nName Of listing: %s \nPrice Of the Listing: %s\nTime Of Listing: %s \nListing ID: %s "%(nameOfListing, priceOfListing, timeOfListing, listingID))#contents removes all the tags and attributes to give what they

            listingObj = CraigslistPostObj(listingID,nameOfListing,priceOfListing,timeOfListing)

            print(listingObj.__str__())
            print(self.stack[0])


            if(self.stack[0].__eq__( listingObj)):
                print("they are the same")

                
            else:
                print("they are NOT the same")
            time.sleep(60)
            
            
        
            

        
def main():
    
    url = "http://seattle.craigslist.org/search/sss?sort=pricedsc&minAsk=10&maxAsk=30&query=gay"
    url1 ="http://seattle.craigslist.org/search/sss?sort=rel&minAsk=10&maxAsk=900000&query=s2000"
    notify = ["Dannyly199@gmail.com","danny19@uw.edu"]
    application = CraigslistBot(url1, notify)
    application.start()
    application.run()

if __name__ == "__main__":
    main()

"""
    
url = "http://seattle.craigslist.org/search/sss?sort=pricedsc&minAsk=10&maxAsk=30&query=gay"


request = urllib.request.urlopen(url)

soup = BeautifulSoup(request.read())

x = soup('p',{"class":"row"})#access all p tags with attribute class = "row"

title = soup.title.contents[0]#get title of the Doc

getListID = x[0]
listingID = getListID['data-pid']


cont = 0
for line in x[0]:
    print("LINE\n",line,"\n")
print(x[0],len(x[0]))

listofShit =''


print(len(x[0]))

print("da LIST:", listofShit)


#print(x[0]["data-ids"])

#link = soup.find("link",{"href"})
timeOfListing = x[0].find("time").contents[0]

#print(link)
nameOfListing = x[0].find('a',{"class":"hdrlnk"}).contents[0]#contends shows all but the tags, and puts the information into a list,
#calling the list by the index shows what the tagsg AND the commands were wrapping
priceOfListing = x[0].find("span", {"class":"price"}).contents[0]
print("Title Of this search result: %s \nName Of listing: %s \nPrice Of the Listing: %s\nTime Of Listing: %s \nListing ID: %s "%(title,nameOfListing, priceOfListing, timeOfListing, listingID))#contents removes all the tags and attributes to give what they
#were wraping

for i in range(0, len(x)-1):
        #link = soup.find("link",{"href"})
    timeOfListing = x[i].find("time").contents[0]

    #print(link)
    nameOfListing = x[i].find('a',{"class":"hdrlnk"}).contents[0]#contends shows all but the tags, and puts the information into a list,
    #calling the list by the index shows what the tagsg AND the commands were wrapping
    priceOfListing = x[i].find("span", {"class":"price"}).contents[0]
    print("Title Of this search result: %s \nName Of listing: %s \nPrice Of the Listing: %s\nTime Of Listing: %s \nListing ID: %s "%(title,nameOfListing, priceOfListing, timeOfListing, listingID))#contents removes all the tags and attributes to give what they
    #were wraping

"""

