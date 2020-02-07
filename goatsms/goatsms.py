from twilio.rest import Client
import os
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def lambda_handler(event, context):
    message = client.messages \
        .create(
            body='Goat! -From your friendly, neighborhood Savvy',
            from_='+12092059061',
            media_url=['https://placegoat.com/200/200'],
            to=['+15408399215', ]
        )
    print(message.sid)
    return "Success!"
