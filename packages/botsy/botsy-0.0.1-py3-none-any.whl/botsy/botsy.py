#!/usr/bin/env python
import os
import speech_recognition as sr
from googletrans import Translator
import pygame
import openai
from gtts import gTTS

openai.api_key = os.getenv("OPENAI_API_KEY")


text = "Computer online."
tts = gTTS(text=text, lang="en")
tts.save("prompt.mp3")
os.system("mpg321 prompt.mp3")  # Replace 'mpg321' with your media player command


pygame.init()

sound = pygame.mixer.Sound("prompt.wav")


def listen_to_mic(text="", phrase_time_limit=3):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening-{text}...")
        audio = r.listen(source, phrase_time_limit=phrase_time_limit)
        try:
            text = r.recognize_google(
                audio,
                language="en-US",
            )
            return text
        except Exception as e:
            print("Error:", str(e))
            return None


def main():
    translator = Translator()
    while True:
        print("prompting 1")
        text = listen_to_mic(text="1", phrase_time_limit=None)
        print(text)
        if text is not None:
            if text.lower().startswith("computer"):
                print("Command 'Computer.' detected. Translating...")
                translated_text = translator.translate(text, dest="en")
                sound.play()

                while True:
                    print("prompting 2")
                    text = listen_to_mic(text="2", phrase_time_limit=None)

                    if text is not None:
                        translated_text = translator.translate(
                            text, dest="en"
                        ).text.lower()
                        response = openai.Completion.create(
                            model="text-davinci-003",
                            prompt=translated_text,
                            temperature=0,
                            max_tokens=700,
                        )

                        resp_text = response["choices"][0]["text"]
                        tts = gTTS(text=resp_text, lang="en", tld="co.uk")
                        tts.save("cmd.mp3")
                        os.system("mpg321 cmd.mp3")
                        # break
                    else:
                        print("Breaking from here")
                        break
                # print("\n\n\nTranslated text:", translated_text.text)
        else:
            pass
            # print("Could not recognize the speech.")


if __name__ == "__main__":
    main()
