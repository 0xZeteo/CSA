import layout.layout_home as home
import db

import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import webbrowser
import bcrypt
import re
import os
import threading
import time
import datetime

# Color scheme
COLORS = {
    "primary": "#950000",     # Red
    "primary_light": "#c13030", # Lighter red for hover effects
    "secondary": "#010100",   # Blackish
    "bg": "#f0f2f5",          # Light background
    "text": "#333333",        # Dark text
    "entry_bg": "#e0e0e0",    # Light gray entry fields
    "light_text": "#888888"   # Light gray text
}

""" Login Page """
class Login_Page(tk.Frame):
    logged_in = None  # Class variable to store logged in username
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(bg=COLORS["bg"])
        
        # Main container
        container = tk.Frame(self, bg=COLORS["bg"])
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Card with shadow effect
        card_shadow = tk.Frame(container, bg="#dddddd")
        card_shadow.pack(padx=1, pady=1)
        
        card = tk.Frame(card_shadow, bg="white", padx=40, pady=40)
        card.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Logo
        try:
            image_path = "resources/logo.png"
            if not os.path.exists(image_path):
                image_path = r"C:\Users\prist\cybersecurity-assessment-tool - Copy\resources\logo.png"
            
            image = Image.open(image_path)
            image = image.resize((150, 120), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            logo = tk.Label(card, image=photo, bg="white")
            logo.image = photo
            logo.pack(pady=(0, 10))
        except Exception as e:
            print(f"Could not load image: {e}")
            # Fallback if image can't be loaded
            logo_text = tk.Label(card, text="CYBERSECURITY\nASSESSMENT TOOL", 
                                font=("Arial", 16, "bold"), bg="white", fg=COLORS["primary"])
            logo_text.pack(pady=(0, 20))
        
        # Username field
        username_frame = tk.Frame(card, bg="white")
        username_frame.pack(fill="x", pady=10)
        
        username_label = tk.Label(
            username_frame, text="USERNAME", font=("Arial", 10, "bold"), 
            bg="white", fg=COLORS["light_text"], anchor="w"
        )
        username_label.pack(fill="x")
        
        username_entry_frame = tk.Frame(username_frame, bg=COLORS["entry_bg"], bd=0, 
                                      highlightthickness=1, highlightbackground=COLORS["entry_bg"])
        username_entry_frame.pack(fill="x", pady=(5, 0))
        
        username_icon = tk.Label(
            username_entry_frame, text="👤", font=("Segoe UI Emoji", 12),
            bg=COLORS["entry_bg"], fg=COLORS["light_text"], padx=10
        )
        username_icon.pack(side="left")
        
        self.username_entry = tk.Entry(
            username_entry_frame,
            font=("Arial", 12),
            relief='flat',
            bd=0,
            bg=COLORS["entry_bg"],
            fg=COLORS["text"],
            insertbackground=COLORS["text"]
        )
        self.username_entry.pack(fill="x", ipady=10, padx=(0, 10), side="left", expand=True)
        
        # Password field with show/hide toggle
        password_frame = tk.Frame(card, bg="white")
        password_frame.pack(fill="x", pady=10)
        
        password_label = tk.Label(
            password_frame, text="PASSWORD", font=("Arial", 10, "bold"), 
            bg="white", fg=COLORS["light_text"], anchor="w"
        )
        password_label.pack(fill="x")
        
        password_entry_frame = tk.Frame(password_frame, bg=COLORS["entry_bg"], bd=0, 
                                      highlightthickness=1, highlightbackground=COLORS["entry_bg"])
        password_entry_frame.pack(fill="x", pady=(5, 0))
        
        password_icon = tk.Label(
            password_entry_frame, text="🔒", font=("Segoe UI Emoji", 12),
            bg=COLORS["entry_bg"], fg=COLORS["light_text"], padx=10
        )
        password_icon.pack(side="left")
        
        self.password_entry = tk.Entry(
            password_entry_frame,
            font=("Arial", 12),
            relief='flat',
            bd=0,
            bg=COLORS["entry_bg"],
            fg=COLORS["text"],
            insertbackground=COLORS["text"],
            show="•"  # Default to hidden password
        )
        self.password_entry.pack(fill="x", ipady=10, padx=(0, 10), side="left", expand=True)
        
        # Password visibility toggle button
        self.password_visible = False
        
        toggle_btn = tk.Button(
            password_entry_frame,
            text="👁️",  # Eye icon
            font=("Segoe UI Emoji", 12),
            bg=COLORS["entry_bg"],
            fg=COLORS["text"],
            activebackground=COLORS["entry_bg"],
            activeforeground=COLORS["primary"],
            relief="flat",
            bd=0,
            padx=5,
            cursor="hand2",
            command=self.toggle_password_visibility
        )
        toggle_btn.pack(side="right", padx=5)
        
        # Add hover effect
        def on_enter(e):
            toggle_btn['fg'] = COLORS["primary"]
        
        def on_leave(e):
            toggle_btn['fg'] = COLORS["text"]
        
        toggle_btn.bind("<Enter>", on_enter)
        toggle_btn.bind("<Leave>", on_leave)
        
        # Buttons
        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(fill="x", pady=(25, 10))
        
        # Register button
        register_btn = tk.Button(
            btn_frame, text="REGISTER", font=("Arial", 12), 
            bg=COLORS["bg"], fg=COLORS["text"],
            activebackground=COLORS["secondary"], activeforeground="white",
            relief="flat", bd=0, padx=20, pady=10, cursor="hand2",
            command=lambda: master.switch_frame(Register_Page)
        )
        register_btn.pack(side="left", padx=5)
        
        # Login button
        login_btn = tk.Button(
            btn_frame, text="LOGIN", font=("Arial", 12, "bold"),
            bg=COLORS["primary"], fg="white",
            activebackground=COLORS["secondary"], activeforeground="white",
            relief="flat", bd=0, padx=20, pady=10, cursor="hand2",
            command=lambda: self.verify_login(master)
        )
        login_btn.pack(side="right", padx=5)
        
        # Bind enter key to login
        self.bind_all('<Return>', lambda e: self.verify_login(master))
        
        # Set focus to username
        self.username_entry.focus()
    
    def toggle_password_visibility(self):
        # Toggle password visibility
        self.password_visible = not self.password_visible
        
        if self.password_visible:
            self.password_entry.config(show="")  # Show plain text
        else:
            self.password_entry.config(show="•")  # Show bullets
    
    def verify_login(self, frame):
        user_name = self.username_entry.get()
        password = self.password_entry.get()
        
        if not user_name or not password:
            messagebox.showwarning("Warning", "Username and password are required")
            return
        
        preloader = Preloader(frame)
        
        def perform_login():
            try:
                # Database queries
                get_username_query = """ SELECT username FROM users WHERE username=%s; """
                get_password_query = """ SELECT password FROM users WHERE username=%s; """
                
                db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")
                user = db.read_query_data(db_connection, get_username_query, [user_name])
                
                if not user:
                    frame.after(0, lambda: complete_login(False, "Username does not exist"))
                    db_connection.close()
                    return
                
                hash_value = db.read_query_data(db_connection, get_password_query, [user_name])
                db_connection.close()
                
                # Verify password
                if bcrypt.checkpw(password.encode('utf8'), hash_value[0][0].encode('utf8')):
                    frame.after(0, lambda: complete_login(True, user_name))
                else:
                    frame.after(0, lambda: complete_login(False, "Incorrect password"))
                
            except Exception as e:
                frame.after(0, lambda: complete_login(False, f"Login error: {str(e)}"))
        
        def complete_login(success, message):
            preloader.destroy()
            
            if success:
                Login_Page.logged_in = message  # Store username
                frame.switch_frame(home.Home_Page)
            else:
                messagebox.showwarning("Login Failed", message)
        
        # Start login process in background thread
        threading.Thread(target=perform_login, daemon=True).start()

""" Registration Page """
class Register_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(bg=COLORS["bg"])
        
        # Main container
        container = tk.Frame(self, bg=COLORS["bg"])
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Card with shadow
        card_shadow = tk.Frame(container, bg="#dddddd")
        card_shadow.pack(padx=1, pady=1)
        
        card = tk.Frame(card_shadow, bg="white", padx=40, pady=30)
        card.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Logo
        try:
            image_path = "resources/logo.png"
            if not os.path.exists(image_path):
                image_path = r"C:\Users\prist\cybersecurity-assessment-tool - Copy\resources\logo.png"
            
            image = Image.open(image_path)
            image = image.resize((120, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            logo = tk.Label(card, image=photo, bg="white")
            logo.image = photo
            logo.pack(pady=(0, 5))
        except Exception as e:
            print(f"Could not load image: {e}")
            # Fallback if image can't be loaded
            logo_text = tk.Label(card, text="CYBERSECURITY\nASSESSMENT TOOL", 
                                font=("Arial", 14, "bold"), bg="white", fg=COLORS["primary"])
            logo_text.pack(pady=(0, 10))
        
        # Title
        title = tk.Label(
            card, text="CREATE ACCOUNT", font=("Arial", 18, "bold"),
            bg="white", fg=COLORS["primary"]
        )
        title.pack(pady=(0, 20))
        
        # Create a two-column layout for form fields
        form_frame = tk.Frame(card, bg="white")
        form_frame.pack(fill="both", expand=True, pady=10)
        
        # Left column
        left_column = tk.Frame(form_frame, bg="white")
        left_column.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Right column
        right_column = tk.Frame(form_frame, bg="white")
        right_column.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        # Account Information Section
        account_section = tk.Frame(left_column, bg="white")
        account_section.pack(fill="x", pady=5)
        
        section_label = tk.Label(
            account_section, text="ACCOUNT INFORMATION", font=("Arial", 10, "bold"),
            bg="white", fg=COLORS["primary"], anchor="w"
        )
        section_label.pack(fill="x", pady=(0, 5))
        
        # Username field
        self.username_entry = self.create_input_field(account_section, "Username", "👤")
        
        # Password fields with show/hide toggle
        self.password_entry = self.create_password_field(account_section, "Password", "🔒")
        self.confirm_password_entry = self.create_password_field(account_section, "Confirm Password", "🔒")
        
        # Password requirements
        password_info = tk.Label(
            account_section,
            text="Password must be at least 9 characters with 1+ uppercase, 1+ number, and 1+ special character ($,@,#,%)",
            font=("Arial", 9), bg="white", fg=COLORS["light_text"], wraplength=300, justify="left"
        )
        password_info.pack(fill="x", pady=(0, 10))
        
        # Personal Information Section
        personal_section = tk.Frame(right_column, bg="white")
        personal_section.pack(fill="x", pady=5)
        
        section_label = tk.Label(
            personal_section, text="PERSONAL & COMPANY INFORMATION", font=("Arial", 10, "bold"),
            bg="white", fg=COLORS["primary"], anchor="w"
        )
        section_label.pack(fill="x", pady=(0, 5))
        
        # First name and last name
        self.firstname_entry = self.create_input_field(personal_section, "First Name", "👤")
        self.lastname_entry = self.create_input_field(personal_section, "Last Name", "👤")
        
        # Email field
        self.email_entry = self.create_input_field(personal_section, "Email Address", "✉️")
        
        # Company field
        self.company_entry = self.create_input_field(personal_section, "Company Name", "🏢")
        
        # Company info
        company_info = tk.Label(
            personal_section,
            text="This information will be used to customize your assessment based on your organization's profile.",
            font=("Arial", 9), bg="white", fg=COLORS["light_text"], wraplength=300, justify="left"
        )
        company_info.pack(fill="x", pady=(0, 10))
        
        # Divider
        divider = tk.Frame(card, height=1, bg="#e0e0e0")
        divider.pack(fill="x", pady=15)
        
        # Buttons
        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(fill="x", pady=10)
        
        # Cancel button
        cancel_btn = tk.Button(
            btn_frame, text="CANCEL", font=("Arial", 12),
            bg=COLORS["bg"], fg=COLORS["text"],
            activebackground=COLORS["secondary"], activeforeground="white",
            relief="flat", bd=0, padx=20, pady=10, cursor="hand2",
            command=lambda: master.switch_frame(Login_Page)
        )
        cancel_btn.pack(side="left", padx=5)
        
        # Register button
        register_btn = tk.Button(
            btn_frame, text="CREATE ACCOUNT", font=("Arial", 12, "bold"),
            bg=COLORS["primary"], fg="white",
            activebackground=COLORS["secondary"], activeforeground="white",
            relief="flat", bd=0, padx=20, pady=10, cursor="hand2",
            command=lambda: self.register_user(master)
        )
        register_btn.pack(side="right", padx=5)
        
        # Bind enter key
        self.bind_all('<Return>', lambda e: self.register_user(master))
    
    def create_input_field(self, parent, label_text, icon):
        frame = tk.Frame(parent, bg="white")
        frame.pack(fill="x", pady=8)
        
        label = tk.Label(
            frame, text=label_text, font=("Arial", 10, "bold"),
            bg="white", fg=COLORS["light_text"], anchor="w"
        )
        label.pack(fill="x")
        
        entry_frame = tk.Frame(frame, bg=COLORS["entry_bg"], bd=0,
                              highlightthickness=1, highlightbackground=COLORS["entry_bg"])
        entry_frame.pack(fill="x", pady=(3, 0))
        
        icon_label = tk.Label(
            entry_frame, text=icon, font=("Segoe UI Emoji", 12),
            bg=COLORS["entry_bg"], fg=COLORS["light_text"], padx=10
        )
        icon_label.pack(side="left")
        
        entry = tk.Entry(
            entry_frame,
            font=("Arial", 12),
            relief='flat',
            bd=0,
            bg=COLORS["entry_bg"],
            fg=COLORS["text"],
            insertbackground=COLORS["text"]
        )
        entry.pack(fill="x", ipady=8, padx=(0, 10), side="left", expand=True)
        
        return entry
    
    def create_password_field(self, parent, label_text, icon):
        frame = tk.Frame(parent, bg="white")
        frame.pack(fill="x", pady=8)
        
        label = tk.Label(
            frame, text=label_text, font=("Arial", 10, "bold"),
            bg="white", fg=COLORS["light_text"], anchor="w"
        )
        label.pack(fill="x")
        
        entry_frame = tk.Frame(frame, bg=COLORS["entry_bg"], bd=0,
                              highlightthickness=1, highlightbackground=COLORS["entry_bg"])
        entry_frame.pack(fill="x", pady=(3, 0))
        
        icon_label = tk.Label(
            entry_frame, text=icon, font=("Segoe UI Emoji", 12),
            bg=COLORS["entry_bg"], fg=COLORS["light_text"], padx=10
        )
        icon_label.pack(side="left")
        
        # Create password entry with bullet mask by default
        entry = tk.Entry(
            entry_frame,
            font=("Arial", 12),
            relief='flat',
            bd=0,
            bg=COLORS["entry_bg"],
            fg=COLORS["text"],
            insertbackground=COLORS["text"],
            show="•"  # Default to hidden password
        )
        entry.pack(fill="x", ipady=8, padx=(0, 10), side="left", expand=True)
        
        # Password visibility toggle button
        toggle_btn = tk.Button(
            entry_frame,
            text="👁️",  # Eye icon
            font=("Segoe UI Emoji", 12),
            bg=COLORS["entry_bg"],
            fg=COLORS["text"],
            activebackground=COLORS["entry_bg"],
            activeforeground=COLORS["primary"],
            relief="flat",
            bd=0,
            padx=5,
            cursor="hand2",
            command=lambda: self.toggle_password_visibility(entry)
        )
        toggle_btn.pack(side="right", padx=5)
        
        # Add hover effect
        def on_enter(e):
            toggle_btn['fg'] = COLORS["primary"]
        
        def on_leave(e):
            toggle_btn['fg'] = COLORS["text"]
        
        toggle_btn.bind("<Enter>", on_enter)
        toggle_btn.bind("<Leave>", on_leave)
        
        return entry
    
    def toggle_password_visibility(self, entry):
        # Toggle password visibility
        current_show = entry.cget('show')
        
        if current_show == '•':
            entry.config(show="")  # Show plain text
        else:
            entry.config(show="•")  # Show bullets
    
    def register_user(self, frame):
        # Get all field values
        user_name = self.username_entry.get().strip().lower()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        first_name = self.firstname_entry.get().strip()
        last_name = self.lastname_entry.get().strip()
        email = self.email_entry.get().strip().lower()
        company = self.company_entry.get().strip()
        
        # Validation
        if not all([user_name, password, confirm_password, first_name, last_name, email, company]):
            messagebox.showwarning("Warning", "All fields must be filled")
            return
        
        if password != confirm_password:
            messagebox.showwarning("Warning", "Password mismatch")
            return
        
        # Password requirements
        special_chars = ['$', '@', '#', '%']
        if (len(password) < 9 or 
            not any(char.isdigit() for char in password) or 
            not any(char.isupper() for char in password) or 
            not any(char in special_chars for char in password)):
            messagebox.showwarning("Warning", "Password must be 9 characters long with at least 1 numeric, 1 uppercase and 1 special character ($,@,#,%)")
            return
        
        # Email validation
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            messagebox.showwarning("Warning", "Invalid email format")
            return
        
        # Show preloader
        preloader = Preloader(frame)
        
        def perform_registration():
            try:
                # Check if username exists
                get_username_query = """ SELECT username FROM users WHERE username=%s; """
                db_con = db.create_db_connection("localhost", "root", db.rp, "CSA")
                username_exists = db.read_query_data(db_con, get_username_query, [user_name])
                db_con.close()
                
                if username_exists:
                    frame.after(0, lambda: complete_registration(False, "Username already exists"))
                    return
                
                # Generate password hash
                salt = bcrypt.gensalt(rounds=12)
                hashed = bcrypt.hashpw(password.encode('utf8'), salt)
                
                # Insert query - Include date_of_birth with a default value
                insert_users_query = """ 
                INSERT INTO users (first_name, last_name, email, company, username, password, salt, date_of_birth) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s); 
                """
                
                # Use current date as default for date_of_birth
                default_date = datetime.date.today().strftime('%Y-%m-%d')
                
                values = [first_name, last_name, email, company, user_name, hashed, salt, default_date]
                
                # Insert into database
                db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")
                db.execute_query_data(db_connection, insert_users_query, values)
                db_connection.close()
                
                frame.after(0, lambda: complete_registration(True, "Account created successfully! You can now log in."))
                
            except Exception as e:
                frame.after(0, lambda: complete_registration(False, f"Registration error: {str(e)}"))
        
        def complete_registration(success, message):
            preloader.destroy()
            
            if success:
                messagebox.showinfo("Success", message)
                frame.switch_frame(Login_Page)
            else:
                messagebox.showwarning("Registration Failed", message)
        
        # Start registration process in background thread
        threading.Thread(target=perform_registration, daemon=True).start()

""" Preloader Animation """
class Preloader(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("")
        self.overrideredirect(True)
        self.configure(bg="white")
        self.attributes("-alpha", 0.9)
        
        # Center on parent
        width, height = 150, 150
        x = parent.winfo_rootx() + (parent.winfo_width() // 2) - (width // 2)
        y = parent.winfo_rooty() + (parent.winfo_height() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
        # Canvas for spinner
        self.canvas = tk.Canvas(self, width=100, height=100, bg="white", highlightthickness=0)
        self.canvas.pack(expand=True)
        
        # Spinner properties
        self.spinner_size = 40
        self.spinner_width = 8
        self.angle = 0
        
        # Loading text
        self.loading_text = self.canvas.create_text(
            50, 70, text="Processing...", font=("Arial", 10), fill=COLORS["text"]
        )
        
        self.draw_spinner()
        self.animate()
    
    def draw_spinner(self):
        self.canvas.delete("spinner")
        
        x0 = 50 - self.spinner_size // 2
        y0 = 50 - self.spinner_size // 2
        x1 = 50 + self.spinner_size // 2
        y1 = 50 + self.spinner_size // 2
        
        # Background circle
        self.canvas.create_oval(
            x0, y0, x1, y1, outline="#e0e0e0", width=self.spinner_width, tags="spinner"
        )
        
        # Animated arc
        self.canvas.create_arc(
            x0, y0, x1, y1, start=self.angle, extent=90,
            outline=COLORS["primary"], style="arc", width=self.spinner_width, tags="spinner"
        )
    
    def animate(self):
        self.angle = (self.angle + 10) % 360
        self.draw_spinner()
        self.after(30, self.animate)

""" Open URL in Browser """
def open_url(url):
    webbrowser.open_new(url)