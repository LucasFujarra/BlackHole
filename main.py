#---_ BLACK ֍ HOLE 1.2 _---
#---_ By Lucas Fujarra _---
#---_ https://github.com/LucasFujarra _---

#import
import time
import os
from pytubefix import YouTube

#defLogo
def logo():
  print("███████████████████████████████████")
  print("██████████ BLACK ֍ HOLE ███████████")
  print("███████████████████████████████████")

#def tela principal
def tela ():
  print(f"█ URL: {link}")
  print(f"█ Vídeo: {media.title}")
  print(f"█ Canal: {media.author}")
  print("█ ")
  print("█ -- Download--")
  print("█ 1 - Baixar Vídeo (MP4)")
  print("█ 2 - Baixar Áudio (M4A)")

logo()  
time.sleep(2)
stream = ""
select = ""

#controle de repetição
while select != "N" :
  os.system("cls")
  while select != 99:
    logo() 
    link = input("█ Digite a URL: ")
    try:
      media = YouTube(link)
      select = 99
    except:
      os.system("cls")
      print("█ URL inválida")
      time.sleep(1)
      os.system("cls")
  
  #Tela principal 
  os.system("cls")
  logo() 
  tela()
  select = input("█ Digite a opção: ")
  os.system("cls")

  #Tratativa de opção invalida
  while select != "1" and select != "2":
    os.system("cls")
    print("█ Opção inválida")
    time.sleep(1)
    os.system("cls")
    logo()
    tela()
    select = input("█ Digite a opção: ")

   #Seleção de formato 
  if select == "1":
    stream = media.streams.get_highest_resolution()
    print("█ ")
    print("█ Download ...")
    time.sleep(1)
    stream.download()
    os.system("cls")
  elif select == "2":
    stream = media.streams.get_audio_only()
    print("█ ")
    print("█ Download ...")
    time.sleep(1)
    stream.download()
    os.system("cls")
  #Download Concluído
  logo()
  print("█ Download concluído !")
  sel = input("█ Deseja baixar outro Vídeo(S/N): ")
  select = sel.upper()
  os.system("cls")
