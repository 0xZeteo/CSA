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
import threading
import time

# Color scheme - Turquoise and Light Blue
COLORS = {
    "primary": "#950000",     # Red
    "secondary": "#010100",   # Blackish
    "bg": "#f0f2f5",          # Light background
    "text": "#333333",        # Dark text
    "entry_bg": "#e0e0e0",    # Light gray entry fields
    "light_text": "#888888"   # Light gray text
}

""" Home Page """
class Home_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper())
        self.config(bg=COLORS["bg"])

        # Unbind events from login page
        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")
        
        # Create main container with padding
        main_container = tk.Frame(self, bg=COLORS["bg"], padx=40, pady=40)
        main_container.pack(fill="both", expand=True)
        
        # Header with welcome message
        header_frame = tk.Frame(main_container, bg=COLORS["bg"])
        header_frame.pack(fill="x", pady=(0, 30))
        
        welcome_label = tk.Label(
            header_frame, 
            text=f"Welcome, {login.Login_Page.logged_in.capitalize()}",
            font=("Arial", 24, "bold"),
            bg=COLORS["bg"],
            fg=COLORS["primary"]
        )
        welcome_label.pack(side="left")
        
        # Main content area with two columns
        content_frame = tk.Frame(main_container, bg=COLORS["bg"])
        content_frame.pack(fill="both", expand=True)
        
        # Left column - User actions and results
        left_column = tk.Frame(content_frame, bg=COLORS["bg"], width=250)
        left_column.pack(side="left", fill="y", padx=(0, 30))
        
        # User actions section
        actions_frame = tk.Frame(left_column, bg="white", padx=20, pady=20)
        actions_frame.pack(fill="x", pady=(0, 20))
        
        actions_title = tk.Label(
            actions_frame, 
            text="User Actions", 
            font=("Arial", 14, "bold"),
            bg="white", 
            fg=COLORS["primary"]
        )
        actions_title.pack(anchor="w", pady=(0, 10))
        
        # User action buttons
        self.create_action_button(actions_frame, "Logout", lambda: reset_and_logout(master))
        self.create_action_button(actions_frame, "Change Password", lambda: master.switch_frame(Change_Password_Page))
        
        # Results section
        results_frame = tk.Frame(left_column, bg="white", padx=20, pady=20)
        results_frame.pack(fill="x")
        
        results_title = tk.Label(
            results_frame, 
            text="View Results", 
            font=("Arial", 14, "bold"),
            bg="white", 
            fg=COLORS["primary"]
        )
        results_title.pack(anchor="w", pady=(0, 10))
        
        self.create_action_button(results_frame, "Risk Results", lambda: display_irp(master))
        self.create_action_button(results_frame, "Maturity Results", lambda: display_csm(master))
        
        # Right column - Assessment cards
        right_column = tk.Frame(content_frame, bg=COLORS["bg"])
        right_column.pack(side="right", fill="both", expand=True)
        
        # Assessment cards
        self.create_assessment_card(
            right_column,
            "Inherent Risk Profile",
            "The Inherent Risk Profile identifies the institution's inherent risk before implementing controls",
            "Assess Risk",
            lambda: master.switch_frame(irp.IRP_Page)
        )
        
        self.create_assessment_card(
            right_column,
            "Cybersecurity Maturity",
            "The Cybersecurity Maturity includes domains, assessment factors, components, and individual declarative statements across five maturity levels to identify specific controls and practices that are in place",
            "Assess Maturity",
            lambda: master.switch_frame(csm.CSM_Page)
        )
    
    def create_action_button(self, parent, text, command):
        """Create a styled button for actions"""
        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 12),
            bg="white",
            fg=COLORS["text"],
            activebackground=COLORS["secondary"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=10,
            pady=8,
            cursor="hand2",
            anchor="w",
            width=15,
            command=command
        )
        button.pack(fill="x", pady=5)
        
        # Add hover effect
        button.bind("<Enter>", lambda e: button.config(bg=COLORS["entry_bg"]))
        button.bind("<Leave>", lambda e: button.config(bg="white"))
        
        return button
    
    def create_sidebar_button(self, parent, text, command):
        """Create a styled button for the sidebar"""
        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 12),
            bg=COLORS["bg"],
            fg=COLORS["text"],
            activebackground=COLORS["secondary"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            anchor="w",
            width=15,
            command=command
        )
        button.pack(fill="x", pady=5)
        
        # Add hover effect
        button.bind("<Enter>", lambda e: button.config(bg=COLORS["entry_bg"]))
        button.bind("<Leave>", lambda e: button.config(bg=COLORS["bg"]))
        
        return button
    
    def create_assessment_card(self, parent, title, description, button_text, command):
        """Create a card for assessment options"""
        # Card with shadow effect
        card_shadow = tk.Frame(parent, bg="#dddddd")
        card_shadow.pack(fill="x", pady=15, padx=1)
        
        card = tk.Frame(card_shadow, bg="white", padx=25, pady=25)
        card.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Title
        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"],
            anchor="w"
        )
        title_label.pack(fill="x", pady=(0, 10))
        
        # Description
        desc_frame = tk.Frame(card, bg="white")
        desc_frame.pack(fill="x", pady=(0, 15))
        
        desc_text = tk.Text(
            desc_frame,
            height=3,
            wrap="word",
            font=("Arial", 12),
            relief="flat",
            bg="white",
            fg=COLORS["text"]
        )
        desc_text.insert(tk.END, description)
        desc_text.config(state="disabled")
        desc_text.pack(fill="x")
        
        # Button
        button = tk.Button(
            card,
            text=button_text,
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"],
            fg="white",
            activebackground=COLORS["secondary"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=command
        )
        button.pack(side="right")


""" Change Password Page """
class Change_Password_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - Change Password')
        self.config(bg=COLORS["bg"])
        
        # Main container
        container = tk.Frame(self, bg=COLORS["bg"])
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Card with shadow effect
        card_shadow = tk.Frame(container, bg="#dddddd")
        card_shadow.pack(padx=1, pady=1)
        
        card = tk.Frame(card_shadow, bg="white", padx=40, pady=40)
        card.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Title
        title = tk.Label(
            card, 
            text="CHANGE PASSWORD", 
            font=("Arial", 16, "bold"),
            bg="white", 
            fg=COLORS["primary"]
        )
        title.pack(pady=(0, 30))
        
        # Password fields
        old_password_entry = self.create_input_field(card, "CURRENT PASSWORD", "🔒", True)
        new_password_entry = self.create_input_field(card, "NEW PASSWORD", "🔒", True)
        confirm_password_entry = self.create_input_field(card, "CONFIRM PASSWORD", "🔒", True)
        
        # Password requirements
        password_info = tk.Label(
            card,
            text="Password must be at least 9 characters long, with 1+ uppercase, 1+ numeric and 1+ special characters ($,@,#,%)",
            font=("Arial", 9), 
            bg="white", 
            fg=COLORS["light_text"], 
            wraplength=400, 
            justify="left"
        )
        password_info.pack(fill="x", pady=(5, 20))
        
        # Buttons
        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(fill="x", pady=(10, 0))
        
        # Cancel button
        cancel_btn = tk.Button(
            btn_frame, 
            text="CANCEL", 
            font=("Arial", 12),
            bg=COLORS["bg"], 
            fg=COLORS["text"],
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=20, 
            pady=10, 
            cursor="hand2",
            command=lambda: master.switch_frame(Home_Page)
        )
        cancel_btn.pack(side="left", padx=5)
        
        # Confirm button
        confirm_btn = tk.Button(
            btn_frame, 
            text="CONFIRM", 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=20, 
            pady=10, 
            cursor="hand2",
            command=lambda: self.change_password(
                master, 
                old_password_entry.get(), 
                new_password_entry.get(), 
                confirm_password_entry.get()
            )
        )
        confirm_btn.pack(side="right", padx=5)
    
    def create_input_field(self, parent, label_text, icon, is_password=False):
        """Create a styled input field"""
        frame = tk.Frame(parent, bg="white")
        frame.pack(fill="x", pady=10)
        
        label = tk.Label(
            frame, 
            text=label_text, 
            font=("Arial", 10, "bold"),
            bg="white", 
            fg=COLORS["light_text"], 
            anchor="w"
        )
        label.pack(fill="x")
        
        entry_frame = tk.Frame(
            frame, 
            bg=COLORS["entry_bg"], 
            bd=0,
            highlightthickness=1, 
            highlightbackground=COLORS["entry_bg"]
        )
        entry_frame.pack(fill="x", pady=(5, 0))
        
        icon_label = tk.Label(
            entry_frame, 
            text=icon, 
            font=("Segoe UI Emoji", 12),
            bg=COLORS["entry_bg"], 
            fg=COLORS["light_text"], 
            padx=10
        )
        icon_label.pack(side="left")
        
        kwargs = {
            'font': ("Arial", 12),
            'relief': 'flat',
            'bd': 0,
            'bg': COLORS["entry_bg"],
            'fg': COLORS["text"],
            'insertbackground': COLORS["text"],
            'width': 20
        }
        
        if is_password:
            kwargs['show'] = "•"
            
        entry = tk.Entry(entry_frame, **kwargs)
        entry.pack(fill="x", ipady=10, padx=(0, 10), side="left", expand=True)
        
        return entry
    
    def change_password(self, frame, old_pass, new_pass, confirm_new_pass):
        """Handle password change with validation"""
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

        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your password?')
        if confirm:
            # if empty fields
            if (old_pass == "") or (new_pass == "") or (confirm_new_pass == ""):
                messagebox.showwarning("Warning", "All fields must be filled")
            # if wrong old password entered
            elif not bcrypt.checkpw(old_pass.encode('utf8'), old_hash[0][0].encode('utf8')):
                messagebox.showwarning("Warning", "Wrong password")
            # if new password does not match the confirm new password 
            elif new_pass != confirm_new_pass:
                messagebox.showwarning("Warning", "Password mismatch")
            # if new password does not conform to the required format 
            elif (len(new_pass) < 9 or not any(char.isdigit() for char in new_pass) or 
                  not any(char.isupper() for char in new_pass) or not any(char in SpecialChar for char in new_pass)):
                messagebox.showwarning("Warning", "Password must be 9 characters long with at least 1 numeric, 1 uppercase and 1 special character ($,@,#,%)")
            else:
                db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")
                db.execute_query_data(db_connection, change_password_query, new_values)
                db_connection.close()
                messagebox.showinfo("Success", "Password changed successfully!")
                frame.switch_frame(Home_Page)


""" Tooltip Class """
class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltipwindow = None

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        self.tooltipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx()-10, self.widget.winfo_rooty()-15))
        
        label = tk.Label(
            tw, 
            text=self.text, 
            background="#ffffe0", 
            relief='solid', 
            borderwidth=1,
            font=("Arial", 9),
            padx=5,
            pady=5
        )
        label.pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        if tw is not None:
            tw.destroy()
        self.tooltipwindow = None


""" Preloader Animation """
class Preloader(tk.Toplevel):
    def __init__(self, parent, message="Loading..."):
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
            50, 70, text=message, font=("Arial", 10), fill=COLORS["text"]
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


""" Display IRP Results Page """
class Display_IRP(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        master.title(login.Login_Page.logged_in.upper() + ' - Inherent Risk Profile Results')
        self.config(bg=COLORS["bg"])

        # Main container with better padding
        container = tk.Frame(self, bg=COLORS["bg"], padx=30, pady=30)
        container.pack(fill="both", expand=True)
        
        # Header with improved styling
        header_frame = tk.Frame(container, bg="white", padx=25, pady=20)
        header_frame.pack(fill="x", pady=(0, 20))
        
        title = tk.Label(
            header_frame, 
            text="Inherent Risk Profile Results", 
            font=("Arial", 18, "bold"),
            bg="white", 
            fg=COLORS["primary"]
        )
        title.pack(side="left")
        
        # Action buttons with improved placement
        button_frame = tk.Frame(header_frame, bg="white")
        button_frame.pack(side="right")
        
        back_button = tk.Button(
            button_frame, 
            text='Back to Home', 
            font=("Arial", 12),
            bg=COLORS["bg"], 
            fg=COLORS["text"],
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: master.switch_frame(Home_Page)
        )
        back_button.pack(side="left", padx=10)
        
        graph_button = tk.Button(
            button_frame, 
            text='Graph Display', 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: self.graph(table.item(table.focus()))
        )
        graph_button.pack(side="left")
        
        # Admin delete button
        if login.Login_Page.logged_in == 'admin':
            delete_button = tk.Button(
                button_frame, 
                text="Delete Selected", 
                font=("Arial", 12),
                bg="#ff6b6b", 
                fg="white",
                activebackground="#ff8787", 
                activeforeground="white",
                relief="flat", 
                bd=0, 
                padx=15, 
                pady=8, 
                cursor="hand2",
                command=lambda: self.delete(table.item(table.focus()), master)
            )
            delete_button.pack(side="left", padx=10)
        
        # Table frame with shadow
        table_shadow = tk.Frame(container, bg="#dddddd")
        table_shadow.pack(fill="both", expand=True, padx=1, pady=1)
        
        table_frame = tk.Frame(table_shadow, bg="white", padx=15, pady=15)
        table_frame.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Style the treeview
        style = ttk.Style()
        style.theme_use("default")
        
        # Configure the Treeview colors
        style.configure(
            "Treeview",
            background="white",
            foreground=COLORS["text"],
            rowheight=25,
            fieldbackground="white",
            font=("Arial", 10)
        )
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        
        # Change selected color
        style.map("Treeview", background=[("selected", COLORS["secondary"])])
        
        # Columns of the display table
        cols = ('Date','Name','Least','Minimal','Moderate','Significant','Most','Risk Level')
        table = ttk.Treeview(table_frame, columns=cols, show='headings', style="Treeview")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        table.configure(yscrollcommand=scrollbar.set)
        
        # Database connection
        cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
        
        get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
        username = [login.Login_Page.logged_in]
        uid = db.read_query_data(cnx, get_user_id_query, username)
        
        get_irp_query = """ SELECT date, name, least, minimal, moderate, significant, most, risk_level FROM irp WHERE user=%s ORDER BY date DESC; """
        get_irp_all_query = """ SELECT date, name, least, minimal, moderate, significant, most, risk_level FROM irp ORDER BY date DESC; """
        user = [uid[0][0]]
        
        if login.Login_Page.logged_in == 'admin':
            results = db.read_query(cnx, get_irp_all_query)
        else:
            results = db.read_query_data(cnx, get_irp_query, user)
        
        cnx.close()
        
        # Display table column names and width
        for col in cols:
            table.heading(col, text=col)
            if col in ['Date', 'Name', 'Risk Level']:
                table.column(col, width=120, anchor='center')
            else:
                table.column(col, width=80, anchor='center')
        
        # Insert data rows into display table
        for result in results:
            vals = []
            for i in range(len(result)):
                vals.append(result[i])
            table.insert("", "end", values=tuple(vals))
        
        table.pack(side=tk.LEFT, expand=True, fill='both')
    
    def graph(self, row):
        """Display selected assessment as a graph"""
        values = row.get('values')
        
        if not values:
            messagebox.showwarning('Warning', 'Select an assessment to visualize')
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            get_irp_query = """ SELECT least, minimal, moderate, significant, most FROM irp WHERE name=%s; """
            name_value = [values[1]]
            result = db.read_query_data(cnx, get_irp_query, name_value)
            cnx.close()
            
            # Configure plot style
            plt.style.use('ggplot')
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Labels on the x-axis
            x_axis = ['Least', 'Minimal', 'Moderate', 'Significant', 'Most']
            
            # Create the bars with custom colors using the new primary color
            bars = ax.bar(x_axis, result[0], color=[COLORS["secondary"], '#98d4f3', '#66c2ff', '#33b0ff', COLORS["primary"]])
            
            # Add value labels on top of bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{height}', ha='center', va='bottom', fontweight='bold')
            
            # Customize plot
            ax.set_title(f'Assessment: {values[1]}', fontsize=16, fontweight='bold')
            ax.set_xlabel('Risk Categories', fontsize=12)
            ax.set_ylabel('Count', fontsize=12)
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            
            plt.tight_layout()
            plt.show()
    
    def delete(self, row, frame):
        """Delete selected assessment"""
        values = row.get('values')
        
        if not values:
            messagebox.showwarning("Warning", "Select a row to delete")
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            delete_row_query = """ DELETE FROM irp WHERE name=%s; """
            name_value = [values[1]]
            if messagebox.askyesno("Confirmation", f"Are you sure you want to delete the assessment '{values[1]}'?"):
                db.execute_query_data(cnx, delete_row_query, name_value)
                messagebox.showinfo("Success", "Assessment deleted successfully")
                frame.switch_frame(Display_IRP)
            cnx.close()


""" Display CSM Results Page """
class Display_CSM(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        master.title(login.Login_Page.logged_in.upper() + ' - Cybersecurity Maturity Results')
        self.config(bg=COLORS["bg"])
        
        # Main container with better padding
        container = tk.Frame(self, bg=COLORS["bg"], padx=30, pady=30)
        container.pack(fill="both", expand=True)
        
        # Header with improved styling
        header_frame = tk.Frame(container, bg="white", padx=25, pady=20)
        header_frame.pack(fill="x", pady=(0, 20))
        
        title = tk.Label(
            header_frame, 
            text="Cybersecurity Maturity Results", 
            font=("Arial", 18, "bold"),
            bg="white", 
            fg=COLORS["primary"]
        )
        title.pack(side="left")
        
        # Help icon with better placement
        help_frame = tk.Frame(header_frame, bg="white")
        help_frame.pack(side="left", padx=10)
        
        help_icon = tk.Label(
            help_frame, 
            text="ℹ️", 
            font=("Segoe UI Emoji", 16),
            bg="white", 
            fg=COLORS["primary"],
            cursor="hand2"
        )
        help_icon.pack()
        
        # Create tooltip for help icon
        ToolTip(help_icon, 'Symbols: B: Baseline, E: Evolving, I/Inter: Intermediate, A: Advanced, I/Inno: Innovative\n(Y): Yes, (C): Compensating, (N): No')
        
        # Action buttons
        button_frame = tk.Frame(header_frame, bg=COLORS["bg"])
        button_frame.pack(side="right")
        
        back_button = tk.Button(
            button_frame, 
            text='Back to Home', 
            font=("Arial", 12),
            bg=COLORS["bg"], 
            fg=COLORS["text"],
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: master.switch_frame(Home_Page)
        )
        back_button.pack(side="left", padx=10)
        
        graph_button = tk.Button(
            button_frame, 
            text='Graph Display', 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: self.graph(table.item(table.focus()))
        )
        graph_button.pack(side="left")
        
        # Admin delete button
        if login.Login_Page.logged_in == 'admin':
            delete_button = tk.Button(
                button_frame, 
                text="Delete Selected", 
                font=("Arial", 12),
                bg="#ff6b6b", 
                fg="white",
                activebackground="#ff8787", 
                activeforeground="white",
                relief="flat", 
                bd=0, 
                padx=15, 
                pady=8, 
                cursor="hand2",
                command=lambda: self.delete(table.item(table.focus()), master)
            )
            delete_button.pack(side="left", padx=10)
        
        # Table frame with shadow
        table_shadow = tk.Frame(container, bg="#dddddd")
        table_shadow.pack(fill="both", expand=True, padx=1, pady=1)
        
        table_frame = tk.Frame(table_shadow, bg="white", padx=15, pady=15)
        table_frame.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Style the treeview
        style = ttk.Style()
        style.theme_use("default")
        
        # Configure the Treeview colors
        style.configure(
            "Treeview",
            background="white",
            foreground=COLORS["text"],
            rowheight=25,
            fieldbackground="white",
            font=("Arial", 10)
        )
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        
        # Change selected color
        style.map("Treeview", background=[("selected", COLORS["secondary"])])
        
        # Columns of the display table
        cols = ('Date','Name',
        'B (Y)', 'E (Y)', 'Inter (Y)', 'A (Y)', 'Inno (Y)',
        'B (C)', 'E (C)', 'Inter (C)', 'A (C)', 'Inno (C)',
        'B (N)', 'E (N)', 'Inter (N)', 'A (N)', 'Inno (N)',
        'Maturity Level')
        
        table = ttk.Treeview(table_frame, columns=cols, show='headings', style="Treeview")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        table.configure(yscrollcommand=scrollbar.set)
        
        # Database connection
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
        
        if login.Login_Page.logged_in == 'admin':
            results = db.read_query(cnx, get_csm_all_query)
        else:
            results = db.read_query_data(cnx, get_csm_query, user)
        
        cnx.close()
        
        # Display table column names and width
        for col in cols:
            table.heading(col, text=col)
            if col in ['Date', 'Name', 'Maturity Level']:
                table.column(col, width=120, anchor='center')
            else:
                table.column(col, width=60, anchor='center')
        
        # Insert data rows into display table
        for result in results:
            vals = []
            for i in range(len(result)):
                vals.append(result[i])
            table.insert("", "end", values=tuple(vals))
        
        table.pack(side=tk.LEFT, expand=True, fill='both')
    
    def graph(self, row):
        """Display selected assessment as a graph"""
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
            
            # Configure plot style
            plt.style.use('ggplot')
            fig, ax = plt.subplots(figsize=(12, 7))
            
            # Labels on the x-axis
            x_axis = ['B(Y)', 'E(Y)', 'I(Y)', 'A(Y)', 'I(Y)',
                      'B(C)', 'E(C)', 'I(C)', 'A(C)', 'I(C)',
                      'B(N)', 'E(N)', 'I(N)', 'A(N)', 'I(N)']
            
            # Create color groups
            colors = [COLORS["primary"], COLORS["primary"], COLORS["primary"], COLORS["primary"], COLORS["primary"],
                     COLORS["secondary"], COLORS["secondary"], COLORS["secondary"], COLORS["secondary"], COLORS["secondary"],
                     '#ff9999', '#ff9999', '#ff9999', '#ff9999', '#ff9999']
            
            # Create the bars with custom colors
            bars = ax.bar(x_axis, result[0], color=colors)
            
            # Add value labels on top of bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{height}', ha='center', va='bottom', fontweight='bold')
            
            # Customize plot
            ax.set_title(f'Assessment: {values[1]}', fontsize=16, fontweight='bold')
            ax.set_xlabel('Categories', fontsize=12)
            ax.set_ylabel('Count', fontsize=12)
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Add legend
            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor=COLORS["primary"], label='Yes'),
                Patch(facecolor=COLORS["secondary"], label='Compensating'),
                Patch(facecolor='#ff9999', label='No')
            ]
            ax.legend(handles=legend_elements, loc='upper right')
            
            plt.tight_layout()
            plt.show()
    
        # Action buttons
        button_frame = tk.Frame(header_frame, bg="white")
        button_frame.pack(side="right")
        
        back_button = tk.Button(
            button_frame, 
            text='Back to Home', 
            font=("Arial", 12),
            bg=COLORS["bg"], 
            fg=COLORS["text"],
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: master.switch_frame(Home_Page)
        )
        back_button.pack(side="left", padx=10)
        
        graph_button = tk.Button(
            button_frame, 
            text='Graph Display', 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["secondary"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: self.graph(table.item(table.focus()))
        )
        graph_button.pack(side="left")
    
    def delete(self, row, frame):
        """Delete selected assessment"""
        values = row.get('values')
        
        if not values:
            messagebox.showwarning("Warning", "Select a row to delete")
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            delete_row_query = """ DELETE FROM csm WHERE name=%s; """
            name_value = [values[1]]
            if messagebox.askyesno("Confirmation", f"Are you sure you want to delete the assessment '{values[1]}'?"):
                db.execute_query_data(cnx, delete_row_query, name_value)
                messagebox.showinfo("Success", "Assessment deleted successfully")
                frame.switch_frame(Display_CSM)
            cnx.close()


""" Utility Functions """

def display_irp(frame):
    """Check if IRP results exist before displaying"""
    # Show loading indicator
    preloader = Preloader(frame, "Loading results...")
    
    def check_results():
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
        
        # Simulate delay (remove in production)
        time.sleep(0.5)
        
        # Update UI in main thread
        frame.after(0, lambda: complete_check(results))
    
    def complete_check(results):
        preloader.destroy()
        
        if not results:
            messagebox.showwarning("Warning", "No assessments have been saved by this user")
        else:
            frame.switch_frame(Display_IRP)
    
    # Start check in background thread
    threading.Thread(target=check_results, daemon=True).start()


def display_csm(frame):
    """Check if CSM results exist before displaying"""
    # Show loading indicator
    preloader = Preloader(frame, "Loading results...")
    
    def check_results():
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
        
        # Simulate delay (remove in production)
        time.sleep(0.5)
        
        # Update UI in main thread
        frame.after(0, lambda: complete_check(results))
    
    def complete_check(results):
        preloader.destroy()
        
        if not results:
            messagebox.showwarning("Warning", "No assessments have been saved by this user")
        else:
            frame.switch_frame(Display_CSM)
    
    # Start check in background thread
    threading.Thread(target=check_results, daemon=True).start()


def reset_and_logout(frame):
    """Reset assessments and logout"""
    confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to logout? Unsaved results will be lost')
    if confirm:
        # Show loading indicator
        preloader = Preloader(frame, "Logging out...")
        
        def perform_logout():
            # Reset assessments
            csm.reset_csm()
            irp.reset_irp()
            
            # Simulate delay (remove in production)
            time.sleep(0.5)
            
            # Update UI in main thread
            frame.after(0, complete_logout)
        
        def complete_logout():
            preloader.destroy()
            frame.switch_frame(login.Login_Page)
        
        # Start logout process in background thread
        threading.Thread(target=perform_logout, daemon=True).start()
