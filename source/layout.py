import tkinter as tk
from tkinter import ttk
from tkinter.constants import VERTICAL
from ctypes import windll
import DATA


class Main_App(tk.Tk):
    #region
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("900x700")
        self.minsize(900, 700)
        self.maxsize(900, 700)
        self.switch_frame(IRP_Cat1_Page)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    #endregion


class Home_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Assessment")

        irp_button = tk.Button(self, text="Go", command=lambda: master.switch_frame(IRP_Page))
        csm_button = tk.Button(self, text="Go", command=lambda: master.switch_frame(CSM_Page))

        # add 2 text fields

        irp_button.pack()
        csm_button.pack()
    #endregion


class IRP_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        cat1_button = tk.Button(self, text="Technologies and Connection Types", command=lambda: master.switch_frame(IRP_Cat1_Page))
        #cat2_button = tk.Button(self, text="Category 2", command=lambda: master.switch_frame(IRP_Cat2_Page))
        #cat3_button = tk.Button(self, text="Category 3", command=lambda: master.switch_frame(IRP_Cat3_Page))
        #cat4_button = tk.Button(self, text="Category 4", command=lambda: master.switch_frame(IRP_Cat4_Page))
        #cat5_button = tk.Button(self, text="Category 5", command=lambda: master.switch_frame(IRP_Cat5_Page))

        cat1_button.pack()
    #endregion


# Inherent Risk Profile - Category 1 (Technologies and Connection Types)
# Responsible for the layout of Category 1 displaying all the questions and possible answers
class IRP_Cat1_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        # Top frame contains navigation widgets
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, anchor=tk.N)

        b = tk.Button(top_frame, text='temp')
        b.pack(side=tk.LEFT, padx=10)

        d = tk.Button(top_frame, text='temp 1')
        d.pack(side=tk.RIGHT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, anchor=tk.SE)

        submit_button = tk.Button(bottom_frame, text='Submit')
        submit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        clear_button = tk.Button(bottom_frame, text='Clear')
        clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Middle frame contains the questions and possible answers
        #middle_frame = tk.Frame(self)
        #middle_frame.pack(fill=tk.BOTH)

        # Create a Main Frame
        #main_frame = tk.Frame(master)
        #main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a canvas
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=50)

        # add a scrollbar to the canvas
        my_scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=900, height=600)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # create another frame inside the canvas
        middle_frame = tk.Frame(my_canvas, borderwidth=3, relief="sunken")

        # add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=middle_frame, anchor="w")

        #tv = ttk.Treeview(middle_frame)
        #tv['columns']=('Question', 'Least', 'Minimal', 'Moderate', 'Significant', 'Most')
        #tv.column('#0', width=0, stretch=tk.NO)
        #tv.column('Question', anchor=tk.CENTER, width=80)
        #tv.column('Least', anchor=tk.CENTER, width=80)
        #tv.column('Minimal', anchor=tk.CENTER, width=80)
        #tv.column('Moderate', anchor=tk.CENTER, width=80)
        #tv.column('Significant', anchor=tk.CENTER, width=80)
        #tv.column('Most', anchor=tk.CENTER, width=80)

        #tv.heading('#0', text='', anchor=tk.CENTER)
        #tv.heading('Question', text='Question', anchor=tk.CENTER)
        #tv.heading('Least', text='Least', anchor=tk.CENTER)
        #tv.heading('Minimal', text='Minimal', anchor=tk.CENTER)
        #tv.heading('Moderate', text='Moderate', anchor=tk.CENTER)
        #tv.heading('Significant', text='Significant', anchor=tk.CENTER)
        #tv.heading('Most', text='Most', anchor=tk.CENTER)

        #tv.insert(parent='', index=0, iid=0, text='qqqq', values=('qqqqqq'))
        #tv.pack()

        label1 = tk.Label(middle_frame, text="Least", padx=15, pady=5, borderwidth=3, relief="raised")
        label1.grid(row=0, column=1, sticky='w')
        label2 = tk.Label(middle_frame, text="Minimal", padx=15, pady=5, borderwidth=3, relief="raised")
        label2.grid(row=0, column=2, sticky='w')
        label3 = tk.Label(middle_frame, text="Moderate", padx=15, pady=5, borderwidth=3, relief="raised")
        label3.grid(row=0, column=3, sticky='w')
        label4 = tk.Label(middle_frame, text="Significant", padx=15, pady=5, borderwidth=3, relief="raised")
        label4.grid(row=0, column=4, sticky='w')
        label5 = tk.Label(middle_frame, text="Most", padx=15, pady=5, borderwidth=3, relief="raised")
        label5.grid(row=0, column=5, sticky='w')

        i = 0
        for key, value in DATA.IRP_Category1.items():
            #tv.insert(parent='', index=i, iid=i, text='', values=(key, "", "", "", "", ""))
            tempQ = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT, padx=5, pady=10)
            tempQ.grid(row=i+1, column=0, sticky='w')
            for j in range(5):
                #tv.insert(parent='', index=i, iid=i, text='', values=(key,value[j]))
                tempA = tk.Radiobutton(middle_frame, text=value[j], padx=15, pady=10)
                tempA.grid(row=i+1, column=j+1, sticky='w')
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)

    #endregion


class CSM_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        start_button = tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(Home_Page))

        start_button.pack()
    #endregion


if __name__ == "__main__":
    app = Main_App()
    app.mainloop()