# gui - test 
from tkinter import *
from tkinter import ttk,messagebox

# set frame
GUI = Tk()
GUI.title("program multiple by 1000")
GUI.geometry('800x600')

# label 1 
L = Label(GUI,text="enter number",font=(None,18))
L.pack()

# use image
# bg = PhotoImage (file='pic001.jpg')
# BG = Label(GUI,image=bg)
# BG.pack()

# inputbox 
v_quality = StringVar() # varible for store text when submit
E1 = ttk.Entry(GUI,textvariable=v_quality,font=(None,18))
E1.pack()

def Cal():
	try:
		quan = float(v_quality.get())
		cal = quan*1000
		messagebox.showinfo('show info',f'total price{cal}')
		v_quality.set('1')
		E1.focus()
	except:
		messagebox.showwarning('error',f'input only number !!')
		v_quality.set('1')
		E1.focus()


# button 
B = ttk.Button(GUI,text='submit',command=Cal)
B.pack(ipadx=30,ipady=20)


GUI.mainloop() # program run all time 
