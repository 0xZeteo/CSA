import tkinter as tk
import db
import bcrypt
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

        user_label = tk.Label(self, text="Username")
        password_label = tk.Label(self, text="Password")
        first_name_label = tk.Label(self, text="First Name")
        last_name_label = tk.Label(self, text="Last Name")
        dob_label = tk.Label(self, text="Date of Birth")
        email_label = tk.Label(self, text="Email")
        company_label = tk.Label(self, text="Company")

        # TO DO - check exportselection option in entries

        user_entry = tk.Entry(self)
        password_entry = tk.Entry(self, show="*")

        ######################################################################
        # limit entry to characters only
        def only_numbers(char):
            return char.isalpha()

        validation = self.register(only_numbers)
        first_name_entry = tk.Entry(self, validate="key", validatecommand=(validation, '%S'))
        ######################################################################

        last_name_entry = tk.Entry(self)
        dob_entry = tk.Entry(self)
        email_entry = tk.Entry(self)
        company_entry = tk.Entry(self)

        user_label.grid(row=0, column=0)
        password_label.grid(row=1, column=0)
        first_name_label.grid(row=2, column=0)
        last_name_label.grid(row=3, column=0)
        dob_label.grid(row=4, column=0)
        email_label.grid(row=5, column=0)
        company_label.grid(row=6, column=0)

        user_entry.grid(row=0, column=1)
        password_entry.grid(row=1, column=1)
        first_name_entry.grid(row=2, column=1)
        last_name_entry.grid(row=3, column=1)
        dob_entry.grid(row=4, column=1)
        email_entry.grid(row=5, column=1)
        company_entry.grid(row=6, column=1)

        cancel_button = tk.Button(self, text="Cancel", command=lambda: master.switch_frame(Login_Page))
        cancel_button.grid(row=7, column=0, pady=50)

        register_button = tk.Button(self, text="Register", command=lambda: registration(master, user_entry.get(), password_entry.get()))
        register_button.grid(row=7, column=1, pady=50)
    #endregion

    
def registration(frame, user_name, password):

        print(user_name, password)

        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        insert_query = """ INSERT INTO users (username, password, salt) VALUES (%s, %s, %s); """
        values = [user_name, hashed, salt]

        db_connection = db.create_db_connection("localhost", "root", "TemNewPass#158", "CSA")
        db.execute_query_data(db_connection, insert_query, values)
        db_connection.close()

        frame.switch_frame(Login_Page)


def verify_login(frame, user_name, password):

    get_password_query = """ SELECT password FROM users WHERE username=%s; """
    values = [user_name]

    db_connection = db.create_db_connection("localhost", "root", "TemNewPass#158", "CSA")
    hash = db.read_query_data(db_connection, get_password_query, values)

    # check password against a hashed value
    if bcrypt.checkpw(password.encode('utf8'), hash[0][0].encode('utf8')):
        print("match")
        Login_Page.logged_in = user_name
        frame.switch_frame(home.Home_Page)
    else:
        print("Does not match")

    db_connection.close()

    