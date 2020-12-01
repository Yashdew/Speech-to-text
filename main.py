import io
import os
import json
import pandas as pd
import csv
# Imports the Google Cloud client library
from google.cloud import speech

credential_path = "C:/Users/yashd/OneDrive/Documents/Github Master/Google APi/Audio Transcription-c560d92a32dd.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

#Column Name
fields = ['Transcript']    


# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(os.path.dirname(__file__),"resources", "audio.mp3")  #check resources folder 
#print(file_name)
# Loads the audio into memory
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)


if '.mp3' in file_name:
    config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED, 
    sample_rate_hertz=16000,
    language_code="en-US",
)

else:
    config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, 
    sample_rate_hertz=16000,
    language_code="en-US",
)





# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

print(response)

     
Transcript=["Transcript"]

for result in response.results:
    Transcript.append(result.alternatives[0].transcript)
    #print("Transcript: {}".format(result.alternatives[0].transcript))

for x in Transcript:
  #print(x)
  print("\n")

print(Transcript)

with open("Speech.csv", 'w') as myfile:
     #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for x in Transcript:
         myfile.write(x)
         myfile.write("\n")