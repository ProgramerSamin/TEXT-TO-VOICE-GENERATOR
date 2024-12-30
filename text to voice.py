from gtts import gTTS
import os
import time

def speak_text(text):
    """
    Convert text to speech and play it.
    """
    try:
        # Generate a unique filename based on the current timestamp
        audio_file = f"output_{int(time.time())}.mp3"
        
        # Convert text to speech and save the file
        tts = gTTS(text=text, lang='en')
        tts.save(audio_file)
        
        # Play the audio file
        if os.name == 'nt':  # For Windows
            os.system(f"start {audio_file}")
        elif os.name == 'posix':  # For macOS/Linux
            os.system(f"open {audio_file}")
        else:
            print(f"Audio saved as {audio_file}, but unable to auto-play on this OS.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print("Text-to-Speech Program")
    user_text = input("Enter text to speak: ")
    speak_text(user_text)