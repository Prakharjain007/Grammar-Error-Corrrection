'''

import speech_recognition as sr

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

def get_voice_input():
    with sr.Microphone() as source:
        print("Listening... (Press and hold the 'P' key to speak)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

def main():
    while True:
        try:
            audio = get_voice_input()

            # Use Google Web Speech API to convert audio to text
            spoken_text = recognizer.recognize_google(audio)
            print("Spoken Text:", spoken_text)

            # Return the spoken text (or you can process it further if needed)
            return spoken_text

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()

'''


import speech_recognition as sr

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

def get_voice_input():
    with sr.Microphone() as source:
        print("Listening for up to 5 seconds...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            return audio
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected for 5 seconds.")
            return None

def main():
    while True:
        try:
            audio = get_voice_input()

            if audio is not None:
                # Use Google Web Speech API to convert audio to text
                spoken_text = recognizer.recognize_google(audio)
                print("Spoken Text:", spoken_text)

                # Return the spoken text (or you can process it further if needed)
                return spoken_text

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
