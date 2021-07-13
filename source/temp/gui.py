import tkinter as tk
from tkinter.constants import LEFT
import requests
from PIL import Image, ImageTk

def show_frame(frame):
    frame.tkraise()

root = tk.Tk() # main window
root.state('zoomed')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

for frame in (frame1,frame2,frame3):
    frame.grid(row=0, column=0, sticky='nsew')

# Frame 1 code
frame1_title = tk.Label(frame1, text='This is frame 1', bg='red')
frame1_title.pack(fill='x')
frame1_btn = tk.Button(frame1, text='Enter', command=lambda:show_frame(frame2))
frame1_btn.pack()

# Frame 2 code
frame2_title = tk.Label(frame2, text='This is frame 2', bg='green')
frame2_title.pack(fill='x')
frame2_btn = tk.Button(frame2, text='Enter', command=lambda:show_frame(frame3))
frame2_btn.pack()

# Frame 3 code
frame3_title = tk.Label(frame3, text='This is frame 3', bg='blue')
frame3_title.pack(fill='x')
frame3_btn = tk.Button(frame3, text='Enter', command=lambda:show_frame(frame1))
frame3_btn.pack()

show_frame(frame1)

root.mainloop() # main loop