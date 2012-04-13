from email.message import Message
from subprocess import Popen, PIPE
from config import USER_EMAIL, FROM_EMAIL

def sendmail(subject, body, to=USER_EMAIL, from_addr=FROM_EMAIL):
    m = Message()
    m.add_header('To', to)
    m.add_header('Subject', subject)
    m.add_header('From', from_addr)
    m.set_payload(body)

    sendmail = Popen('sendmail -t', stdin=PIPE, shell=True)
    sendmail.communicate(input=m.as_string())
