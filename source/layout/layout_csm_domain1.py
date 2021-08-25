
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

        home_button = tk.Button(self, width=10, text="HOME", font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        back_button = tk.Button(self, width=10, text="BACK", font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(csm.CSM_Page))

        governance_button = tk.Button(self, text="Governance", font='Calibri 14', relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                      command=lambda: master.switch_frame(CSM_Domain1_Governance_Page))

        risk_management_button = tk.Button(self, text="Risk Management", font='Calibri 14', relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                           command=lambda: master.switch_frame(CSM_Domain1_RiskManagement_Page))

        resources_button = tk.Button(self, text="Resources", font='Calibri 14', relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                     command=lambda: master.switch_frame(CSM_Domain1_Resources_Page))

        training_and_culture_button = tk.Button(self, text="Training and Culture", font='Calibri 14', relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                                command=lambda: master.switch_frame(CSM_Domain1_TrainingAndCulture_Page))

        governance_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                    text=str(csm.submit_pressed(CSM_Domain1_Governance_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance])) + " Answered")
        
        risk_management_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                         text=str(csm.submit_pressed(CSM_Domain1_RiskManagement_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement])) + " Answered")
        
        resources_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                   text=str(csm.submit_pressed(CSM_Domain1_Resources_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources])) + " Answered")
        
        training_and_culture_label = tk.Label(self, font="Calibri 15", bg="ghost white", 
                                              text=str(csm.submit_pressed(CSM_Domain1_TrainingAndCulture_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture])) + " Answered")

        reset_button = tk.Button(self, text='RESET', width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: CSM_Domain1_Page.reset(master))

        home_button.place(relx=0.1, rely=0.1)
        back_button.place(relx=0.25, rely=0.1)

        governance_button.place(relx=0.5, rely=0.3, anchor='center')
        risk_management_button.place(relx=0.5, rely=0.4, anchor='center')
        resources_button.place(relx=0.5, rely=0.5, anchor='center')
        training_and_culture_button.place(relx=0.5, rely=0.6, anchor='center')

        governance_label.place(relx=0.67, rely=0.3, anchor='center')
        risk_management_label.place(relx=0.67, rely=0.4, anchor='center')
        resources_label.place(relx=0.67, rely=0.5, anchor='center')
        training_and_culture_label.place(relx=0.67, rely=0.6, anchor='center')

        reset_button.place(relx=0.5, rely=0.8, anchor='center')

    def reset(frame):
        csm.clear_pressed(CSM_Domain1_Governance_Page.values)
        csm.clear_pressed(CSM_Domain1_RiskManagement_Page.values)
        csm.clear_pressed(CSM_Domain1_Resources_Page.values)
        csm.clear_pressed(CSM_Domain1_TrainingAndCulture_Page.values)
        frame.switch_frame(CSM_Domain1_Page)
    #endregion


class CSM_Domain1_Governance_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Governance")
        self.config(bg='ghost white')

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")

        home_button = tk.Button(top_frame, text="HOME", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        home_button.pack(side=tk.LEFT, padx=20, pady=20)

        back_button = tk.Button(top_frame, text="BACK", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(CSM_Domain1_Page))

        submit_button.pack(side=tk.RIGHT, padx=20)

        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: csm.clear_pressed(self.values))

        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor='center')
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg='white')

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar

        middle_frame = tk.Frame(my_canvas, bg='white')
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_Governance.items():               
            for j in range(len(values)): 

                question = tk.Label(middle_frame, text=values[j], width=140, wraplength=1200, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])

                if key.endswith('1'):
                    yes_answer['value'] = 11
                    yes_c_answer['value'] = 21
                    no_answer['value'] = 31

                if key.endswith('2'):
                    yes_answer['value'] = 12
                    yes_c_answer['value'] = 22
                    no_answer['value'] = 32

                if key.endswith('3'):
                    yes_answer['value'] = 13
                    yes_c_answer['value'] = 23
                    no_answer['value'] = 33

                if key.endswith('4'):
                    yes_answer['value'] = 14
                    yes_c_answer['value'] = 24
                    no_answer['value'] = 34

                if key.endswith('5'):
                    yes_answer['value'] = 15
                    yes_c_answer['value'] = 25
                    no_answer['value'] = 35

                yes_answer.grid(row=i, column=1, padx=20)
                yes_c_answer.grid(row=i, column=2, padx=10)
                no_answer.grid(row=i, column=3, padx=15)

                i += 1
    #endregion


class CSM_Domain1_RiskManagement_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Governance")
        self.config(bg='ghost white')

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")

        home_button = tk.Button(top_frame, text="HOME", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        home_button.pack(side=tk.LEFT, padx=20, pady=20)

        back_button = tk.Button(top_frame, text="BACK", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(CSM_Domain1_Page))

        submit_button.pack(side=tk.RIGHT, padx=20)

        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: csm.clear_pressed(self.values)) #############

        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor='center')
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg='white')

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar

        middle_frame = tk.Frame(my_canvas, bg='white')
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_RiskManagement.items():               
            for j in range(len(values)): 

                question = tk.Label(middle_frame, text=values[j], width=140, wraplength=1200, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])

                if key.endswith('1'):
                    yes_answer['value'] = 11
                    yes_c_answer['value'] = 21
                    no_answer['value'] = 31

                if key.endswith('2'):
                    yes_answer['value'] = 12
                    yes_c_answer['value'] = 22
                    no_answer['value'] = 32

                if key.endswith('3'):
                    yes_answer['value'] = 13
                    yes_c_answer['value'] = 23
                    no_answer['value'] = 33

                if key.endswith('4'):
                    yes_answer['value'] = 14
                    yes_c_answer['value'] = 24
                    no_answer['value'] = 34

                if key.endswith('5'):
                    yes_answer['value'] = 15
                    yes_c_answer['value'] = 25
                    no_answer['value'] = 35

                yes_answer.grid(row=i, column=1, padx=20)
                yes_c_answer.grid(row=i, column=2, padx=10)
                no_answer.grid(row=i, column=3, padx=15)

                i += 1
    #endregion


class CSM_Domain1_Resources_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Governance")
        self.config(bg='ghost white')

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")

        home_button = tk.Button(top_frame, text="HOME", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        home_button.pack(side=tk.LEFT, padx=20, pady=20)

        back_button = tk.Button(top_frame, text="BACK", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg='ghost white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(CSM_Domain1_Page))

        submit_button.pack(side=tk.RIGHT, padx=20)

        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: csm.clear_pressed(self.values)) #############

        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame
        middle_frame = tk.Frame(self, bg='white', relief='groove', borderwidth=3)
        middle_frame.pack(anchor='nw', fill='x')

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_Resources.items():               
            for j in range(len(values)):

                question = tk.Label(middle_frame, text=values[j], width=140, wraplength=1200, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                
                if key.endswith('1'):
                    yes_answer['value'] = 11
                    yes_c_answer['value'] = 21
                    no_answer['value'] = 31

                if key.endswith('2'):
                    yes_answer['value'] = 12
                    yes_c_answer['value'] = 22
                    no_answer['value'] = 32

                if key.endswith('3'):
                    yes_answer['value'] = 13
                    yes_c_answer['value'] = 23
                    no_answer['value'] = 33

                if key.endswith('4'):
                    yes_answer['value'] = 14
                    yes_c_answer['value'] = 24
                    no_answer['value'] = 34

                if key.endswith('5'):
                    yes_answer['value'] = 15
                    yes_c_answer['value'] = 25
                    no_answer['value'] = 35
                
                yes_answer.grid(row=i, column=1, padx=20)
                yes_c_answer.grid(row=i, column=2, padx=10)
                no_answer.grid(row=i, column=3, padx=15)

                i += 1
    #endregion


class CSM_Domain1_TrainingAndCulture_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Risk Management and Oversight - Governance")
        self.config(bg='ghost white')

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")

        home_button = tk.Button(top_frame, text="HOME", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        home_button.pack(side=tk.LEFT, padx=20, pady=20)

        back_button = tk.Button(top_frame, text="BACK", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(CSM_Domain1_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(CSM_Domain1_Page))

        submit_button.pack(side=tk.RIGHT, padx=20)

        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: csm.clear_pressed(self.values)) #############

        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor='center')
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg='white')

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar

        middle_frame = tk.Frame(my_canvas, bg='white')
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain1_TrainingAndCulture.items():               
            for j in range(len(values)):

                question = tk.Label(middle_frame, text=values[j], width=140, wraplength=1200, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                
                if key.endswith('1'):
                    yes_answer['value'] = 11
                    yes_c_answer['value'] = 21
                    no_answer['value'] = 31

                if key.endswith('2'):
                    yes_answer['value'] = 12
                    yes_c_answer['value'] = 22
                    no_answer['value'] = 32

                if key.endswith('3'):
                    yes_answer['value'] = 13
                    yes_c_answer['value'] = 23
                    no_answer['value'] = 33

                if key.endswith('4'):
                    yes_answer['value'] = 14
                    yes_c_answer['value'] = 24
                    no_answer['value'] = 34

                if key.endswith('5'):
                    yes_answer['value'] = 15
                    yes_c_answer['value'] = 25
                    no_answer['value'] = 35
                
                yes_answer.grid(row=i, column=1, padx=20)
                yes_c_answer.grid(row=i, column=2, padx=10)
                no_answer.grid(row=i, column=3, padx=15)

                i += 1
    #endregion


