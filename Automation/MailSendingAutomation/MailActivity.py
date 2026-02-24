import smtplib
from email.message import EmailMessage

def send_mail(sender,app_password,receiver,subject,body):
     msg=EmailMessage()
     
     msg["From"]=sender
     msg["To"]=receiver
     msg["Subject"]=subject
     
     msg.set_content(body)
     
     smtp=smtplib.SMTP_SSL("smtp.gmail.com",465);
     
     smtp.login(sender,app_password)
     
     smtp.send_message(msg)
     
     smtp.quit()  
     

def main():
    sender_email="riddhianujasonawane@gmail.com"
    app_password="sfdi ktyq vwik dnvr"
    receiver_email="kedarlute@gmail.com"
    subject="Test Mail from Python Script"
    body="""Jay Ganesh,
    This is a test email sent using  Marvellous Python"""
    
    send_mail(sender_email,app_password,receiver_email,subject,body)
    print("Marvellous mail sent successfull")
    
if __name__ == '__main__':
    main()
    