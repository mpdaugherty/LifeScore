from email.message import Message
from subprocess import Popen, PIPE
import config

def sendmail(subject, body, to=config.USER_EMAIL, from=config.FROM_EMAIL):
    m = Message()
    m.add_header('To', to)
    m.add_header('Subject', subject)
    m.add_header('From', from)
    m.set_payload(ghp.message)

    sendmail = Popen('sendmail -t', stdin=PIPE, shell=True)
    sendmail.communicate(input=m.as_string())
