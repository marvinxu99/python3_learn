
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Step 1: Load the environment variables from the .env file
load_dotenv()  # take environment variables

# Step 2: Access the variables using os.getenv() or os.environ.get()
# Your Account SID from twilio.com/console
# account_sid = "xxxxx"
account_sid = os.getenv('TWILIO_SID')

# Your Auth Token from twilio.com/console
# auth_token = "xxxx"
auth_token = os.getenv('TWILIO_TOKEN')


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17789186208",
    from_="+12056351364",
    body="Hello from Python!")

# Sending a message to multiple phone numbers:
# numbers_to_message = ['+15558675310', '+14158141829', '+15017122661']
# for number in numbers_to_message:
#     client.messages.create(
#         body='Hello from my Twilio number!',
#         from_='+15017122662',
#         to=number
#     )

# Send a message containing media (MMS)
# message = client.messages.create(
#     body="This is the ship that made the Kessel Run in fourteen parsecs?",
#     from_="+15017122661",
#     media_url=[
#         "https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg"
#     ],
#     to="+15558675310",
# )


print(message.sid, message.status)
