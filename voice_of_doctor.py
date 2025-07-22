#Step1a: Setup Text to Speech–TTS–model with gTTS
from gtts import gTTS
from dotenv import load_dotenv
import elevenlabs
import os
# elevenlabs.set_api_key("sk_825406e37e1a049560b71be4fff1be77de76be4ddf972a3b")  # Replace with your actual API key

from elevenlabs.client import ElevenLabs
import subprocess
import platform

load_dotenv()

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with Hassan!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.wav")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs



def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs()
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "wav",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)


#Step2: Use Model for Text output to Voice



def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi this is Ai with Hassan, autoplay testing!"


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    try:
        client = ElevenLabs(api_key=os.getenv("elevenlabs_API_KEY"))
        audio = client.generate(
            text=input_text,
            voice="Aria",
            output_format="wav",  # Make sure this matches file extension
            model="eleven_turbo_v2"
        )
        elevenlabs.save(audio, output_filepath)
        return output_filepath
    except Exception as e:
        print(f"🚨 ElevenLabs TTS Error: {e}")
        return None

#text_to_speech_with_elevenlabs(input_text, output_filepath="e