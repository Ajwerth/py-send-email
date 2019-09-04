import logging
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

# Set loggin level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

def get_contacts(filename):
    """ 
    Return two lists on of names and one of addresses, these are gotten from contacts.txt
    """
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])

    return names, emails


def create_temp_obj(filename):
    """
    Create a template object from message.txt
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    return Template(template_file_content)


def main(HOST, PORT, MY_ADDRESS, PASSWORD):
    """
    Main Email send function, this function creates the SMTP object, 
    and sends emails to contacts in the lists 
    """
    names, emails = get_contacts('contacts.txt') # read contacts
    message_template = create_temp_obj('message.txt')
    
    # set up the SMTP server
    logging.info(f"Creating SMTP object with Host:{HOST} and Port: {PORT}....")
    logging.info(f"Connecting to email server with {MY_ADDRESS} and {PASSWORD}...")
    s = smtplib.SMTP(host=HOST, port=PORT)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    

    # For each contact, send the email:
    for name, email in zip(names, emails):
        # create a message
        msg = MIMEMultipart()       

        # add in the actual person name to the message template
        message = message_template.substitute(RECIPIENT=name.title())

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