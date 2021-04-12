import datetime as dt
from tkinter import *

root = Tk()
root.geometry("420x200")
root.resizable(0, 0)
    
def digital_clock():
    time_now = dt.datetime.now()
    str_time_now = time_now.strftime("%I:%M:%S")
    time_label.config(text=str_time_now)
    time_label.after(1000,digital_clock)

#Font and BGs
text_font = ('Boulder', 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

root.configure(background=background)

time_label = Label(root, font=text_font,bg=background,fg=foreground,bd=border_width)
time_label.grid(row=0, column=1)

msg_label = Label(root,text='(Time in 12hr format only)',font=('Boulder',10,'italic'),bg=background,fg=foreground)
msg_label.grid(row=1, column=1)

digital_clock()

root.mainloop()