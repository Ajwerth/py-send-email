import logging
from string import Template

# Set loggin level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# Create a list of names and emails from contacts.txt
def get_contacts(filename):
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])

            logging.info(f'Names are {names}')
            logging.info(f'Emails are {emails}')
    return names, emails

