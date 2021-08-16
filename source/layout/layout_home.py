import tkinter as tk
import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_login as login

#from tkinter import ttk
#from ttkthemes import ThemedStyle


""" This class handles the the layout of the Home page as in the first page after logging in """
class Home_Page(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #master.title("Logged in - " + login.Login_Page.logged_in)

        #style = ThemedStyle(self)
        #style.set_theme("plastik")

        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")

        logout_button = tk.Button(self, width=10, text="Logout", command=lambda: master.switch_frame(login.Login_Page))

        irp_text = "The Inherent Risk Profile identifies the institution’s inherent risk before implementing controls"
        csm_text = "The Cybersecurity Maturity includes domains, assessment factors, components, and individual declarative statements across five maturity levels to identify specific controls and practices that are in place"

        irp_textbox = tk.Text(self, height=5, width=60, wrap="word")
        csm_textbox = tk.Text(self, height=5, width=60, wrap="word")

        irp_textbox.insert(tk.END, irp_text)
        csm_textbox.insert(tk.END, csm_text)

        irp_textbox.config(state="disabled")
        csm_textbox.config(state="disabled")

        irp_button = tk.Button(self, width=12, text="Assess Risk", command=lambda: master.switch_frame(irp.IRP_Page))
        csm_button = tk.Button(self, width=12, text="Assess Maturity", command=lambda: master.switch_frame(csm.CSM_Page))

        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, minsize=50)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=50)
        self.columnconfigure(4, weight=1)

        logout_button.grid(row=0, column=0)

        irp_textbox.grid(row=1, column=2)
        csm_textbox.grid(row=3, column=2)

        irp_button.grid(row=1, column=3, padx=50)
        csm_button.grid(row=3, column=3, padx=50)