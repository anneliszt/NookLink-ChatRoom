from tkinter import *
import pyglet
pyglet.font.add_file('chatRoom/Inter-Regular.ttf')

# GUI function
def GUI():
    # initialize tkinter object
    root = Tk()
    
    # set window title
    root.title("NookLink")
    
    # Creating object of photoimage class 
    # Image should be in the same folder 
    # in which script is saved 
    p1 = PhotoImage(file = 'chatRoom/Animal_Crossing_Leaf.svg.png') 
    
    # Setting icon of master window 
    root.iconphoto(False, p1) 
    
    # set window size
    root.geometry("400x500")
    
    # change background color
    root.config(bg="#F4F0E3")
    
    # button to end session
    endButton = Button(root, font=("Inter", 9, "bold"), text="End Session",
                        bd=0, bg="#FD6275", activebackground="#C2B4B2")
    
    # canvas to display chat title
    canvas = Canvas(root, width=300, height=30, bg="#ABD2B6", bd=0, highlightthickness=0)
    canvas.create_text(100, 15, text="NookLink Server", font=("Inter", 12, "bold"), fill="#685552")
    
    # text space to display messages
    chatLog = Text(root, bd=0, bg="white", font=("Inter", 10))
    chatLog.config(state=DISABLED)
    
    # button to send messages
    sendButton = Button(root, font=("Inter", 12, "bold"), text="Send",
                        bd=0, bg="#ABD2B6", activebackground="#ABD2B6")
    
    # textbox to write messages
    entryBox = Text(root, bd=0, bg="white", font=("Inter", 10))
    
    # place all objects on window
    canvas.place(x=0, y=0)
    endButton.place(x=300, y=0, height=30, width=107)
    chatLog.place(x=8, y=40, height=386, width=380)
    entryBox.place(x=8, y=435, height=50, width=265)
    sendButton.place(x=280, y=435, height=50, width=107)
    
    
    # to keep window in loop
    root.mainloop()
    
if __name__ == "__main__":
    GUI()
    