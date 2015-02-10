
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
            return "\nPosting Title: " + self.getTitle() + "\nPost Price: " + str(self.getPrice()) + "\nPosting Date: " + str(self.getDate()) + "\nPosting ID: " + str(self.getID())


    #def __eq__(self, other):
        #return self.getID() == other.getID()

        #return str(self.getTitle())==(str(other.getTitle())) and self.getID()== other.getID()







def main():
    test0 = CraigslistPostObj(124586,"hellow","0060650","World")
    test = CraigslistPostObj(124586,"hellow","0060650","World")
    
    test1 = CraigslistPostObj(123456,"hey how","542582","wrod")
    test2 = CraigslistPostObj(123456,"hey how","0060650","World")

    print(test)
    eq = (test == test1)
    print(eq)
    eq1 = (test0.__eq__(test))
    print(eq1)
    
    



if __name__ == "__main__":
    main()
    
        

        
