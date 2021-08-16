import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
import db
import bcrypt
import layout.layout_home as home


""" This class handles the layout of the Login page (Grid Layout) """
class Login_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Login")

        user_label = tk.Label(self, text="Username", font="Times 15")
        password_label = tk.Label(self, text="Password", font="Times 15")

        user_entry = tk.Entry(self, font="Times 11")
        password_entry = tk.Entry(self, show="*", font="Times 11")

        register_button = tk.Button(self, text="Register", width=10, font="Times 12", command=lambda: master.switch_frame(Register_Page))
        login_button = tk.Button(self, text="Login", width=10, font="Times 12", command=lambda: verify_login(master, user_entry.get(), password_entry.get()))

        # Configure the empty rows and columns on each corner to make them scalable when the window is resized
        # Keeps all the widgets in the middle of the screen

        self.columnconfigure(0, weight=1) # empty first column that scales
        self.columnconfigure(3, weight=1) # empty last column that scales

        self.rowconfigure(0, weight=1)    # empty first row that scales
        self.rowconfigure(4, weight=1)    # empty last row that scales

        user_label.grid         (row=1, column=1, padx=15, pady=20, sticky='E') 
        password_label.grid     (row=2, column=1, padx=15, pady=20, sticky='E')

        user_entry.grid         (row=1, column=2, padx=15, pady=20, sticky='W')
        password_entry.grid     (row=2, column=2, padx=15, pady=20, sticky='W')

        register_button.grid    (row=3, column=1, pady=30, sticky='E')
        login_button.grid       (row=3, column=2, padx=15, pady=30, sticky='E')

        # bind enter key to the verify_login function === Login button pressed
        self.bind_all('<Return>', lambda e: verify_login(master, user_entry.get(), password_entry.get()))
        
        user_entry.focus() # Set the focus to the username entry
    #endregion


""" This class handles the layout of the Registration page (Grid Layout) """
class Register_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Registration")

        # Bind enter key to the registration function === Submit button pressed
        self.bind_all('<Return>', lambda e: registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                        firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), 
                                        dob_entry.get_date()))

        # limit entry to characters only
        def only_characters(char):
            return char.isalpha()

        validation = self.register(only_characters) # register the function

        username_label = tk.Label(self, text="Username", font="Times 14")
        password_label = tk.Label(self, text="Password", font="Times 14")
        confirm_password_label = tk.Label(self, text="Confirm Password", font="Times 14")
        firstname_label = tk.Label(self, text="First Name", font="Times 14")
        lastname_label = tk.Label(self, text="Last Name", font="Times 14")
        email_label = tk.Label(self, text="Email", font="Times 14")
        company_label = tk.Label(self, text="Company", font="Times 14")
        dob_label = tk.Label(self, text="Date of Birth", font="Times 14")
        
        username_entry = tk.Entry(self, font="Times 11")
        password_entry = tk.Entry(self, show="*", font="Times 11")
        confirm_password_entry = tk.Entry(self, show="*", font="Times 11")
        firstname_entry = tk.Entry(self, width=25, font="Times 11", validate="key", validatecommand=(validation, '%S'))
        lastname_entry = tk.Entry(self, width=25, font="Times 11", validate="key", validatecommand=(validation, '%S'))
        email_entry = tk.Entry(self, width=25, font="Times 11")
        company_entry = tk.Entry(self, font="Times 11")
        dob_entry = DateEntry(self, font="Times 11", width=17, background='darkblue', foreground='white', borderwidth=2)

        cancel_button = tk.Button(self, width=10, text="Cancel", font="Times 12", command=lambda: master.switch_frame(Login_Page))

        register_button = tk.Button(self, width=10, text="Register", font="Times 12", command=lambda: 
                                    registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                        firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), 
                                        dob_entry.get_date()))

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
        self.columnconfigure(6, minsize=25)
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


""" This function handles the registration of the user when the Register button is pressed
    @Arg frame - represents the parent frame (master) to be switched
    @Args - the remaining arguments represent all the entries in the registration page that the user can fill """    
def registration(frame, user_name, password, confirm_password, first_name, last_name, email, company, dob):

        # Generate salt and a hash code from the user's entered password
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        # Insert into DB query
        insert_users_query = """ 
        INSERT INTO users (first_name, last_name, date_of_birth, email, company, username, password, salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); 
        """
        values = [first_name, last_name, dob, email, company, user_name, hashed, salt]

        # if there's an empty field
        if (user_name == "") or (password == "") or (confirm_password == "") or (first_name == "") or (last_name == "") or (email == "") or (company == ""):
            messagebox.showwarning("Warning", "All fields must be filled")
        # if passwords do not match
        elif (password != confirm_password):
            messagebox.showwarning("Warning", "Password mismatch")
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
    u_values = [user_name]
    p_values = [user_name]

    db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA") # open db connection
    user = db.read_query_data(db_connection, get_username_query, u_values)                 # get username from db
    hash = db.read_query_data(db_connection, get_password_query, p_values)                 # get hash from db
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

    