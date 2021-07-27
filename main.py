from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
from pydub import AudioSegment
import webbrowser

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Dark: Anlayamadım")
        except sr.RequestError:
            print("Dark: Sistem çalışmıyor")
        return voice

def response(voice):       
       
        #Sistemler
        if voice == "sistemleri kapat":
            speak("Tabii Efendim, sistemleri kapatıyorum")
            exit()
        
        elif voice == "uyku moduna geç":
            speak("Tabii Efendim, uyku moduna geçiyorum")
            exit()

        #Selamlaşma
        elif "merhaba" in voice or "selam" in voice:
         konuşma = ["Merhaba efendim, size nasıl yardımcı olabilirim ?",
                "Selam efendim, size nasıl yardımcı olabilirim ?",
                "İyi günler efendim, size nasıl yardımcı olabilirim ?",]
         secim = choice(konuşma)
         speak(secim)
        
        #Gün
        elif voice == "hangi gündeyiz":
            today = time.strftime("%A")
            today.capitalize()
            if today == "Monday":
                today = "Tabii Efendim, pazartesi günündeyiz"

            elif today == "Tuesday":
                today = "Tabii Efendim, salı günündeyiz"

            elif today == "Wednesday":
                today = "Tabii Efendim, çarşamba günündeyiz"

            elif today == "Thursday":
                today = "Tabii Efendim, perşembe günündeyiz"

            elif today == "Friday":
                today = "Tabii Efendim, cuma günündeyiz"

            elif today == "Saturday":
                today = "Tabii Efendim, Cumartesi günündeyiz"

            elif today == "Sunday":
                today = "Tabii Efendim, Pazar günündeyiz"

            speak(today)

        #Saat
        elif voice == "saat kaç":
           speak(datetime.now().strftime('Tabii Efendim, saat %H:%M'))

        #Google Chrome 
        elif voice == "arama yap":
            speak("Tabii Efendim, ne aramak istersiniz ?")
            search = record()
            url = "https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            speak("Efendim {} hakkında bulduklarımı listeledim".format(search))
       
        #Google Chrome 
        elif voice == "youtube":
            speak("Tabii Efendim, ne aramak istersiniz ?")
            search = record()
            url = "https://www.youtube.com/results?search_query={}".format(search)
            webbrowser.get().open(url)
            speak("Efendim {} hakkında bulduklarımı listeledim".format(search))

        #Toplu Programlar
        elif "programları aç" in voice or "toplu aç" in voice:
           os.startfile("C:\\Users\\mmust\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord")
           os.startfile("C:\\Users\\mmust\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe")
           os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")
           os.startfile("C:\\Users\\mmust\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code")
           speak("Tabii Efendim, ilgili sık kullandığınız programları açıyorum")
        
        #Programlar
        elif "dosyalarım" in voice or "dosyalarım aç" in voice:
           os.startfile("C:\\Users\\mmust\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Ramzan Emre Abra")
           speak("Tabii Efendim, ilgili dosyanızı açıyorum")
        
        elif "discord" in voice or "discord aç" in voice:
           os.startfile("C:\\Users\\mmust\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord")
           speak("Tabii Efendim, ilgili programı açıyorum")
        
        elif "spotify" in voice or "spotify aç" in voice:
           os.startfile("C:\\Users\\mmust\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe")
           speak("Tabii Efendim, ilgili programı açıyorum") 
        
        elif "google chrome" in voice or "google chrome aç" in voice:
           os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")
           speak("Tabii Efendim, ilgili programı açıyorum")

        elif "visual studio code" in voice or "visual studio code aç" in voice:
           os.startfile("C:\\Users\\mmust\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code")
           speak("Tabii Efendim, ilgili programı açıyorum")
        
        #Oyun Launcher
        elif "steam" in voice or "steam aç" in voice: 
           os.startfile("C:\\Users\\mmust\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam")
           speak("Tabii Efendim, ilgili launcherı açıyorum")
       
        elif "epic games" in voice or "epic games aç" in voice: 
           os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Epic Games Launcher")
           speak("Tabii Efendim, ilgili launcherı açıyorum")
        
        elif "gameloop" in voice or "gameloop aç" in voice: 
           os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Tencent Software\\Gameloop\\Gameloop")
           speak("Tabii Efendim, ilgili launcherı açıyorum")
        
        #Oyunlar
        elif "minecraft" in voice or "minecraft aç" in voice: 
           os.startfile("E:\\Ramzan Emre Abra\\Oyunlar\\Minecraft.exe")
           speak("Tabii Efendim, ilgili oyunu açıyorum")
        
        elif "rise" in voice or "rise aç" in voice: 
           os.startfile("E:\\Ramzan Emre Abra\\Oyunlar\\RiseLauncher.exe")
           speak("Tabii Efendim, ilgili oyunu açıyorum")
        
        elif "roblox" in voice or "roblox aç" in voice: 
           os.startfile("C:\\Program Files (x86)\\Roblox\\Versions\\version-f98ef77f473148f6\\RobloxPlayerLauncher.exe")
           speak("Tabii Efendim, ilgili oyunu açıyorum")
        
        elif "valorant" in voice or "volorant aç" in voice: 
           os.startfile("E:\\Ramzan Emre Abra\\Oyunlar\\Riot Games\\Riot Client\\RiotClientServices.exe")
           speak("Tabii Efendim, ilgili oyunu açıyorum")
        
        elif "zula" in voice or "zula aç" in voice: 
           os.startfile("E:\\Ramzan Emre Abra\\Oyunlar\\Zula\\zula_launcher.exe")
           speak("Tabii Efendim, ilgili oyunu açıyorum")
        
        elif "pubg mobile" in voice or "pubg mobile aç" in voice: 
           os.startfile("E:\\Ramzan Emre Abra\\Oyunlar\\PUBG Mobile")
           speak("Tabii Efendim, ilgili oyunu açıyorum")

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

#speak("Sistemler başlatıldı")
playsound("GIRIS.mp3")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)

   