
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE INHERENT RISK PROFILE """

import tkinter as tk
import DATA
import layout.layout_home as home


""" This class is responsible for the layout of the Inherent Risk Profile's Main page
    Contains the 5 categories and links to each one """
class IRP_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile")

        self.unbind_all("<MouseWheel>")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(6, minsize=50)
        self.rowconfigure(1, minsize=50)
        self.rowconfigure(2, minsize=50)
        self.rowconfigure(3, minsize=50)
        self.rowconfigure(4, minsize=50)
        self.rowconfigure(5, minsize=50)

        home_button = tk.Button(self, width=10, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.grid(row=0, column=0)

        cat1_button = tk.Button(self, width=40, text="Technologies and Connection Types", command=lambda: master.switch_frame(IRP_Cat1_Page))
        cat2_button = tk.Button(self, width=40, text="Delivery Channels", command=lambda: master.switch_frame(IRP_Cat2_Page))
        cat3_button = tk.Button(self, width=40, text="Online/Mobile Products and Technology Services", command=lambda: master.switch_frame(IRP_Cat3_Page))
        cat4_button = tk.Button(self, width=40, text="Organizational Characteristics", command=lambda: master.switch_frame(IRP_Cat4_Page))
        cat5_button = tk.Button(self, width=40, text="External Threats", command=lambda: master.switch_frame(IRP_Cat5_Page))

        cat1_button.grid(row=1, column=1, sticky="NSWE", pady=10)
        cat2_button.grid(row=2, column=1, sticky="NSWE", pady=10)
        cat3_button.grid(row=3, column=1, sticky="NSWE", pady=10)
        cat4_button.grid(row=4, column=1, sticky="NSWE", pady=10)
        cat5_button.grid(row=5, column=1, sticky="NSWE", pady=10)

        cat1_label = tk.Label(self, text=str(submit_pressed(IRP_Cat1_Page.values)[5]) + "/" + str(len(DATA.IRP_Category1)) + " Answered")
        cat1_label.grid(row=1, column=2, padx=30, sticky='w')
        cat2_label = tk.Label(self, text=str(submit_pressed(IRP_Cat2_Page.values)[5]) + "/" + str(len(DATA.IRP_Category2)) + " Answered")
        cat2_label.grid(row=2, column=2, padx=30, sticky='w')
        cat3_label = tk.Label(self, text=str(submit_pressed(IRP_Cat3_Page.values)[5]) + "/" + str(len(DATA.IRP_Category3)) + " Answered")
        cat3_label.grid(row=3, column=2, padx=30, sticky='w')
        cat4_label = tk.Label(self, text=str(submit_pressed(IRP_Cat4_Page.values)[5]) + "/" + str(len(DATA.IRP_Category4)) + " Answered")
        cat4_label.grid(row=4, column=2, padx=30, sticky='w')
        cat5_label = tk.Label(self, text=str(submit_pressed(IRP_Cat5_Page.values)[5]) + "/" + str(len(DATA.IRP_Category5)) + " Answered")
        cat5_label.grid(row=5, column=2, padx=30, sticky='w')

        submit_button = tk.Button(self, width=10, text="Submit", state="disabled")
        submit_button.grid(row=7, column=2)
        ToolTip(widget=submit_button, text="You need to answer all the questions to proceed")

        # if all the questions are answered, then enable the submit button
        if (calculate_total()[0] + calculate_total()[1] + calculate_total()[2] + calculate_total()[3] + calculate_total()[4] == int(str(len(DATA.IRP_Category1))) + int(str(len(DATA.IRP_Category2))) + int(str(len(DATA.IRP_Category3))) + int(str(len(DATA.IRP_Category4))) + int(str(len(DATA.IRP_Category5)))):
            submit_button['state'] = "normal"

        #total_least_label = tk.Label(self, text="Total Least = " + str(calculate_total()[0]))
        #total_least_label.grid(row=6, column=1)
        #total_minimal_label = tk.Label(self, text="Total Minimal = " + str(calculate_total()[1]))
        #total_minimal_label.grid(row=7, column=1)
        #total_moderate_label = tk.Label(self, text="Total Moderate = " + str(calculate_total()[2]))
        #total_moderate_label.grid(row=8, column=1)
        #total_significant_label = tk.Label(self, text="Total Significant = " + str(calculate_total()[3]))
        #total_significant_label.grid(row=9, column=1)
        #total_most_label = tk.Label(self, text="Total Most = " + str(calculate_total()[4]))
        #total_most_label.grid(row=10, column=1)
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
        top_frame = tk.Frame(self, bg="light steel blue")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")
        home_button = tk.Button(top_frame, width=10, text="HOME", bg="white", command=lambda: master.switch_frame(home.Home_Page))
        #home_button.pack(side=tk.LEFT, padx=50, pady=20)
        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button = tk.Button(top_frame, width=10, text="BACK", bg="white", command=lambda: master.switch_frame(IRP_Page))
        #back_button.pack(side=tk.LEFT)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="light steel blue")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")
        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', bg="white", command=lambda: master.switch_frame(IRP_Page))
        submit_button.pack(side=tk.RIGHT, padx=40, pady=20)
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', bg="white", command=lambda: clear_pressed(self.values))
        clear_button.pack(side=tk.RIGHT)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="light steel blue")

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas, borderwidth=3, relief="sunken", bg="gray99")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        top_frame.columnconfigure(2, minsize=220)
        top_frame.columnconfigure(4, minsize=60)
        top_frame.columnconfigure(6, minsize=115)
        top_frame.columnconfigure(8, minsize=105)
        top_frame.columnconfigure(10, minsize=150)

        # Labels representing the risk levels
        label1 = tk.Label(top_frame, width=15, text="Least", borderwidth=3, relief="groove")
        #label1.grid(row=0, column=1, pady=5, sticky="n")
        label1.grid(row=1, column=3)
        label2 = tk.Label(top_frame, width=15, text="Minimal", borderwidth=3, relief="groove")
        #label2.grid(row=0, column=2, pady=5, sticky="n")
        label2.grid(row=1, column=5)
        label3 = tk.Label(top_frame, width=15, text="Moderate", borderwidth=3, relief="groove")
        #label3.grid(row=0, column=3, pady=5, sticky="n")
        label3.grid(row=1, column=7)
        label4 = tk.Label(top_frame, width=15, text="Signigicant", borderwidth=3, relief="groove")
        #label4.grid(row=0, column=4, pady=5, sticky="n")
        label4.grid(row=1, column=9)
        label5 = tk.Label(top_frame, width=15, text="Most", borderwidth=3, relief="groove")
        #label5.grid(row=0, column=5, pady=5, sticky="n")
        label5.grid(row=1, column=11)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category1.items():
            question = tk.Label(middle_frame, width=45, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="bold", bg="gray99")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())
            #self.values[i].set(None)
            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, bg="gray99")
                answer.grid(row=i+1, column=j+1, padx=15, pady=10, sticky="W")
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

        middle_frame = tk.Frame(self)
        middle_frame.pack(anchor="w")

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
        
        middle_frame = tk.Frame(self)
        middle_frame.pack(anchor="w")

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
        
        middle_frame = tk.Frame(self)
        middle_frame.pack(anchor="w")

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


class ToolTip(object):
    #region
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        self.tooltipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1) # window without border and no normal means of closing
        tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx()-10, self.widget.winfo_rooty()-15))
        label = tk.Label(tw, text = self.text, background = "#ffffe0", relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        tw.destroy()
        self.tooltipwindow = None
    #endregion


""" This function clears the selection of radio buttons 
    @Arg = List[] | contains the variable that is a reference to the radio buttons """
def clear_pressed(values):
    for i in range(len(values)):
        values[i].set(0)


""" This function counts the number of selected values in the radio buttons
    @Arg = List[] | contains the variable that is a reference to the radio buttons """
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


""" This functions calculates the total value of each risk level across all the categories of the Inherent Risk Profile """           
def calculate_total():
    least_total = submit_pressed(IRP_Cat1_Page.values)[0] + submit_pressed(IRP_Cat2_Page.values)[0] + submit_pressed(IRP_Cat3_Page.values)[0] + submit_pressed(IRP_Cat4_Page.values)[0] + submit_pressed(IRP_Cat5_Page.values)[0]
    minimal_total = submit_pressed(IRP_Cat1_Page.values)[1] + submit_pressed(IRP_Cat2_Page.values)[1] + submit_pressed(IRP_Cat3_Page.values)[1] + submit_pressed(IRP_Cat4_Page.values)[1] + submit_pressed(IRP_Cat5_Page.values)[1]
    moderate_total = submit_pressed(IRP_Cat1_Page.values)[2] + submit_pressed(IRP_Cat2_Page.values)[2] + submit_pressed(IRP_Cat3_Page.values)[2] + submit_pressed(IRP_Cat4_Page.values)[2] + submit_pressed(IRP_Cat5_Page.values)[2]
    significant_total = submit_pressed(IRP_Cat1_Page.values)[3] + submit_pressed(IRP_Cat2_Page.values)[3] + submit_pressed(IRP_Cat3_Page.values)[3] + submit_pressed(IRP_Cat4_Page.values)[3] + submit_pressed(IRP_Cat5_Page.values)[3]
    most_total = submit_pressed(IRP_Cat1_Page.values)[4] + submit_pressed(IRP_Cat2_Page.values)[4] + submit_pressed(IRP_Cat3_Page.values)[4] + submit_pressed(IRP_Cat4_Page.values)[4] + submit_pressed(IRP_Cat5_Page.values)[4]

    return [least_total, minimal_total, moderate_total, significant_total, most_total]
