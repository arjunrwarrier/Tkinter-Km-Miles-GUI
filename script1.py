from tkinter import * #going to use many functions in tkinter, 

window = Tk()  #initialising window

def km_to_miles():
    print("Km To Miles")

b1 = Button(window,text="Execute", command=km_to_miles)

b1.grid(row = 0,column=0)

e1 = Entry(window)
e1.grid(row = 0, column = 1)

t1 = Text(window, height=1, width = 20)
t1.grid(row=0,column = 2)




window.mainloop() 

