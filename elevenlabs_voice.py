from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from utils import ELEVENLABS_API_KEY

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def speak(text):

    audio = client.text_to_speech.convert(
        text=text,
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel voice
        model_id="eleven_multilingual_v2"
    )

    play(audio)