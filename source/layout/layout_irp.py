
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE INHERENT RISK PROFILE """

import tkinter as tk
import DATA
import layout.layout_home as home
# from ctypes import windll

""" This class is responsible for the layout of the Inherent Risk Profile's Main page
    Contains the 5 categories and links to each one """
class IRP_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile")

        home_button = tk.Button(self, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.grid(row=0, column=0)

        cat1_button = tk.Button(self, text="Technologies and Connection Types", command=lambda: master.switch_frame(IRP_Cat1_Page))
        cat2_button = tk.Button(self, text="Delivery Channels", command=lambda: master.switch_frame(IRP_Cat2_Page))
        cat3_button = tk.Button(self, text="Online/Mobile Products and Technology Services", command=lambda: master.switch_frame(IRP_Cat3_Page))
        cat4_button = tk.Button(self, text="Organizational Characteristics", command=lambda: master.switch_frame(IRP_Cat4_Page))
        cat5_button = tk.Button(self, text="External Threats", command=lambda: master.switch_frame(IRP_Cat5_Page))

        cat1_button.grid(row=1, column=1)
        cat2_button.grid(row=2, column=1)
        cat3_button.grid(row=3, column=1)
        cat4_button.grid(row=4, column=1)
        cat5_button.grid(row=5, column=1)

        cat1_label = tk.Label(self, text=str(submit_pressed(IRP_Cat1_Page.values)[5]) + "/" + str(len(DATA.IRP_Category1)))
        cat1_label.grid(row=1, column=2)
        cat2_label = tk.Label(self, text=str(submit_pressed(IRP_Cat2_Page.values)[5]) + "/" + str(len(DATA.IRP_Category2)))
        cat2_label.grid(row=2, column=2)
        cat3_label = tk.Label(self, text=str(submit_pressed(IRP_Cat3_Page.values)[5]) + "/" + str(len(DATA.IRP_Category3)))
        cat3_label.grid(row=3, column=2)
        cat4_label = tk.Label(self, text=str(submit_pressed(IRP_Cat4_Page.values)[5]) + "/" + str(len(DATA.IRP_Category4)))
        cat4_label.grid(row=4, column=2)
        cat5_label = tk.Label(self, text=str(submit_pressed(IRP_Cat5_Page.values)[5]) + "/" + str(len(DATA.IRP_Category5)))
        cat5_label.grid(row=5, column=2)

        total_least_label = tk.Label(self, text="Total Least = " + str(calculate_total()[0]))
        total_least_label.grid(row=6, column=1)
        total_minimal_label = tk.Label(self, text="Total Minimal = " + str(calculate_total()[1]))
        total_minimal_label.grid(row=7, column=1)
        total_moderate_label = tk.Label(self, text="Total Moderate = " + str(calculate_total()[2]))
        total_moderate_label.grid(row=8, column=1)
        total_significant_label = tk.Label(self, text="Total Significant = " + str(calculate_total()[3]))
        total_significant_label.grid(row=9, column=1)
        total_most_label = tk.Label(self, text="Total Most = " + str(calculate_total()[4]))
        total_most_label.grid(row=10, column=1)
    #endregion


""" Inherent Risk Profile - Category 1 (Technologies and Connection Types) 
    Responsible for the layout of Category 1 displaying all the questions and possible answers """
class IRP_Cat1_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(IRP_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(IRP_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: clear_pressed(self.values))
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, text="Least", borderwidth=3, relief="raised")
        label1.grid(row=0, column=1, sticky="n")
        label2 = tk.Label(middle_frame, text="Minimal", borderwidth=3, relief="raised")
        label2.grid(row=0, column=2, sticky="n")
        label3 = tk.Label(middle_frame, text="Moderate", borderwidth=3, relief="raised")
        label3.grid(row=0, column=3, sticky="n")
        label4 = tk.Label(middle_frame, text="Signigicant", borderwidth=3, relief="raised")
        label4.grid(row=0, column=4, sticky="n")
        label5 = tk.Label(middle_frame, text="Most", borderwidth=3, relief="raised")
        label5.grid(row=0, column=5, sticky="n")

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category1.items():
            question = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT)       # borderwidth=3, relief="raised", width=40
            question.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.values.append(tk.IntVar())
            #self.values[i].set(None)
            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1)
                answer.grid(row=i+1, column=j+1, padx=10, pady=10, sticky="w")
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 2 (Delivery Channels) 
    Responsible for the layout of Category 2 """
class IRP_Cat2_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Delivery Channels")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(IRP_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(IRP_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: clear_pressed(self.values))
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, text="Least", borderwidth=3, relief="raised")
        label1.grid(row=0, column=1, sticky="n")
        label2 = tk.Label(middle_frame, text="Minimal", borderwidth=3, relief="raised")
        label2.grid(row=0, column=2, sticky="n")
        label3 = tk.Label(middle_frame, text="Moderate", borderwidth=3, relief="raised")
        label3.grid(row=0, column=3, sticky="n")
        label4 = tk.Label(middle_frame, text="Signigicant", borderwidth=3, relief="raised")
        label4.grid(row=0, column=4, sticky="n")
        label5 = tk.Label(middle_frame, text="Most", borderwidth=3, relief="raised")
        label5.grid(row=0, column=5, sticky="n")

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category2.items():
            question = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT)       # borderwidth=3, relief="raised", width=40
            question.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.values.append(tk.IntVar())
            #self.values[i].set(None)
            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1)
                answer.grid(row=i+1, column=j+1, padx=10, pady=10, sticky="w")
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 3 (Online/Mobile Products and Technology Services) 
    Responsible for the layout of Category 3 """
class IRP_Cat3_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Online/Mobile Products and Technology Services")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(IRP_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(IRP_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: clear_pressed(self.values))
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, text="Least", borderwidth=3, relief="raised")
        label1.grid(row=0, column=1, sticky="n")
        label2 = tk.Label(middle_frame, text="Minimal", borderwidth=3, relief="raised")
        label2.grid(row=0, column=2, sticky="n")
        label3 = tk.Label(middle_frame, text="Moderate", borderwidth=3, relief="raised")
        label3.grid(row=0, column=3, sticky="n")
        label4 = tk.Label(middle_frame, text="Signigicant", borderwidth=3, relief="raised")
        label4.grid(row=0, column=4, sticky="n")
        label5 = tk.Label(middle_frame, text="Most", borderwidth=3, relief="raised")
        label5.grid(row=0, column=5, sticky="n")

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category3.items():
            question = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT)       # borderwidth=3, relief="raised", width=40
            question.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.values.append(tk.IntVar())
            #self.values[i].set(None)
            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1)
                answer.grid(row=i+1, column=j+1, padx=10, pady=10, sticky="w")
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 4 (Organizational Characteristics) 
    Responsible for the layout of Category 4 """
class IRP_Cat4_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Organizational Characteristics")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(IRP_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(IRP_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: clear_pressed(self.values))
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, text="Least", borderwidth=3, relief="raised")
        label1.grid(row=0, column=1, sticky="n")
        label2 = tk.Label(middle_frame, text="Minimal", borderwidth=3, relief="raised")
        label2.grid(row=0, column=2, sticky="n")
        label3 = tk.Label(middle_frame, text="Moderate", borderwidth=3, relief="raised")
        label3.grid(row=0, column=3, sticky="n")
        label4 = tk.Label(middle_frame, text="Signigicant", borderwidth=3, relief="raised")
        label4.grid(row=0, column=4, sticky="n")
        label5 = tk.Label(middle_frame, text="Most", borderwidth=3, relief="raised")
        label5.grid(row=0, column=5, sticky="n")

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category4.items():
            question = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT)       # borderwidth=3, relief="raised", width=40
            question.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.values.append(tk.IntVar())
            #self.values[i].set(None)
            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1)
                answer.grid(row=i+1, column=j+1, padx=10, pady=10, sticky="w")
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


""" Inherent Risk Profile - Category 5 (External Threats) 
    Responsible for the layout of Category 5 """
class IRP_Cat5_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - External Threats")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(IRP_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(IRP_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: clear_pressed(self.values))
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, text="Least", borderwidth=3, relief="raised")
        label1.grid(row=0, column=1, sticky="n")
        label2 = tk.Label(middle_frame, text="Minimal", borderwidth=3, relief="raised")
        label2.grid(row=0, column=2, sticky="n")
        label3 = tk.Label(middle_frame, text="Moderate", borderwidth=3, relief="raised")
        label3.grid(row=0, column=3, sticky="n")
        label4 = tk.Label(middle_frame, text="Signigicant", borderwidth=3, relief="raised")
        label4.grid(row=0, column=4, sticky="n")
        label5 = tk.Label(middle_frame, text="Most", borderwidth=3, relief="raised")
        label5.grid(row=0, column=5, sticky="n")

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category5.items():
            question = tk.Label(middle_frame, text=key, wraplength=300, justify=tk.LEFT)       # borderwidth=3, relief="raised", width=40
            question.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            self.values.append(tk.IntVar())
            #self.values[i].set(None)
            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1)
                answer.grid(row=i+1, column=j+1, padx=10, pady=10, sticky="w")
            i += 1

        #windll.shcore.SetProcessDpiAwareness(1)
    #endregion


def clear_pressed(values):
    for i in range(len(values)):
        values[i].set(0)


def submit_pressed(values):
    least = minimal = moderate = significant = most = total_selected = 0
    
    for i in range(len(values)):
        if (values[i].get() == 1):
            least += 1
            total_selected += 1
        elif (values[i].get() == 2):
            minimal += 1
            total_selected += 1
        elif (values[i].get() == 3):
            moderate += 1
            total_selected += 1
        elif (values[i].get() == 4):
            significant += 1
            total_selected += 1
        elif (values[i].get() == 5):
            most += 1
            total_selected += 1

    return [least, minimal, moderate, significant, most, total_selected]

            
def calculate_total():
    least_total = submit_pressed(IRP_Cat1_Page.values)[0] + submit_pressed(IRP_Cat2_Page.values)[0] + submit_pressed(IRP_Cat3_Page.values)[0] + submit_pressed(IRP_Cat4_Page.values)[0] + submit_pressed(IRP_Cat5_Page.values)[0]
    minimal_total = submit_pressed(IRP_Cat1_Page.values)[1] + submit_pressed(IRP_Cat2_Page.values)[1] + submit_pressed(IRP_Cat3_Page.values)[1] + submit_pressed(IRP_Cat4_Page.values)[1] + submit_pressed(IRP_Cat5_Page.values)[1]
    moderate_total = submit_pressed(IRP_Cat1_Page.values)[2] + submit_pressed(IRP_Cat2_Page.values)[2] + submit_pressed(IRP_Cat3_Page.values)[2] + submit_pressed(IRP_Cat4_Page.values)[2] + submit_pressed(IRP_Cat5_Page.values)[2]
    significant_total = submit_pressed(IRP_Cat1_Page.values)[3] + submit_pressed(IRP_Cat2_Page.values)[3] + submit_pressed(IRP_Cat3_Page.values)[3] + submit_pressed(IRP_Cat4_Page.values)[3] + submit_pressed(IRP_Cat5_Page.values)[3]
    most_total = submit_pressed(IRP_Cat1_Page.values)[4] + submit_pressed(IRP_Cat2_Page.values)[4] + submit_pressed(IRP_Cat3_Page.values)[4] + submit_pressed(IRP_Cat4_Page.values)[4] + submit_pressed(IRP_Cat5_Page.values)[4]

    return [least_total, minimal_total, moderate_total, significant_total, most_total]