from tkinter import *
from math import sqrt as sq
print('Calculator App starting.......')
root = Tk()
root.title('            Calculator')
#funs = {"add":sum([int(first),int(second1)])}
fun = ""
e = Entry(root,width = 10,borderwidth=0,justify =RIGHT,bg = '#eeeeee',font = ('Arial',20))
e.grid(row=0,column=3,columnspan=6)

def button_click(n):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(n))
def clear():
	e.delete(0,END)
def add():
	global first
	first = e.get()
	global fun 
	fun = "add"
	e.delete(0,END)
def sub():
    global first
    first = e.get()
    global fun
    fun = "sub"
    e.delete(0,END)
def mul():
	global first
	first = e.get()
	global fun 
	fun = "mul"
	e.delete(0,END)
def div():
	global first
	first = e.get()
	global fun 
	fun = "div"
	e.delete(0,END)
def power():
	global first
	first = e.get()
	global fun 
	fun = "pow"
	e.delete(0,END)

def rot():
	global first
	first = e.get()
	global fun
	fun = "root"
	e.delete(0,END)

def square():
	global first
	first = e.get()
	global fun
	fun = "square"
	e.delete(0,END)

def equal():
	second = e.get()
	print(fun)
	e.delete(0,END)

	if fun=="add":
		e.insert(0,float(first)+float(second))
	elif fun=="sub":
		e.insert(0,float(first)-float(second))
	elif fun=="mul":
		e.insert(0,float(first)*float(second))
	elif fun=="pow":
		e.insert(0,float(first)**float(second))
	elif fun=="root":
		e.insert(0,sq(float(first)))
	elif fun=="square":
		e.insert(0,float(first)**2)
	else:
		e.insert(0,float(first)/float(second))



button1 = Button(root,text="1",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(1)).grid(row=1,column=1)
button2 = Button(root,text="2",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(2)).grid(row=1,column=2)
button3 = Button(root,text="3",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(3)).grid(row=1,column=3)

button4 = Button(root,text="4",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(4)).grid(row=2,column=1)
button5 = Button(root,text="5",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(5)).grid(row=2,column=2)
button6 = Button(root,text="6",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(6)).grid(row=2,column=3)

button7 = Button(root,text="7",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(7)).grid(row=3,column=1)
button8 = Button(root,text="8",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(8)).grid(row=3,column=2)
button9 = Button(root,text="9",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(9)).grid(row=3,column=3)

button0 = Button(root,text="0",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(0)).grid(row=4,column=2)

button_equal = Button(root,text="=",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=equal).grid(row=4,column=3)
button_decimal = Button(root,text=".",padx=11,pady=12,font=('Verdana' ,17),activebackground='#bbbbbb',border=0,relief=GROOVE,command=lambda:button_click(".")).grid(row=4,column=1)

button_div 	 = 	 Button(root,text="/",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=div).	grid(row=1,column=4)
button_mul   =   Button(root,text="*",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=mul).	grid(row=2,column=4)
button_minus =   Button(root,text="-",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=sub).	grid(row=3,column=4)
button_add   =   Button(root,text="+",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=add).	grid(row=4,column=4)
button_clear =   Button(root,text="C",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=clear).grid(row=4,column=5)
button_power =   Button(root,text="^",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=power).grid(row=3,column=5)
button_root =    Button(root,text="√",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=rot).	grid(row=2,column=5)
button_square =  Button(root,text="  x²",padx=11,pady=12,font=('Verdana' ,15),activebackground='#bbbbbb',border=0,relief=GROOVE,command=square).grid(row=1,column=5)


#--------------------------------------
root.mainloop()