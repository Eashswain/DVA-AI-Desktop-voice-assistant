import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio) #it allow the system to speak
    engine.runAndWait() #this function helps to run the system by which the system speaks

#fuction for wish me based on time
def wishMe():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon")
        else:
            speak("Good Evening!")

        speak("I am DOVA sir,Please tell how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
                   #seconds of non-speaking audio beforea phrase is considered completes
                
            
            
            try:   
                print("Recognizing....")
                query=r.recognize_google(audio,language='en-in')
                print(f"user said: {query}\n")
            except Exception as e:
                print(e)
                print("Say that again please....")
                return "None"
            return query


         
if __name__ == "__main__":
        wishMe()
        while True:
            query=takeCommand().lower()

        #logic for executing based on task
            if 'wikipedia' in query:
                    speak('Searching wikipedia...')
                    query=query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=1)
                    speak("According to Wikipedia")
                    speak(results)
                    print(results)
            elif 'open youtube' in query:
                 webbrowser.open("youtube.com")
            elif 'open google' in query:
                 webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                 webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                 music_dir='D:\\Songs\\FavouriteSongs'
                 Songs=os.listdir(music_dir)
                 print(Songs)
                 
                 os.startfile(os.path.join(music_dir,Songs[0]))
            
            elif'the time' in query:
                 strTime=datetime.datetime.now().strftime("%H:%H:%S")
                 speak(f"Maam,the time is {strTime}")
                 print(strTime)

            elif 'open code' in query:
                 Codepath="C:\\Users\\Eash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"     
                 os.startfile(Codepath)
            
            elif 'email to' in query:
                try:
                      speak("what should I say?")
                      content=takeCommand()
                      to ="eashswain3001@gmail.com"
                      sendEmail(to,content)
                      speak("your email has been sent")
                except Exception as e:
                     print(e)
                     speak("Sorry Am not able to send this email")
                
