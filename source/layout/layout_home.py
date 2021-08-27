import tkinter as tk
import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_login as login
import db

import matplotlib.pyplot as plt


""" This class handles the the layout of the Home page as in the first page after logging in """
class Home_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Logged in - " + login.Login_Page.logged_in)

        self.config(bg='ghost white')

        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")

        logout_button = tk.Button(self, width=10, text="LOGOUT", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: reset_and_logout(master))

        irp_text = "The Inherent Risk Profile identifies the institution’s inherent risk before implementing controls"
        csm_text = "The Cybersecurity Maturity includes domains, assessment factors, components, and individual declarative statements across five maturity levels to identify specific controls and practices that are in place"

        irp_textbox = tk.Text(self, height=5, width=60, wrap="word", font="Calibri 15", relief='groove', borderwidth=3, bg='ghost white')
        csm_textbox = tk.Text(self, height=5, width=60, wrap="word", font="Calibri 15", relief='groove', borderwidth=3, bg='ghost white')

        irp_textbox.insert(tk.END, irp_text)
        csm_textbox.insert(tk.END, csm_text)

        irp_textbox.config(state="disabled")
        csm_textbox.config(state="disabled")

        irp_button = tk.Button(self, width=13, text="Assess Risk", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                               command=lambda: master.switch_frame(irp.IRP_Page))

        csm_button = tk.Button(self, width=13, text="Assess Maturity", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                               command=lambda: master.switch_frame(csm.CSM_Page))

        past_results_button = tk.Button(self, width=13, text="Past Results", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                           command=lambda: display_graph())

        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, minsize=50)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=50)
        self.columnconfigure(5, weight=1)

        logout_button.grid(row=0, column=1)

        irp_textbox.grid(row=1, column=2)
        csm_textbox.grid(row=3, column=2)

        irp_button.grid(row=1, column=3, padx=50)
        csm_button.grid(row=3, column=3, padx=50)

        past_results_button.grid(row=4, column=2)
    #endregion


def display_graph():
    get_assessment_name = """ SELECT name FROM irp WHERE iid=8; """
    get_irp_test = """ SELECT least, minimal, moderate, significant, most FROM irp WHERE iid=8; """

    cnx = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
    name = db.read_query(cnx, get_assessment_name)
    result = db.read_query(cnx, get_irp_test)
    cnx.close()

    x_axis = ['Least', 'Minimal', 'Moderate', 'Significant', 'Most']
    plt.bar(x_axis, result[0])
    plt.ylim(0, 20)
    plt.xlabel("Risk Level")
    plt.ylabel("Score")
    plt.title('Results of {}'.format(name[0][0]))
    plt.show()


def reset_and_logout(frame):
    csm.reset_csm()
    irp.reset_irp()
    frame.switch_frame(login.Login_Page)
