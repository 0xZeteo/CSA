
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE CYBERSECURITY MATURITY """

import tkinter as tk
import DATA
import layout.layout_home as home
import layout.layout_csm as csm

""" This file is responsible for the layout of the Cybersecurity Maturity's Domain 1 page and everything within it """

class CSM_Domain5_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Maturity - Cyber Incident Management and Resilience")

        self.unbind_all("<MouseWheel>")

        home_button = tk.Button(self, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        back_button = tk.Button(self, text="Back", command=lambda: master.switch_frame(csm.CSM_Page))
        home_button.grid(row=0, column=0)
        back_button.grid(row=0, column=1)

        incident_planning_and_strategy_button = tk.Button(self, text="Governance", command=lambda: master.switch_frame(CSM_Domain5_IncidentPlanningAndStrategy_Page))
        detection_response_and_mitigation_button = tk.Button(self, text="Risk Management", command=lambda: master.switch_frame(CSM_Domain5_DetectionResponseAndMitigation_Page))
        escalation_and_reporting_button = tk.Button(self, text="Resources", command=lambda: master.switch_frame(CSM_Domain5_EscalationAndReporting_Page))

        incident_planning_and_strategy_button.grid(row=1, column=2)
        detection_response_and_mitigation_button.grid(row=2, column=2)
        escalation_and_reporting_button.grid(row=3, column=2)

        incident_planning_and_strategyincident_planning_and_strategy_label = tk.Label(self, text=str(csm.submit_pressed(CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain5_IncidentPlanningAndStrategy[i]) for i in DATA.CSM_Domain5_IncidentPlanningAndStrategy])))
        detection_response_and_mitigation_label = tk.Label(self, text=str(csm.submit_pressed(CSM_Domain5_DetectionResponseAndMitigation_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain5_DetectionResponseAndMitigation[i]) for i in DATA.CSM_Domain5_DetectionResponseAndMitigation])))
        escalation_and_reporting_label = tk.Label(self, text=str(csm.submit_pressed(CSM_Domain5_EscalationAndReporting_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain5_EscalationAndReporting[i]) for i in DATA.CSM_Domain5_EscalationAndReporting])))

        incident_planning_and_strategyincident_planning_and_strategy_label.grid(row=1, column=3)
        detection_response_and_mitigation_label.grid(row=2, column=3)
        escalation_and_reporting_label.grid(row=3, column=3)
    #endregion


class CSM_Domain5_IncidentPlanningAndStrategy_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Incident Management and Resilience - Incident Planning and Strategy")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain5_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain5_Page))
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
        for key,values in DATA.CSM_Domain5_IncidentPlanningAndStrategy.items():               
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


class CSM_Domain5_DetectionResponseAndMitigation_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Incident Management and Resilience - Detection Response and Mitigation")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain5_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain5_Page))
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
        for key,values in DATA.CSM_Domain5_DetectionResponseAndMitigation.items():               
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


class CSM_Domain5_EscalationAndReporting_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cyber Incident Management and Resilience - Escalation and Reporting")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain5_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain5_Page))
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
        for key,values in DATA.CSM_Domain5_EscalationAndReporting.items():               
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
