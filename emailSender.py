##########################
#Author: Danny Ly
#Date: 2/7/2014
#Desc. : This will act as our componenet to communicate to the
#mailing providers to send a message to the given email address
#Version: 0.1
##########################


import smtplib
from email.mime.text import MIMEText

class EmailSender:
    """Python class designed to send an email to the given address upon
notification"""
    def __init__(self):
        """Initilizer  """
        self.loginUser = "dannyly19@gmail.com" #just some variables login info
        self.password = "hondaper"

        self.sendTo = ["dannyly199@gmail.com", "danny19@uw.edu"] #recipeants that will be sent the message

        self.smtpAddress = "smtp.gmail.com:587" #the mailing host address, RELAY
 
        self.server = smtplib.SMTP(self.smtpAddress)#start the instance of the server


        self.server.starttls() #starts the instance of our server
        self.server.login(self.loginUser,self.password) #log into the provided account
      
        self.server.ehlo()

        
    def sendMessage(self, message):
        """This function will be the method to call when we need to send a message to the
    given email and send the given message"""


        """msg = MIMEText(fp.read())
      

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'The contents of %s' % textfile
        msg['From'] = me
        msg['To'] = you

        """

        self.server.sendmail(self.loginUser,self.sendTo,message)
        
    
def main():
    test = EmailSender()
    print("poassed 1")
    test.sendMessage("HEY fuck face")


if __name__ == "__main__":
    #python special variables, if the file is run then main's MAIN name variable will call THIS mains
    #other wise sets its MAIN variable to the calling files name
    main()


    
