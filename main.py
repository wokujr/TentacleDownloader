from tkinter import *

#Create a Window
window = Tk()
window.title("My GUI")
window.minsize(width=700, height=500)
window.config(bg="black")

label = Label(text="Hallo step-GUI", font=("Arial", 28, "bold"), fg="white", bg="black")
label.pack()

def button_clicked():
    #label.config(text="Ay got clicked !", font=("Arial", 28, "bold"), fg="white", bg="black")
    new_text = input.get()
    if button:
        label.config(text=new_text, font=("Arial", 28, "bold"), fg="white", bg="black")

#Text
text = Text(width=45, height=3)
text.focus()
text.insert(END, "Manga Downloader... but work for tentacle xD")
text.pack()

#Button
button = Button(text="click me!", command=button_clicked)
button.pack()

#Entry
input = Entry(bd=3)
input.pack()
input.get()


window.mainloop()
