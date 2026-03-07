import whisper
import sounddevice as sd
from scipy.io.wavfile import write

model = whisper.load_model("base")

def record_audio(filename="input.wav", duration=6, fs=44100):
    print("Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("Recording complete")

def speech_to_text(audio_file="input.wav"):
    result = model.transcribe(audio_file)
    return result["text"]