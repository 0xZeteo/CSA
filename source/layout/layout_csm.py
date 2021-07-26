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

        home_button = tk.Button(self, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack()

        domain1_button = tk.Button(self, text="Cyber Risk Management and Oversight", command=lambda: master.switch_frame(d1.CSM_Domain1_Page))
        domain2_button = tk.Button(self, text="Threat Intelligence and Collaboration", command=lambda: master.switch_frame(d2.CSM_Domain2_Page))
        domain3_button = tk.Button(self, text="Cybersecurity Controls", command=lambda: master.switch_frame(d3.CSM_Domain3_Page))
        domain4_button = tk.Button(self, text="External Dependency Management", command=lambda: master.switch_frame(d4.CSM_Domain4_Page))
        domain5_button = tk.Button(self, text="Cyber Incident Management and Resilience", command=lambda: master.switch_frame(d5.CSM_Domain5_Page))

        domain1_button.pack()
        domain2_button.pack()
        domain3_button.pack()
        domain4_button.pack()
        domain5_button.pack()
        
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