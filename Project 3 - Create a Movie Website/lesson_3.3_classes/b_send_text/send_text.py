# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

from twilio import rest

# Your code here.

account_sid = "ACac4ff19ca85d45ab0ad5f86a289914db" # Your Account SID from www.twilio.com/console
auth_token  = "45b2e4c91bd8b3c1e6bbd61a65e050a8"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Kuei-Jung Hu?",
    to="+16266930098",    # Replace with your phone number
    from_="+13038725971") # Replace with your Twilio number

print(message.sid)
