import layout.layout_home as home

import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Toplevel, messagebox
import db
import bcrypt
import re
from PIL import Image, ImageTk
import webbrowser


""" This class handles the layout of the Login page (Grid Layout) """
class Login_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Login")

        self.config(bg='ghost white')

        user_label = tk.Label       (self, text="Username", font="Calibri 20", bg='ghost white')
        password_label = tk.Label   (self, text="Password", font="Calibri 20", bg='ghost white')

        user_entry = tk.Entry       (self, font="Calirbi 15", relief='groove', borderwidth=3, bg='SlateGray4', 
                                     fg='white', insertbackground='white', cursor='top_left_arrow')

        password_entry = tk.Entry   (self, font="Calirbi 15", relief='groove', borderwidth=3, bg='SlateGray4', 
                                     fg='white', insertbackground='white', cursor='top_left_arrow', show="*") 

        register_button = tk.Button (self, text="REGISTER", width=10, font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                     command=lambda: master.switch_frame(Register_Page))

        login_button = tk.Button    (self, text="LOGIN", width=10, font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                     command=lambda: verify_login(master, user_entry.get(), password_entry.get()))

        # Configure the empty rows and columns on each corner to make them scalable when the window is resized
        # Keeps all the widgets in the middle of the screen

        self.columnconfigure(0, weight=1) # empty first column that scales 
        self.columnconfigure(3, weight=1) # empty last column that scales 

        self.rowconfigure(0, weight=1)    # empty first row that scales
        self.rowconfigure(1, minsize=100)
        self.rowconfigure(5, weight=1)    # empty last row that scales

        user_label.grid         (row=2, column=1, padx=15, pady=20, sticky='nsew') 
        password_label.grid     (row=3, column=1, padx=15, pady=20, sticky='nsew')

        user_entry.grid         (row=2, column=2, padx=15, pady=20, sticky='w')
        password_entry.grid     (row=3, column=2, padx=15, pady=20, sticky='w')

        register_button.grid    (row=4, column=1, pady=30, sticky='e')
        login_button.grid       (row=4, column=2, padx=15, pady=30, sticky='n')

        # bind enter key to the verify_login function === Login button pressed
        self.bind_all('<Return>', lambda e: verify_login(master, user_entry.get(), password_entry.get()))
        
        user_entry.focus() # Set the focus to the username entry

        image = Image.open("resources/imt.png")
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo_image)
        image_label.image = photo_image
        image_label.place(relx=0.5, rely=0.2, anchor='center')

        about_label = tk.Label(self, text='About', font="Calibri 15 underline", bg='ghost white', fg='blue')
        about_label.place(relx=0.5, rely=0.9, anchor='center')
        about_label.bind("<Button-1>", lambda e: top_level(self, about_label))
    #endregion


""" This class handles the layout of the Registration page (Grid Layout) """
class Register_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Register")

        self.config(bg='ghost white')

        # Bind enter key to the registration function === Submit button pressed
        self.bind_all('<Return>', lambda e: registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                        firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), dob_entry.get_date()))

        # limit entry to alphabetical characters only
        def only_alpha(char):
            return char.isalpha()

        # limit entry to alphanumeric characters only
        def only_alphanumeric(char):
            return char.isalnum()

        alpha_validation = self.register(only_alpha)
        alpha_num_validation = self.register(only_alphanumeric)

        username_label = tk.Label           (self, text="Username", font="Calibri 12", bg='ghost white')
        password_label = tk.Label           (self, text="Password", font="Calibri 12", bg='ghost white')
        confirm_password_label = tk.Label   (self, text="Confirm Password", font="Calibri 12", bg='ghost white')
        firstname_label = tk.Label          (self, text="First Name", font="Calibri 12", bg='ghost white')
        lastname_label = tk.Label           (self, text="Last Name", font="Calibri 12", bg='ghost white')
        email_label = tk.Label              (self, text="Email", font="Calibri 12", bg='ghost white')
        company_label = tk.Label            (self, text="Company", font="Calibri 12", bg='ghost white')
        dob_label = tk.Label                (self, text="Date of Birth", font="Calibri 12", bg='ghost white')
        
        username_entry = tk.Entry           (self, font="Calirbi 11 bold", relief='groove', borderwidth=3, bg='SlateGray4',
                                             fg='white', insertbackground='white', cursor='top_left_arrow', validate="key", validatecommand=(alpha_num_validation, '%S'))

        password_entry = tk.Entry           (self, font="Calirbi 11 bold", relief='groove', borderwidth=3, bg='SlateGray4',
                                             fg='white', insertbackground='white', cursor='top_left_arrow', show='*')

        confirm_password_entry = tk.Entry   (self, font="Calirbi 11 bold", relief='groove', borderwidth=3, bg='SlateGray4',
                                             fg='white', insertbackground='white', cursor='top_left_arrow', show='*')

        firstname_entry = tk.Entry          (self, width=25, font="Calirbi 11 bold", relief='groove', borderwidth=3, bg='SlateGray4',
                                             fg='white', insertbackground='white', cursor='top_left_arrow', validate="key", validatecommand=(alpha_validation, '%S'))

        lastname_entry = tk.Entry           (self, width=25, font="Calirbi 11 bold", relief='groove', borderwidth=3, bg='SlateGray4',
                                             fg='white', insertbackground='white', cursor='top_left_arrow', validate="key", validatecommand=(alpha_validation, '%S'))

        email_entry = tk.Entry              (self, width=25, font="Calirbi 11 bold", relief='groove', borderwidth=3, bg='SlateGray4',
                                             fg='white', insertbackground='white', cursor='top_left_arrow')

        company_entry = tk.Entry            (self, font="Calirbi 11 bold", relief='groove', borderwidth=3, bg='SlateGray4',
                                             fg='white', insertbackground='white', cursor='top_left_arrow')

        dob_entry = DateEntry               (self, width=17, font="Calirbi 11", relief='groove', borderwidth=3, bg='SlateGray4')

        cancel_button = tk.Button(self, width=10, text="CANCEL", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue', 
                                  command=lambda: master.switch_frame(Login_Page))

        register_button = tk.Button(self, width=10, text="REGISTER", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue', 
                                    command=lambda: registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                        firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), dob_entry.get_date()))

        ToolTip(widget=password_entry, text="Password must be at least 9 characters long, with 1+ uppercase, 1+ numeric and 1+ special characters ($,@,#,%)")

        # Configure empty rows and columns in every corner as well as in the middle making the windgets scalable when the window is resized
        # Keeps all the widgets relatively centered 

        # rows
        self.rowconfigure(0, weight=2)
        self.rowconfigure(4, minsize=25)
        self.rowconfigure(6, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        # columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, minsize=25)
        self.columnconfigure(6, minsize=15)
        self.columnconfigure(9, weight=1)

        username_label.grid             (row=1, column=1, padx=10, pady=20)
        password_label.grid             (row=2, column=1, padx=10, pady=20)
        confirm_password_label.grid     (row=3, column=1, padx=10, pady=20)
        firstname_label.grid            (row=1, column=4, padx=10, pady=20)
        lastname_label.grid             (row=2, column=4, padx=10, pady=20)
        email_label.grid                (row=3, column=4, padx=10, pady=20)
        company_label.grid              (row=1, column=7, padx=10, pady=20)
        dob_label.grid                  (row=2, column=7, padx=10, pady=20)

        username_entry.grid             (row=1, column=2, padx=10, pady=20)
        password_entry.grid             (row=2, column=2, padx=10, pady=20)
        confirm_password_entry.grid     (row=3, column=2, padx=10, pady=20)
        firstname_entry.grid            (row=1, column=5, padx=10, pady=20)
        lastname_entry.grid             (row=2, column=5, padx=10, pady=20)
        email_entry.grid                (row=3, column=5, padx=10, pady=20)
        company_entry.grid              (row=1, column=8, padx=10, pady=20)
        dob_entry.grid                  (row=2, column=8, padx=10, pady=20)
        
        cancel_button.grid              (row=5, column=7)
        register_button.grid            (row=5, column=8)
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


def top_level(frame, widget):
    top = tk.Toplevel(frame, background = "#ffffe0", relief = 'solid')
    top.geometry("+{}+{}".format(widget.winfo_rootx()-250, widget.winfo_rooty()-50))
    top.wm_overrideredirect(1)

    info_label = tk.Label(top, background = "#ffffe0", font='Calibri 10', text='This project is powered by python.\nIt was made for the university of IMT Mines Ales and is completely open-source at their request.\nFeel free to contribute to the project via its github repository below.\nIf you have any concerns, requests or recommendations, you can reach me at miles.muollas@gmail.com')
    git_label = tk.Label(top, background = "#ffffe0", fg='blue', font='Calibri 10 underline', text='https://github.com/Dynamic-Void/Cybersecurity-Assessment-Tool')
    
    git_label.bind('<Button-1>', lambda e: open_url('https://github.com/Dynamic-Void/Cybersecurity-Assessment-Tool'))

    info_label.pack()
    git_label.pack()
    top.focus()

    top.bind('<Escape>', lambda e: hide())
    top.bind('<FocusOut>', lambda e: hide())

    def hide():
        top.destroy()


""" This function handles the registration of the user when the Register button is pressed
    @Arg frame - represents the parent frame (master) to be switched
    @Args - the remaining arguments represent all the entries in the registration page that the user can fill """    
def registration(frame, user_name, password, confirm_password, first_name, last_name, email, company, dob):

    SpecialChar = ['$', '@', '#', '%']
    user_name = user_name.lower()
    email = email.lower()

    # Generate salt and a hash code from the user's entered password
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf8'), salt)

    # Get username query
    get_username_query = """ SELECT username FROM users WHERE username=%s; """
    u_value = [user_name]
    db_con = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
    username = db.read_query_data(db_con, get_username_query, u_value)
    db_con.close()

    # Insert into DB query
    insert_users_query = """ 
    INSERT INTO users (first_name, last_name, date_of_birth, email, company, username, password, salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); 
    """
    values = [first_name, last_name, dob, email, company, user_name, hashed, salt]

    # if there's an empty field
    if (user_name == "") or (password == "") or (confirm_password == "") or (first_name == "") or (last_name == "") or (email == "") or (company == ""):
        messagebox.showwarning("Warning", "All fields must be filled")
    # Check if username exists
    elif username:
        messagebox.showwarning("Warning", "Username already exists")
    # if passwords do not match
    elif (password != confirm_password):
        messagebox.showwarning("Warning", "Password mismatch")
    elif (len(password) < 9 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char in SpecialChar for char in password)):
        messagebox.showwarning("Warning", "Password must be 9 characters long with at least 1 numeric, 1 uppercase and 1 special character ($,@,#,%)")
    # check if email is valid
    elif (not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)):
        messagebox.showwarning("Warning", "Invalid email")
    else:
        db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA") # open db connection
        db.execute_query_data(db_connection, insert_users_query, values)                       # insert values into db
        db_connection.close()                                                                  # close connection
        frame.switch_frame(Login_Page)                                                         # switch frame to Login page


""" This function handles the verification of the username and password when the user presses Login
    @Arg frame - represents the parent frame (master) to be switched 
    @Args - username and password """
def verify_login(frame, user_name, password):

    # get from db queries
    get_username_query = """ SELECT username FROM users WHERE username=%s; """
    get_password_query = """ SELECT password FROM users WHERE username=%s; """
    u_value = [user_name]

    db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA") # open db connection
    user = db.read_query_data(db_connection, get_username_query, u_value)                  # get username from db
    hash = db.read_query_data(db_connection, get_password_query, u_value)                  # get hash from db
    db_connection.close()                                                                  # close connection

    # if there's an empty field
    if (user_name == "") or (password == ""):
        messagebox.showwarning("Warning", "All fields must be filled")
    # if username does not exist in the db
    elif not user:
        messagebox.showwarning("Warning", "Username does not exist")
    # if password is wrong
    elif not bcrypt.checkpw(password.encode('utf8'), hash[0][0].encode('utf8')): # check password against a hashed value
        messagebox.showwarning("Warning", "Wrong Password")
    else:
        Login_Page.logged_in = user_name     # This variable holds the name of the logged in username
        frame.switch_frame(home.Home_Page)   # switch frame to Home page
 

def open_url(url):
    webbrowser.open_new(url)