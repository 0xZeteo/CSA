
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE CYBERSECURITY MATURITY """

import tkinter as tk
import DATA
import layout.layout_home as home
import layout.layout_csm as csm

""" This file is responsible for the layout of the Cybersecurity Maturity's Domain 1 page and everything within it """

class CSM_Domain1_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Maturity - Cyber Risk Management and Oversight")

        self.unbind_all("<MouseWheel>")
        self.config(bg="ghost white")

        # font="Calibri 14", relief='groove', borderwidth=3, bg='light gray', activebackground='light blue' (Button)

        # font="Calibri 15", bg="ghost white",  (Label)

        home_button = tk.Button(self, width=10, text="Home", font='Calibri 14', relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        back_button = tk.Button(self, width=10, text="Back", font='Calibri 14', relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(csm.CSM_Page))

        governance_button = tk.Button(self, text="Governance", font='Calibri 14', relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                      command=lambda: master.switch_frame(CSM_Domain1_Governance_Page))

        risk_management_button = tk.Button(self, text="Risk Management", font='Calibri 14', relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                           command=lambda: master.switch_frame(CSM_Domain1_RiskManagement_Page))

        resources_button = tk.Button(self, text="Resources", font='Calibri 14', relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                     command=lambda: master.switch_frame(CSM_Domain1_Resources_Page))

        training_and_culture_button = tk.Button(self, text="Training and Culture", font='Calibri 14', relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                                command=lambda: master.switch_frame(CSM_Domain1_TrainingAndCulture_Page))

        governance_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                    text=str(csm.submit_pressed(CSM_Domain1_Governance_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance])))
        
        risk_management_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                         text=str(csm.submit_pressed(CSM_Domain1_RiskManagement_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement])))
        
        resources_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                   text=str(csm.submit_pressed(CSM_Domain1_Resources_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources])))
        
        training_and_culture_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                              text=str(csm.submit_pressed(CSM_Domain1_TrainingAndCulture_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture])))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(2, minsize=25)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)

        home_button.grid(row=0, column=0)
        back_button.grid(row=0, column=1)

        governance_button.grid(row=1, column=3)
        risk_management_button.grid(row=2, column=3)
        resources_button.grid(row=3, column=3)
        training_and_culture_button.grid(row=4, column=3)

        governance_label.grid(row=1, column=4)
        risk_management_label.grid(row=2, column=4)
        resources_label.grid(row=3, column=4)
        training_and_culture_label.grid(row=4, column=4)
    #endregion


class CSM_Domain1_Governance_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Governance")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain1_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: csm.clear_pressed(self.values)) #############
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor='center')
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar

        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_Governance.items():               
            for j in range(len(values)):

                question = tk.Label(middle_frame, text=values[j], width=190, wraplength=1500, justify=tk.LEFT)
                question.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", variable=self.values[i], value=1)
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", variable=self.values[i], value=2)
                no_answer = tk.Radiobutton(middle_frame, text="N", variable=self.values[i], value=3)
                yes_answer.grid(row=i, column=1)
                yes_c_answer.grid(row=i, column=2)
                no_answer.grid(row=i, column=3)

                i += 1
    #endregion


class CSM_Domain1_RiskManagement_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Risk Management")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain1_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: csm.clear_pressed(self.values)) #############
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

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_RiskManagement.items():               
            for j in range(len(values)):
                question = tk.Label(middle_frame, text=values[j], wraplength=700, justify=tk.LEFT)
                question.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                    
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", variable=self.values[i], value=1)
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", variable=self.values[i], value=2)
                no_answer = tk.Radiobutton(middle_frame, text="N", variable=self.values[i], value=3)
                yes_answer.grid(row=i, column=1)
                yes_c_answer.grid(row=i, column=2)
                no_answer.grid(row=i, column=3)

                i += 1
    #endregion


class CSM_Domain1_Resources_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Resources")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain1_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: csm.clear_pressed(self.values)) #############
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

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_Resources.items():               
            for j in range(len(values)):
                question = tk.Label(middle_frame, text=values[j], wraplength=700, justify=tk.LEFT)
                question.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                    
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", variable=self.values[i], value=1)
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", variable=self.values[i], value=2)
                no_answer = tk.Radiobutton(middle_frame, text="N", variable=self.values[i], value=3)
                yes_answer.grid(row=i, column=1)
                yes_c_answer.grid(row=i, column=2)
                no_answer.grid(row=i, column=3)

                i += 1
    #endregion


class CSM_Domain1_TrainingAndCulture_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Training and Culture")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain1_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: csm.clear_pressed(self.values)) #############
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

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_TrainingAndCulture.items():               
            for j in range(len(values)):
                question = tk.Label(middle_frame, text=values[j], wraplength=700, justify=tk.LEFT)
                question.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                    
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", variable=self.values[i], value=1)
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", variable=self.values[i], value=2)
                no_answer = tk.Radiobutton(middle_frame, text="N", variable=self.values[i], value=3)
                yes_answer.grid(row=i, column=1)
                yes_c_answer.grid(row=i, column=2)
                no_answer.grid(row=i, column=3)

                i += 1
    #endregion


