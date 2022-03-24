import speech_recognition as sr

#! pip install pipwin
#! pipwin install pyaudio
#? ^^^ Used the libraries above to get speech_recognition installed.

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak Anything : ')
    audio = r.listen(source)
    
    text = r.recognize_google(audio)        
    print('You said: {}'.format(text))
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print("I did not understant you.")
        
        
