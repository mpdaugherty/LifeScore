from email.message import Message
from subprocess import Popen, PIPE
from config import USER_EMAIL, FROM_EMAIL, EMAIL_METHOD, AWS_KEY, AWS_SECRET
from sesmail.amazon_sender import AmazonSender

def sendmail(subject, body, to=USER_EMAIL, from_addr=FROM_EMAIL):
    if EMAIL_METHOD is 'SES':
        sendmail_ses(subject, body, to, from_addr)
    else:
        sendmail_sendmail(subject, body, to, from_addr)

def sendmail_ses(subject, body, to=USER_EMAIL, from_addr=FROM_EMAIL):
    A = AmazonSender(AWS_KEY, AWS_SECRET)
    A.send_email(from_addr, to, subject, body)

def sendmail_sendmail(subject, body, to=USER_EMAIL, from_addr=FROM_EMAIL):
    m = Message()
    m.add_header('To', to)
    m.add_header('Subject', subject)
    m.add_header('From', from_addr)
    m.set_payload(body)

    sendmail = Popen('sendmail -t', stdin=PIPE, shell=True)
    sendmail.communicate(input=m.as_string())
