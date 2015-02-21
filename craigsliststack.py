##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : My Custom Stack data structure, i am considering implementing the
#        Implementing the Craigslist Object factory into the structure, into the add method
#Version: 0.1
##########################



class CraigslistStack(list):
    """This will by my self defined stack class, i did not like the built in to much
    bleh more fun and practice"""

   

    def __init__(self):
        super().__init__()
        
    def append(self, toPush):
        self.insert(len(self),toPush)

    def peek(self):
        return self[0]

    def pop(self):
        return self.remove(self[0])


