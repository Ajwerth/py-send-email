import logging
from helpers import get_contacts

# Set loggin level
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

get_contacts('contacts.txt')