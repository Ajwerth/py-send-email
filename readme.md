# Py Email Send
    Py email send, creates a list of specified names and emails addresses, and sends a pre drafted email to all the addresses in the list.

## Specifying Names and Emails
    The names and email addresses can be specified in the contacts.txt file. There can only be one contact per line, formatted with the *name* followed by a *space* and the *email address*
    `name name@address.com`

## Specifying Message
    The message can be customized in the message.txt file. The message is generated using template strings. If you change the message some adjusting may be needed in the email_send.py fil, for you're message to be sent correctly.