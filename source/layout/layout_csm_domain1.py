""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE CYBERSECURITY MATURITY DOMAIN 1 """

import layout.layout_home as home
import layout.layout_csm as csm
import layout.layout_login as login
import DATA

import tkinter as tk
from tkinter import messagebox

# Define color constants for consistent styling
COLORS = {
    "primary": "#950000",     # Red
    "primary_light": "#c13030", # Lighter red for hover effects
    "primary_dark": "#6b0000", # Darker red for accents
    "secondary": "#010100",   # Blackish
    "secondary_light": "#333333", # Lighter black for hover
    "bg": "#f0f2f5",          # Light background
    "text": "#333333",        # Dark text
    "entry_bg": "#e0e0e0",    # Light gray entry fields
    "light_text": "#888888",  # Light gray text
    "success": "#4CAF50",     # Green for completed items
    "warning": "#FFC107",     # Yellow for in-progress
    "card_bg": "#ffffff",     # White for card backgrounds
    "accent": "#ff9800"       # Orange accent color
}

# Define maturity level colors
MATURITY_COLORS = {
    "baseline": "#4CAF50",      # Green for baseline
    "evolving": "#8BC34A",      # Light green for evolving
    "intermediate": "#FFC107",  # Yellow for intermediate
    "advanced": "#FF9800",      # Orange for advanced
    "innovative": "#F44336"     # Red for innovative
}

""" This class is responsible for the layout of the Cybersecurity Maturity's Domain 1 page """
class CSM_Domain1_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Cyber Risk Management and Oversight")

        self.unbind_all("<MouseWheel>")
        self.config(bg=COLORS["bg"])

        # Main container with padding
        main_container = tk.Frame(self, bg=COLORS["bg"], padx=40, pady=40)
        main_container.pack(fill="both", expand=True)
        
        # Header with title and decorative element
        header_frame = tk.Frame(main_container, bg=COLORS["bg"])
        header_frame.pack(fill="x", pady=(0, 30))
        
        # Decorative line
        line_frame = tk.Frame(header_frame, bg=COLORS["primary"], height=3, width=50)
        line_frame.pack(side="left", padx=(0, 15), pady=(15, 0))
        
        title_label = tk.Label(
            header_frame, 
            text="Cyber Risk Management and Oversight",
            font=("Arial", 24, "bold"),
            bg=COLORS["bg"],
            fg=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # Navigation buttons
        button_frame = tk.Frame(main_container, bg=COLORS["bg"], pady=20)
        button_frame.pack(fill="x")
        
        home_button = tk.Button(
            button_frame, 
            text="HOME", 
            font=("Arial", 12, "bold"),
            bg=COLORS["bg"], 
            fg=COLORS["text"],
            activebackground=COLORS["secondary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=20, 
            pady=10, 
            cursor="hand2",
            command=lambda: master.switch_frame(home.Home_Page)
        )
        home_button.pack(side="left", padx=5)
        
        # Add hover effect
        def home_enter(e):
            home_button['bg'] = COLORS["entry_bg"]
        
        def home_leave(e):
            home_button['bg'] = COLORS["bg"]
        
        home_button.bind("<Enter>", home_enter)
        home_button.bind("<Leave>", home_leave)
        
        back_button = tk.Button(
            button_frame, 
            text="BACK", 
            font=("Arial", 12),
            bg=COLORS["bg"], 
            fg=COLORS["text"],
            activebackground=COLORS["secondary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=20, 
            pady=10, 
            cursor="hand2",
            command=lambda: master.switch_frame(csm.CSM_Page)
        )
        back_button.pack(side="left", padx=5)
        
        # Add hover effect
        def back_enter(e):
            back_button['bg'] = COLORS["entry_bg"]
        
        def back_leave(e):
            back_button['bg'] = COLORS["bg"]
        
        back_button.bind("<Enter>", back_enter)
        back_button.bind("<Leave>", back_leave)
        
        reset_button = tk.Button(
            button_frame, 
            text="RESET", 
            font=("Arial", 12),
            bg=COLORS["bg"], 
            fg=COLORS["text"],
            activebackground=COLORS["secondary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=20, 
            pady=10, 
            cursor="hand2",
            command=lambda: self.reset(master)
        )
        reset_button.pack(side="right", padx=5)
        
        # Add hover effect
        def reset_enter(e):
            reset_button['bg'] = COLORS["entry_bg"]
        
        def reset_leave(e):
            reset_button['bg'] = COLORS["bg"]
        
        reset_button.bind("<Enter>", reset_enter)
        reset_button.bind("<Leave>", reset_leave)
        
        # Content area with a subtle shadow effect
        content_frame = tk.Frame(main_container, bg=COLORS["bg"], bd=0)
        content_frame.pack(fill="both", expand=True)
        
        # Categories section with a subtle shadow
        categories_shadow = tk.Frame(content_frame, bg="#bbbbbb")
        categories_shadow.pack(fill="both", expand=True, padx=1, pady=1)

        categories_frame = tk.Frame(categories_shadow, bg="white", padx=15, pady=15)
        categories_frame.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Create a grid layout for the categories
        # First row - 2 cards side by side
        row1_frame = tk.Frame(categories_frame, bg="white")
        row1_frame.pack(fill="x", pady=5)

        # Left column in first row
        col1_frame = tk.Frame(row1_frame, bg="white")
        col1_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        # Right column in first row
        col2_frame = tk.Frame(row1_frame, bg="white")
        col2_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        # Second row - 2 cards side by side
        row2_frame = tk.Frame(categories_frame, bg="white")
        row2_frame.pack(fill="x", pady=5)

        # Left column in second row
        col3_frame = tk.Frame(row2_frame, bg="white")
        col3_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        # Right column in second row
        col4_frame = tk.Frame(row2_frame, bg="white")
        col4_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))
        
        # Create category cards in grid layout
        self.create_category_card(
            col1_frame,
            "Governance",
            csm.submit_pressed(CSM_Domain1_Governance_Page.values)[3],
            sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance]),
            lambda: master.switch_frame(CSM_Domain1_Governance_Page)
        )
        
        self.create_category_card(
            col2_frame,
            "Risk Management",
            csm.submit_pressed(CSM_Domain1_RiskManagement_Page.values)[3],
            sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement]),
            lambda: master.switch_frame(CSM_Domain1_RiskManagement_Page)
        )
        
        self.create_category_card(
            col3_frame,
            "Resources",
            csm.submit_pressed(CSM_Domain1_Resources_Page.values)[3],
            sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources]),
            lambda: master.switch_frame(CSM_Domain1_Resources_Page)
        )
        
        self.create_category_card(
            col4_frame,
            "Training and Culture",
            csm.submit_pressed(CSM_Domain1_TrainingAndCulture_Page.values)[3],
            sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture]),
            lambda: master.switch_frame(CSM_Domain1_TrainingAndCulture_Page)
        )

    def create_category_card(self, parent, text, answered, total, command):
        """Create a styled card for categories with question count"""
        # Card with shadow effect
        card_shadow = tk.Frame(parent, bg="#bbbbbb")
        card_shadow.pack(fill="both", expand=True, pady=5, padx=1)
        
        # Calculate completion percentage
        completion_pct = (answered / total) * 100 if total > 0 else 0
        
        # Determine card shadow color based on completion
        shadow_color = COLORS["primary"] if completion_pct == 100 else (
            COLORS["accent"] if completion_pct > 0 else "#bbbbbb"
        )
        
        # Update shadow color
        card_shadow.config(bg=shadow_color)
        
        card = tk.Frame(card_shadow, bg=COLORS["card_bg"], padx=15, pady=10)
        card.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Left side - text and count
        info_frame = tk.Frame(card, bg=COLORS["card_bg"])
        info_frame.pack(side="left", fill="both", expand=True)
        
        # Category name with icon based on completion
        category_frame = tk.Frame(info_frame, bg=COLORS["card_bg"])
        category_frame.pack(fill="x", anchor="w")
        
        # Icon indicator based on completion
        icon_text = "✓" if completion_pct == 100 else ("⋯" if completion_pct > 0 else "○")
        icon_color = COLORS["success"] if completion_pct == 100 else (
            COLORS["warning"] if completion_pct > 0 else COLORS["light_text"]
        )
        
        icon_label = tk.Label(
            category_frame,
            text=icon_text,
            font=("Arial", 12, "bold"),
            bg=COLORS["card_bg"],
            fg=icon_color
        )
        icon_label.pack(side="left", padx=(0, 5))
        
        # Category name
        category_label = tk.Label(
            category_frame,
            text=text,
            font=("Arial", 12, "bold"),
            bg=COLORS["card_bg"],
            fg=COLORS["primary"],
            anchor="w"
        )
        category_label.pack(side="left", fill="x")
        
        # Questions answered count
        count_frame = tk.Frame(info_frame, bg=COLORS["card_bg"])
        count_frame.pack(fill="x", pady=(5, 0))
        
        count_label = tk.Label(
            count_frame,
            text=f"{answered}/{total} Answered",
            font=("Arial", 9),
            bg=COLORS["card_bg"],
            fg=COLORS["text"],
            anchor="w"
        )
        count_label.pack(side="left", padx=(20, 0))
        
        # Progress bar with improved dynamic updating
        progress_frame = tk.Frame(info_frame, bg=COLORS["card_bg"], pady=5)
        progress_frame.pack(fill="x")
        
        progress_bg = tk.Frame(progress_frame, bg=COLORS["entry_bg"], height=6)
        progress_bg.pack(fill="x", padx=20)
        
        # Create the progress indicator with the correct width based on percentage
        if completion_pct > 0:
            # We need to create the progress bar after the main window is drawn
            # so we can get the actual width of the background
            def update_progress_bar(bg_frame, fg_color, completion):
                # Get the actual width of the background frame
                bg_width = bg_frame.winfo_width()
                if bg_width > 1:  # Ensure the frame has been rendered
                    # Calculate the width of the progress bar
                    progress_width = int((completion / 100) * bg_width)
                    # Create the progress indicator
                    progress_fg = tk.Frame(bg_frame, bg=fg_color, height=6, width=progress_width)
                    progress_fg.place(x=0, y=0)
                else:
                    # If the frame hasn't been rendered yet, try again after a short delay
                    bg_frame.after(50, lambda: update_progress_bar(bg_frame, fg_color, completion))
            
            # Determine color based on completion
            progress_color = COLORS["success"] if completion_pct == 100 else COLORS["warning"]
            
            # Schedule the progress bar update
            progress_bg.after(50, lambda: update_progress_bar(progress_bg, progress_color, completion_pct))
        
        # Button with hover effect and improved styling
        button = tk.Button(
            card,
            text="View Assessment",
            font=("Arial", 9, "bold"),
            bg=COLORS["primary"],
            fg="white",
            activebackground=COLORS["primary_light"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=10,
            pady=5,
            cursor="hand2",
            command=command  # This is the key issue - ensure command is passed directly
        )
        button.pack(side="right", padx=(10, 0))
        
        # Add hover effect
        def on_enter(e):
            button['bg'] = COLORS["primary_light"]
        
        def on_leave(e):
            button['bg'] = COLORS["primary"]
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return card

    # reset the answers of Domain 1
    def reset(self, frame):
        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your answers?')
        if confirm:
            csm.clear_pressed(CSM_Domain1_Governance_Page.values)
            csm.clear_pressed(CSM_Domain1_RiskManagement_Page.values)
            csm.clear_pressed(CSM_Domain1_Resources_Page.values)
            csm.clear_pressed(CSM_Domain1_TrainingAndCulture_Page.values)
            frame.switch_frame(CSM_Domain1_Page)


""" This class is responsible for the layout of the Cybersecurity Maturity's Domain 1 - Governance page """
class CSM_Domain1_Governance_Page(tk.Frame):
    values = []
    selected_containers = [] # holds references to the currently selected containers

    # Initialize the values list with enough elements if it's empty
    @classmethod
    def initialize_values(cls):
        if not cls.values:
            total_questions = sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance])
            for _ in range(total_questions):
                cls.values.append(tk.IntVar())

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Governance")
        self.config(bg=COLORS["bg"])
        
        # Initialize values list if needed
        self.initialize_values()

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        # Header with title and navigation
        header_container = tk.Frame(top_frame, bg="white", padx=20, pady=15)
        header_container.pack(fill="x")
        
        # Title and back button
        title_frame = tk.Frame(header_container, bg="white")
        title_frame.pack(side="left")
        
        back_button = tk.Button(
            title_frame, 
            text="← Back",
            font=("Arial", 12),
            bg="white", 
            fg=COLORS["primary"],
            activebackground=COLORS["bg"], 
            activeforeground=COLORS["primary"],
            relief="flat", 
            bd=0, 
            padx=5, 
            pady=0, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Governance",
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # Home button
        home_button = tk.Button(
            header_container, 
            text="HOME", 
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
            command=lambda: master.switch_frame(home.Home_Page)
        )
        home_button.pack(side="right")
        
        # Progress indicator
        total_questions = sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance])
        answered_questions = csm.submit_pressed(self.values)[3]
        progress_text = f"{answered_questions}/{total_questions} Answered"
        progress_label = tk.Label(
            header_container,
            text=progress_text,
            font=("Arial", 12),
            bg="white",
            fg=COLORS["text"]
        )
        progress_label.pack(side="right", padx=15)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        button_container = tk.Frame(bottom_frame, bg="white", padx=20, pady=15)
        button_container.pack(fill="x")
        
        # Help text
        help_label = tk.Label(
            button_container,
            text="Select an answer for each question",
            font=("Arial", 11, "italic"),
            bg="white",
            fg=COLORS["light_text"]
        )
        help_label.pack(side="left")
        
        # Action buttons
        clear_button = tk.Button(
            button_container, 
            text='CLEAR ANSWERS', 
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
            command=lambda: csm.clear_category(self.values, self.selected_containers)
        )
        clear_button.pack(side="right", padx=5)
        
        submit_button = tk.Button(
            button_container, 
            text='SAVE & CONTINUE', 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["primary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        submit_button.pack(side="right", padx=5)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self, bg="white")
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, bg="white")

        # defines the scrolling distance when mousewheel is used
        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white", padx=20, pady=20)
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Initialize selected_containers list if needed
        total_questions = sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance])
        if len(self.selected_containers) < total_questions:
            for _ in range(total_questions - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        question_index = 0
        for key, values in DATA.CSM_Domain1_Governance.items():
            for j in range(len(values)):
                # Add to values list if not already there
                if question_index >= len(self.values):
                    self.values.append(tk.IntVar())
                
                # Question card with shadow effect
                card_shadow = tk.Frame(middle_frame, bg="#dddddd")
                card_shadow.pack(fill="x", pady=10, padx=1)
                
                # Determine shadow color based on answer
                selected_value = self.values[question_index].get()
                if selected_value == 0:
                    shadow_color = "#dddddd"  # Not answered
                else:
                    shadow_color = COLORS["primary"]  # Answered
                
                # Update the shadow color
                card_shadow.config(bg=shadow_color)
                
                # Create the question frame
                question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
                question_frame.pack(fill="both", expand=True, padx=3, pady=3)
                
                # Question text
                question = tk.Label(
                    question_frame, 
                    text=values[j], 
                    wraplength=1000, 
                    justify=tk.LEFT, 
                    font=("Arial", 12),
                    bg="white",
                    fg=COLORS["text"],
                    anchor="w"
                )
                question.pack(fill="x", expand=True, anchor="w")
                
                # Answer options frame
                answer_frame = tk.Frame(question_frame, bg="white", pady=10)
                answer_frame.pack(fill="x")
                
                # Store containers for this question
                question_containers = []
                
                # Create answer options
                options = [
                    ("Y", "Yes"),
                    ("Y(C)", "Yes (Compensating)"),
                    ("N", "No")
                ]
                
                for k, (option_text, option_desc) in enumerate(options):
                    option_frame = tk.Frame(answer_frame, bg="white", padx=5)
                    option_frame.pack(side="left", padx=10)
                    
                    # Create a container for the option
                    radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                    radio_container.pack(fill="both", expand=True)
                    question_containers.append(radio_container)
                    
                    # Add the option text
                    option_label = tk.Label(
                        radio_container,
                        text=option_text,
                        font=("Arial", 12, "bold"),
                        bg="white",
                        fg=COLORS["text"],
                        padx=10,
                        pady=5
                    )
                    option_label.pack()
                    
                    # Add a tooltip frame that shows on hover
                    tooltip_frame = tk.Frame(radio_container, bg=COLORS["bg"], padx=5, pady=2)
                    tooltip_label = tk.Label(
                        tooltip_frame,
                        text=option_desc,
                        font=("Arial", 9),
                        bg=COLORS["bg"],
                        fg=COLORS["text"]
                    )
                    tooltip_label.pack()
                    
                    # Add a hidden radio button for tracking the selection
                    radio_var = self.values[question_index]
                    
                    # First part of the value references the answer (1 = yes | 2 = yes compensating | 3 = no)
                    # Second part of the value references the maturity level (1-5)
                    maturity_num = int(key[-1])
                    option_value = (k + 1) * 10 + maturity_num
                    
                    radio_btn = tk.Radiobutton(
                        radio_container, 
                        variable=radio_var, 
                        value=option_value,
                        bg="white",
                        activebackground="white",
                        highlightthickness=0,
                        bd=0,
                        padx=0,
                        pady=0
                    )
                    
                    # If this option is selected, update the container appearance
                    if radio_var.get() == option_value:
                        radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        option_label.config(bg=COLORS["bg"])
                        self.selected_containers[question_index] = radio_container
                    
                    # Make the entire container clickable
                    def make_click_handler(radio_btn, container, question_idx, containers, card_shadow):
                        def on_click(event):
                            # First reset all containers for this question
                            for c in containers:
                                c.config(relief="raised", bd=1, bg="white")
                                for widget in c.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            
                            # Then update the selected container
                            radio_btn.select()
                            container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if isinstance(widget, tk.Label):
                                    widget.config(bg=COLORS["bg"])
                            
                            # Update the selected container reference
                            self.selected_containers[question_idx] = container
                            
                            # Update the question card shadow color
                            card_shadow.config(bg=COLORS["primary"])
                        return on_click
                    
                    # Bind click events to all elements
                    radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    option_label.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    
                    # Add hover effect
                    def make_hover_handler(container, tooltip):
                        def on_hover(event):
                            if container != self.selected_containers[question_index]:  # Only apply hover to non-selected containers
                                container.config(bg=COLORS["bg"])
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg=COLORS["bg"])
                            tooltip.pack()
                        return on_hover
                    
                    def make_leave_handler(container, tooltip):
                        def on_leave(event):
                            if container != self.selected_containers[question_index]:  # Only revert hover on non-selected containers
                                container.config(bg="white")
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            tooltip.pack_forget()
                        return on_leave
                    
                    radio_container.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    radio_container.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    option_label.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    option_label.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    
                    # Initially hide the tooltip
                    tooltip_frame.pack_forget()
                
                question_index += 1


""" This class is responsible for the layout of the Cybersecurity Maturity's Domain 1 - Risk Management page """
class CSM_Domain1_RiskManagement_Page(tk.Frame):
    values = []
    selected_containers = [] # holds references to the currently selected containers

    # Initialize the values list with enough elements if it's empty
    @classmethod
    def initialize_values(cls):
        if not cls.values:
            total_questions = sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement])
            for _ in range(total_questions):
                cls.values.append(tk.IntVar())

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Risk Management")
        self.config(bg=COLORS["bg"])
        
        # Initialize values list if needed
        self.initialize_values()

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        # Header with title and navigation
        header_container = tk.Frame(top_frame, bg="white", padx=20, pady=15)
        header_container.pack(fill="x")
        
        # Title and back button
        title_frame = tk.Frame(header_container, bg="white")
        title_frame.pack(side="left")
        
        back_button = tk.Button(
            title_frame, 
            text="← Back",
            font=("Arial", 12),
            bg="white", 
            fg=COLORS["primary"],
            activebackground=COLORS["bg"], 
            activeforeground=COLORS["primary"],
            relief="flat", 
            bd=0, 
            padx=5, 
            pady=0, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Risk Management",
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # Home button
        home_button = tk.Button(
            header_container, 
            text="HOME", 
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
            command=lambda: master.switch_frame(home.Home_Page)
        )
        home_button.pack(side="right")
        
        # Progress indicator
        total_questions = sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement])
        answered_questions = csm.submit_pressed(self.values)[3]
        progress_text = f"{answered_questions}/{total_questions} Answered"
        progress_label = tk.Label(
            header_container,
            text=progress_text,
            font=("Arial", 12),
            bg="white",
            fg=COLORS["text"]
        )
        progress_label.pack(side="right", padx=15)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        button_container = tk.Frame(bottom_frame, bg="white", padx=20, pady=15)
        button_container.pack(fill="x")
        
        # Help text
        help_label = tk.Label(
            button_container,
            text="Select an answer for each question",
            font=("Arial", 11, "italic"),
            bg="white",
            fg=COLORS["light_text"]
        )
        help_label.pack(side="left")
        
        # Action buttons
        clear_button = tk.Button(
            button_container, 
            text='CLEAR ANSWERS', 
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
            command=lambda: csm.clear_category(self.values, self.selected_containers)
        )
        clear_button.pack(side="right", padx=5)
        
        submit_button = tk.Button(
            button_container, 
            text='SAVE & CONTINUE', 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["primary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        submit_button.pack(side="right", padx=5)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self, bg="white")
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, bg="white")

        # defines the scrolling distance when mousewheel is used
        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white", padx=20, pady=20)
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Initialize selected_containers list if needed
        total_questions = sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement])
        if len(self.selected_containers) < total_questions:
            for _ in range(total_questions - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        question_index = 0
        for key, values in DATA.CSM_Domain1_RiskManagement.items():
            for j in range(len(values)):
                # Add to values list if not already there
                if question_index >= len(self.values):
                    self.values.append(tk.IntVar())
                
                # Question card with shadow effect
                card_shadow = tk.Frame(middle_frame, bg="#dddddd")
                card_shadow.pack(fill="x", pady=10, padx=1)
                
                # Determine shadow color based on answer
                selected_value = self.values[question_index].get()
                if selected_value == 0:
                    shadow_color = "#dddddd"  # Not answered
                else:
                    shadow_color = COLORS["primary"]  # Answered
                
                # Update the shadow color
                card_shadow.config(bg=shadow_color)
                
                # Create the question frame
                question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
                question_frame.pack(fill="both", expand=True, padx=3, pady=3)
                
                # Question text
                question = tk.Label(
                    question_frame, 
                    text=values[j], 
                    wraplength=1000, 
                    justify=tk.LEFT, 
                    font=("Arial", 12),
                    bg="white",
                    fg=COLORS["text"],
                    anchor="w"
                )
                question.pack(fill="x", expand=True, anchor="w")
                
                # Answer options frame
                answer_frame = tk.Frame(question_frame, bg="white", pady=10)
                answer_frame.pack(fill="x")
                
                # Store containers for this question
                question_containers = []
                
                # Create answer options
                options = [
                    ("Y", "Yes"),
                    ("Y(C)", "Yes (Compensating)"),
                    ("N", "No")
                ]
                
                for k, (option_text, option_desc) in enumerate(options):
                    option_frame = tk.Frame(answer_frame, bg="white", padx=5)
                    option_frame.pack(side="left", padx=10)
                    
                    # Create a container for the option
                    radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                    radio_container.pack(fill="both", expand=True)
                    question_containers.append(radio_container)
                    
                    # Add the option text
                    option_label = tk.Label(
                        radio_container,
                        text=option_text,
                        font=("Arial", 12, "bold"),
                        bg="white",
                        fg=COLORS["text"],
                        padx=10,
                        pady=5
                    )
                    option_label.pack()
                    
                    # Add a tooltip frame that shows on hover
                    tooltip_frame = tk.Frame(radio_container, bg=COLORS["bg"], padx=5, pady=2)
                    tooltip_label = tk.Label(
                        tooltip_frame,
                        text=option_desc,
                        font=("Arial", 9),
                        bg=COLORS["bg"],
                        fg=COLORS["text"]
                    )
                    tooltip_label.pack()
                    
                    # Add a hidden radio button for tracking the selection
                    radio_var = self.values[question_index]
                    
                    # First part of the value references the answer (1 = yes | 2 = yes compensating | 3 = no)
                    # Second part of the value references the maturity level (1-5)
                    maturity_num = int(key[-1])
                    option_value = (k + 1) * 10 + maturity_num
                    
                    radio_btn = tk.Radiobutton(
                        radio_container, 
                        variable=radio_var, 
                        value=option_value,
                        bg="white",
                        activebackground="white",
                        highlightthickness=0,
                        bd=0,
                        padx=0,
                        pady=0
                    )
                    
                    # If this option is selected, update the container appearance
                    if radio_var.get() == option_value:
                        radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        option_label.config(bg=COLORS["bg"])
                        self.selected_containers[question_index] = radio_container
                    
                    # Make the entire container clickable
                    def make_click_handler(radio_btn, container, question_idx, containers, card_shadow):
                        def on_click(event):
                            # First reset all containers for this question
                            for c in containers:
                                c.config(relief="raised", bd=1, bg="white")
                                for widget in c.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            
                            # Then update the selected container
                            radio_btn.select()
                            container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if isinstance(widget, tk.Label):
                                    widget.config(bg=COLORS["bg"])
                            
                            # Update the selected container reference
                            self.selected_containers[question_idx] = container
                            
                            # Update the question card shadow color
                            card_shadow.config(bg=COLORS["primary"])
                        return on_click
                    
                    # Bind click events to all elements
                    radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    option_label.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    
                    # Add hover effect
                    def make_hover_handler(container, tooltip):
                        def on_hover(event):
                            if container != self.selected_containers[question_index]:  # Only apply hover to non-selected containers
                                container.config(bg=COLORS["bg"])
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg=COLORS["bg"])
                            tooltip.pack()
                        return on_hover
                    
                    def make_leave_handler(container, tooltip):
                        def on_leave(event):
                            if container != self.selected_containers[question_index]:  # Only revert hover on non-selected containers
                                container.config(bg="white")
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            tooltip.pack_forget()
                        return on_leave
                    
                    radio_container.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    radio_container.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    option_label.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    option_label.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    
                    # Initially hide the tooltip
                    tooltip_frame.pack_forget()
                
                question_index += 1


""" This class is responsible for the layout of the Cybersecurity Maturity's Domain 1 - Resources page """
class CSM_Domain1_Resources_Page(tk.Frame):
    values = []
    selected_containers = [] # holds references to the currently selected containers

    # Initialize the values list with enough elements if it's empty
    @classmethod
    def initialize_values(cls):
        if not cls.values:
            total_questions = sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources])
            for _ in range(total_questions):
                cls.values.append(tk.IntVar())

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Resources")
        self.config(bg=COLORS["bg"])
        
        # Initialize values list if needed
        self.initialize_values()

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        # Header with title and navigation
        header_container = tk.Frame(top_frame, bg="white", padx=20, pady=15)
        header_container.pack(fill="x")
        
        # Title and back button
        title_frame = tk.Frame(header_container, bg="white")
        title_frame.pack(side="left")
        
        back_button = tk.Button(
            title_frame, 
            text="← Back",
            font=("Arial", 12),
            bg="white", 
            fg=COLORS["primary"],
            activebackground=COLORS["bg"], 
            activeforeground=COLORS["primary"],
            relief="flat", 
            bd=0, 
            padx=5, 
            pady=0, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Resources",
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # Home button
        home_button = tk.Button(
            header_container, 
            text="HOME", 
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
            command=lambda: master.switch_frame(home.Home_Page)
        )
        home_button.pack(side="right")
        
        # Progress indicator
        total_questions = sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources])
        answered_questions = csm.submit_pressed(self.values)[3]
        progress_text = f"{answered_questions}/{total_questions} Answered"
        progress_label = tk.Label(
            header_container,
            text=progress_text,
            font=("Arial", 12),
            bg="white",
            fg=COLORS["text"]
        )
        progress_label.pack(side="right", padx=15)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        button_container = tk.Frame(bottom_frame, bg="white", padx=20, pady=15)
        button_container.pack(fill="x")
        
        # Help text
        help_label = tk.Label(
            button_container,
            text="Select an answer for each question",
            font=("Arial", 11, "italic"),
            bg="white",
            fg=COLORS["light_text"]
        )
        help_label.pack(side="left")
        
        # Action buttons
        clear_button = tk.Button(
            button_container, 
            text='CLEAR ANSWERS', 
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
            command=lambda: csm.clear_category(self.values, self.selected_containers)
        )
        clear_button.pack(side="right", padx=5)
        
        submit_button = tk.Button(
            button_container, 
            text='SAVE & CONTINUE', 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["primary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        submit_button.pack(side="right", padx=5)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self, bg="white")
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, bg="white")

        # defines the scrolling distance when mousewheel is used
        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white", padx=20, pady=20)
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Initialize selected_containers list if needed
        total_questions = sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources])
        if len(self.selected_containers) < total_questions:
            for _ in range(total_questions - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        question_index = 0
        for key, values in DATA.CSM_Domain1_Resources.items():
            for j in range(len(values)):
                # Add to values list if not already there
                if question_index >= len(self.values):
                    self.values.append(tk.IntVar())
                
                # Question card with shadow effect
                card_shadow = tk.Frame(middle_frame, bg="#dddddd")
                card_shadow.pack(fill="x", pady=10, padx=1)
                
                # Determine shadow color based on answer
                selected_value = self.values[question_index].get()
                if selected_value == 0:
                    shadow_color = "#dddddd"  # Not answered
                else:
                    shadow_color = COLORS["primary"]  # Answered
                
                # Update the shadow color
                card_shadow.config(bg=shadow_color)
                
                # Create the question frame
                question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
                question_frame.pack(fill="both", expand=True, padx=3, pady=3)
                
                # Question text
                question = tk.Label(
                    question_frame, 
                    text=values[j], 
                    wraplength=1000, 
                    justify=tk.LEFT, 
                    font=("Arial", 12),
                    bg="white",
                    fg=COLORS["text"],
                    anchor="w"
                )
                question.pack(fill="x", expand=True, anchor="w")
                
                # Answer options frame
                answer_frame = tk.Frame(question_frame, bg="white", pady=10)
                answer_frame.pack(fill="x")
                
                # Store containers for this question
                question_containers = []
                
                # Create answer options
                options = [
                    ("Y", "Yes"),
                    ("Y(C)", "Yes (Compensating)"),
                    ("N", "No")
                ]
                
                for k, (option_text, option_desc) in enumerate(options):
                    option_frame = tk.Frame(answer_frame, bg="white", padx=5)
                    option_frame.pack(side="left", padx=10)
                    
                    # Create a container for the option
                    radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                    radio_container.pack(fill="both", expand=True)
                    question_containers.append(radio_container)
                    
                    # Add the option text
                    option_label = tk.Label(
                        radio_container,
                        text=option_text,
                        font=("Arial", 12, "bold"),
                        bg="white",
                        fg=COLORS["text"],
                        padx=10,
                        pady=5
                    )
                    option_label.pack()
                    
                    # Add a tooltip frame that shows on hover
                    tooltip_frame = tk.Frame(radio_container, bg=COLORS["bg"], padx=5, pady=2)
                    tooltip_label = tk.Label(
                        tooltip_frame,
                        text=option_desc,
                        font=("Arial", 9),
                        bg=COLORS["bg"],
                        fg=COLORS["text"]
                    )
                    tooltip_label.pack()
                    
                    # Add a hidden radio button for tracking the selection
                    radio_var = self.values[question_index]
                    
                    # First part of the value references the answer (1 = yes | 2 = yes compensating | 3 = no)
                    # Second part of the value references the maturity level (1-5)
                    maturity_num = int(key[-1])
                    option_value = (k + 1) * 10 + maturity_num
                    
                    radio_btn = tk.Radiobutton(
                        radio_container, 
                        variable=radio_var, 
                        value=option_value,
                        bg="white",
                        activebackground="white",
                        highlightthickness=0,
                        bd=0,
                        padx=0,
                        pady=0
                    )
                    
                    # If this option is selected, update the container appearance
                    if radio_var.get() == option_value:
                        radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        option_label.config(bg=COLORS["bg"])
                        self.selected_containers[question_index] = radio_container
                    
                    # Make the entire container clickable
                    def make_click_handler(radio_btn, container, question_idx, containers, card_shadow):
                        def on_click(event):
                            # First reset all containers for this question
                            for c in containers:
                                c.config(relief="raised", bd=1, bg="white")
                                for widget in c.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            
                            # Then update the selected container
                            radio_btn.select()
                            container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if isinstance(widget, tk.Label):
                                    widget.config(bg=COLORS["bg"])
                            
                            # Update the selected container reference
                            self.selected_containers[question_idx] = container
                            
                            # Update the question card shadow color
                            card_shadow.config(bg=COLORS["primary"])
                        return on_click
                    
                    # Bind click events to all elements
                    radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    option_label.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    
                    # Add hover effect
                    def make_hover_handler(container, tooltip):
                        def on_hover(event):
                            if container != self.selected_containers[question_index]:  # Only apply hover to non-selected containers
                                container.config(bg=COLORS["bg"])
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg=COLORS["bg"])
                            tooltip.pack()
                        return on_hover
                    
                    def make_leave_handler(container, tooltip):
                        def on_leave(event):
                            if container != self.selected_containers[question_index]:  # Only revert hover on non-selected containers
                                container.config(bg="white")
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            tooltip.pack_forget()
                        return on_leave
                    
                    radio_container.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    radio_container.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    option_label.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    option_label.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    
                    # Initially hide the tooltip
                    tooltip_frame.pack_forget()
                
                question_index += 1


""" This class is responsible for the layout of the Cybersecurity Maturity's Domain 1 - Training and Culture page """
class CSM_Domain1_TrainingAndCulture_Page(tk.Frame):
    values = []
    selected_containers = [] # holds references to the currently selected containers

    # Initialize the values list with enough elements if it's empty
    @classmethod
    def initialize_values(cls):
        if not cls.values:
            total_questions = sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture])
            for _ in range(total_questions):
                cls.values.append(tk.IntVar())

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Training and Culture")
        self.config(bg=COLORS["bg"])
        
        # Initialize values list if needed
        self.initialize_values()

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        # Header with title and navigation
        header_container = tk.Frame(top_frame, bg="white", padx=20, pady=15)
        header_container.pack(fill="x")
        
        # Title and back button
        title_frame = tk.Frame(header_container, bg="white")
        title_frame.pack(side="left")
        
        back_button = tk.Button(
            title_frame, 
            text="← Back",
            font=("Arial", 12),
            bg="white", 
            fg=COLORS["primary"],
            activebackground=COLORS["bg"], 
            activeforeground=COLORS["primary"],
            relief="flat", 
            bd=0, 
            padx=5, 
            pady=0, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Training and Culture",
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # Home button
        home_button = tk.Button(
            header_container, 
            text="HOME", 
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
            command=lambda: master.switch_frame(home.Home_Page)
        )
        home_button.pack(side="right")
        
        # Progress indicator
        total_questions = sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture])
        answered_questions = csm.submit_pressed(self.values)[3]
        progress_text = f"{answered_questions}/{total_questions} Answered"
        progress_label = tk.Label(
            header_container,
            text=progress_text,
            font=("Arial", 12),
            bg="white",
            fg=COLORS["text"]
        )
        progress_label.pack(side="right", padx=15)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="white", relief='flat', borderwidth=1)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        button_container = tk.Frame(bottom_frame, bg="white", padx=20, pady=15)
        button_container.pack(fill="x")
        
        # Help text
        help_label = tk.Label(
            button_container,
            text="Select an answer for each question",
            font=("Arial", 11, "italic"),
            bg="white",
            fg=COLORS["light_text"]
        )
        help_label.pack(side="left")
        
        # Action buttons
        clear_button = tk.Button(
            button_container, 
            text='CLEAR ANSWERS', 
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
            command=lambda: csm.clear_category(self.values, self.selected_containers)
        )
        clear_button.pack(side="right", padx=5)
        
        submit_button = tk.Button(
            button_container, 
            text='SAVE & CONTINUE', 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["primary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=15, 
            pady=8, 
            cursor="hand2",
            command=lambda: master.switch_frame(CSM_Domain1_Page)
        )
        submit_button.pack(side="right", padx=5)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self, bg="white")
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, bg="white")

        # defines the scrolling distance when mousewheel is used
        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white", padx=20, pady=20)
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Initialize selected_containers list if needed
        total_questions = sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture])
        if len(self.selected_containers) < total_questions:
            for _ in range(total_questions - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        question_index = 0
        for key, values in DATA.CSM_Domain1_TrainingAndCulture.items():
            for j in range(len(values)):
                # Add to values list if not already there
                if question_index >= len(self.values):
                    self.values.append(tk.IntVar())
                
                # Question card with shadow effect
                card_shadow = tk.Frame(middle_frame, bg="#dddddd")
                card_shadow.pack(fill="x", pady=10, padx=1)
                
                # Determine shadow color based on answer
                selected_value = self.values[question_index].get()
                if selected_value == 0:
                    shadow_color = "#dddddd"  # Not answered
                else:
                    shadow_color = COLORS["primary"]  # Answered
                
                # Update the shadow color
                card_shadow.config(bg=shadow_color)
                
                # Create the question frame
                question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
                question_frame.pack(fill="both", expand=True, padx=3, pady=3)
                
                # Question text
                question = tk.Label(
                    question_frame, 
                    text=values[j], 
                    wraplength=1000, 
                    justify=tk.LEFT, 
                    font=("Arial", 12),
                    bg="white",
                    fg=COLORS["text"],
                    anchor="w"
                )
                question.pack(fill="x", expand=True, anchor="w")
                
                # Answer options frame
                answer_frame = tk.Frame(question_frame, bg="white", pady=10)
                answer_frame.pack(fill="x")
                
                # Store containers for this question
                question_containers = []
                
                # Create answer options
                options = [
                    ("Y", "Yes"),
                    ("Y(C)", "Yes (Compensating)"),
                    ("N", "No")
                ]
                
                for k, (option_text, option_desc) in enumerate(options):
                    option_frame = tk.Frame(answer_frame, bg="white", padx=5)
                    option_frame.pack(side="left", padx=10)
                    
                    # Create a container for the option
                    radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                    radio_container.pack(fill="both", expand=True)
                    question_containers.append(radio_container)
                    
                    # Add the option text
                    option_label = tk.Label(
                        radio_container,
                        text=option_text,
                        font=("Arial", 12, "bold"),
                        bg="white",
                        fg=COLORS["text"],
                        padx=10,
                        pady=5
                    )
                    option_label.pack()
                    
                    # Add a tooltip frame that shows on hover
                    tooltip_frame = tk.Frame(radio_container, bg=COLORS["bg"], padx=5, pady=2)
                    tooltip_label = tk.Label(
                        tooltip_frame,
                        text=option_desc,
                        font=("Arial", 9),
                        bg=COLORS["bg"],
                        fg=COLORS["text"]
                    )
                    tooltip_label.pack()
                    
                    # Add a hidden radio button for tracking the selection
                    radio_var = self.values[question_index]
                    
                    # First part of the value references the answer (1 = yes | 2 = yes compensating | 3 = no)
                    # Second part of the value references the maturity level (1-5)
                    maturity_num = int(key[-1])
                    option_value = (k + 1) * 10 + maturity_num
                    
                    radio_btn = tk.Radiobutton(
                        radio_container, 
                        variable=radio_var, 
                        value=option_value,
                        bg="white",
                        activebackground="white",
                        highlightthickness=0,
                        bd=0,
                        padx=0,
                        pady=0
                    )
                    
                    # If this option is selected, update the container appearance
                    if radio_var.get() == option_value:
                        radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        option_label.config(bg=COLORS["bg"])
                        self.selected_containers[question_index] = radio_container
                    
                    # Make the entire container clickable
                    def make_click_handler(radio_btn, container, question_idx, containers, card_shadow):
                        def on_click(event):
                            # First reset all containers for this question
                            for c in containers:
                                c.config(relief="raised", bd=1, bg="white")
                                for widget in c.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            
                            # Then update the selected container
                            radio_btn.select()
                            container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if isinstance(widget, tk.Label):
                                    widget.config(bg=COLORS["bg"])
                            
                            # Update the selected container reference
                            self.selected_containers[question_idx] = container
                            
                            # Update the question card shadow color
                            card_shadow.config(bg=COLORS["primary"])
                        return on_click
                    
                    # Bind click events to all elements
                    radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    option_label.bind("<Button-1>", make_click_handler(radio_btn, radio_container, question_index, question_containers, card_shadow))
                    
                    # Add hover effect
                    def make_hover_handler(container, tooltip):
                        def on_hover(event):
                            if container != self.selected_containers[question_index]:  # Only apply hover to non-selected containers
                                container.config(bg=COLORS["bg"])
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg=COLORS["bg"])
                            tooltip.pack()
                        return on_hover
                    
                    def make_leave_handler(container, tooltip):
                        def on_leave(event):
                            if container != self.selected_containers[question_index]:  # Only revert hover on non-selected containers
                                container.config(bg="white")
                                for widget in container.winfo_children():
                                    if isinstance(widget, tk.Label):
                                        widget.config(bg="white")
                            tooltip.pack_forget()
                        return on_leave
                    
                    radio_container.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    radio_container.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    option_label.bind("<Enter>", make_hover_handler(radio_container, tooltip_frame))
                    option_label.bind("<Leave>", make_leave_handler(radio_container, tooltip_frame))
                    
                    # Initially hide the tooltip
                    tooltip_frame.pack_forget()
                
                question_index += 1
