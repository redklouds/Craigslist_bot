##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : Engine
#Version: 0.1
##########################
"""

I left off at searching how to print a list of objects the pythonic way
"""
from emailsender import EmailSender
from bs4 import BeautifulSoup
import urllib.request, time
from craigslistpostobj import CraigslistPostObj
from craigsliststack import CraigslistStack

class CraigslistBot():

    """
    NOTES: BUGS#######################
    ***********BUG DOES NOT CORRECTLY ADD THE FIRST LISTING IN IT. 

    
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
        print(len(soup))
        #searchTitle = bsObj.title.contents[0]

        for listing in range(0, len(bsObj) -1):
            
            createObj = self.__buildListingObj(bsObj,listing)
            print(str(listing) + "th object to add to stack" + createObj.__str__())
            print("length" + str(len(bsObj)))
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
        
        
      
        while(True):

                    
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
                self.stack.append(listingObj)
                self.mailMan.sendMessage(
                    ["dannyly199@gmail.com","danny19@uw.edu"],
                    "We have a UPDATE\n" + listingObj.__str__())
                
                print("they are NOT the same")
                
            time.sleep(120)
            
            
        
            

        
def main():
    url = input(str("Please enter the craigslsit URL you wish to watch: "))
    
    url0 = "http://seattle.craigslist.org/search/sss?sort=rel&minAsk=10&maxAsk=15&query=monitor"

    notify = ["Dannyly199@gmail.com","danny19@uw.edu"]
    
    application = CraigslistBot(url, notify)
    application.run()



if __name__ == "__main__":
    main()






    
"""    
    def start(self):
        
        Just using this function as a entry/starting point for program run 

        soupGetDom = BeautifulSoup(self.request.read())#reads from the URL and gets the document online into DOM

        #soup = soupGetDom('p', {"class": "row"}) # finds p tags (paragraph) with attribute "class: row" attached to them


        searchKeyWord = soupGetDom.title.contents[0] # using BeautifulSoup find command to find the DOC title and gets its contents
        ## Contents gets all the text that the tags are wrapping

        print("key word for this Search: %s"%(searchKeyWord))
        
        for posting in range(0, len(soup)-1):


            listingObj = self.getdata(soupGetDom, posting)

            #self.DBListing.push(listingObj)
            self.stack.append(listingObj)
"""
"""
soup = soupGetDom('p', {"class": "row"}) # finds p tags (paragraph) with attribute "class: row" attached to them

timeOfListing = soup[0].find("time").contents[0]
listingLink = soup[0].find('a')["href"]

listingID = soup[0]['data-pid']

nameOfListing = soup[0].find('a',{"class":"hdrlnk"}).contents[0]

priceOfListing = soup[0].find("span", {"class":"price"}).contents[0]



#print("\nName Of listing: %s \nPrice Of the Listing: %s\nTime Of Listing: %s \nListing ID: %s "%(nameOfListing, priceOfListing, timeOfListing, listingID))#contents removes all the tags and attributes to give what they

listingObj = CraigslistPostObj(nameOfListing,
                               listingID,
                               priceOfListing,
                               timeOfListing,
                               self.baseURL + listingLink)
                               """




"""
timeOfListing = soup[posting].find("time").contents[0]

listingID = soup[posting]['data-pid']


listingLink = soup[posting].find('a')["href"] # get all a href tags
#print(listingLink['href']) # from the list of hred get the value of 'href'



nameOfListing = soup[posting].find('a',{"class":"hdrlnk"}).contents[0] #get title

priceOfListing = soup[posting].find("span", {"class":"price"}).contents[0]



#print("\nName Of listing: %s \nPrice Of the Listing: %s\nTime Of Listing: %s \nListing ID: %s "%(nameOfListing, priceOfListing, timeOfListing, listingID))#contents removes all the tags and attributes to give what they

listingObj = CraigslistPostObj(nameOfListing,
                               listingID,
                               priceOfListing,
                               timeOfListing,
                               self.baseURL +listingLink)
"""

            

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

