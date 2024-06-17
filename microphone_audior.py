import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak now...")
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # Listen for audio
    audio = r.listen(source)

try:
    # Use Google Speech Recognition to convert audio to text
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")