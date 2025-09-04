import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import time

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 170)  # speed of speech

recognizer = sr.Recognizer()

def speak(text):
    """Make the assistant speak"""
    print(f"Assistant: {text}")  # also show in console
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for a voice command and return it as text"""
    with sr.Microphone() as source:
        print("Clearing background noises... please wait!")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-in")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Google Speech Recognition service is not available.")
        return ""

def run_assistant():
    while True:
        command = take_command()
        if command == "":
            continue  # skip empty input

        print(f"You said: {command}")

        if "time" in command:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time_now}")

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif "play" in command:
            song = command.replace("play", "").strip()
            if song:
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)
                time.sleep(2)  # give browser time to open
            else:
                speak("Please tell me what to play.")

        elif "open whatsapp" in command:
            webbrowser.open("https://web.whatsapp.com")
            speak("Opening WhatsApp")

        elif "open instagram" in command:
            webbrowser.open("https://instagram.com")
            speak("Opening Instagram")

        elif "open gmail" in command:
            webbrowser.open("https://mail.google.com")
            speak("Opening Gmail")

        elif "shutdown" in command:
            speak("Shutting down your system")
            subprocess.call(["shutdown", "/s", "/t", "5"])

        elif "stop" in command:
            speak("Okay, I will stop listening. Say 'wake up' to continue.")
            while True:
                wake = take_command()
                if "wake up" in wake:
                    speak("I'm back, how can I help?")
                    break

        elif "exit" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I did not understand that.")

# Run the assistant in loop
run_assistant()





