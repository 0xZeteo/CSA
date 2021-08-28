import tkinter as tk
import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_login as login
import bcrypt
import db
from tkinter import messagebox

import matplotlib.pyplot as plt


""" This class handles the the layout of the Home page as in the first page after logging in """
class Home_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper())

        self.config(bg='ghost white')

        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")

        logout_button = tk.Button(self, width=10, text="LOGOUT", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: reset_and_logout(master))

        change_pass_button = tk.Button(self, width=15, text="Change Password", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(Change_Password_Page))

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
        self.rowconfigure(1, minsize=50)
        self.rowconfigure(3, minsize=50)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=50)
        self.columnconfigure(5, weight=1)

        irp_textbox.grid(row=2, column=2)
        csm_textbox.grid(row=4, column=2)

        irp_button.grid(row=2, column=3, padx=50)
        csm_button.grid(row=4, column=3, padx=50)

        logout_button.place(relx=0.25, rely=0.1, anchor='center')
        past_results_button.place(relx=0.40, rely=0.1, anchor='center')
        change_pass_button.place(relx=0.55, rely=0.1, anchor='center')
    #endregion


class Change_Password_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - Change Password')
        self.config(bg='ghost white')

        old_password_label = tk.Label(self, text="Current Password", font="Calibri 20", bg='ghost white')
        new_password_label = tk.Label(self, text="New Password", font="Calibri 20", bg='ghost white')
        confirm_new_password_label = tk.Label(self, text="Confirm New Password", font="Calibri 20", bg='ghost white')

        old_password_entry = tk.Entry(self, font="Calirbi 15", relief='groove', borderwidth=3, bg='SlateGray4', 
                                     fg='white', insertbackground='white', cursor='top_left_arrow', show="*")

        new_password_entry = tk.Entry(self, font="Calirbi 15", relief='groove', borderwidth=3, bg='SlateGray4', 
                                     fg='white', insertbackground='white', cursor='top_left_arrow', show="*")

        confirm_new_password_entry = tk.Entry(self, font="Calirbi 15", relief='groove', borderwidth=3, bg='SlateGray4', 
                                     fg='white', insertbackground='white', cursor='top_left_arrow', show="*")

        cancel_button = tk.Button(self, text="CANCEL", width=10, font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', 
                                   activebackground='light blue', command=lambda: master.switch_frame(Home_Page))

        confirm_button = tk.Button(self, text="CONFIRM", width=10, font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue', 
                                   command=lambda: Change_Password_Page.change_password(master, old_password_entry.get(), new_password_entry.get(), confirm_new_password_entry.get()))

        old_password_label.place(relx=0.35, rely=0.3, anchor='center')
        new_password_label.place(relx=0.35, rely=0.4, anchor='center')
        confirm_new_password_label.place(relx=0.35, rely=0.5, anchor='center')

        old_password_entry.place(relx=0.65, rely=0.3, anchor='center')
        new_password_entry.place(relx=0.65, rely=0.4, anchor='center')
        confirm_new_password_entry.place(relx=0.65, rely=0.5, anchor='center')

        cancel_button.place(relx=0.4, rely=0.7, anchor='center')
        confirm_button.place(relx=0.6, rely=0.7, anchor='center')

        ToolTip(widget=new_password_entry, text='Password must be at least 9 characters long, with 1+ uppercase, 1+ numeric and 1+ special characters ($,@,#,%)')
        ToolTip(widget=confirm_new_password_entry, text='Password must be at least 9 characters long, with 1+ uppercase, 1+ numeric and 1+ special characters ($,@,#,%)')

    
    def change_password(frame, old_pass, new_pass, confirm_new_pass):
        SpecialChar = ['$', '@', '#', '%']

        # Generate salt and a hash code from the user's entered password
        salt = bcrypt.gensalt(rounds=12)
        new_hash = bcrypt.hashpw(new_pass.encode('utf8'), salt)

        get_password_query = """ SELECT password FROM users WHERE username=%s; """
        change_password_query = """ UPDATE users SET password=%s, salt=%s WHERE username=%s; """
        u_value = [login.Login_Page.logged_in]
        new_values = [new_hash, salt, login.Login_Page.logged_in]

        db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
        old_hash = db.read_query_data(db_connection, get_password_query, u_value)
        db_connection.close()

        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your password ?')
        if confirm:
            if (old_pass == "") or (new_pass == "") or (confirm_new_pass == ""):
                messagebox.showwarning("Warning", "All fields must be filled")
            elif not bcrypt.checkpw(old_pass.encode('utf8'), old_hash[0][0].encode('utf8')): # check password against a hashed value
                messagebox.showwarning("Warning", "Wrong password")
            elif new_pass != confirm_new_pass:
                messagebox.showwarning("Warning", "Password mismatch")
            elif (len(new_pass) < 9 or not any(char.isdigit() for char in new_pass) or not any(char.isupper() for char in new_pass) or not any(char in SpecialChar for char in new_pass)):
                messagebox.showwarning("Warning", "Password must be 9 characters long with at least 1 numeric, 1 uppercase and 1 special character ($,@,#,%)")
            else:
                db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
                db.execute_query_data(db_connection, change_password_query, new_values)
                db_connection.close()
                frame.switch_frame(Home_Page)
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
    plt.title('Results of {}'.format(name[0][0])) ##### change frame title
    plt.show()


def reset_and_logout(frame):
    confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to logout ?')
    if confirm:
        csm.reset_csm()
        irp.reset_irp()
        frame.switch_frame(login.Login_Page)
