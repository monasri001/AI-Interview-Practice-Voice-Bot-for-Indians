from question_bank import questions
from whisper_input import record_audio, speech_to_text
from interview_chain import evaluate_answer
from elevenlabs_voice import speak
import random

def run_interview():

    print("AI Interview Bot Started")

    question = random.choice(questions)

    print("Question:", question)

    speak(question)

    record_audio()

    user_answer = speech_to_text()

    print("\nYour Answer:")
    print(user_answer)

    feedback = evaluate_answer(user_answer)

    print("\nAI Feedback:")
    print(feedback)

    speak(feedback)

if __name__ == "__main__":
    run_interview()