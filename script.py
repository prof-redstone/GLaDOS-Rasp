"""import playsound

# Définir l'URL de l'API
url = "http://192.168.1.101:8124/synthesize/Hi"

# Fonction pour lire le fichier audio
def lire_audio(url):
    #p = vlc.MediaPlayer("test.wav")
    #p.play()
    playsound.playsound(url)
    print("1")


# Lancement de la fonction
lire_audio(url)
"""
import io
import sounddevice as sd
import soundfile as sf
from urllib.request import urlopen

def lire_fichier_audio(url) :
	resp = urlopen(url)
	audio_data = io.BytesIO(resp.read())
	
	with sf.SoundFile(audio_data, 'rb') as f:
		audio_format = f.format
		audio_rate = f.samplerate
		audio_frames = f.frames
	
	sd.play(audio_frames, audio_rate)
	
url = "http://192.168.1.101:8124/synthesize/Hi"
lire_fichier_audio(url)
