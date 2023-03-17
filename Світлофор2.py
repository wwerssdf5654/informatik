from tkinter import  *


def chenge ( ):
if var.get ( ) == 0:
		label [ 'bg' ] = 'red'
	elif var.get  ( ) == 1:
		label [' bg '] = 'green'
	elif var.get ( ) ==2
		label [' bg '] = 'yellow'

window = Tk ( )
var = IntVar ( )
var.set (0)

red = radiobutton ( text = "червоний ", variable=var, value=0)
green  = radiobutton ( text = "Зелений ", variable=var, value=1) 
yellow = radiobutton ( text = "жовтий ", variable=var, value=2)
red.pack ( )
green.pack ( )
yellow.pack ( )

button = Button (text ="змінити", comand = change)
button.pack( )

label = Label (width=20,  height=10)
label.pack( ) 

window.mainloop( )
