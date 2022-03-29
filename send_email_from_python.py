#prerequisite:
#to get started I would suggest create a new gmail account and then try this as to make it work we need to change the security settings.
#Open the below link and turned on less secure app setting
#https://myaccount.google.com/lesssecureapps

# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import getpass #added for password


toaddr = input("Please provide toaddr")
fromaddr = input("Please provide fromaddr")


fromaddr = fromaddr
toaddr = toaddr

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

#Many programs that interact with the user via the terminal need to ask the user for password values without showing what the user types on the screen.
#The getpass module provides a portable way to handle such password prompts securely.
pwd = getpass.getpass(prompt='Password ?')

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the subject 
msg['Subject'] = "Email testing from Python"

# string to store the body of the mail 
body = "<b>Welcome to the python programming to send an email from your gmail account.</b>"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'html')) 


# open the file to be sent as an attachment
filename = "log.txt"
attachment = open("c:\log.txt", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 


# Authentication 
s.login(fromaddr, pwd) 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 
