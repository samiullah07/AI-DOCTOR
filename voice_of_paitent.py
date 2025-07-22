import logging
import sounddevice as sd
import soundfile as sf
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, duration=10, samplerate=44100, channels=1):
    try:
        logging.info("Recording will start. Speak into the microphone...")
        
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate,
                            channels=channels, dtype='int16')
        sd.wait()
        logging.info("Recording complete.")
        
        sf.write(file_path, audio_data, samplerate)
        logging.info(f"Audio saved to {file_path}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def transcribe_with_groq(model_id, audio_filepath):
    try:
        client = Groq()  
        if not os.path.exists(audio_filepath) or os.path.getsize(audio_filepath) == 0:
            logging.error("Audio file does not exist or is empty.")
            return
        
        with open(audio_filepath, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=model_id,
                file=audio_file,
                language="en"
            )
            return transcription.text
    except Exception as e:
        logging.error(f"Transcription failed: {e}")

