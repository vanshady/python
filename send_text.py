from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd156580962dde098452f6540c6f00dcb"
auth_token  = "f0dd959ee34d158240898800cdc728d1"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I love you",
    to="+8613818149617",    # Replace with your phone number
    from_="+12512723087") # Replace with your Twilio number
print message.sid