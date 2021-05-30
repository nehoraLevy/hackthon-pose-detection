from twilio.rest import TwilioRestClient
from twilio.rest import Client
import time

#This code from this link:https://www.youtube.com/watch?v=3fhyDptV-ss

list_of_targets=["+972505351212", "+972542774427", "+972586099315", "972543972436"] #Zofiya, Nehora, haleli,
FROM = "+972542240652" #twilio number
CALLED = "+972505351212"
ACCOUNT_SID = "ACece77d26da8a581fee421d078cc0684d"
TOKEN = "c829849ea4c07678e3047b851ad78efd"

class Call:
    def __init__(self):
        self.FROM = FROM
        self.CALLED = CALLED
        self.ACCOUNT_SID = ACCOUNT_SID
        self.TOKEN = TOKEN
        self.callCounter = 0 #iterations with calls
        self.LIMIT = 1


    def set_target(self):
        self.CALLED = "+972505351212"#str(input("Enter phone number of target, use '+972' before:"))

    def makeCall(self):
        client = Client(self.ACCOUNT_SID, self.TOKEN)
        while self.callCounter < self.LIMIT:
            call = client.calls.create(to=self.CALLED, from_=self.FROM, twiml='<Response><Say>gagagagagagag</Say></Response>') #url=
            #message = client.messages.create(body='Hello. A fall was detected. Please check quickly and call for medical help if necessary', from_=self.FROM, to=self.CALLED)
            self.callCounter += 1
            print("Call #", self.callCounter)



#robo = Call()
#robo.set_target()
#robo.makeCall()


