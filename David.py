import tkinter as tk
from speaker import speak, takecommand
from speaker import takecommand
import datetime
import wikipedia
import webbrowser
import weather
from translate import Translator
import os

HEIGHT = 512
WIDTH = 512



def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    elif hour>=16 and hour<20:
        speak(" Good Evening! ")
    else:
        speak("Good Night!")
    speak(" welcome! how may I help you ")

def tr():
    print("Enter the language in which you want to convert your text:")
    speak("Enter the language in which you want to convert your text:")
    lang=takecommand()
    print("Do you want to enter data or speak data or do you want to exit ? ")
    speak("Do you want to enter data or speak data or do you want to exit ? ")
    flag=takecommand()
    t=Translator(to_lang=lang)
    if flag=="enter data":
        dat=input("Enter data.....")
        translation=t.translate(dat)
        speak(translation)
    elif flag=="exit":
        speak("bye")
    elif flag=="speak data":
        speak("speak the data to be translated")
        data=''
        speak("Speak Sir")
        data=takecommand()
        translation=t.translate(data)
        speak(translation)
    else:
        speak("please enter the right choise")
        tr()

def David():
    query=takecommand()
    query=query.lower()
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(results)
    elif 'open youtube' in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")
    elif "exit" in query:
        exit()
    elif 'open google' in query:
        speak("opening google")
        webbrowser.open("google.com")
    elif "translate" in query:
        tr()
    elif 'open powerpoint' in query:
        powerpath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(powerpath)
    elif query.find('open')!=-1:
        q=query.replace("open","")
        q=q.strip()
        print(q)
        speak("opening"+q+".com")
        webbrowser.open(q+".com")
    elif 'bye' in query or 'end' in query:
        exit()
    else :
        speak("you said"+query)
def know_me():
    speak("I am David do you want to know about me??")
    query=takecommand()
    if query=="yes":
        speak("I am your personal assistant always ready to help you")
    else:
        speak("ok have a great time")
if __name__=="__main__":
    wishme()
    root = tk.Tk()
    root.title("Dekstop Assistant")
    root.resizable(0,0)

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='background.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    about=tk.PhotoImage(file="about.png")
    button1 = tk.Button(root, bg="white", fg="black", borderwidth=0, font=80,image= about, command=lambda: know_me())
    button1.place(relx=0.70, rely=0.10, relheight=0.20, relwidth=0.20)
    mic=tk.PhotoImage(file="mic.png")
    button2 = tk.Button(root, bg="white", fg="black", borderwidth=0, font=80, image= mic, command=lambda: David())
    button2.place(relx=0.35, rely=0.40, relheight=0.20, relwidth=0.30)
    weather1=tk.PhotoImage(file="weather.png")
    button3 = tk.Button(root, bg="white", fg="black", borderwidth=0, image=weather1, font=80, command=lambda: weather.weather())
    button3.place(relx=0.70, rely=0.70, relheight=0.20, relwidth=0.20)
    translator=tk.PhotoImage(file="translator.png")
    button4 = tk.Button(root, bg="white", fg="black", borderwidth=0, image=translator, font=80, command=lambda: tr())
    button4.place(relx=0.10, rely=0.70, relheight=0.20, relwidth=0.20)
    escape=tk.PhotoImage(file="escape.png")
    button5 = tk.Button(root, bg="white", fg="black", borderwidth=0, image=escape, font=80, command=lambda: exit())
    button5.place(relx=0.10, rely=0.10, relheight=0.20, relwidth=0.20)
    root.mainloop()