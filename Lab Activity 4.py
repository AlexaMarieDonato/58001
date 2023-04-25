from tkinter import*
win = Tk()
win.geometry("255x315+10+10")
win.title("Calculator")

txt1 = Entry(win, bd=20, width="35", bg= "light blue")
txt1.grid(row=0, sticky="nw")
txt1.insert(0, "                     ")

btn1 = Button(win, bd=1, height="-15", text="C", width="20", font=("Arial",15, "bold"))
btn1.grid(sticky="nw", padx=5)

btn2 = Button(win, bd=1, width="8", text="7", height="2")
btn2.grid(row=2, sticky="w", padx=5,pady=2)

btn3 = Button(win, bd=1, width="8", text="8", height="2", command=lambda:screen.insert("end"))
btn3.grid(row=2, sticky="w",padx=70, pady=2)

btn4 = Button(win, bd=1, width="8", text="9", height="2", command=lambda:screen.insert("end"))
btn4.grid(row=2, sticky="w",padx=135, pady=2)

btn5 = Button(win, bd=1, width="6", text="/", height="2", command=lambda:screen.insert("end"))
btn5.grid(row=2, sticky="w",padx=200, pady=2)

btn6 = Button(win, bd=1, width="8", text="4", height="2", command=lambda:screen.insert("end"))
btn6.grid(row=3, sticky="w",padx=5,pady=2)

btn7 = Button(win, bd=1, width="8", text="5", height="2", command=lambda:screen.insert("end"))
btn7.grid(row=3, sticky="w",padx=70, pady=2)

btn8 = Button(win, bd=1, width="8", text="6", height="2",command=lambda:screen.insert("end"))
btn8.grid(row=3, sticky="w",padx=135, pady=2)

btn9 = Button(win, bd=1, width="6", text="*", height="2", command=lambda:screen.insert("end"))
btn9.grid(row=3, sticky="w",padx=200, pady=2)

btn10 = Button(win, bd=1, width="8", text="1", height="2", command=lambda:screen.insert("end"))
btn10.grid(row=4, sticky="w",padx=5,pady=2)

btn11 = Button(win, bd=1, width="8", text="2", height="2", command=lambda:screen.insert("end"))
btn11.grid(row=4, sticky="w",padx=70, pady=2)

btn12 = Button(win, bd=1, width="8", text="3", height="2", command=lambda:screen.insert("end"))
btn12.grid(row=4, sticky="w",padx=135, pady=2)

btn13 = Button(win, bd=1, width="6", text="-", height="2", command=lambda:screen.insert("end"))
btn13.grid(row=4, sticky="w", padx=200, pady=2)

btn14 = Button(win, bd=1, width="10", text="0", height="2", command=lambda:screen.insert("end"))
btn14.grid(row=5, sticky="w",padx=5,pady=2)

btn15 = Button(win, bd=1, width="11", text=".", height="2", command=lambda:screen.insert("end"))
btn15.grid(row=5, sticky="w",padx=85, pady=2)

btn16 = Button(win, bd=1, width="10", text="+", height="2", command=lambda:screen.insert("end"))
btn16.grid(row=5, sticky="w", padx=172, pady=2)

btn1 = Button(win, bd=1, justify="center", width ="20", height="-15", text="=", font=("Arial",15, "bold"), command=lambda:screen.insert("end"))
btn1.grid(sticky="nw", padx=5)

win.mainloop()