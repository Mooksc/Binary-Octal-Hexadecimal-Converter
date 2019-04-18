from tkinter import *
import os

def output_int(*args, **kwargs):

	# Create integers with different base values from the user entry
	octal_num = int(entry.get())
	hex_num = int(entry.get())
	binary_num = int(entry.get())
	# Create a readable string from the integers assigend above
	octal_out.configure(text=str("{0:o}".format(octal_num)))
	hex_out.configure(text=str("{0:x}".format(hex_num)))
	binary_out.configure(text=str("{0:b}".format(binary_num)))



display = Tk()

Label(display, text='Enter numbers to convert').grid(row=0, column=1)

Button(display, text='Convert', command = output_int).grid(row=2, column=1)

entry = Entry(display)
entry.bind('<Return>', output_int)
entry.grid(row=1, column=1)

Label(display, text='Octal').grid(row=5, column=0)

octal_out = Label(display, text="0")
octal_out.grid(row=5, column=5)

Label(display, text='Hexadecimal').grid(row=7, column=0)

hex_out = Label(display, text="0")
hex_out.grid(row=7, column=5)

Label(display, text='Binary').grid(row=3, column=0)

binary_out = Label(display, text='0')
binary_out.grid(row=3, column=5)

display.mainloop()