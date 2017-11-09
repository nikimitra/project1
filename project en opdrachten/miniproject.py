import smtplib
import datetime
import random
import re

class MailAuthentication:
    def sendPassWord(self,emailAddress,PassWord):
        self.emailAdress=emailAddress
        self.passWordord=PassWord
        PassWord = "wachtwoord"
        emailAddress = smtplib.SMTP( 'smtp.gmail.com', 587 )
        emailAddress.ehlo()
        emailAddress.starttls()
        emailAddress.login( 'ns.fietsstalling.miniproject@gmail.com', 'nsfiets1234$' )
        emailAddress.sendmail( 'ns.fietsstalling.miniproject@gmail.com', 'destination@gmail.com', PassWord,today )
        emailAddress.close()
        print( "Er word een email met wachtwoord gestuurd" )

    def sendNotification(self,alert_emailAddress):
        self.emailAdress=alert_emailAddress

        while  True:            #als een fiets opgehaald word

            alert_emailAddress = "uw fiets is opgehaald op "
            emailAddress = smtplib.SMTP( 'smtp.gmail.com', 587 )
            emailAddress.ehlo()
            emailAddress.starttls()
            emailAddress.login( 'email@gmail.com', 'wachtwoord' )
            emailAddress.sendmail( 'source@gmail.com', 'destination@gmail.com', alert_emailAddress, today )
            emailAddress.close()

class PassWord():

    def generatePassWord(self,PassWord):
        self.PassWord=PassWord
        PassWord=''
        letters='abcdefghijklmnopqrstuvwxyz'
        PwLen=9
        for i in range (PwLen):
            next_index=random.randrange(len(letters))
            PassWord=PassWord+letters[next_index]
    #een of twee letters worden met getallen vervagen
        for i in range (1,3):
            replace_index=random.randrange(len(PassWord)//2)
            PassWord=PassWord[0:replace_index]+str(random.randrange(10))


p= input("Input your password")
x = True
while x:
    if (len(p)<9 or len(p)>10):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")


today = datetime.date.today()
