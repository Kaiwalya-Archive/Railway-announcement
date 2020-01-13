import os
import pandas 
from pydub import gTTS

#pip install pyaudio
#pip install pydub
#pip install pandas
#pip install gTTS



def textToSpeech(text,filename):
    pass
#This function returns pydubs audio segment

def mergeAudios (audios):
    pass

def generateSkeleton():
    audio = AudioSegment.from_mp3('Railway.mp3')
#Generate Kripaa dhya de...
start= 
finish=
audioProcessed = audio[start:finish]
audioProcessed.export("1_hindi.mp3", format= "mp3")

#2 is from-city
start = 
finish =
audioProcessed = audio[start:finish]
audioProcessed.export("2_hindi.mp3", format= "mp3")

#3 - generate se chalkar
start = 
finish =
audioProcessed = audio[start:finish]
audioProcessed.export("3_hindi.mp3", format= "mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():



if __name__ == '__main__':
    print ("Generaing Skeleton...")
    genearateSkelton()
    print ("Now Geenerating announcement...")
    generateAnnouncement('announce_hindi.xlsx')

    