from flask import Flask, request, send_file
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

app = Flask(__name__)

# IBM Watson TTS setup using env variable
authenticator = IAMAuthenticator(os.environ.get("WATSON_API_KEY"))
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url("https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/fdf15af7-7c80-4206-a97c-7c89f06153a4")

@app.route("/speak", methods=["POST"])
def speak():
    text = request.json.get("text", "Hello from Watson.")
    response = tts.synthesize(
        text,
        voice="en-US_HenryV3Voice",
        accept="audio/mp3"
    ).get_result()

    with open("output.mp3", "wb") as out:
        out.write(response.content)

    return send_file("output.mp3", mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(port=5001)
