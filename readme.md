# Py Email Send
Py email send, creates a list of specified names and emails addresses, 
and sends a pre drafted email to all the addresses in the list.

## Specifying Names and Emails
The names and email addresses can be specified in the `contacts.txt` file. 

### Formatting
One contact per line, with the **name** followed by a **space** and the **email address** 
`name name@address.com`

## Specifying Message
The message can be customized in the message.txt file. The message is generated using template strings. If you change the message some adjusting may be needed in the `email_send.py` file, for you're message to be sent correctly.

## SMTP Setup
The SMTP plugin requires the host and port number of the email service that you are using. As well as the address and password of the account that you are using.

## Config
You'll need to create your own env_file to define the `HOST`, `PORT`, `EMAIL` and `PASS` variables. I suggest also adding this file to your .gitignore so you don't upload personal credentials to github