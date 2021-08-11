import tkinter as tk
import db
import bcrypt
from tkcalendar import DateEntry
from tkinter import messagebox
import layout.layout_home as home


class Login_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Welcome")

        user_label = tk.Label(self, text="Username", font="Courier 16 bold")
        password_label = tk.Label(self, text="Password", font="Courier 16 bold")

        user_entry = tk.Entry(self, font="Courier 10")
        password_entry = tk.Entry(self, show="*", font="Courier 10")

        register_button = tk.Button(self, text="Register", width=10, font="Courier 10 bold",
                                    command=lambda: master.switch_frame(Register_Page))

        login_button = tk.Button(self, text="Login", width=10, font="Courier 10 bold", 
                                 command=lambda: verify_login(master, user_entry.get(), password_entry.get()))

        #self.configure(bg='red')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        user_label.grid(row=1, column=1, padx=10, pady=10, sticky='E') 
        password_label.grid(row=2, column=1, padx=10, pady=10, sticky='E')

        user_entry.grid(row=1, column=2, padx=10, pady=10, sticky='W')
        password_entry.grid(row=2, column=2, padx=10, pady=10, sticky='W')

        register_button.grid(row=3, column=1, pady=20, sticky='E')
        login_button.grid(row=3, column=2, pady=20, sticky='N')

        self.bind_all('<Return>', lambda e: verify_login(master, user_entry.get(), password_entry.get()))
        
        user_entry.focus()
    #endregion


class Register_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Register")

        self.bind_all('<Return>', lambda e: registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                        firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), 
                                        dob_entry.get_date()))

        # limit entry to characters only
        def only_characters(char):
            return char.isalpha()

        validation = self.register(only_characters)

        # TO DO - check exportselection option in entries

        top_frame = tk.Frame(self)
        top_frame.grid(row=1, column=1)

        bottom_frame = tk.Frame(self)
        bottom_frame.grid(row=3, column=1)

        username_label = tk.Label(top_frame, text="Username")
        password_label = tk.Label(top_frame, text="Password")
        confirm_password_label = tk.Label(top_frame, text="Confirm Password")
        firstname_label = tk.Label(top_frame, text="First Name")
        lastname_label = tk.Label(top_frame, text="Last Name")
        email_label = tk.Label(top_frame, text="Email")
        company_label = tk.Label(top_frame, text="Company")
        dob_label = tk.Label(top_frame, text="Date of Birth")
        
        username_entry = tk.Entry(top_frame)
        password_entry = tk.Entry(top_frame, show="*")
        confirm_password_entry = tk.Entry(top_frame, show="*")
        firstname_entry = tk.Entry(top_frame, validate="key", validatecommand=(validation, '%S'))
        lastname_entry = tk.Entry(top_frame, validate="key", validatecommand=(validation, '%S'))
        email_entry = tk.Entry(top_frame)
        company_entry = tk.Entry(top_frame)
        dob_entry = DateEntry(top_frame, width=17, background='darkblue', foreground='white', borderwidth=2)

        cancel_button = tk.Button(bottom_frame, width=10, text="Cancel", command=lambda: master.switch_frame(Login_Page))
        register_button = tk.Button(bottom_frame, width=10, text="Register", command=lambda: 
                                    registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                        firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), 
                                        dob_entry.get_date()))

        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, minsize=30)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        bottom_frame.columnconfigure(0, minsize=400)

        username_label.grid(row=0, column=0, sticky="e")
        password_label.grid(row=1, column=0, sticky="e")
        confirm_password_label.grid(row=2, column=0, sticky="e")
        firstname_label.grid(row=0, column=2, sticky="e")
        lastname_label.grid(row=1, column=2, sticky="e")
        email_label.grid(row=2, column=2, sticky="e")
        company_label.grid(row=0, column=5, sticky="e")
        dob_label.grid(row=1, column=5, sticky="e")

        username_entry.grid(row=0, column=1, padx=10, pady=10)
        password_entry.grid(row=1, column=1, padx=10, pady=10)
        confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)
        firstname_entry.grid(row=0, column=4, padx=10, pady=10)
        lastname_entry.grid(row=1, column=4, padx=10, pady=10)
        email_entry.grid(row=2, column=4, padx=10, pady=10)
        company_entry.grid(row=0, column=6, padx=10, pady=10)
        dob_entry.grid(row=1, column=6, padx=10, pady=10)
        
        cancel_button.grid(row=0, column=1, padx=30)
        register_button.grid(row=0, column=2)
    #endregion

    
def registration(frame, user_name, password, confirm_password, first_name, last_name, email, company, dob):

        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        insert_users_query = """ 
        INSERT INTO users (first_name, last_name, date_of_birth, email, company, username, password, salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); 
        """
        values = [first_name, last_name, dob, email, company, user_name, hashed, salt]

        if (user_name == "") or (password == "") or (confirm_password == "") or (first_name == "") or (last_name == "") or (email == "") or (company == ""):
            messagebox.showwarning("Warning", "All fields must be filled")
        elif (password != confirm_password):
            messagebox.showwarning("Warning", "Password mismatch")
        else:
            db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
            db.execute_query_data(db_connection, insert_users_query, values)
            db_connection.close()
            frame.switch_frame(Login_Page)



def verify_login(frame, user_name, password):

    get_username_query = """ SELECT username FROM users WHERE username=%s"""
    get_password_query = """ SELECT password FROM users WHERE username=%s; """
    u_values = [user_name]
    p_values = [user_name]

    db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
    user = db.read_query_data(db_connection, get_username_query, u_values)
    hash = db.read_query_data(db_connection, get_password_query, p_values)
    db_connection.close()

    if (user_name == "") or (password == ""):
        messagebox.showwarning("Warning", "All fields must be filled")
    elif not user:
        messagebox.showwarning("Warning", "Username does not exist")
    # check password against a hashed value
    elif not bcrypt.checkpw(password.encode('utf8'), hash[0][0].encode('utf8')):
        messagebox.showwarning("Warning", "Wrong Password")
    else:
        print("Success")
        Login_Page.logged_in = user_name
        frame.switch_frame(home.Home_Page)

    