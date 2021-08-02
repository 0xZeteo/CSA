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
        login_button = tk.Button(self, text="Login", command=lambda: verify_login(master))

        register_button.grid(row=2, column=0)
        login_button.grid(row=2, column=1)


class Register_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Register")

        user_label = tk.Label(self, text="Username")
        password_label = tk.Label(self, text="Password")

        user_label.grid(row=0, column=0)
        password_label.grid(row=1, column=0)

        user_entry = tk.Entry(self)
        password_entry = tk.Entry(self, show="*")

        user_entry.grid(row=0, column=1)
        password_entry.grid(row=1, column=1)

        register_button = tk.Button(self, text="Register", command=lambda: registration(master, user_entry.get(), password_entry.get()))
        register_button.grid(row=3, column=1)

    
def registration(frame, user_name, password):

        print(user_name, password)

        salt = bcrypt.gensalt(rounds=10)
        hashed = bcrypt.hashpw(password.encode('utf8'), salt)

        print("Salt: " + str(salt) + " Hashed: " + str(hashed))

        insert_query = """INSERT INTO users (username, password, salt) VALUES (%s, %s, %s);"""
        values = [user_name, hashed, salt]

        db_connection = db.create_db_connection("localhost", "root", "TemNewPass#158", "CSA")
        db.execute_query_data(db_connection, insert_query, values)

        frame.switch_frame(Login_Page)


def verify_login(frame):

    # check password against a hashed value
    #if bcrypt.checkpw(password, hashed):
        #print("match")
    #else:
        #print("Does not match")

    frame.switch_frame(home.Home_Page)

