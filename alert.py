import smtplib

#create a server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#authenticate the user
server.login("emailid1","password") #add email id and password
# .sendmail(from,to,message)
server.sendmail("emailid1", "emailid2","Depression diagnosed")
server.quit()
