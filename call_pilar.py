from twilio.rest import Client
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

dereksAccount_sid = "AC56128df038a050044d46a260a167b628"

pilarsAccount_sid = "AC81483797b5e106ad6bbaaf9ff2915bac"

pilarsAuth_token = "65425b0233fc469f39a77886cace24c7"

dereksAuth_token = "5ed8e20a9ee53b08480721ac08ceb167"


# app = Flask(__name__)
# @app.route("/answer", methods=['GET', 'POST'])
# def answer_call():
#     resp = VoiceResponse()
#     resp.say("Derek is always watching you")
#     return str(resp)
#
# if __name__ == "__main__":
#     app.run()


client = Client(dereksAccount_sid, dereksAuth_token)

# while True:
#
#     client.messages.create(
#         to=phone_number,
#         from_="+13522681589",
#         body="Gotcha!")

dereksTrialNumber = "+13522688914"

pilarsTrialNumber = "+13522681589"

dereksNumber = "+13523211166"

pilarsNumber = "+13522337206"

call = client.calls.create(to=dereksNumber,from_=dereksTrialNumber,
                           url='https://amber-kangaroo-1450.twil.io/assets/message.xml')

# print(client.sid)










