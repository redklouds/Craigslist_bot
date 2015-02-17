##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : Engine
#Version: 0.1
##########################
"""

I left off at searching how to print a list of objects the pythonic way
"""
import urllib.request, time, random
from emailsender import EmailSender
from bs4 import BeautifulSoup
from craigslistpostobj import CraigslistPostObj
from craigsliststack import CraigslistStack

class CraigslistBot():

    """
    NOTES: BUGS#######################
    ***********BUG DOES NOT CORRECTLY ADD THE FIRST LISTING IN IT. 
#Note to self, need to make sure i change the collections tructure to using a QUeue instead of a stack,
#the stack does not allow me to know the first item added**** self notes****

    
    1)when passing s url without giving price perameters, it will crash

    2)Need to add a try and catch to catch python winError 10060, connection time out and reconnect if this happens
    
    
    NOTES: Still needs development################
    1)
    """

    def __init__(self,URL, notifyAddr, explicitKeywords = None):
        """URL: craigslist link including price parameters entered.
           notifyAddr: Passed as an list if there are 2 or more /
           recipiants, else accepts a stringexplicitKeywords: if /
           there are specific keywords to include in the title of/
           the posting list them here as a list if two or more
        """
        #####   Variables
        self.url = URL
        
        self.baseURL = URL[:URL.find("org")+3] # accessing substring from start of URL to end of 'org' domain

        self.notifyAddr = notifyAddr # address to send notifications to
        
        self.explicitKeywords = explicitKeywords #NOT implemented yet

        self.mailMan = EmailSender() #create the instance of EmailSender to send notifications to email

        #self.request = urllib.request.urlopen(self.url)
        
   
        
        #self.stack = list()
        self.stack = CraigslistStack()


    def __buildInitalListing(self):
        """ Will build a stack with the current listed postings,
        Creates a craiglist object, then appends them to the stack"""

        request = urllib.request.urlopen(self.url)

        bsObj = BeautifulSoup(request.read())

        soup = bsObj('p', {"class": "row"})
       # print(len(soup))
        #searchTitle = bsObj.title.contents[0]

        for listing in range(0, len(soup) -1):
            
            createObj = self.__buildListingObj(bsObj,listing)
           # print(str(listing) + "th object to add to stack" + createObj.__str__())
           # print("length" + str(len(bsObj)))
            self.stack.append(createObj)

    def __buildListingObj(self, DOM, index = 0):
        
        """Testing this method to optimize the code
        This method is reused whenever we need to parse the tags and create a listing Object from that imformation"""


    
        soup = DOM('p', {"class": "row"}) # finds p tags (paragraph) with attribute "class: row" attached to them

        timeOfListing = soup[index].find("time").contents[0] #gets the date of the listing
        listingLink = soup[index].find('a')["href"] #get's the href link address tot he listing
     
        listingID = soup[index]['data-pid'] #gets the postings ID this is used to identify if two post are identical or not.
        
        nameOfListing = soup[index].find('a',{"class":"hdrlnk"}).contents[0] # gets the name of the listing
        
        priceOfListing = soup[index].find("span", {"class":"price"}).contents[0] #get the price of the listing
        

        return CraigslistPostObj(nameOfListing,
                                       listingID,
                                       priceOfListing,
                                       timeOfListing,
                                       self.baseURL + listingLink) # returns an object of type CraigslistPostingObj

        
    def run(self):
        self.__buildInitalListing()
        sleepTime = 260
        
      
        while(True):

            try:
                request = urllib.request.urlopen(self.url)
            
                soupGetDom = BeautifulSoup(request.read())#reads from the URL and gets the document online into DOM
                

                listingObj = self.__buildListingObj(soupGetDom)#testing!!!
                

                print("This is the current listing being checked online:"\
                      + listingObj.__str__())
                print("\n")
                print("THIS IS THE CURRENT ITEM AT THE BEGINNING OF THE STACK"\
                      + self.stack[0].__str__())
                print("\n")

                                


                if(self.stack.peek().__eq__( listingObj)):
                    print("they are the same")
                    #emailSender.sendMessage(["dannyly199@gmail.com","danny19@uw.edu"],
                    #"We have a update\n" + listingObj.__str__())
                    #emailSender.sendMessage(["dannyly199@gmail.com","danny19@uw.edu"], "same posting" + listingObj.__str__())
                    
                else:
                    self.stack.insert(0, listingObj)

                   # self.stack.append(listingObj)
                    self.mailMan.sendMessage(
                        ["dannyly199@gmail.com","danny19@uw.edu"],
                        "We have a UPDATE\n" + listingObj.__str__())
                    
                    print("they are NOT the same")

                    
            except Exception as e:
                print("\n\n\n   THERE WAS AN ERROR OR SOME TIMEOUT OCCURED")
                sleepTime = random.randint(0,sleepTime) + sleepTime

                self.mailMan.sendMessage(["dannyly199@gmail.com"],"WE have encountered a problem")
            time.sleep(sleepTime)
            
            
            self.mailMan.sendMessage(
                        ["dannyly199@gmail.com","danny19@uw.edu"],
                        "I'm still  here and running ")
        
            

        
def main():
    url = input(str("Please enter the craigslsit URL you wish to watch: "))
    
    url0 = "http://seattle.craigslist.org/search/sss?sort=rel&minAsk=10&maxAsk=15&query=monitor"

    notify = ["Dannyly199@gmail.com","danny19@uw.edu"]
    
    application = CraigslistBot(url, notify)
    application.run()



if __name__ == "__main__":
    main()



