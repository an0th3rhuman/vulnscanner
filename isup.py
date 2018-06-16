import smtplib
import pyping

error_msg = "Server is down!"
Server_ping = pyping.ping('google.com')

if Server_ping.ret_code == 0:
    print("Server is up!")
else:
     mail=smtplib.SMTP('smtp.gmail.com',587)
     mail.ehlo()
     mail.starttls()
     mail.login('','')
     mail.sendmail('email2raghul@gmail.com','email2sumathi@gmail.com',error_msg)
     mail.close()