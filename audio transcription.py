#Python and Sphinx Transcription
#KTanner 07/31/2016
#Written in Python3
#Trial 1: Stress_Pill.wav

#first set up our packages. Only need to do this once
#Code taken from github! 
#https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py
import sys
sys.path.insert(0, '/home/katie/anaconda3/lib/python3.5/site-packages')
sys.path
import speech_recognition as sr

#Path to audio Files
AUDIO_FILE = '/tmp/mozilla_katie0/stress_pill.wav'

#Read the Audio File
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

#transcribe the Audio File using Sphinx
try:
    print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    
#Write this to a text file
file = open('/home/katie/Desktop/stress_pill.txt', 'w')
file.write(r.recognize_sphinx(audio))
file.close()
    
#Trial 2: hal_9000.wav

#Path to audio File
AUDIO_FILE2 = '/tmp/mozilla_katie0/hal_9000.wav'

#Read the Audio File
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE2) as source:
    audio = r.record(source)

#transcribe the Audio File using Sphinx
try:
    print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    
#Write this to a text file
file = open('/home/katie/Desktop/hal_9000.txt', 'w')
file.write(r.recognize_sphinx(audio))
file.close()


#Trial 3: human_error.wav
AUDIO_FILE3 = '/tmp/mozilla_katie0/human_error.wav'

#Read the Audio File
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE3) as source:
    audio = r.record(source)

#transcribe the Audio File using Sphinx
try:
    print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    
#Write this to a text file
file = open('/home/katie/Desktop/human_error.txt', 'w')
file.write(r.recognize_sphinx(audio))
file.close()

#Trial 4: foolproof.wav
AUDIO_FILE4 = '/tmp/mozilla_katie0/foolproof.wav'

#Read the Audio File
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE4) as source:
    audio = r.record(source)

#transcribe the Audio File using Sphinx
try:
    print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    
#Write this to a text file
file = open('/home/katie/Desktop/foolproof.txt', 'w')
file.write(r.recognize_sphinx(audio))
file.close()