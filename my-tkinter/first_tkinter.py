import tkinter as tk
def quit_out():
    first.destroy()

first = tk.Tk()
first.geometry('800x600')
concern = tk.Button(first,text='确认',font=('黑体',20),command=quit_out)
# concern.place(x=700, y=420, width=150, height=60)
concern.pack(expand=0,fill='none',ipadx =23,side='left')
first.mainloop()