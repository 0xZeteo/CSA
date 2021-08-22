import tkinter as tk
import layout.layout_home as home
import layout.layout_csm_domain1 as d1
import layout.layout_csm_domain2 as d2
import layout.layout_csm_domain3 as d3
import layout.layout_csm_domain4 as d4
import layout.layout_csm_domain5 as d5

""" This class is responsible for the layout of the Cybersecurity Maturity's Main page
    Contains all the categories and links to each one """

class CSM_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Maturity")

        self.config(bg="ghost white")

        self.unbind_all("<MouseWheel>")

        home_button = tk.Button(self, width=10, text="Home", font="Calibri 14", relief="groove", borderwidth=3, bg="light gray", activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        domain1_button = tk.Button(self, text="Cyber Risk Management and Oversight", font='Calibri 14', relief="groove", borderwidth=3, bg='light gray', activebackground='light blue',
                                   command=lambda: master.switch_frame(d1.CSM_Domain1_Page))

        domain2_button = tk.Button(self, text="Threat Intelligence and Collaboration", font="Calibri 14", relief="groove", borderwidth=3, bg="light gray", activebackground='light blue',
                                   command=lambda: master.switch_frame(d2.CSM_Domain2_Page))

        domain3_button = tk.Button(self, text="Cybersecurity Controls", font="Calibri 14", relief="groove", borderwidth=3, bg="light gray", activebackground='light blue',
                                   command=lambda: master.switch_frame(d3.CSM_Domain3_Page))

        domain4_button = tk.Button(self, text="External Dependency Management", font="Calibri 14", relief="groove", borderwidth=3, bg="light gray", activebackground='light blue',
                                   command=lambda: master.switch_frame(d4.CSM_Domain4_Page))

        domain5_button = tk.Button(self, text="Cyber Incident Management and Resilience", font="Calibri 14", relief="groove", borderwidth=3, bg="light gray", activebackground='light blue', 
                                   command=lambda: master.switch_frame(d5.CSM_Domain5_Page))


        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)

        home_button.grid(row=0, column=0)
        domain1_button.grid(row=1, column=1, pady=10)
        domain2_button.grid(row=2, column=1, pady=10)
        domain3_button.grid(row=3, column=1, pady=10)
        domain4_button.grid(row=4, column=1, pady=10)
        domain5_button.grid(row=5, column=1, pady=10)
        
    #endregion

def clear_pressed(values):
    for i in range(len(values)):
        values[i].set(0)

def submit_pressed(values):
    y = y_c = n = total_selected = 0

    for i in range(len(values)):
        if (values[i].get() == 1):
            y += 1
            total_selected += 1
        elif (values[i].get() == 2):
            y_c += 1
            total_selected += 1
        elif (values[i].get() == 3):
            n += 1
            total_selected += 1

    return [y, y_c, n, total_selected]