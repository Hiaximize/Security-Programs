from twilio.rest import Client
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

yourSID = "Enter your Account SID"

yourAuth_Token = "Enter your Auth Token"


# app = Flask(__name__)
# @app.route("/answer", methods=['GET', 'POST'])
# def answer_call():
#     resp = VoiceResponse()
#     resp.say("Derek is always watching you")
#     return str(resp)
#
# if __name__ == "__main__":
#     app.run()


client = Client(yourSID, yourAuth_Token)

# For flooding calls set inside of infinite loop

# while True:  
#
#     client.messages.create(
#         to=phone_number,
#         from_="+13522681589",
#         body="Gotcha!")

twilioNumber = "Enter your Twilio Number"

numberToCall = "Enter desired number to call or flood"



call = client.calls.create(to=numberToCall,from_=twilioNumber, #These can be pulled from another file as well if you have a list of numbers
                           url='Location where your XML file is')

# print(client.sid)










