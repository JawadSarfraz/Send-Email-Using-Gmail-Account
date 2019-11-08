import smtplib
import imaplib
from credentials import Singleton

#SENDING EMAIL FUNCTION
def sendEmail(senderEmailAddr, subject, msgBody):
    try:
        server = smtplib.SMTP(obj.getInstance().smtpUrl) #connecting server
        server.ehlo()
        server.starttls()
        try: #login credentials checking
            server.login(obj.getInstance().emailAddr,obj.getInstance().password) # tryig to login
            message = 'Subject: {}\n\n{}'.format(subject, msgBody)
            try: #sender email checking
                server.sendmail(obj.getInstance().emailAddr, senderEmailAddr, message) # sending message to sender
                print "Email Sent Successfully!"
            except:
                print "Incorrect Sender Email. Email Didn't Sent..!"
        except:
            print "Login Unsuccessful. Email Didn't Sent..!" 
        server.quit()
    except:
        print "Problem in establishing connection. Email Didn't Sent..!"

#SEARCHING EMAIL FUNCTION FORM SUBJECT OR BODY
def searchEmail(searchText):
    try:    # to catch connection Failure Error
        mail = imaplib.IMAP4_SSL(obj.getInstance().imapUrl)

        mail.login(obj.getInstance().emailAddr,obj.getInstance().password)
        mail.list()
        # Out: list of "folders" aka labels in gmail.
        mail.select("inbox") # connect to inbox.
        try: #to catch Query error to access gmail
            result, data = mail.search(None, '(OR SUBJECT {} BODY {})'.format(searchText,searchText)) # search through Subject and Body
            getData = data[0] # data is a list.
            ls = getData.split() # ids is a space separated string, ls has all id's number of matches based on query
            print "There are ",len(ls)," inbox emails match the cases"

            if not ls:
                print("Message not found..!")
            else:
                print "Latest Email is Printed...! \n"
                latest_email_id = ls[-0] # get the latest
                result, data = mail.fetch(latest_email_id, "(UID BODY[TEXT])") # fetch the email's BODY
                raw_email = data[0][1] # here's the body, which is raw text of the whole email
                
                print(raw_email)
        except:
            print "Error in Query"
        mail.shutdown()
        #return raw_email
    except:
        print "Connection Failed..."

if __name__ == '__main__':
    
    obj = Singleton()
    while 1==1:
        choice = raw_input("\n1 --> search text in Email *** 2--> Sent Mail *** anyother key to exit : ");
        if choice == "1":
            searchText = raw_input("\nEnter whole subject or part of subject : ")
            # function call for searching email by email title and subject
            searchEmail(searchText)
        elif choice == "2":
            emailAddr = raw_input("\nEnter receipt email address : ") #Receipt's Email Address
            subject   = raw_input("Enter Subject : ") # Title of the email
            msgBody   = raw_input("Enter message : ") # Message given to them
            sendEmail(emailAddr, subject, msgBody)
        else:
            break