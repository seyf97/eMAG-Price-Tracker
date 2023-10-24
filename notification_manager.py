from twilio.rest import Client
from dotenv import load_dotenv
import os


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self, msg):
        load_dotenv()
        self.ACC_SID = os.getenv("ACC_SID")
        self.AUTH_TOKEN = os.getenv("AUTH_TOKEN")
        self.PHONE_NUM = os.getenv("PHONE_NUM")
        client = Client(self.ACC_SID, self.AUTH_TOKEN)

        message = client.messages \
            .create(
            body=msg,
            from_='+12185206909',
            to=self.PHONE_NUM
        )
        print(message.status)