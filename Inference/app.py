from flask import Flask, render_template, request, jsonify
import subprocess
import speech_recognition as sr 

app = Flask(__name__)

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

def start_listening():
    with sr.Microphone() as source:
        print("Listening... (Press and hold the 'P' key to speak)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    audio = start_listening()

    try:
        # Use Google Web Speech API to convert audio to text
        spoken_text = recognizer.recognize_google(audio)
        print("Spoken Text:", spoken_text)

        # Pass the spoken text as a command-line argument to gecmodel.py
        result = subprocess.run(["python", "gecmodel.py", spoken_text], capture_output=True, text=True)
        gec_output = result.stdout.strip()

        response_data = {"spoken_text": spoken_text, "gec_output": gec_output}

        return jsonify(response_data)

    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand the audio."})
    except sr.RequestError as e:
        return jsonify({"error": f"Could not request results; {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
