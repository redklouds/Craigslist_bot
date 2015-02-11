
##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : This will be the Object factory to create craigslist posting objects
#       to be used in putting into a stack for history tracking
#Version: 0.1
##########################


class CraigslistPostObj:

    def __init__(self, postTitle, postId, postPrice, postDate, postLink):
        """ returns an object of this posting"""
        self.title = postTitle
        self.price = postPrice
        self.date = postDate
        self.Id = postId
        self.link = postLink
        #return self how to return self?>

        
    def getId(self):
        return self.Id
    
    def getTitle(self):
        return self.title
    
    def getPrice(self):
        return self.price
    
    def getDate(self):
        return self.date
    
    def getLink(self):
        return self.link

    def setID(self,newId):
        #note sure if i will implemt setters
        self.Id = newId

    def setpostTitle(self, newTitle):
        self.title = newTitle

    def __str__(self):
        return "\nPosting Title: " + self.getTitle() + "\nPost Price: " + str(self.getPrice()) +\
               "\nPosting Date: " + str(self.getDate()) + "\nPosting ID: " + str(self.getId()) +\
               "\nPosting Link: " + str(self.getLink())

    def __eq__(self,other):
        if( isinstance(other,CraigslistPostObj)):
            return str(self.getId()) == str(other.getId())
        return "not same type, or not implemented" # python will look at other and se that either
    #other is not of type this or eq was not implemented






def main():
    test0 = CraigslistPostObj(124586,"hellow","0060650","World")
    test = CraigslistPostObj(124586,"hellow","0060650","World")
    
    test1 = CraigslistPostObj(123456,"hey how","542582","wrod")
    test2 = CraigslistPostObj(123456,"hey how","0060650","World")
    
    test6 = object()
    print(test)
 
    
    eq1 = (test0.__eq__(test))
    print(eq1)

    print(test0.__eq__(test6))
    
    



if __name__ == "__main__":
    main()
    
        

        
