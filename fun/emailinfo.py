import smtplib
import email.utils
from email.mime.text import MIMEText

# Ask for user input for various details about the exam session
to_email = input("Candidate's email?")  # email address of the candidate
servername = ""  # address of the email server
username = ""  # username for the email account
password = ""  # password for the email account
CandidateName = input("Candidate's name?")  # name of the candidate
testpin = input("Candidate's pin?")  # exam session PIN
zoomlink = input("What is the zoom link for the session?")  # link to the Zoom session for the exam
testtime = input("What time is the person test time, in 15 minutes")  # exam start time
GLAARGID = input("What is your session ID?")  # ID for the exam session

# Create the email message using a template and the details above
lemsg = """Hi {Candidate}!

Just following up with you regarding some instructions on joining for your amateur radio exam session tomorrow.

{pin}

And finally, join the Zoom video conferencing session at the following link:

{zoom}

As there are also other candidates in this session, we are tentatively assigning you a test window of {testtime} PM EDT. 
Please let us know if this does not work well, and we can arrange something else. 

Please let me know if you have any questions or if you have any change of plans!

Grant Baron
YARC VE Team

""".format(length='multi-line', Candidate=CandidateName, pin=testpin, zoom=zoomlink, testtime=testtime)

# Ask for confirmation from the user that the message is correct
Join = input(lemsg + ' Message looks good?').lower()
if Join.startswith('y'):
    goodmsg = lemsg
elif Join.lower().startswith("n"):
    print("Let's try again")
    exit()

# Create the email message object
msg = MIMEText(goodmsg)  # create a MIME message object containing the email text
msg.set_unixfrom('author')  # set the "from" address
msg['To'] = email.utils.formataddr((CandidateName, to_email))  # set the "to" address
msg['From'] = email.utils.formataddr(('VE Team', 'exam@test.com'))  # set the "from" address
msg['Subject'] = '#' + GLAARGID + ' Exam'  # set the subject

# Set up an SMTP connection to the email server and send the email message
server = smtplib.SMTP(servername)
try:
    server.set_debuglevel(True)  # enable debugging output
    server.ehlo()  # identify ourselves to the email server
    if server.has_extn('STARTTLS'):  # check if we can encrypt the session
        server.starttls()  # encrypt the session using STARTTLS
        server.ehlo()  # re-identify ourselves over the encrypted session
    server.login(username, password)  # log in to the email account
    server.sendmail('exam@test.com', [to_email], msg.as_string())  # send the email message
finally:
    server.quit()  # close the SMTP connection to the email server
