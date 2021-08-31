
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE INHERENT RISK PROFILE """

import layout.layout_home as home
import layout.layout_login as login
import DATA
import db

import tkinter as tk
from tkinter import messagebox
from datetime import datetime


""" This class is responsible for the layout of the Inherent Risk Profile's Main page
    Contains the 5 categories and links to each one """
class IRP_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Inherent Risk Profile")   # window title

        self.config(bg="ghost white")       # frame background
        self.unbind_all("<MouseWheel>")     # unbind mousewheel

        home_button = tk.Button(self, width=10, text="HOME", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        cat1_button = tk.Button(self, text="Technologies and Connection Types", 
                                font="Calibri 14", relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat1_Page))

        cat2_button = tk.Button(self, text="Delivery Channels",  
                                font="Calibri 14", relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat2_Page))

        cat3_button = tk.Button(self, text="Online/Mobile Products and Technology Services",  
                                font="Calibri 14", relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat3_Page))

        cat4_button = tk.Button(self, text="Organizational Characteristics",  
                                font="Calibri 14", relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat4_Page))

        cat5_button = tk.Button(self, text="External Threats",  
                                font="Calibri 14", relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat5_Page))

        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(6, minsize=50)
        self.rowconfigure(1, minsize=50)
        self.rowconfigure(2, minsize=50)
        self.rowconfigure(3, minsize=50)
        self.rowconfigure(4, minsize=50)
        self.rowconfigure(5, minsize=50)

        home_button.grid(row=0, column=0)
        cat1_button.grid(row=1, column=1, pady=10)
        cat2_button.grid(row=2, column=1, pady=10)
        cat3_button.grid(row=3, column=1, pady=10)
        cat4_button.grid(row=4, column=1, pady=10)
        cat5_button.grid(row=5, column=1, pady=10)

        cat1_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat1_Page.values)[5]) + "/" + str(len(DATA.IRP_Category1)) + " Answered")

        cat2_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat2_Page.values)[5]) + "/" + str(len(DATA.IRP_Category2)) + " Answered")
        
        cat3_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat3_Page.values)[5]) + "/" + str(len(DATA.IRP_Category3)) + " Answered")
        
        cat4_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat4_Page.values)[5]) + "/" + str(len(DATA.IRP_Category4)) + " Answered")
        
        cat5_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat5_Page.values)[5]) + "/" + str(len(DATA.IRP_Category5)) + " Answered")
    
        cat1_label.grid(row=1, column=2, padx=30, sticky='nsew')
        cat2_label.grid(row=2, column=2, padx=30, sticky='nsew')
        cat3_label.grid(row=3, column=2, padx=30, sticky='nsew')
        cat4_label.grid(row=4, column=2, padx=30, sticky='nsew')
        cat5_label.grid(row=5, column=2, padx=30, sticky='nsew')

        reset_button = tk.Button(self, width=10, text='RESET', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: IRP_Page.reset_switch_irp(master))

        final_score_button = tk.Button(self, width=10, text="Final Score", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', 
                                  activebackground='light blue', command=lambda: master.switch_frame(IRP_Final), state="disabled")

        reset_button.grid(row=7, column=1)
        final_score_button.grid(row=7, column=2)

        # adds a tooltip to the final score button
        ToolTip(widget=final_score_button, text="Answer all the questions to proceed")

        # if all the questions are answered, then enable the submit button
        if (calculate_total()[0] + calculate_total()[1] + calculate_total()[2] + calculate_total()[3] + calculate_total()[4] == len(DATA.IRP_Category1) + len(DATA.IRP_Category2) + len(DATA.IRP_Category3) + len(DATA.IRP_Category4) + len(DATA.IRP_Category5)):
            final_score_button['state'] = "normal"


    # confirmation window which resets the IRP answers if the user clicks ok
    def reset_switch_irp(frame):
        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your answers ?')
        if confirm:
            reset_irp()
            frame.switch_frame(IRP_Page)    # switch frame to IRP_Page
    #endregion


""" Inherent Risk Profile - Category 1 (Technologies and Connection Types) 
    Responsible for the layout of Category 1 displaying all the questions and possible answers """
class IRP_Cat1_Page(tk.Frame):
    #region

    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Technologies and Connection Types")

        self.config(bg="ghost white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)

        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg="white")

        # defines the scrolling distance when mousewheel is used
        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(middle_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(middle_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(middle_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(middle_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        label3.grid(row=0, column=3, sticky='w', padx=30)
        label4.grid(row=0, column=4, sticky='w', padx=30)
        label5.grid(row=0, column=5, sticky='w', padx=30)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category1.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=20, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 2 (Delivery Channels) 
    Responsible for the layout of Category 2 """
class IRP_Cat2_Page(tk.Frame):
    #region

    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Delivery Channels")

        self.config(bg="white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)

        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")
                                                   
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')
        my_canvas.configure(xscrollcommand=horizontal_scrollbar.set, bg='white')
        
        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(middle_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(middle_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(middle_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(middle_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        label3.grid(row=0, column=3, sticky='w', padx=30)
        label4.grid(row=0, column=4, sticky='w', padx=30)
        label5.grid(row=0, column=5, sticky='w', padx=30)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category2.items():

            question = tk.Label(middle_frame, width=40, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=50, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 3 (Online/Mobile Products and Technology Services) 
    Responsible for the layout of Category 3 """
class IRP_Cat3_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Online/Mobile Products and Technology Services")

        self.config(bg="ghost white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)

        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg="white")

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(middle_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(middle_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(middle_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(middle_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        label3.grid(row=0, column=3, sticky='w', padx=30)
        label4.grid(row=0, column=4, sticky='w', padx=30)
        label5.grid(row=0, column=5, sticky='w', padx=30)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category3.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=20, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 4 (Organizational Characteristics) 
    Responsible for the layout of Category 4 """
class IRP_Cat4_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Organizational Characteristics")

        self.config(bg="ghost white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)

        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg="white")

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(middle_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(middle_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(middle_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(middle_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        label3.grid(row=0, column=3, sticky='w', padx=30)
        label4.grid(row=0, column=4, sticky='w', padx=30)
        label5.grid(row=0, column=5, sticky='w', padx=30)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category4.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=20, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 5 (External Threats) 
    Responsible for the layout of Category 5 """
class IRP_Cat5_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - External Threats")

        self.config(bg="white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)

        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")
                                                   
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')
        my_canvas.configure(xscrollcommand=horizontal_scrollbar.set, bg='white')

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(middle_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(middle_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(middle_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(middle_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        label3.grid(row=0, column=3, sticky='w', padx=30)
        label4.grid(row=0, column=4, sticky='w', padx=30)
        label5.grid(row=0, column=5, sticky='w', padx=30)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category5.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=150, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Score page """
class IRP_Final(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Inherent Risk Profile - Score")
        self.config(bg="ghost white")

        # limit entry to alphanumeric characters only
        def only_alphanumeric(char):
            return char.isalnum()

        alpha_num_validation = self.register(only_alphanumeric)

        home_button = tk.Button(self, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue', 
                                text='HOME', width=10, command=lambda: master.switch_frame(home.Home_Page))

        back_button = tk.Button(self, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                text='BACK', width=10, command=lambda: master.switch_frame(IRP_Page))

        least_total_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Least: ' + str(calculate_total()[0]) + ' Point(s)')
        minimal_total_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Minimal: ' + str(calculate_total()[1]) + ' Point(s)')
        moderate_total_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Moderate: ' + str(calculate_total()[2]) + ' Point(s)')
        significant_total_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Significant: ' + str(calculate_total()[3]) + ' Point(s)')
        most_total_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Most: ' + str(calculate_total()[4]) + ' Point(s)')
        final_score_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Risk Level: ' + IRP_Final.find_max())                      
        
        assessment_name_entry = tk.Entry(self, font="Calirbi 11 bold", relief='groove', borderwidth=3, fg='white', insertbackground='white', cursor='top_left_arrow',
                                         bg='SlateGray4', width=20, validate='key', validatecommand=(alpha_num_validation, '%S'))

        # add tooltip for the assessment name entry field
        ToolTip(widget=assessment_name_entry, text="Enter a unique name for the assessment")
        
        save_results_button = tk.Button(self, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                        text='SAVE', width=10, command=lambda: IRP_Final.save(master, assessment_name_entry.get()))

        home_button.place(relx=0.1, rely=0.1, anchor='nw')
        back_button.place(relx=0.25, rely=0.1, anchor='nw')

        least_total_label.place(relx=0.51, rely=0.3, anchor='center')
        minimal_total_label.place(relx=0.51, rely=0.36, anchor='center')
        moderate_total_label.place(relx=0.51, rely=0.42, anchor='center')
        significant_total_label.place(relx=0.51, rely=0.48, anchor='center')
        most_total_label.place(relx=0.51, rely=0.54, anchor='center')
        final_score_label.place(relx=0.51, rely=0.66, anchor='center')

        assessment_name_entry.place(relx=0.51, rely=0.8, anchor='center')
        save_results_button.place(relx=0.68, rely=0.8, anchor='center')


    # find the risk category with the maximum answers and return it as a String
    def find_max():
        max_value = max(calculate_total())
        indexes = [i for i, j in enumerate(calculate_total()) if j == max_value]
        if max_value == 0:
            return ''
        elif 4 in indexes:
            return 'Most'
        elif 3 in indexes:
            return 'Significant'
        elif 2 in indexes:
            return 'Moderate'
        elif 1 in indexes:
            return 'Minimal'
        elif 0 in indexes:
            return 'Least'

    # handles saving the results to the database with all the validations required
    def save(frame, name):
        name = name.lower()
        get_userInfo_query = """ SELECT uid,company FROM users WHERE username=%s; """
        u_value = [login.Login_Page.logged_in]

        db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA") # open db connection
        uInfo = db.read_query_data(db_connection, get_userInfo_query, u_value)

        insert_irp_query = """ 
        INSERT INTO irp (name, date, user, company, least, minimal, moderate, significant, most, risk_level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); 
        """
        values = [name, datetime.now(), uInfo[0][0], uInfo[0][1], calculate_total()[0], calculate_total()[1], calculate_total()[2], calculate_total()[3], calculate_total()[4], IRP_Final.find_max()]
        
        get_assessment_name_query = """ SELECT name FROM irp WHERE name=%s; """
        name_value = [name]
        assessment_name = db.read_query_data(db_connection, get_assessment_name_query, name_value)

        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to save your results ?')

        if confirm:
            if name == "":
                messagebox.showwarning("Warning", "You need to enter a name for the assessment")
            elif assessment_name:
                messagebox.showwarning("Warning", "An assessment with this name already exists")
            else:
                db.execute_query_data(db_connection, insert_irp_query, values)
                reset_irp()
                frame.switch_frame(home.Home_Page)

        db_connection.close()
    #endregion


""" This class handles the display of the tooltip """
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
        if tw is not None:
            tw.destroy()
        self.tooltipwindow = None
    #endregion


# this funtion resets the answers of all the IRP categories
def reset_irp():
    clear_pressed(IRP_Cat1_Page.values)
    clear_pressed(IRP_Cat2_Page.values)
    clear_pressed(IRP_Cat3_Page.values)
    clear_pressed(IRP_Cat4_Page.values)
    clear_pressed(IRP_Cat5_Page.values)


# this function clears the answers of a category after a confirmation window
def clear_category(values):
    confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your answers ?')
    if confirm:
        clear_pressed(values)


""" This function clears the selection of radio buttons 
    @arg = List[] | contains the variable that is a reference to the radio buttons """
def clear_pressed(values):
    for i in range(len(values)):
        values[i].set(0)


""" This function counts the number of answers in each risk level in every category independently
    @arg = List[] | contains the variable that is a reference to the radio buttons """
def calculate_total_per_category(values):
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
    least_total = calculate_total_per_category(IRP_Cat1_Page.values)[0] + calculate_total_per_category(IRP_Cat2_Page.values)[0] + calculate_total_per_category(IRP_Cat3_Page.values)[0] + calculate_total_per_category(IRP_Cat4_Page.values)[0] + calculate_total_per_category(IRP_Cat5_Page.values)[0]
    minimal_total = calculate_total_per_category(IRP_Cat1_Page.values)[1] + calculate_total_per_category(IRP_Cat2_Page.values)[1] + calculate_total_per_category(IRP_Cat3_Page.values)[1] + calculate_total_per_category(IRP_Cat4_Page.values)[1] + calculate_total_per_category(IRP_Cat5_Page.values)[1]
    moderate_total = calculate_total_per_category(IRP_Cat1_Page.values)[2] + calculate_total_per_category(IRP_Cat2_Page.values)[2] + calculate_total_per_category(IRP_Cat3_Page.values)[2] + calculate_total_per_category(IRP_Cat4_Page.values)[2] + calculate_total_per_category(IRP_Cat5_Page.values)[2]
    significant_total = calculate_total_per_category(IRP_Cat1_Page.values)[3] + calculate_total_per_category(IRP_Cat2_Page.values)[3] + calculate_total_per_category(IRP_Cat3_Page.values)[3] + calculate_total_per_category(IRP_Cat4_Page.values)[3] + calculate_total_per_category(IRP_Cat5_Page.values)[3]
    most_total = calculate_total_per_category(IRP_Cat1_Page.values)[4] + calculate_total_per_category(IRP_Cat2_Page.values)[4] + calculate_total_per_category(IRP_Cat3_Page.values)[4] + calculate_total_per_category(IRP_Cat4_Page.values)[4] + calculate_total_per_category(IRP_Cat5_Page.values)[4]

    return [least_total, minimal_total, moderate_total, significant_total, most_total]
