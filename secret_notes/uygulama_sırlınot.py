from tkinter import *

FONT=("Verdena",20,"normal")

window =Tk()
window.title("Secret Notes")
window.config(padx=30,pady=30)

title_info_label  = Label(text="Enter your title",font=FONT)
title_info_label.pack()

title_entry = Entry(width=30)
title_entry.pack()

window.mainloop()