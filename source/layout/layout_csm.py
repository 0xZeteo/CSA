
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE CYBERSECURITY MATURITY """

import tkinter as tk
import DATA
import layout.layout_home as home

""" This class is responsible for the layout of the Cybersecurity Maturity's Main page
    Contains all the categories and links to each one """
class CSM_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #start_button = tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(home.Home_Page))
        #start_button.pack()

        domain1_label = tk.Label(self, text="Cyber Risk Management and Oversight")
        domain1_label.grid(row=0, column=0)
        factor1_button = tk.Button(self, text="Governance", command=lambda: master.switch_frame(CSM_Governance_Page))
        factor1_button.grid(row=1, column=0)
        factor2_button = tk.Button(self, text="Risk Management", command=lambda: master.switch_frame(CSM_Governance_Page))
        factor2_button.grid(row=2, column=0)
        factor3_button = tk.Button(self, text="Resources", command=lambda: master.switch_frame(CSM_Governance_Page))
        factor3_button.grid(row=3, column=0)
        factor4_button = tk.Button(self, text="Training and Culture", command=lambda: master.switch_frame(CSM_Governance_Page))
        factor4_button.grid(row=4, column=0)

        domain2_label = tk.Label(self, text="Threat Intelligence and Collaboration")
        domain2_label.grid(row=0, column=1)
        factor5_button = tk.Button(self, text="Threat Intelligence", command=lambda: master.switch_frame(CSM_Governance_Page))
        factor5_button.grid(row=1, column=1)
        factor6_button = tk.Button(self, text="Monitoring and Analyzing", command=lambda: master.switch_frame(CSM_Governance_Page))
        factor6_button.grid(row=2, column=1)
        factor7_button = tk.Button(self, text="Information Sharing", command=lambda: master.switch_frame(CSM_Governance_Page))
        factor7_button.grid(row=3, column=1)
    #endregion

class CSM_Governance_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Maturity - Domain 1")

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

    #endregion