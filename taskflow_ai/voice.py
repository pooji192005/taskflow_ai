import speech_recognition as sr

def listen_voice():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.WaitTimeoutError:
        return "Voice timeout"
    except sr.UnknownValueError:
        return "Could not understand voice"
    except Exception as e:
        return f"Voice error: {str(e)}"