import random

# Define a variable ticnumber and set it to 0
ticnumber = 0

# Ask the user to input a ticket number and keep in ticnumber
ticnumber = input("Enter Ticket number:")

# Ask the user to input a name and keep it in the 'NAME' variable
NAME = input("What is the persons first name?:")

# Ask the user to input whether the ticket was solved or escalated and keep in the 'SORE' variable
SORE = input("Enter S for solved or E for escalated:")

# Define a URL for the CSAT survey using the 'ticnumber' variable
CSAT = f"https://test.com/{ticnumber}"

# Define a message for when a ticket is solved
ASolved = f"Hi, {NAME} I am about to solve ticket. If you need any further help please let us know! About an hour after " \
     f"the ticket closes, you will receive an email with a short satisfaction survey on how I was able to assist " \
     f"you today. We welcome and appreciate your feedback! You can find your ticket at {CSAT}"

# Define another message for when a ticket is solved
BSolved = f"Hey {NAME}, Just a little reminder of the CSAT survey you'll receive about an hour after I close out the " \
     f"ticket.  If you would like to review the ticket, please click the following {CSAT}. Our team welcomes and " \
     f"appreciates feedback! "

# Define a message for when a ticket is escalated
AEscalated = f"Hey, {NAME}, it's looking like I am going to be forwarding this ticket to a Corporate IT Engineer, " \
             f"for them to take a look, in the meantime, you can follow this request at {CSAT}"

# Define another message for when a ticket is escalated
BEscalated = f"{NAME}, I took a look at your request, and I will have to forward it on to our Corporate IT Engineers," \
     f"They will reach out when they can, you can follow this ticket at {CSAT}"

# If the ticket was solved, randomly choose between ASolved and BSolved
if SORE in 'S':
    ans = random.choice([ASolved, BSolved])
    print(ans)
# If the ticket was escalated, randomly choose between AEscalated and BEscalated
else:
    if SORE in 'E':
        ans = random.choice([AEscalated, BEscalated])
        print(ans)
    # If the input was not recognized, provide a helpful error
    else:
        print("Letter not recognized. Try again, You can either put E for escalated or S for solved.")
