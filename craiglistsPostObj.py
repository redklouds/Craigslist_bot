
##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : This will be the Object factory to create craigslist posting objects
#       to be used in putting into a stack for history tracking
#Version: 0.1
##########################


class CraigslistPostObj:

    def __init__(self,postID, postTitle, postPrice, postDate):
        """ returns an object of this posting"""
        self.title = postTitle
        self.price = postPrice
        self.date = postDate
        self.ID = postID
        #return self how to return self?>


        
    def getID(self):
        return self.ID
    def getTitle(self):
        return self.title
    def getPrice(self):
        return self.price
    def getDate(self):
        return self.date

    def __str__(self):
        if(self == None):
            return "README.md    #$#################################################################################"
        else:
            return "\nPosting Title: " + self.getTitle() + "\nPost Price: " + self.getPrice() + "\nPosting Date: " + self.getDate() + "\nPosting ID: " + self.getID()


    #def __eq__(self, other):
        
        #if(other == None):
            #raise Exception("do not pass a Null object please")


        #return str(self.getTitle())==(str(other.getTitle())) and self.getID()== other.getID()







def main():
    test = CraigslistPostObj(124586,"hellow","0060650","World")
    test1 = CraigslistPostObj(123456,"hey how","542582","wrod")
    test2 = CraigslistPostObj(123456,"hey how","0060650","World")
    
    print(test)
    print(test1)

    #print(test1 ==(test2))




if __name__ == "__main__":
    main()
    
        

        
