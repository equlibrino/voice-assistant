from playsound import playsound       # playsound modülü, ses dosyalarını çalmak için kullanılır.
from gtts import gTTS                 # gTTS (Google Text-to-Speech), metni sese çevirmek için kullanılır.
import speech_recognition as sr       # speech_recognition modülü, konuşmayı metne çevirmek için kullanılır.
import os                             # os modülü, işletim sistemi komutlarını çalıştırmak için kullanılır.
import time                           # time modülü, zamanla ilgili işlemler için kullanılır.
from datetime import date, datetime   # datetime modülü, tarih ve saat bilgilerini almak için kullanılır.
import random                         # random modülü, rastgele seçimler yapmak için kullanılır.
from random import choice             # choice fonksiyonu, listeden rastgele bir seçim yapmak için kullanılır.
from pydub import AudioSegment        # pydub modülü, ses dosyaları ile çalışmak için kullanılır (bu kodda kullanılmamış).
import webbrowser                     # webbrowser modülü, internet tarayıcısında sayfa açmak için kullanılır.

r = sr.Recognizer()                   # speech_recognition için bir 'Recognizer' nesnesi oluşturur; bu nesne, konuşmayı tanımak için kullanılır.

def record(ask=False):                # record fonksiyonu, kullanıcının sesli komutlarını kaydeder ve metne çevirir.
    with sr.Microphone() as source:   # Mikrofonu 'source' olarak kullanmak için açar.
        if ask:
            print(ask)                # Eğer 'ask' parametresi varsa, bu mesajı ekrana yazdırır.
        audio = r.listen(source)      # Mikrofon aracılığıyla ses dinler ve 'audio' olarak kaydeder.
        voice = ""                    # voice değişkenini boş bir string olarak tanımlar.
        try:
            voice = r.recognize_google(audio, language="tr-TR")  # Google'ın Türkçe dil modelini kullanarak sesi metne çevirir.
        except sr.UnknownValueError:  # Ses tanınmazsa bu hata yakalanır.
            print("Dark: Anlayamadım")
        except sr.RequestError:       # Google API'ye ulaşılamazsa bu hata yakalanır.
            print("Dark: Sistem çalışmıyor")
        return voice

def response(voice):                  # response fonksiyonu, kullanıcının komutuna göre yanıt verir.
       
        # Sistemler
        if voice == "sistemleri kapat":  # "sistemleri kapat" komutunda asistan kapanır.
            speak("Tabii Efendim, sistemleri kapatıyorum")
            exit()
        
        elif voice == "uyku moduna geç": # "uyku moduna geç" komutunda asistan kapanır.
            speak("Tabii Efendim, uyku moduna geçiyorum")
            exit()

        # Selamlaşma
        elif "merhaba" in voice or "selam" in voice:   # "merhaba" veya "selam" içeren komutları yanıtlar.
         konuşma = ["Merhaba efendim, size nasıl yardımcı olabilirim ?",
                    "Selam efendim, size nasıl yardımcı olabilirim ?",
                    "İyi günler efendim, size nasıl yardımcı olabilirim ?",]
         secim = choice(konuşma)  # Rastgele bir selamlaşma mesajı seçer.
         speak(secim)
        
        # Gün
        elif voice == "hangi gündeyiz":  # Bugünün günü sorulursa, yanıt verir.
            today = time.strftime("%A")  # Haftanın gününü İngilizce olarak alır.
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

        # Saat
        elif voice == "saat kaç":  # "saat kaç" sorusuna saati söyler.
           speak(datetime.now().strftime('Tabii Efendim, saat %H:%M'))

        # Google Chrome 
        elif voice == "arama yap": # "arama yap" komutuyla Google'da arama yapar.
            speak("Tabii Efendim, ne aramak istersiniz ?")
            search = record()      # Kullanıcıdan arama terimini kaydeder.
            url = "https://www.google.com/search?q={}".format(search)  # Google arama URL'si oluşturur.
            webbrowser.get().open(url)   # Tarayıcıda arama sayfasını açar.
            speak("Efendim {} hakkında bulduklarımı listeledim".format(search))
       
        elif voice == "youtube":   # "youtube" komutuyla YouTube'da arama yapar.
            speak("Tabii Efendim, ne aramak istersiniz ?")
            search = record()      # Kullanıcıdan arama terimini kaydeder.
            url = "https://www.youtube.com/results?search_query={}".format(search)  # YouTube arama URL'si oluşturur.
            webbrowser.get().open(url)   # Tarayıcıda arama sayfasını açar.
            speak("Efendim {} hakkında bulduklarımı listeledim".format(search))

        # Toplu Programlar
        elif "programı aç" in voice or "" in voice:  # "programları aç" veya "" komutlarıyla belirtilen programları açar.
           os.startfile("C:\\Users\\")  # Belirtilen klasörü açar.

           speak("Tabii Efendim, programı açıyorum")
        
def speak(string):                    # speak fonksiyonu, verilen metni sese çevirir ve çalar.
    tts = gTTS(text=string, lang="tr", slow=False)   # Metni Türkçe dilinde sese çevirir.
    file = "answer.mp3"               # Ses dosyasını 'answer.mp3' olarak kaydeder.
    tts.save(file)                    # Dosyayı kaydeder.
    playsound(file)                   # Kaydedilen dosyayı çalar.
    os.remove(file)                   # Dosyayı siler.

# speak("Sistemler başlatıldı")       # Bu satır, sistem başlatıldığında bir selam sesi çalmak için kullanılmış ancak yorum satırına alınmış.
playsound("gırıs.mp3")                # Başlangıçta 'GIRIS.mp3' dosyasını çalar.

while True:                           # Sonsuz döngü başlatılır.
    voice = record()                  # Kullanıcıdan sesli komut kaydedilir.
    if voice != '':                   # Boş değilse (ses tanımlandıysa),
        voice = voice.lower()         # Komut küçük harfe dönüştürülür.
        print(voice.capitalize())     # Tanınan sesli komut ekrana yazdırılır.
        response(voice)               # Komuta uygun yanıt fonksiyonu çağrılır
#Equ
