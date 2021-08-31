"""" Here is everything related to the home page after logging in """

import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_login as login
import db

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import nametofont
import matplotlib.pyplot as plt
import bcrypt


""" This class handles the the layout of the Home page as in the first page after logging in """
class Home_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper())

        self.config(bg='ghost white')

        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")

        logout_button = tk.Button(self, width=15, text="Logout", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
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

        display_irp_button = tk.Button(self, width=15, text="Risk Results", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                           command=lambda: display_irp(master))

        display_csm_button = tk.Button(self, width=15, text="Maturity Results", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                           command=lambda: display_csm(master))

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, minsize=50)
        self.rowconfigure(3, minsize=50)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=100)
        self.columnconfigure(5, weight=1)

        irp_textbox.grid(row=2, column=2)
        csm_textbox.grid(row=4, column=2)

        irp_button.grid(row=2, column=3, padx=50)
        csm_button.grid(row=4, column=3, padx=50)

        logout_button.place(relx=0.1, rely=0.1, anchor='center')
        display_irp_button.place(relx=0.1, rely=0.3, anchor='center')
        display_csm_button.place(relx=0.1, rely=0.4, anchor='center')
        change_pass_button.place(relx=0.1, rely=0.2, anchor='center')

        # if admin is logged in
    #endregion


""" This class handles the layout of the change password page """
class Change_Password_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - Change Password')
        self.config(bg='ghost white')

        old_password_label = tk.Label(self, text="Current Password", font="Calibri 20", bg='ghost white')
        new_password_label = tk.Label(self, text="New Password", font="Calibri 20", bg='ghost white')
        confirm_new_password_label = tk.Label(self, text="Confirm Password", font="Calibri 20", bg='ghost white')

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

        # add tooltips to the new password and confirm password entry fields
        ToolTip(widget=new_password_entry, text='Password must be at least 9 characters long, with 1+ uppercase, 1+ numeric and 1+ special characters ($,@,#,%)')
        ToolTip(widget=confirm_new_password_entry, text='Password must be at least 9 characters long, with 1+ uppercase, 1+ numeric and 1+ special characters ($,@,#,%)')

    
    """ This function handles all the verifications and the changing of the password
        @arg frame - parent frame (master) to switch
        @arg old_pass - references the user's old password
        @arg new_pass - references the user's new password
        @arg confirm_new_pass - references the password confirmation """
    def change_password(frame, old_pass, new_pass, confirm_new_pass):
        SpecialChar = ['$', '@', '#', '%']

        # Generate salt and a hash code from the user's entered password
        salt = bcrypt.gensalt(rounds=12)
        new_hash = bcrypt.hashpw(new_pass.encode('utf8'), salt)

        get_password_query = """ SELECT password FROM users WHERE username=%s; """
        change_password_query = """ UPDATE users SET password=%s, salt=%s WHERE username=%s; """
        u_value = [login.Login_Page.logged_in]
        new_values = [new_hash, salt, login.Login_Page.logged_in]

        db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")
        old_hash = db.read_query_data(db_connection, get_password_query, u_value)
        db_connection.close()

        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your password ?')
        if confirm:
            # if empty fields
            if (old_pass == "") or (new_pass == "") or (confirm_new_pass == ""):
                messagebox.showwarning("Warning", "All fields must be filled")
            # if wrong old password entered
            elif not bcrypt.checkpw(old_pass.encode('utf8'), old_hash[0][0].encode('utf8')): # check password against a hashed value
                messagebox.showwarning("Warning", "Wrong password")
            # if new password does not match the confirm new password 
            elif new_pass != confirm_new_pass:
                messagebox.showwarning("Warning", "Password mismatch")
            # if new password does not conform to the required format 
            elif (len(new_pass) < 9 or not any(char.isdigit() for char in new_pass) or not any(char.isupper() for char in new_pass) or not any(char in SpecialChar for char in new_pass)):
                messagebox.showwarning("Warning", "Password must be 9 characters long with at least 1 numeric, 1 uppercase and 1 special character ($,@,#,%)")
            else:
                db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")
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



""" This class handles the layout of the IRP results page """
class Display_IRP(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        master.title(login.Login_Page.logged_in.upper() + ' - Inherent Risk Profile Results')
        self.config(bg='ghost white')

        # top frame
        top_frame = tk.Frame(self, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill='x')

        back_button = tk.Button(top_frame, text='BACK', width=10, font="Calibri 10", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(Home_Page))     

        graph_button = tk.Button(top_frame, text='Graph Display', width=12, relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: Display_IRP.graph(table.item(table.focus())))

        back_button.pack(side=tk.LEFT, padx=50, pady=10)
        graph_button.place(relx=0.5, rely=0.5, anchor='center')

        # bottom frame
        bottom_frame = tk.Frame(self, borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, expand='yes', fill='both')

        # columns of the display table
        cols = ('Date','Name','Least','Minimal','Moderate','Significant','Most','Risk Level')
        table = ttk.Treeview(bottom_frame, columns=cols, show='headings')

        scrollbar = ttk.Scrollbar(bottom_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        table.configure(yscrollcommand=scrollbar.set)

        cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

        get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
        username = [login.Login_Page.logged_in]
        uid = db.read_query_data(cnx, get_user_id_query, username)

        get_irp_query = """ SELECT date, name, least, minimal, moderate, significant, most, risk_level FROM irp WHERE user=%s ORDER BY date DESC; """
        get_irp_all_query = """ SELECT date, name, least, minimal, moderate, significant, most, risk_level FROM irp ORDER BY date DESC; """
        user = [uid[0][0]]

        if login.Login_Page.logged_in == 'admin':
            results = db.read_query(cnx, get_irp_all_query)
            delete_button = tk.Button(top_frame, text="Delete Row",  width=10, font="Calibri 10", relief='raised', borderwidth=2, bg='azure3', 
                                      activebackground='light blue', command=lambda: Display_IRP.delete(table.item(table.focus()), master))
            delete_button.pack(side='left')
        else:
            results = db.read_query_data(cnx, get_irp_query, user)

        cnx.close()

        # display table column names and width
        for col in cols:
            table.heading(col, text=col)
            table.column(col, width=50, anchor='center')

        # insert data rows into display table
        for result in results:
            vals = []
            for i in range(len(result)):
                vals.append(result[i])
            table.insert("", "end", values=tuple(vals))
        
        nametofont("TkHeadingFont").configure(weight='bold')    # headings font bold
        table.pack(side=tk.LEFT, expand='yes', fill='both')

    # this function handles the display of a single row from the table as a bar graph
    def graph(row):
        values = row.get('values')
        
        if not values:
            messagebox.showwarning('Warning', 'Select an assessment to visualize')
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            get_irp_query = """ SELECT least, minimal, moderate, significant, most FROM irp WHERE name=%s; """
            name_value = [values[1]]
            result = db.read_query_data(cnx, get_irp_query, name_value)
            cnx.close()

            # labels on the x-axis
            x_axis = ['Least', 'Minimal', 'Moderate', 'Significant', 'Most']

            plt.bar(x_axis, result[0])                          # create the bars
            plt.title('Assessment: {}'.format(values[1]))       # assessment name as the title for the graph
            plt.show()                                          # show graph

    # this function deletes a row from the irp table when given the name of the assessment in the row
    def delete(row, frame):
        values = row.get('values')

        if not values:
            messagebox.showwarning("Warning", "Select a row to delete")
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            delete_row_query = """ DELETE FROM irp WHERE name=%s; """
            name_value = [values[1]]
            if messagebox.askyesno("Confirmation", "Are you sure you want to delete this row ?"):
                db.execute_query_data(cnx, delete_row_query, name_value)
                frame.switch_frame(Display_IRP)
            cnx.close()
    #endregion


""" This class handles the layout of the CSM results page """
class Display_CSM(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        master.title(login.Login_Page.logged_in.upper() + ' - Cybersecurity Maturity Results')
        self.config(bg='ghost white')

        # top frame
        top_frame = tk.Frame(self, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill='x')

        back_button = tk.Button(top_frame, text='BACK', width=10, font="Calibri 10", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(Home_Page))

        graph_button = tk.Button(top_frame, text='Graph Display', width=12, relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: Display_CSM.graph(table.item(table.focus())))

        back_button.pack(side=tk.LEFT, padx=50, pady=10)
        graph_button.place(relx=0.5, rely=0.5, anchor='center')

        # bottom frame
        bottom_frame = tk.Frame(self, borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, expand='yes', fill='both')

        # columns of the display table
        cols = ('Date','Name',
        'B (Y)', 'E (Y)', 'Inter (Y)', 'A (Y)', 'Inno (Y)',
        'B (C)', 'E (C)', 'Inter (C)', 'A (C)', 'Inno (C)',
        'B (N)', 'E (N)', 'Inter (N)', 'A (N)', 'Inno (N)',
        'Maturity Level')

        table = ttk.Treeview(bottom_frame, columns=cols, show='headings')

        # scrollbar
        scrollbar = ttk.Scrollbar(bottom_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        table.configure(yscrollcommand=scrollbar.set)

        # Display table column names and width
        for col in cols:
            table.heading(col, text=col)
            if col == 'Date' or col == 'Name':
                table.column(col, width=70, anchor='center')
            elif col == 'Maturity Level':
                table.column(col, width=45, anchor='center')
            else:
                table.column(col, width=15, anchor='center')

        cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

        get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
        username = [login.Login_Page.logged_in]
        uid = db.read_query_data(cnx, get_user_id_query, username)
        
        get_csm_query = """ 
        SELECT date, name, 
        baseline_yes, evolving_yes, intermediate_yes, innovative_yes, advanced_yes, 
        baseline_compensating, evolving_compensating, intermediate_compensating, advanced_compensating, innovative_compensating,
        baseline_no, evolving_no, intermediate_no, advanced_no, innovative_no,
        maturity_level FROM csm WHERE user=%s ORDER BY date DESC; """

        get_csm_all_query = """ 
        SELECT date, name, 
        baseline_yes, evolving_yes, intermediate_yes, innovative_yes, advanced_yes, 
        baseline_compensating, evolving_compensating, intermediate_compensating, advanced_compensating, innovative_compensating,
        baseline_no, evolving_no, intermediate_no, advanced_no, innovative_no,
        maturity_level FROM csm ORDER BY date DESC; """

        user = [uid[0][0]]

        if uid[0][0] == 1:
            results = db.read_query(cnx, get_csm_all_query)
            delete_button = tk.Button(top_frame, text="Delete Row",  width=10, font="Calibri 10", relief='raised', borderwidth=2, bg='azure3', 
                                      activebackground='light blue', command=lambda: Display_CSM.delete(table.item(table.focus()), master))
            delete_button.pack(side='left')
        else:
            results = db.read_query_data(cnx, get_csm_query, user)

        cnx.close()

        # insert values into display table
        for result in results:
            vals = []
            for i in range(len(result)):
                vals.append(result[i])
            table.insert("", "end", values=tuple(vals))

        nametofont("TkHeadingFont").configure(weight='bold') # make headings bold
        table.pack(side=tk.LEFT, expand='yes', fill='both')

        # hint label that displays information about the symbols found on this page
        hint_label = tk.Label(top_frame, text='Hint', font="Calibri 10 underline", bg='ghost white', fg='blue')
        hint_label.place(relx=0.9, rely=0.5, anchor='center')
        hint_label.bind("<Button-1>", lambda e: top_level(self, hint_label))

    # this function handles the display of a single row from the table as a bar graph
    def graph(row):
        values = row.get('values')
        
        if not values:
            messagebox.showwarning('Warning', 'Select an assessment to visualize')
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            get_csm_query = """ SELECT 
            baseline_yes, evolving_yes, intermediate_yes, innovative_yes, advanced_yes, 
            baseline_compensating, evolving_compensating, intermediate_compensating, advanced_compensating, innovative_compensating,
            baseline_no, evolving_no, intermediate_no, advanced_no, innovative_no 
            FROM csm WHERE name=%s; """
            name_value = [values[1]]
            result = db.read_query_data(cnx, get_csm_query, name_value)
            cnx.close()

            # labels on the x-axis
            x_axis = ['B(Y)', 'E(Y)', 'I(Y)', 'A(Y)', 'I(Y)',
                      'B(C)', 'E(C)', 'I(C)', 'A(C)', 'I(C)',
                      'B(N)', 'E(N)', 'I(N)', 'A(N)', 'I(N)']

            plt.bar(x_axis, result[0])                      # create the bars
            plt.title('Assessment: {}'.format(values[1]))   # assessment name as the title of the graph
            plt.show()                                      # show graph

    # this function deletes a row from the csm table when given the name of the assessment in the row
    def delete(row, frame):
        values = row.get('values')

        if not values:
            messagebox.showwarning("Warning", "Select a row to delete")
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            delete_row_query = """ DELETE FROM csm WHERE name=%s; """
            name_value = [values[1]]
            if messagebox.askyesno("Confirmation", "Are you sure you want to delete this row ?"):
                db.execute_query_data(cnx, delete_row_query, name_value)
                frame.switch_frame(Display_CSM)
            cnx.close()
    #endregion


# this function handles the top level window when the hint label is pressed (displays information about the symbols)
def top_level(frame, widget):
    top = tk.Toplevel(frame, background = "#ffffe0", relief = 'solid')
    top.geometry("+{}+{}".format(widget.winfo_rootx()-300, widget.winfo_rooty()))
    top.wm_overrideredirect(1)

    info_label = tk.Label(top, background = "#ffffe0", font='Calibri 10', 
                          text='Symbols found in this page:\nB: Baseline, E: Evolving, I/Inter: Intermediate, A: Advanced, I/Inno: Innovative\n(Y): Yes, (C): Compensating, (N): No')
    
    info_label.pack()
    top.focus()

    top.bind('<Escape>', lambda e: hide())
    top.bind('<FocusOut>', lambda e: hide())

    def hide():
        top.destroy()


# this function handles the validation before displaying the IRP results
def display_irp(frame):
    cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

    get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
    username = [login.Login_Page.logged_in]
    uid = db.read_query_data(cnx, get_user_id_query, username)

    get_irp_query = """ SELECT iid FROM irp WHERE user=%s; """
    get_irp_all_query = """ SELECT iid FROM irp; """
    user = [uid[0][0]]

    if uid[0][0] == 1:
        results = db.read_query(cnx, get_irp_all_query)
    else:
        results = db.read_query_data(cnx, get_irp_query, user)

    cnx.close()

    if not results:
        messagebox.showwarning("Warning", "No assessments have been saved by this user")
    else:
        frame.switch_frame(Display_IRP)


# this function handles the validation before displaying the CSM results 
def display_csm(frame):
    cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

    get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
    username = [login.Login_Page.logged_in]
    uid = db.read_query_data(cnx, get_user_id_query, username)

    get_csm_query = """ SELECT cid FROM csm WHERE user=%s; """
    get_csm_all_query = """ SELECT cid FROM csm; """
    user = [uid[0][0]]

    if uid[0][0] == 1:
        results = db.read_query(cnx, get_csm_all_query)
    else:
        results = db.read_query_data(cnx, get_csm_query, user)

    cnx.close()

    if not results:
        messagebox.showwarning("Warning", "No assessments have been saved by this user")
    else:
        frame.switch_frame(Display_CSM)


# this function displays a confirmation box and then resets all the answers before logging out
def reset_and_logout(frame):
    confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to logout ? Unsaved results will be lost')
    if confirm:
        csm.reset_csm()
        irp.reset_irp()
        frame.switch_frame(login.Login_Page)
