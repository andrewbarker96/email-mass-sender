import pandas as pd
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

# Load the Recipients
recipient_data = pd.read_csv('recipientList.csv') # csv file uses "fullName", "email" as headers

# Load the CC List
cc = list(pd.read_csv('ccList.csv')['email'])  # List of CC recipients
cc_string = ', '.join(cc)  # Convert list to comma-separated string for the 'Cc' field

subject = os.getenv('EMAIL_SUBJECT')
body = open('body.html').read()

def sendMassEmail(subject, body, recipient_data):
    try:
        # Connect to Server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() # Secure the connection
        server.login(email_address, email_password)
        
        for index, row in recipient_data.iterrows():
            full_name = row['fullName']
            first_name = full_name.split(' ')[0]
            recipient_email = row['email']
            
            # Incorporate the first name into the email
            message = f'Dear {first_name},<br>{body}'
            
            # Create Message
            msg = MIMEMultipart()
            msg['From'] = email_address
            msg['To'] = recipient_email
            msg['Cc'] = cc_string
            msg['Subject'] = subject
            
            # Attach the message to the email
            msg.attach(MIMEText(message, 'html'))
            
            # Send Email
            server.sendmail(email_address, recipient_email, msg.as_string())
            print(f'Email sent to {recipient_email}')
            
        # Close the server
        server.quit()
    
    except Exception as e:
        print(f'Error: {e}')
        print(f'Failed to send email. Error: {e}')

sendMassEmail(subject, body, recipient_data)
    
