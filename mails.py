import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import base64
from rich import print

env = Environment(loader=FileSystemLoader(f'{os.getcwd()}/templates/'))

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']

def get_creds():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def create_message(diff_dict, address_from, address_to):
    template = env.get_template('child.html')
    bodyContent = template.render(data=diff_dict)
    message = MIMEMultipart()
    message.attach(MIMEText(bodyContent, "html"))
    message['to'] = address_to
    message['from'] = address_from
    message['subject'] = f'New Messages from Regions: {str(list(diff_dict.keys()))}'
    raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
    return {'raw': raw_message.decode("utf-8")}

def send_mail(diff_dict, address_from, address_to):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = get_creds()
    service = build('gmail', 'v1', credentials=creds)
    message = service.users().messages().send(userId=address_from, body=create_message(diff_dict, address_from, address_to)).execute()
    
    print(message)