from tkinter import *

window=Tk()
window.title("BMI CALCULATOR")
window.minsize(350,250)
hesap=0
label3=Label(text="")
label4=Label(text="")
label5=Label(text="")


def writecheck():
    if entry1.get()=="" or entry2.get()=="":
        label5.config(text="Please enter Both",fg="green")
        label5.config(padx=20,pady=20)
        label5.pack()
        return False
    return True


## calculate
def calculate():
    global hesap
    if not writecheck():
        return
    hesap=float(entry1.get())/(float(entry2.get())/(100))**2
    label3.config(text=f"Your BMI:{hesap} ",fg="red")
    label3.config(padx=10,pady=20)
    label3.pack()
    if hesap < 18.5:
        label4.config(text="You are have less height")
        label4.config(padx=20, pady=20)
        label4.pack()
    elif 24.99 >= hesap >= 18.5:
        label4.config(text=f"You are have normal height")
        label4.config(padx=20, pady=20)
        label4.pack()
    elif 29.99 >= hesap >= 25:
        label4.config(text=f"You are have extra height")
        label4.config(padx=20, pady=20)
        label4.pack()
    else:
        label4.config(text=f"You are too high")
        label4.config(padx=20,pady=20)
        label4.pack()


#1.screen
label1=Label(text="Enter Your Weight(Kg)")
label1.config(padx=10,pady=10)
label1.pack()
entry1=Entry(width=20)
entry1.pack()

#2.screen
label2=Label(text="Enter Your Height(cm)")
label2.config(padx=10,pady=10)
label2.pack()
entry2=Entry(width=20)
entry2.pack()

button=Button(text="Calculate",command=calculate)
button.config(padx=10,pady=5)
button.pack()

window.mainloop()