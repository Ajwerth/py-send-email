from string import Template

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