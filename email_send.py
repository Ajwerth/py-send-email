import logging
import smtplib

from helpers import get_contacts, create_temp_obj
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set loggin level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

MY_ADDRESS = 'my_address@example.comm'
PASSWORD = 'mypassword'
logging.info(f'SMTP Address set: {MY_ADDRESS}')
logging.info(f'SMTP Password Set: {PASSWORD}')

# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

create_temp_obj('message.txt')
get_contacts('contacts.txt')