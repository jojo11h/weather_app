from twilio.rest import Client
from dotenv import load_dotenv
from os import getenv
from content_message import readfile, make_message

load_dotenv()
data = readfile('file.json')

account_sid = getenv('ACCOUNT_SID')
auth_token = getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+17345476725',
    body=make_message(data),
    to='+33620155408'
)

print(message.sid)
