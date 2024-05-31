#oaaw hezg nisz gkpx 
import smtplib
try:
    server = smtplib.SMTP(host = 'smtp.gmail.com',port =587)
    server.starttls()
    recever_email = input("enter your email")
    sender_email ='singhm.techvala@gmail.com'
    passwd = 'oaaw hezg nisz gkpx'
    server.login(sender_email,password=passwd)
    subject = input("what is your problem")
    body = input("Toda details me batoo")
    message = f"subject: {subject}\n\n{boby}"
    server.sendmail(sender_email,recever_email,message)
    print("mene mail send krdi hai ")
    server.quit()
except Exception as e:
    print("mail send nhi huiii")      