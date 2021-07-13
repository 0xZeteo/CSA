from tkinter import *

# raise / show a frame
def raise_frame(frame):
    frame.tkraise()

root = Tk() # main window

# Home page
frame_home = Frame(root)

text_home_irp = Text(frame_home)
text_home_irp.insert(INSERT, 'This is the Inherent Risk Profile')
text_home_irp.grid(row=0, column=0)

button_home_irp = Button(frame_home, text='Go')
button_home_irp.grid(row=0, column=1)

text_home_csm = Text(frame_home)
text_home_csm.insert(INSERT, 'This is the Cybersecurity Maturity')
text_home_csm.grid(row=1, column=0)

button_home_csm = Button(frame_home, text='Go')
button_home_csm.grid(row=1, column=1)

# Inherent Risk Profile page
frame_irp = Frame(root)

# Inherent Risk Profile category 1 page 
frame_irp_category1 = Frame(root)

# Place the frames on top of eachother
for frame in (frame_home, frame_irp, frame_irp_category1):
    frame.grid(row=0, column=0, sticky='news')

#Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
#Label(f1, text='FRAME 1').pack()

raise_frame(frame_home) # show the home page first
root.mainloop()