
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE INHERENT RISK PROFILE """

import tkinter as tk
import DATA
# from ctypes import windll

""" This class is responsible for the layout of the Inherent Risk Profile's Main page
    Contains the 5 categories and links to each one """
class IRP_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        cat1_button = tk.Button(self, text="Technologies and Connection Types", command=lambda: master.switch_frame(IRP_Cat1_Page))
        cat2_button = tk.Button(self, text="Delivery Channels", command=lambda: master.switch_frame(IRP_Cat2_Page))
        cat3_button = tk.Button(self, text="Online/Mobile Products and Technology Services", command=lambda: master.switch_frame(IRP_Cat3_Page))
        cat4_button = tk.Button(self, text="Organizational Characteristics", command=lambda: master.switch_frame(IRP_Cat4_Page))
        cat5_button = tk.Button(self, text="External Threats", command=lambda: master.switch_frame(IRP_Cat5_Page))

        cat1_button.pack()
        cat2_button.pack()
        cat3_button.pack()
        cat4_button.pack()
        cat5_button.pack()
    #endregion


""" Inherent Risk Profile - Category 1 (Technologies and Connection Types) 
    Responsible for the layout of Category 1 displaying all the questions and possible answers """
class IRP_Cat1_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        # Top frame contains navigation widgets
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, anchor=tk.N)
        temp_button = tk.Button(top_frame, text='Go Here')
        temp_button.pack(side=tk.LEFT, padx=10)
        temp_button_2 = tk.Button(top_frame, text='Go There')
        temp_button_2.pack(side=tk.RIGHT, anchor=tk.E)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, anchor=tk.SE)
        submit_button = tk.Button(bottom_frame, text='Submit')
        submit_button.pack(side=tk.RIGHT, padx=10, pady=10)
        clear_button = tk.Button(bottom_frame, text='Clear')
        clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a canvas
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=50)

        # add a scrollbar to the canvas
        my_scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=900, height=600)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # create another frame inside the canvas
        middle_frame = tk.Frame(my_canvas, borderwidth=3, relief="sunken")

        # add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=middle_frame, anchor="w")

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
            tempQ = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT, padx=5, pady=10)
            tempQ.grid(row=i+1, column=0, sticky='w')
            for j in range(5):
                tempA = tk.Radiobutton(middle_frame, text=value[j], padx=15, pady=10)
                tempA.grid(row=i+1, column=j+1, sticky='w')
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 2 (Delivery Channels) 
    Responsible for the layout of Category 2 """
class IRP_Cat2_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        # Top frame contains navigation widgets
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, anchor=tk.N)
        temp_button = tk.Button(top_frame, text='Go Here')
        temp_button.pack(side=tk.LEFT, padx=10)
        temp_button_2 = tk.Button(top_frame, text='Go There')
        temp_button_2.pack(side=tk.RIGHT, anchor=tk.E)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, anchor=tk.SE)
        submit_button = tk.Button(bottom_frame, text='Submit')
        submit_button.pack(side=tk.RIGHT, padx=10, pady=10)
        clear_button = tk.Button(bottom_frame, text='Clear')
        clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a canvas
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=50)

        # add a scrollbar to the canvas
        my_scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=900, height=600)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # create another frame inside the canvas
        middle_frame = tk.Frame(my_canvas, borderwidth=3, relief="sunken")

        # add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=middle_frame, anchor="w")

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
            tempQ = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT, padx=5, pady=10)
            tempQ.grid(row=i+1, column=0, sticky='w')
            for j in range(5):
                tempA = tk.Radiobutton(middle_frame, text=value[j], padx=15, pady=10)
                tempA.grid(row=i+1, column=j+1, sticky='w')
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 3 (Online/Mobile Products and Technology Services) 
    Responsible for the layout of Category 3 """
class IRP_Cat3_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        # Top frame contains navigation widgets
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, anchor=tk.N)
        temp_button = tk.Button(top_frame, text='Go Here')
        temp_button.pack(side=tk.LEFT, padx=10)
        temp_button_2 = tk.Button(top_frame, text='Go There')
        temp_button_2.pack(side=tk.RIGHT, anchor=tk.E)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, anchor=tk.SE)
        submit_button = tk.Button(bottom_frame, text='Submit')
        submit_button.pack(side=tk.RIGHT, padx=10, pady=10)
        clear_button = tk.Button(bottom_frame, text='Clear')
        clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a canvas
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=50)

        # add a scrollbar to the canvas
        my_scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=900, height=600)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # create another frame inside the canvas
        middle_frame = tk.Frame(my_canvas, borderwidth=3, relief="sunken")

        # add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=middle_frame, anchor="w")

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
            tempQ = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT, padx=5, pady=10)
            tempQ.grid(row=i+1, column=0, sticky='w')
            for j in range(5):
                tempA = tk.Radiobutton(middle_frame, text=value[j], padx=15, pady=10)
                tempA.grid(row=i+1, column=j+1, sticky='w')
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 4 (Organizational Characteristics) 
    Responsible for the layout of Category 4 """
class IRP_Cat4_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        # Top frame contains navigation widgets
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, anchor=tk.N)
        temp_button = tk.Button(top_frame, text='Go Here')
        temp_button.pack(side=tk.LEFT, padx=10)
        temp_button_2 = tk.Button(top_frame, text='Go There')
        temp_button_2.pack(side=tk.RIGHT, anchor=tk.E)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, anchor=tk.SE)
        submit_button = tk.Button(bottom_frame, text='Submit')
        submit_button.pack(side=tk.RIGHT, padx=10, pady=10)
        clear_button = tk.Button(bottom_frame, text='Clear')
        clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a canvas
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=50)

        # add a scrollbar to the canvas
        my_scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=900, height=600)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # create another frame inside the canvas
        middle_frame = tk.Frame(my_canvas, borderwidth=3, relief="sunken")

        # add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=middle_frame, anchor="w")

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
            tempQ = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT, padx=5, pady=10)
            tempQ.grid(row=i+1, column=0, sticky='w')
            for j in range(5):
                tempA = tk.Radiobutton(middle_frame, text=value[j], padx=15, pady=10)
                tempA.grid(row=i+1, column=j+1, sticky='w')
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 5 (External Threats) 
    Responsible for the layout of Category 5 """
class IRP_Cat5_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        # Top frame contains navigation widgets
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, anchor=tk.N)
        temp_button = tk.Button(top_frame, text='Go Here')
        temp_button.pack(side=tk.LEFT, padx=10)
        temp_button_2 = tk.Button(top_frame, text='Go There')
        temp_button_2.pack(side=tk.RIGHT, anchor=tk.E)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, anchor=tk.SE)
        submit_button = tk.Button(bottom_frame, text='Submit')
        submit_button.pack(side=tk.RIGHT, padx=10, pady=10)
        clear_button = tk.Button(bottom_frame, text='Clear')
        clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a canvas
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=50)

        # add a scrollbar to the canvas
        my_scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=900, height=600)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # create another frame inside the canvas
        middle_frame = tk.Frame(my_canvas, borderwidth=3, relief="sunken")

        # add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=middle_frame, anchor="w")

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
            tempQ = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT, padx=5, pady=10)
            tempQ.grid(row=i+1, column=0, sticky='w')
            for j in range(5):
                tempA = tk.Radiobutton(middle_frame, text=value[j], padx=15, pady=10)
                tempA.grid(row=i+1, column=j+1, sticky='w')
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion