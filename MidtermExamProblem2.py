from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="Enter Given Name: ")
        self.lbl1.place(x=150, y=50)
        self.lbl2 = Label(win, text="Enter Middle Name: ")
        self.lbl2.place(x=150, y=80)
        self.lbl3 = Label(win, text="Enter Last Name: ")
        self.lbl3.place(x=150, y=110)
        self.lbl4 = Label(win, text="My Full Name is: ")
        self.lbl4.place(x=150, y=150)
        self.lbl5 = Label(win, text="My Full Name")
        self.lbl5.place(x=290, y=25)
        self.txt1 = Entry(win,bd=2)
        self.txt1.place(x=400,y=50)
        self.txt2 = Entry(win,bd=2)
        self.txt2.place(x=400,y=80)
        self.txt3 = Entry(win,bd=2)
        self.txt3.place(x=400,y=110)
        self.txt4 = Entry(win,bd=2)
        self.txt4.place(x=400,y=150)
        self.btnadd = Button(win,text="Show Full Name")
        self.btnadd.place(x=290,y=200)
        self.btnadd.bind('<Button-1>', self.add)

    def add(self,add):
        self.txt4.delete(0, 'end')
        num1 = str(self.txt1.get())
        num2 = str(self.txt2.get())
        num3 = str(self.txt3.get())
        result = num1 + num2 + num3
        self.txt4.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()