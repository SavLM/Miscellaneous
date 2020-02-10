from twilio.rest import Client
import os
from random import randint
import boto3

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def change_time():
    value = randint(12,17)
    schedule = 'cron(0 ' + value + ' * * ? *)'
    sched = boto3.client('events')
    sched.put_rule(
        Name='goattime',
        ScheduleExpression=schedule,
    )

def lambda_handler(event, context):
    ret = ''
    numbers = ["+15408399215","+14346889846","+12526730188"]
    for number in numbers:
        message = client.messages \
            .create(
                body="\n-\n- \n \nA goat!!! \n\n- From your friendly, neighborhood Savvy",
                from_="+12092059061",
                media_url=["https://placegoat.com/200/200"],
                to=number
            )
        ret += message.sid + ' '
    change_time()
    return ret
