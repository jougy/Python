import speech_recognition as sr
import urllib.request
from gtts import gTTS

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyCrNaGdfRa4Rh5RhbWnew-qFGO6Na2Z_fo'

rec = sr.Recognizer()

#print(sr.Microphone().list_microphone_names(),"\n\n")
microfoneInput = 0 #Troque esse numero para mudar de microfone do seu PC de acordo  com a lista

def microfone ():
    with sr.Microphone(microfoneInput) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Pode falar: ")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
    return str(texto)
print(microfone())



