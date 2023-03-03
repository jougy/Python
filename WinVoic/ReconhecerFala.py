import speech_recognition as sr

rec = sr.Recognizer()

print(sr.Microphone().list_microphone_names())
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode Falar...")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
