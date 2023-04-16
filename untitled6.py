from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry("400x400")
root.title("ENDLESS POKEMON CARD GAME")
root.configure(background="orange")

player1=Label(root,text="Player 1",bg="red",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="Player 2",bg="red",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER) 

player1_score=Label(root,bg="royal blue",fg="white")
player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_score=Label(root,bg="royal blue",fg="white")
player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)

label1=Label(root)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
