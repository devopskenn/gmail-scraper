# Importing libraries
import imaplib
import email
import pandas as pd
import yaml  #To load saved login credentials from a yaml file


# Opening the YAML credentials file
with open("credentials.yml") as f:
    content = f.read()

# from credentials.yml import user name and password
my_credentials = yaml.load(content, Loader=yaml.FullLoader)

#Load the user name and passwd from yaml file
user, password = my_credentials["user_two"], my_credentials["pass_two"]

#URL for IMAP connection
imap_url = 'imap.gmail.com'

# Connection with GMAIL using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in using your credentials
my_mail.login(user, password)

# Select the Inbox to fetch messages
my_mail.select('Inbox')

collection = [] #list to collect all email_id's and other items

result, data = my_mail.uid('search', None, "ALL") # search all email and return uids
if result == 'OK':
    for num in data[0].split():
        result, data = my_mail.uid('fetch', num, '(RFC822)')
        if result == 'OK':
            email_message = email.message_from_bytes(data[0][1])    # raw email text including headers
            collection.append(email_message['From'])
            #print('From:' + email_message['From'])

my_mail.close()
my_mail.logout() 

# Saving the data colelcted in a dataframe, then to a spreadsheet file
df_collection = pd.DataFrame(collection, columns=["From"], index=None)
df_collection.to_excel("My Received Mails.xlsx", index=False)

