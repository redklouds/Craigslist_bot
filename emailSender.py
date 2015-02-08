import smtplib
from email.mime.text import MIMEText

class EmailSender:
    """Python class designed to send an email to the given address upon
notification"""
    def __init__(self):
        self.loginUser = "dannyly19@gmail.com"
        self.password = "hondaper"

        self.sendTo = ["dannyly199@gmail.com", "danny19@uw.edu"]

        self.smtpAddress = "smtp.gmail.com:587"
 
        self.server = smtplib.SMTP(self.smtpAddress)#start the instance of the server


        self.server.starttls()
        self.server.login(self.loginUser,self.password) #log into the provided account
      
        self.server.ehlo()

        
    def sendMessage(self, message):
        """This function will be the method to call when we need to send a message to the
    given email and send the given message"""
        #msg = MIMEText()

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
    print("passed 2")
main()
