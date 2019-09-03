from string import Template

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

# Create message object using template string from message.txt
def create_temp_obj(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    return Template(template_file_content)