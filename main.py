from pytube import YouTube 
import moviepy.editor as mp
import os
import re

from requests import patch

#Link do video e o caminho da pasta onde será salvo a musica 
link = input("Informe o link do video: ")
patch = input("Informe o caminho do diretorio a ser salvo: ")
yt = YouTube(link)

#Inicia o download do video
print("Iniciando download do video...")
ys = yt.streams.filter(only_audio=True).first().download(patch)
print("Download do video completo...")

#Convertando o video para mp3
print("Convertendo o video para mp3...")
for file in os.listdir(patch):
    if file.endswith(".mp4"):
        if re.search('mp4', file):
            mp4_path = os.path.join(patch, file)
            mp3_path = os.path.join(patch, os.path.splitext(file)[0] + ".mp3")
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
print("Video convertido com sucesso!")
