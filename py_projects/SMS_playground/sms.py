
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxx"
# Your Auth Token from twilio.com/console
auth_token = "xxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17789186208",
    from_="+12566661469",
    body="Hello from Python!")

print(message.sid)
