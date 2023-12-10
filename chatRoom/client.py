from tkinter import *
import pyglet, PIL
from PIL import ImageTk, Image
pyglet.font.add_file('./Inter-Regular.ttf')

# icon path
icon_path = './Animal_Crossing_Leaf.svg.png'


# GUI function
def GUI():
    # initialize tkinter object
    root = Tk()
    
    # Creating object of photoimage class 
    # Image should be in the same folder 
    # in which script is saved 
    icon = PhotoImage(file = icon_path) 
    
    # Setting icon of master window 
    root.iconphoto(False, icon) 
    
    # set window title
    root.title("NookLink")
    
    # set window size
    root.geometry("400x500")
    
    # change background color
    root.config(bg="#F4F0E3")
    
    # canvas to display chat title
    canvas = Canvas(root, width=400, height=30, bg="#ABD2B6", bd=0, highlightthickness=0)
    canvas.create_text(200, 15, text="NookLink User", font=("Inter", 12, "bold"), fill="#685552")
    canvas.place(x=0, y=0)
    
    # text space to display messages
    chatLog = Text(root, bd=0, bg="white", font=("Inter", 10), borderwidth=0, highlightthickness=0)
    chatLog.config(state=DISABLED)
    
    # button to send messages
    sendButton = Button(root, font=("Inter", 12, "bold"), text="Send",
                        bd=0, fg="#685552", bg="#ABD2B6", activebackground="white")
    

   
    
    
    
    # textbox to write messages
    entryBox = Text(root, bd=0, bg="white", font=("Inter", 10))
    

    
    # place all objects on window
    chatLog.place(x=8, y=40, height=386, width=380)
    entryBox.place(x=70, y=435, height=50, width=200)
    sendButton.place(x=280, y=435, height=50, width=107)
    
    # add message
    add_message(chatLog, "Hello World")
    add_message(chatLog, "Hello >:()")
    
    # to keep window in loop
    root.mainloop()

def add_message(chatLog, message):
    chatLog.config(state=NORMAL)
    chatLog.insert(END, message + "\n")
    chatLog.config(state=DISABLED)
    chatLog.see(END)

if __name__ == "__main__":
    GUI()
    