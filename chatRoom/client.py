from tkinter import *
import pyglet
pyglet.font.add_file('chatRoom/Inter-Regular.ttf')

# GUI function
def GUI():
    # initialize tkinter object
    root = Tk()
    
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
    entryBox.place(x=8, y=435, height=50, width=265)
    sendButton.place(x=280, y=435, height=50, width=107)
    
    # to keep window in loop
    root.mainloop()
    
if __name__ == "__main__":
    GUI()
    