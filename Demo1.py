from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("My first GUI")

btn1 = Button(window, text = "Click me",fg = "red", bg = "yellow" )
btn1.place(x = 200, y = 200)

txt = Entry(window, border = 10)
txt.place(x=180, y = 150)

lbl = Label(window, text = "My First Demo",font= "Verdana")
lbl.place(x=180, y=50)

window.mainloop()
