import logging
import smtplib

from env_file import HOST, PORT
from helpers import get_contacts, create_temp_obj
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set loggin level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

MY_ADDRESS = 'my_address@example.com'
PASSWORD = 'mypassword'

logging.info(f'SMTP Address set: {MY_ADDRESS}')
logging.info(f'SMTP Password Set: {PASSWORD}')

def main(HOST, PORT):
    names, emails = get_contacts('contacts.txt') # read contacts
    message_template = create_temp_obj('message.txt')
    
    # set up the SMTP server
    s = smtplib.SMTP(host=HOST, port=PORT)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()