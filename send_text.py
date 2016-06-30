from twilio.rest import TwilioRestClient

account_sid = "AC16adcde48ab8be2404063a0152065735" # Your Account SID from www.twilio.com/console
auth_token  = "030dc6fe0fcea0ebd43aff0e34e73b72"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+918466905904",    # Replace with your phone number
    from_="+13158494899") # Replace with your Twilio number

print(message.sid)
