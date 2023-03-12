import pyttsx3  #text to speech module
import datetime
import speech_recognition as sr #SpeechRecognition
import wikipedia 
import smtplib #inbuilt for email
import webbrowser as wb
import os 
import pyautogui

engine=pyttsx3.init() #call inittialfunction of pyttx3


def speak(audio):
    engine.say(audio)  #converts text passed into speech
    engine.runAndWait() #Waits till it finish speaking

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #retrieves the current time and formats it as a string in the format of "HH:MM:SS" using the datetime module
    speak("the current time is")
    speak(Time)

def date():
    year = str(datetime.datetime.now().year) 
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome sir")
    # time()
    # date()
    hour=int(datetime.datetime.now().hour) #typecast to integer
    #Conditional greeting as per hour
    if hour>=6 and hour <12:
        speak("Good morning sir")
    elif hour >=12 and hour< 18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour <24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("JARVIS at your service Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: # act as a source for input
        print("Listening..")
        r.pause_threshold = 1  # 1s delay to listen
        audio=r.listen(source)

    try:
        print("...Recognizing...")
        query = r.recognize_google(audio, language='en-in') #takes the audio as input and an optional language parameter specifying the language of the audio.
        print(query)

    except Exception as e:
        print(e)
        speak("say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #used to initiate the connection between your Python script and the SMTP server you are connecting to
    server.starttls() #to enable TLS encryption for the connection
    server.login('aplaproject25@gmail.com','Project@2025') #authentication
    server.sendmail('aplaproject25@gmail.com', to, content) #where the first argument is the sender's email address, the second argument is a list of recipient email addresses, and the third argument is the email content in the form of a string
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\Hackathon\\Python_Project_9586_9603\\ss.png")

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("...Searching...")
            query = query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences=3) #returns a summary/ short snippet of our search result from wikipedia
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                to = 'aplaproject25@gmail.com'
                sendEmail(to,content)
                speak("Email was sent successfully")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'search in chrome' in query:
            speak("What should i search?")
            chromepath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'play songs' in query:
            songs_dir = ''
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'screenshot' in query:
            screenshot()
            speak("I have taken the screenshot")
        elif 'offline' in query:
            speak("I hope I was useful to you sir")
            quit()
        



        





