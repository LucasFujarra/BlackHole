#---_ BLACK ֍ HOLE APP 1.2 _---
#---_ By Lucas Fujarra _---
#---_ https://github.com/LucasFujarra _---
import os
import re
import streamlit as st
from pytubefix import YouTube

#Busca por URL
def buscar(link):
    try:
        media = YouTube(link)
        return media
    except:
        media = ""
        return media

#logo
with st.columns(3)[1]:
    st.image("https://raw.githubusercontent.com/LucasFujarra/BlackHole/refs/heads/main/screenshot/background.png")

st.title("BLACK ֍ HOLE")

link = st.text_input("Digite a URL: ", key="link")
pesquisar = st.button("Pesquisar")

if pesquisar :
    media = buscar(link)
    if media:
        #Tratativa de caracteres
        r = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]','',media.title)
        titulo = r
        canal = media.author
        audio = media.streams.get_audio_only()
        video = media.streams.get_highest_resolution()
        st.success("Link Valido")
        st.text(f"█ Vídeo: {titulo}")
        st.text(f"█ Canal: {canal}")
        st.image(YouTube(link).thumbnail_url)
        
        # Download audio e video 
        audio_filename = f"{titulo}.mp3"
        video_filename = f"{titulo}.mp4"
        audio.download(filename=audio_filename) 
        video.download(filename=video_filename)

        #Seleção de formato               
        st.download_button(
            label="Download Áudio (MP3)",
            data=open(audio_filename, "rb").read(),
            file_name=audio_filename,
            mime="audio/mpeg"
        )

        st.download_button(
            label="Download Vídeo (MP4)",
            data=open(video_filename, "rb").read(),
            file_name=video_filename,
            mime="video/mp4"
        )
               
        
    else:
        st.error("Link invalido")