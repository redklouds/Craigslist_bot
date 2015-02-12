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
        self.insert(0,toPush)

    def peek(self):
        return self[0]

    def pop(self):
        return self.remove(self[0])


def main():
    x = CraigslistStack()
    x.append(5)
    print(x)
    x.append(7)
    print(x)
    print(x[0])
    print("peek: " + str(x.peek()))



if __name__ == "__main__":
    main()
