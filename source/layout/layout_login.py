import tkinter as tk
import db
import bcrypt
from tkcalendar import DateEntry
import layout.layout_home as home


class Login_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Welcome")

        user_label = tk.Label(self, text="Username")
        password_label = tk.Label(self, text="Password")

        user_label.grid(row=0, column=0)
        password_label.grid(row=1, column=0)

        user_entry = tk.Entry(self)
        password_entry = tk.Entry(self, show="*")

        user_entry.grid(row=0, column=1)
        password_entry.grid(row=1, column=1)

        register_button = tk.Button(self, text="Register", command=lambda: master.switch_frame(Register_Page))
        login_button = tk.Button(self, text="Login", command=lambda: verify_login(master, user_entry.get(), password_entry.get()))

        register_button.grid(row=2, column=0)
        login_button.grid(row=2, column=1)


class Register_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Register")

        # limit entry to characters only
        def only_characters(char):
            return char.isalpha()

        validation = self.register(only_characters)

        # TO DO - check exportselection option in entries

        username_label = tk.Label(self, text="Username")
        password_label = tk.Label(self, text="Password")
        confirm_password_label = tk.Label(self, text="Confirm Password")
        firstname_label = tk.Label(self, text="First Name")
        lastname_label = tk.Label(self, text="Last Name")
        email_label = tk.Label(self, text="Email")
        company_label = tk.Label(self, text="Company")
        dob_label = tk.Label(self, text="Date of Birth")
        
        username_entry = tk.Entry(self)
        password_entry = tk.Entry(self, show="*")
        confirm_password_entry = tk.Entry(self, show="*")
        firstname_entry = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))
        lastname_entry = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))
        email_entry = tk.Entry(self)
        company_entry = tk.Entry(self)
        dob_entry = DateEntry(self, background='darkblue', foreground='white', borderwidth=2)

        username_label.grid(row=0, column=0, pady=20)
        password_label.grid(row=1, column=0, pady=20)
        confirm_password_label.grid(row=2, column=0, pady=20)
        firstname_label.grid(row=0, column=2, pady=20)
        lastname_label.grid(row=1, column=2, pady=20)
        email_label.grid(row=2, column=2, pady=20)
        company_label.grid(row=0, column=4, pady=20)
        dob_label.grid(row=1, column=4, pady=20)

        username_entry.grid(row=0, column=1, pady=20)
        password_entry.grid(row=1, column=1, pady=20)
        confirm_password_entry.grid(row=2, column=1, pady=20)
        firstname_entry.grid(row=0, column=3, pady=20)
        lastname_entry.grid(row=1, column=3, pady=20)
        email_entry.grid(row=2, column=3, pady=20)
        company_entry.grid(row=0, column=5, pady=20)
        dob_entry.grid(row=1, column=5, pady=20)
        
        cancel_button = tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Login_Page))
        cancel_button.grid(row=5, column=4, pady=50)

        register_button = tk.Button(self, text="Register", command=lambda: registration(master, username_entry.get(), password_entry.get(), firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), dob_entry.get_date()))
        register_button.grid(row=5, column=5, pady=50)
    #endregion

    
def registration(frame, user_name, password, first_name, last_name, email, company, dob):

        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        insert_users_query = """ 
        INSERT INTO users (first_name, last_name, date_of_birth, email, company, username, password, salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); 
        """

        db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
        values = [first_name, last_name, dob, email, company, user_name, hashed, salt]
        db.execute_query_data(db_connection, insert_users_query, values)
        db_connection.close()

        frame.switch_frame(Login_Page)


def verify_login(frame, user_name, password):

    get_password_query = """ SELECT password FROM users WHERE username=%s; """
    values = [user_name]

    db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA")
    hash = db.read_query_data(db_connection, get_password_query, values)
    db_connection.close()

    # check password against a hashed value
    if bcrypt.checkpw(password.encode('utf8'), hash[0][0].encode('utf8')):
        print("Success")
        Login_Page.logged_in = user_name
        frame.switch_frame(home.Home_Page)
    else:
        print("Wrong Password")

    