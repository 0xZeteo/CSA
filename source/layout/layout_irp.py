""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE INHERENT RISK PROFILE """

import layout.layout_home as home
import layout.layout_login as login
import DATA
import db

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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

# Define risk level colors
RISK_COLORS = {
    "least": "#4CAF50",       # Green for least risk
    "minimal": "#8BC34A",     # Light green for minimal risk
    "moderate": "#FFC107",    # Yellow for moderate risk
    "significant": "#FF9800", # Orange for significant risk
    "most": "#F44336"         # Red for most risk
}

""" This class is responsible for the layout of the Inherent Risk Profile's Main page
Contains the 5 categories and links to each one """
class IRP_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Inherent Risk Profile")   # window title

        self.config(bg=COLORS["bg"])       # frame background
        self.unbind_all("<MouseWheel>")     # unbind mousewheel

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
            text="Inherent Risk Profile Assessment",
            font=("Arial", 24, "bold"),
            bg=COLORS["bg"],
            fg=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # Subtitle
        subtitle_frame = tk.Frame(main_container, bg=COLORS["bg"])
        subtitle_frame.pack(fill="x", pady=(0, 20))
        
        subtitle_label = tk.Label(
            subtitle_frame,
            text="Select a category to begin your assessment",
            font=("Arial", 12),
            bg=COLORS["bg"],
            fg=COLORS["text"]
        )
        subtitle_label.pack(side="left", padx=(65, 0))
        
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

        # Third row - 1 card centered
        row3_frame = tk.Frame(categories_frame, bg="white")
        row3_frame.pack(fill="x", pady=5)

        # Center column in third row
        col5_frame = tk.Frame(row3_frame, bg="white")
        col5_frame.pack(fill="both", expand=True, padx=100)  # Add padding to make it appear centered

        # Create category cards with integrated question count
        self.create_category_card(
            col1_frame, 
            "Technologies and Connection Types", 
            calculate_total_per_category(IRP_Cat1_Page.values)[5],
            len(DATA.IRP_Category1),
            lambda: master.switch_frame(IRP_Cat1_Page)
        )

        self.create_category_card(
            col2_frame, 
            "Delivery Channels", 
            calculate_total_per_category(IRP_Cat2_Page.values)[5],
            len(DATA.IRP_Category2),
            lambda: master.switch_frame(IRP_Cat2_Page)
        )

        self.create_category_card(
            col3_frame, 
            "Online/Mobile Products and Technology Services", 
            calculate_total_per_category(IRP_Cat3_Page.values)[5],
            len(DATA.IRP_Category3),
            lambda: master.switch_frame(IRP_Cat3_Page)
        )

        self.create_category_card(
            col4_frame, 
            "Organizational Characteristics", 
            calculate_total_per_category(IRP_Cat4_Page.values)[5],
            len(DATA.IRP_Category4),
            lambda: master.switch_frame(IRP_Cat4_Page)
        )

        self.create_category_card(
            col5_frame, 
            "External Threats", 
            calculate_total_per_category(IRP_Cat5_Page.values)[5],
            len(DATA.IRP_Category5),
            lambda: master.switch_frame(IRP_Cat5_Page)
        )
        
        # Action buttons in a styled container
        button_container = tk.Frame(main_container, bg=COLORS["bg"], pady=20)
        button_container.pack(fill="x")
        
        button_frame = tk.Frame(button_container, bg=COLORS["bg"])
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
        
        reset_button = tk.Button(
            button_frame, 
            text='RESET', 
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
            command=lambda: IRP_Page.reset_switch_irp(master)
        )
        reset_button.pack(side="left", padx=5)
        
        # Add hover effect
        def reset_enter(e):
            reset_button['bg'] = COLORS["entry_bg"]
        
        def reset_leave(e):
            reset_button['bg'] = COLORS["bg"]
        
        reset_button.bind("<Enter>", reset_enter)
        reset_button.bind("<Leave>", reset_leave)
        
        final_score_button = tk.Button(
            button_frame, 
            text="FINAL SCORE", 
            font=("Arial", 12, "bold"),
            bg=COLORS["primary"], 
            fg="white",
            activebackground=COLORS["primary_light"], 
            activeforeground="white",
            relief="flat", 
            bd=0, 
            padx=20, 
            pady=10, 
            cursor="hand2",
            command=lambda: master.switch_frame(IRP_Final), 
            state="disabled"
        )
        final_score_button.pack(side="right", padx=5)

        # adds a tooltip to the final score button
        ToolTip(widget=final_score_button, text="Answer all the questions to proceed")

        # if all the questions are answered, then enable the final score button
        if (calculate_total()[0] + calculate_total()[1] + calculate_total()[2] + calculate_total()[3] + calculate_total()[4] == len(DATA.IRP_Category1) + len(DATA.IRP_Category2) + len(DATA.IRP_Category3) + len(DATA.IRP_Category4) + len(DATA.IRP_Category5)):
            final_score_button['state'] = "normal"
            
            # Add hover effect when enabled
            def final_enter(e):
                if final_score_button['state'] == 'normal':
                    final_score_button['bg'] = COLORS["primary_light"]
            
            def final_leave(e):
                if final_score_button['state'] == 'normal':
                    final_score_button['bg'] = COLORS["primary"]
            
            final_score_button.bind("<Enter>", final_enter)
            final_score_button.bind("<Leave>", final_leave)

    def create_category_card(self, parent, text, answered, total, command):
        """Create a styled card for categories with question count"""
        # Card with shadow effect - using a deeper shadow for better appearance
        card_shadow = tk.Frame(parent, bg="#bbbbbb")
        card_shadow.pack(fill="x", pady=5, padx=1)
        
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
            font=("Arial", 14, "bold"),
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
            text=f"Questions answered: {answered}/{total}",
            font=("Arial", 10),
            bg=COLORS["card_bg"],
            fg=COLORS["text"],
            anchor="w"
        )
        count_label.pack(side="left", padx=(20, 0))
        
        # Progress bar with improved dynamic updating
        progress_frame = tk.Frame(info_frame, bg=COLORS["card_bg"], pady=5)
        progress_frame.pack(fill="x")
        
        progress_bg = tk.Frame(progress_frame, bg=COLORS["entry_bg"], height=8)
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
                    progress_fg = tk.Frame(bg_frame, bg=fg_color, height=8, width=progress_width)
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
            text="Start Assessment",
            font=("Arial", 10, "bold"),
            bg=COLORS["primary"],
            fg="white",
            activebackground=COLORS["primary_light"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=10,
            pady=5,
            cursor="hand2",
            command=command
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

    # confirmation window which resets the IRP answers if the user clicks ok
    def reset_switch_irp(frame):
        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your answers?')
        if confirm:
            reset_irp()
            frame.switch_frame(IRP_Page)    # switch frame to IRP_Page


""" Inherent Risk Profile - Category 1 (Technologies and Connection Types) 
Responsible for the layout of Category 1 displaying all the questions and possible answers """
class IRP_Cat1_Page(tk.Frame):
    values = [] # holds references to the values in the radio buttons (possible answers to each question)
    selected_containers = [] # holds references to the currently selected containers

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Technologies and Connection Types")

        self.config(bg=COLORS["bg"])

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
            command=lambda: master.switch_frame(IRP_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Technologies and Connection Types",
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
        progress_text = f"{calculate_total_per_category(self.values)[5]}/{len(DATA.IRP_Category1)} Answered"
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
            text="Select a risk level for each question",
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
            command=lambda: clear_category(self.values, self.selected_containers)
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
            command=lambda: master.switch_frame(IRP_Page)
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

        # Risk level legend
        legend_frame = tk.Frame(middle_frame, bg="white", pady=10)
        legend_frame.pack(fill="x")
        
        legend_title = tk.Label(
            legend_frame,
            text="Risk Levels:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg=COLORS["text"]
        )
        legend_title.pack(side="left", padx=(0, 15))
        
        risk_levels = [
            ("Least", RISK_COLORS["least"]),
            ("Minimal", RISK_COLORS["minimal"]),
            ("Moderate", RISK_COLORS["moderate"]),
            ("Significant", RISK_COLORS["significant"]),
            ("Most", RISK_COLORS["most"])
        ]
        
        for level, color in risk_levels:
            level_frame = tk.Frame(legend_frame, bg="white")
            level_frame.pack(side="left", padx=10)
            
            color_indicator = tk.Frame(level_frame, bg=color, width=12, height=12)
            color_indicator.pack(side="left", padx=(0, 5))
            
            level_label = tk.Label(
                level_frame,
                text=level,
                font=("Arial", 10),
                bg="white",
                fg=COLORS["text"]
            )
            level_label.pack(side="left")

        # Initialize selected_containers list if needed
        if len(self.selected_containers) < len(DATA.IRP_Category1):
            for _ in range(len(DATA.IRP_Category1) - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        for i, (key, value) in enumerate(DATA.IRP_Category1.items()):
            # Add to values list if not already there
            if i >= len(self.values):
                self.values.append(tk.IntVar())
                
            # Question card with shadow effect
            card_shadow = tk.Frame(middle_frame, bg="#dddddd")
            card_shadow.pack(fill="x", pady=10, padx=1)
            
            # Determine shadow color based on answer
            selected_value = self.values[i].get()
            if selected_value == 0:
                shadow_color = "#dddddd"  # Not answered
            else:
                risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                                   RISK_COLORS["significant"], RISK_COLORS["most"]]
                shadow_color = risk_colors_list[selected_value - 1]
            
            # Update the shadow color
            card_shadow.config(bg=shadow_color)
            
            # Create the question frame without a border highlight
            question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
            question_frame.pack(fill="both", expand=True, padx=3, pady=3)  # Increased padding for shadow effect
            
            # Question number and text
            question_header = tk.Frame(question_frame, bg="white")
            question_header.pack(fill="x", anchor="w")
            
            question_num = tk.Label(
                question_header,
                text=f"Question {i+1}:",
                font=("Arial", 12, "bold"),
                bg="white",
                fg=COLORS["primary"],
                anchor="w"
            )
            question_num.pack(side="left", padx=(0, 10))
            
            question = tk.Label(
                question_header, 
                text=key, 
                wraplength=800, 
                justify=tk.LEFT, 
                font=("Arial", 12),
                bg="white",
                fg=COLORS["text"],
                anchor="w"
            )
            question.pack(side="left", fill="x", expand=True)
            
            # Radio button options in a horizontal layout
            radio_frame = tk.Frame(question_frame, bg="white", pady=15)
            radio_frame.pack(fill="x")
            
            # Create a grid for the answer options
            risk_levels = ["Least", "Minimal", "Moderate", "Significant", "Most"]
            risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                               RISK_COLORS["significant"], RISK_COLORS["most"]]
            
            # Store containers for this question
            question_containers = []
            
            for j in range(5):
                option_frame = tk.Frame(radio_frame, bg="white", padx=5, pady=5)
                option_frame.grid(row=0, column=j, sticky="nsew")
                radio_frame.grid_columnconfigure(j, weight=1)  # Equal width columns
                
                # Create a container for the option with improved styling
                # Use a raised relief for better visibility
                radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                radio_container.pack(fill="both", expand=True)
                question_containers.append(radio_container)
                
                # Add the risk level header with color
                level_label = tk.Label(
                    radio_container,
                    text=risk_levels[j],
                    font=("Arial", 10, "bold"),
                    bg=risk_colors_list[j],
                    fg="white",
                    padx=5,
                    pady=2
                )
                level_label.pack(fill="x")
                
                # Add the answer text
                answer_text = tk.Label(
                    radio_container,
                    text=value[j],
                    font=("Arial", 10),
                    bg="white",
                    fg=COLORS["text"],
                    wraplength=150,
                    justify="center",
                    padx=5,
                    pady=10
                )
                answer_text.pack(fill="both", expand=True)
                
                # Add a hidden radio button for tracking the selection
                radio_var = self.values[i]
                radio_btn = tk.Radiobutton(
                    radio_container, 
                    variable=radio_var, 
                    value=j+1,
                    bg="white",
                    activebackground="white",
                    highlightthickness=0,
                    bd=0,
                    padx=0,
                    pady=0
                )
                
                # If this option is selected, update the container appearance
                if radio_var.get() == j+1:
                    radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                    answer_text.config(bg=COLORS["bg"])
                    self.selected_containers[i] = radio_container
                
                # Make the entire container clickable with improved shadow effect
                def make_click_handler(radio_btn, container, question_idx, option_idx, containers):
                    def on_click(event):
                        # First reset all containers for this question
                        for c in containers:
                            c.config(relief="raised", bd=1, bg="white")
                            for widget in c.winfo_children():
                                if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                    widget.config(bg="white")
                        
                        # Then update the selected container
                        radio_btn.select()
                        container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        for widget in container.winfo_children():
                            if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                widget.config(bg=COLORS["bg"])
                        
                        # Update the selected container reference
                        self.selected_containers[question_idx] = container
                        
                        # Update the question card shadow color
                        nonlocal card_shadow
                        card_shadow.config(bg=risk_colors_list[option_idx])
                    return on_click
                
                # Bind click events to all elements
                radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                answer_text.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                
                # Add hover effect that preserves the risk level colors
                def make_hover_handler(container, level_label):
                    def on_hover(event):
                        if container != self.selected_containers[i]:  # Only apply hover to non-selected containers
                            container.config(bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg=COLORS["bg"])
                    return on_hover
                
                def make_leave_handler(container, level_label):
                    def on_leave(event):
                        if container != self.selected_containers[i]:  # Only revert hover on non-selected containers
                            container.config(bg="white")
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg="white")
                    return on_leave
                
                radio_container.bind("<Enter>", make_hover_handler(radio_container, level_label))
                radio_container.bind("<Leave>", make_leave_handler(radio_container, level_label))
                answer_text.bind("<Enter>", make_hover_handler(radio_container, level_label))
                answer_text.bind("<Leave>", make_leave_handler(radio_container, level_label))


""" Inherent Risk Profile - Category 2 (Delivery Channels) 
Responsible for the layout of Category 2 """
class IRP_Cat2_Page(tk.Frame):
    values = [] # holds references to the values in the radio buttons (possible answers to each question)
    selected_containers = [] # holds references to the currently selected containers

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Delivery Channels")

        self.config(bg=COLORS["bg"])

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
            command=lambda: master.switch_frame(IRP_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Delivery Channels",
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
        progress_text = f"{calculate_total_per_category(self.values)[5]}/{len(DATA.IRP_Category2)} Answered"
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
            text="Select a risk level for each question",
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
            command=lambda: clear_category(self.values, self.selected_containers)
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
            command=lambda: master.switch_frame(IRP_Page)
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

        # Risk level legend
        legend_frame = tk.Frame(middle_frame, bg="white", pady=10)
        legend_frame.pack(fill="x")
        
        legend_title = tk.Label(
            legend_frame,
            text="Risk Levels:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg=COLORS["text"]
        )
        legend_title.pack(side="left", padx=(0, 15))
        
        risk_levels = [
            ("Least", RISK_COLORS["least"]),
            ("Minimal", RISK_COLORS["minimal"]),
            ("Moderate", RISK_COLORS["moderate"]),
            ("Significant", RISK_COLORS["significant"]),
            ("Most", RISK_COLORS["most"])
        ]
        
        for level, color in risk_levels:
            level_frame = tk.Frame(legend_frame, bg="white")
            level_frame.pack(side="left", padx=10)
            
            color_indicator = tk.Frame(level_frame, bg=color, width=12, height=12)
            color_indicator.pack(side="left", padx=(0, 5))
            
            level_label = tk.Label(
                level_frame,
                text=level,
                font=("Arial", 10),
                bg="white",
                fg=COLORS["text"]
            )
            level_label.pack(side="left")

        # Initialize selected_containers list if needed
        if len(self.selected_containers) < len(DATA.IRP_Category2):
            for _ in range(len(DATA.IRP_Category2) - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        for i, (key, value) in enumerate(DATA.IRP_Category2.items()):
            # Add to values list if not already there
            if i >= len(self.values):
                self.values.append(tk.IntVar())
                
            # Question card with shadow effect
            card_shadow = tk.Frame(middle_frame, bg="#dddddd")
            card_shadow.pack(fill="x", pady=10, padx=1)
            
            # Determine shadow color based on answer
            selected_value = self.values[i].get()
            if selected_value == 0:
                shadow_color = "#dddddd"  # Not answered
            else:
                risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                                   RISK_COLORS["significant"], RISK_COLORS["most"]]
                shadow_color = risk_colors_list[selected_value - 1]
            
            # Update the shadow color
            card_shadow.config(bg=shadow_color)
            
            # Create the question frame without a border highlight
            question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
            question_frame.pack(fill="both", expand=True, padx=3, pady=3)  # Increased padding for shadow effect
            
            # Question number and text
            question_header = tk.Frame(question_frame, bg="white")
            question_header.pack(fill="x", anchor="w")
            
            question_num = tk.Label(
                question_header,
                text=f"Question {i+1}:",
                font=("Arial", 12, "bold"),
                bg="white",
                fg=COLORS["primary"],
                anchor="w"
            )
            question_num.pack(side="left", padx=(0, 10))
            
            question = tk.Label(
                question_header, 
                text=key, 
                wraplength=800, 
                justify=tk.LEFT, 
                font=("Arial", 12),
                bg="white",
                fg=COLORS["text"],
                anchor="w"
            )
            question.pack(side="left", fill="x", expand=True)
            
            # Radio button options in a horizontal layout
            radio_frame = tk.Frame(question_frame, bg="white", pady=15)
            radio_frame.pack(fill="x")
            
            # Create a grid for the answer options
            risk_levels = ["Least", "Minimal", "Moderate", "Significant", "Most"]
            risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                               RISK_COLORS["significant"], RISK_COLORS["most"]]
            
            # Store containers for this question
            question_containers = []
            
            for j in range(5):
                option_frame = tk.Frame(radio_frame, bg="white", padx=5, pady=5)
                option_frame.grid(row=0, column=j, sticky="nsew")
                radio_frame.grid_columnconfigure(j, weight=1)  # Equal width columns
                
                # Create a container for the option with improved styling
                # Use a raised relief for better visibility
                radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                radio_container.pack(fill="both", expand=True)
                question_containers.append(radio_container)
                
                # Add the risk level header with color
                level_label = tk.Label(
                    radio_container,
                    text=risk_levels[j],
                    font=("Arial", 10, "bold"),
                    bg=risk_colors_list[j],
                    fg="white",
                    padx=5,
                    pady=2
                )
                level_label.pack(fill="x")
                
                # Add the answer text
                answer_text = tk.Label(
                    radio_container,
                    text=value[j],
                    font=("Arial", 10),
                    bg="white",
                    fg=COLORS["text"],
                    wraplength=150,
                    justify="center",
                    padx=5,
                    pady=10
                )
                answer_text.pack(fill="both", expand=True)
                
                # Add a hidden radio button for tracking the selection
                radio_var = self.values[i]
                radio_btn = tk.Radiobutton(
                    radio_container, 
                    variable=radio_var, 
                    value=j+1,
                    bg="white",
                    activebackground="white",
                    highlightthickness=0,
                    bd=0,
                    padx=0,
                    pady=0
                )
                
                # If this option is selected, update the container appearance
                if radio_var.get() == j+1:
                    radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                    answer_text.config(bg=COLORS["bg"])
                    self.selected_containers[i] = radio_container
                
                # Make the entire container clickable with improved shadow effect
                def make_click_handler(radio_btn, container, question_idx, option_idx, containers):
                    def on_click(event):
                        # First reset all containers for this question
                        for c in containers:
                            c.config(relief="raised", bd=1, bg="white")
                            for widget in c.winfo_children():
                                if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                    widget.config(bg="white")
                        
                        # Then update the selected container
                        radio_btn.select()
                        container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        for widget in container.winfo_children():
                            if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                widget.config(bg=COLORS["bg"])
                        
                        # Update the selected container reference
                        self.selected_containers[question_idx] = container
                        
                        # Update the question card shadow color
                        nonlocal card_shadow
                        card_shadow.config(bg=risk_colors_list[option_idx])
                    return on_click
                
                # Bind click events to all elements
                radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                answer_text.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                
                # Add hover effect that preserves the risk level colors
                def make_hover_handler(container, level_label):
                    def on_hover(event):
                        if container != self.selected_containers[i]:  # Only apply hover to non-selected containers
                            container.config(bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg=COLORS["bg"])
                    return on_hover
                
                def make_leave_handler(container, level_label):
                    def on_leave(event):
                        if container != self.selected_containers[i]:  # Only revert hover on non-selected containers
                            container.config(bg="white")
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg="white")
                    return on_leave
                
                radio_container.bind("<Enter>", make_hover_handler(radio_container, level_label))
                radio_container.bind("<Leave>", make_leave_handler(radio_container, level_label))
                answer_text.bind("<Enter>", make_hover_handler(radio_container, level_label))
                answer_text.bind("<Leave>", make_leave_handler(radio_container, level_label))


""" Inherent Risk Profile - Category 3 (Online/Mobile Products and Technology Services) 
Responsible for the layout of Category 3 """
class IRP_Cat3_Page(tk.Frame):
    values = [] # holds references to the values in the radio buttons (possible answers to each question)
    selected_containers = [] # holds references to the currently selected containers

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Online/Mobile Products and Technology Services")

        self.config(bg=COLORS["bg"])

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
            command=lambda: master.switch_frame(IRP_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Online/Mobile Products and Technology Services",
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
        progress_text = f"{calculate_total_per_category(self.values)[5]}/{len(DATA.IRP_Category3)} Answered"
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
            text="Select a risk level for each question",
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
            command=lambda: clear_category(self.values, self.selected_containers)
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
            command=lambda: master.switch_frame(IRP_Page)
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

        # Risk level legend
        legend_frame = tk.Frame(middle_frame, bg="white", pady=10)
        legend_frame.pack(fill="x")
        
        legend_title = tk.Label(
            legend_frame,
            text="Risk Levels:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg=COLORS["text"]
        )
        legend_title.pack(side="left", padx=(0, 15))
        
        risk_levels = [
            ("Least", RISK_COLORS["least"]),
            ("Minimal", RISK_COLORS["minimal"]),
            ("Moderate", RISK_COLORS["moderate"]),
            ("Significant", RISK_COLORS["significant"]),
            ("Most", RISK_COLORS["most"])
        ]
        
        for level, color in risk_levels:
            level_frame = tk.Frame(legend_frame, bg="white")
            level_frame.pack(side="left", padx=10)
            
            color_indicator = tk.Frame(level_frame, bg=color, width=12, height=12)
            color_indicator.pack(side="left", padx=(0, 5))
            
            level_label = tk.Label(
                level_frame,
                text=level,
                font=("Arial", 10),
                bg="white",
                fg=COLORS["text"]
            )
            level_label.pack(side="left")

        # Initialize selected_containers list if needed
        if len(self.selected_containers) < len(DATA.IRP_Category3):
            for _ in range(len(DATA.IRP_Category3) - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        for i, (key, value) in enumerate(DATA.IRP_Category3.items()):
            # Add to values list if not already there
            if i >= len(self.values):
                self.values.append(tk.IntVar())
                
            # Question card with shadow effect
            card_shadow = tk.Frame(middle_frame, bg="#dddddd")
            card_shadow.pack(fill="x", pady=10, padx=1)
            
            # Determine shadow color based on answer
            selected_value = self.values[i].get()
            if selected_value == 0:
                shadow_color = "#dddddd"  # Not answered
            else:
                risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                                   RISK_COLORS["significant"], RISK_COLORS["most"]]
                shadow_color = risk_colors_list[selected_value - 1]
            
            # Update the shadow color
            card_shadow.config(bg=shadow_color)
            
            # Create the question frame without a border highlight
            question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
            question_frame.pack(fill="both", expand=True, padx=3, pady=3)  # Increased padding for shadow effect
            
            # Question number and text
            question_header = tk.Frame(question_frame, bg="white")
            question_header.pack(fill="x", anchor="w")
            
            question_num = tk.Label(
                question_header,
                text=f"Question {i+1}:",
                font=("Arial", 12, "bold"),
                bg="white",
                fg=COLORS["primary"],
                anchor="w"
            )
            question_num.pack(side="left", padx=(0, 10))
            
            question = tk.Label(
                question_header, 
                text=key, 
                wraplength=800, 
                justify=tk.LEFT, 
                font=("Arial", 12),
                bg="white",
                fg=COLORS["text"],
                anchor="w"
            )
            question.pack(side="left", fill="x", expand=True)
            
            # Radio button options in a horizontal layout
            radio_frame = tk.Frame(question_frame, bg="white", pady=15)
            radio_frame.pack(fill="x")
            
            # Create a grid for the answer options
            risk_levels = ["Least", "Minimal", "Moderate", "Significant", "Most"]
            risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                               RISK_COLORS["significant"], RISK_COLORS["most"]]
            
            # Store containers for this question
            question_containers = []
            
            for j in range(5):
                option_frame = tk.Frame(radio_frame, bg="white", padx=5, pady=5)
                option_frame.grid(row=0, column=j, sticky="nsew")
                radio_frame.grid_columnconfigure(j, weight=1)  # Equal width columns
                
                # Create a container for the option with improved styling
                # Use a raised relief for better visibility
                radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                radio_container.pack(fill="both", expand=True)
                question_containers.append(radio_container)
                
                # Add the risk level header with color
                level_label = tk.Label(
                    radio_container,
                    text=risk_levels[j],
                    font=("Arial", 10, "bold"),
                    bg=risk_colors_list[j],
                    fg="white",
                    padx=5,
                    pady=2
                )
                level_label.pack(fill="x")
                
                # Add the answer text
                answer_text = tk.Label(
                    radio_container,
                    text=value[j],
                    font=("Arial", 10),
                    bg="white",
                    fg=COLORS["text"],
                    wraplength=150,
                    justify="center",
                    padx=5,
                    pady=10
                )
                answer_text.pack(fill="both", expand=True)
                
                # Add a hidden radio button for tracking the selection
                radio_var = self.values[i]
                radio_btn = tk.Radiobutton(
                    radio_container, 
                    variable=radio_var, 
                    value=j+1,
                    bg="white",
                    activebackground="white",
                    highlightthickness=0,
                    bd=0,
                    padx=0,
                    pady=0
                )
                
                # If this option is selected, update the container appearance
                if radio_var.get() == j+1:
                    radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                    answer_text.config(bg=COLORS["bg"])
                    self.selected_containers[i] = radio_container
                
                # Make the entire container clickable with improved shadow effect
                def make_click_handler(radio_btn, container, question_idx, option_idx, containers):
                    def on_click(event):
                        # First reset all containers for this question
                        for c in containers:
                            c.config(relief="raised", bd=1, bg="white")
                            for widget in c.winfo_children():
                                if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                    widget.config(bg="white")
                        
                        # Then update the selected container
                        radio_btn.select()
                        container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        for widget in container.winfo_children():
                            if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                    widget.config(bg="white")
                        
                        # Update the selected container reference
                        self.selected_containers[question_idx] = container
                        
                        # Update the question card shadow color
                        nonlocal card_shadow
                        card_shadow.config(bg=risk_colors_list[option_idx])
                    return on_click
                
                # Bind click events to all elements
                radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                answer_text.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                
                # Add hover effect that preserves the risk level colors
                def make_hover_handler(container, level_label):
                    def on_hover(event):
                        if container != self.selected_containers[i]:  # Only apply hover to non-selected containers
                            container.config(bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg=COLORS["bg"])
                    return on_hover
                
                def make_leave_handler(container, level_label):
                    def on_leave(event):
                        if container != self.selected_containers[i]:  # Only revert hover on non-selected containers
                            container.config(bg="white")
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg="white")
                    return on_leave
                
                radio_container.bind("<Enter>", make_hover_handler(radio_container, level_label))
                radio_container.bind("<Leave>", make_leave_handler(radio_container, level_label))
                answer_text.bind("<Enter>", make_hover_handler(radio_container, level_label))
                answer_text.bind("<Leave>", make_leave_handler(radio_container, level_label))


""" Inherent Risk Profile - Category 4 (Organizational Characteristics) 
Responsible for the layout of Category 4 """
class IRP_Cat4_Page(tk.Frame):
    values = [] # holds references to the values in the radio buttons (possible answers to each question)
    selected_containers = [] # holds references to the currently selected containers

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Organizational Characteristics")

        self.config(bg=COLORS["bg"])

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
            command=lambda: master.switch_frame(IRP_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="Organizational Characteristics",
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
        progress_text = f"{calculate_total_per_category(self.values)[5]}/{len(DATA.IRP_Category4)} Answered"
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
            text="Select a risk level for each question",
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
            command=lambda: clear_category(self.values, self.selected_containers)
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
            command=lambda: master.switch_frame(IRP_Page)
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

        # Risk level legend
        legend_frame = tk.Frame(middle_frame, bg="white", pady=10)
        legend_frame.pack(fill="x")
        
        legend_title = tk.Label(
            legend_frame,
            text="Risk Levels:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg=COLORS["text"]
        )
        legend_title.pack(side="left", padx=(0, 15))
        
        risk_levels = [
            ("Least", RISK_COLORS["least"]),
            ("Minimal", RISK_COLORS["minimal"]),
            ("Moderate", RISK_COLORS["moderate"]),
            ("Significant", RISK_COLORS["significant"]),
            ("Most", RISK_COLORS["most"])
        ]
        
        for level, color in risk_levels:
            level_frame = tk.Frame(legend_frame, bg="white")
            level_frame.pack(side="left", padx=10)
            
            color_indicator = tk.Frame(level_frame, bg=color, width=12, height=12)
            color_indicator.pack(side="left", padx=(0, 5))
            
            level_label = tk.Label(
                level_frame,
                text=level,
                font=("Arial", 10),
                bg="white",
                fg=COLORS["text"]
            )
            level_label.pack(side="left")

        # Initialize selected_containers list if needed
        if len(self.selected_containers) < len(DATA.IRP_Category4):
            for _ in range(len(DATA.IRP_Category4) - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        for i, (key, value) in enumerate(DATA.IRP_Category4.items()):
            # Add to values list if not already there
            if i >= len(self.values):
                self.values.append(tk.IntVar())
                
            # Question card with shadow effect
            card_shadow = tk.Frame(middle_frame, bg="#dddddd")
            card_shadow.pack(fill="x", pady=10, padx=1)
            
            # Determine shadow color based on answer
            selected_value = self.values[i].get()
            if selected_value == 0:
                shadow_color = "#dddddd"  # Not answered
            else:
                risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                                   RISK_COLORS["significant"], RISK_COLORS["most"]]
                shadow_color = risk_colors_list[selected_value - 1]
            
            # Update the shadow color
            card_shadow.config(bg=shadow_color)
            
            # Create the question frame without a border highlight
            question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
            question_frame.pack(fill="both", expand=True, padx=3, pady=3)  # Increased padding for shadow effect
            
            # Question number and text
            question_header = tk.Frame(question_frame, bg="white")
            question_header.pack(fill="x", anchor="w")
            
            question_num = tk.Label(
                question_header,
                text=f"Question {i+1}:",
                font=("Arial", 12, "bold"),
                bg="white",
                fg=COLORS["primary"],
                anchor="w"
            )
            question_num.pack(side="left", padx=(0, 10))
            
            question = tk.Label(
                question_header, 
                text=key, 
                wraplength=800, 
                justify=tk.LEFT, 
                font=("Arial", 12),
                bg="white",
                fg=COLORS["text"],
                anchor="w"
            )
            question.pack(side="left", fill="x", expand=True)
            
            # Radio button options in a horizontal layout
            radio_frame = tk.Frame(question_frame, bg="white", pady=15)
            radio_frame.pack(fill="x")
            
            # Create a grid for the answer options
            risk_levels = ["Least", "Minimal", "Moderate", "Significant", "Most"]
            risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                               RISK_COLORS["significant"], RISK_COLORS["most"]]
            
            # Store containers for this question
            question_containers = []
            
            for j in range(5):
                option_frame = tk.Frame(radio_frame, bg="white", padx=5, pady=5)
                option_frame.grid(row=0, column=j, sticky="nsew")
                radio_frame.grid_columnconfigure(j, weight=1)  # Equal width columns
                
                # Create a container for the option with improved styling
                # Use a raised relief for better visibility
                radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                radio_container.pack(fill="both", expand=True)
                question_containers.append(radio_container)
                
                # Add the risk level header with color
                level_label = tk.Label(
                    radio_container,
                    text=risk_levels[j],
                    font=("Arial", 10, "bold"),
                    bg=risk_colors_list[j],
                    fg="white",
                    padx=5,
                    pady=2
                )
                level_label.pack(fill="x")
                
                # Add the answer text
                answer_text = tk.Label(
                    radio_container,
                    text=value[j],
                    font=("Arial", 10),
                    bg="white",
                    fg=COLORS["text"],
                    wraplength=150,
                    justify="center",
                    padx=5,
                    pady=10
                )
                answer_text.pack(fill="both", expand=True)
                
                # Add a hidden radio button for tracking the selection
                radio_var = self.values[i]
                radio_btn = tk.Radiobutton(
                    radio_container, 
                    variable=radio_var, 
                    value=j+1,
                    bg="white",
                    activebackground="white",
                    highlightthickness=0,
                    bd=0,
                    padx=0,
                    pady=0
                )
                
                # If this option is selected, update the container appearance
                if radio_var.get() == j+1:
                    radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                    answer_text.config(bg=COLORS["bg"])
                    self.selected_containers[i] = radio_container
                
                # Make the entire container clickable with improved shadow effect
                def make_click_handler(radio_btn, container, question_idx, option_idx, containers):
                    def on_click(event):
                        # First reset all containers for this question
                        for c in containers:
                            c.config(relief="raised", bd=1, bg="white")
                            for widget in c.winfo_children():
                                if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                    widget.config(bg="white")
                        
                        # Then update the selected container
                        radio_btn.select()
                        container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        for widget in container.winfo_children():
                            if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                widget.config(bg=COLORS["bg"])
                        
                        # Update the selected container reference
                        self.selected_containers[question_idx] = container
                        
                        # Update the question card shadow color
                        nonlocal card_shadow
                        card_shadow.config(bg=risk_colors_list[option_idx])
                    return on_click
                
                # Bind click events to all elements
                radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                answer_text.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                
                # Add hover effect that preserves the risk level colors
                def make_hover_handler(container, level_label):
                    def on_hover(event):
                        if container != self.selected_containers[i]:  # Only apply hover to non-selected containers
                            container.config(bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg=COLORS["bg"])
                    return on_hover
                
                def make_leave_handler(container, level_label):
                    def on_leave(event):
                        if container != self.selected_containers[i]:  # Only revert hover on non-selected containers
                            container.config(bg="white")
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg="white")
                    return on_leave
                
                radio_container.bind("<Enter>", make_hover_handler(radio_container, level_label))
                radio_container.bind("<Leave>", make_leave_handler(radio_container, level_label))
                answer_text.bind("<Enter>", make_hover_handler(radio_container, level_label))
                answer_text.bind("<Leave>", make_leave_handler(radio_container, level_label))


""" Inherent Risk Profile - Category 5 (External Threats) 
Responsible for the layout of Category 5 """
class IRP_Cat5_Page(tk.Frame):
    values = [] # holds references to the values in the radio buttons (possible answers to each question)
    selected_containers = [] # holds references to the currently selected containers

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - External Threats")

        self.config(bg=COLORS["bg"])

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
            command=lambda: master.switch_frame(IRP_Page)
        )
        back_button.pack(side="left", padx=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="External Threats",
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
        progress_text = f"{calculate_total_per_category(self.values)[5]}/{len(DATA.IRP_Category5)} Answered"
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
            text="Select a risk level for each question",
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
            command=lambda: clear_category(self.values, self.selected_containers)
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
            command=lambda: master.switch_frame(IRP_Page)
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

        # Risk level legend
        legend_frame = tk.Frame(middle_frame, bg="white", pady=10)
        legend_frame.pack(fill="x")
        
        legend_title = tk.Label(
            legend_frame,
            text="Risk Levels:",
            font=("Arial", 12, "bold"),
            bg="white",
            fg=COLORS["text"]
        )
        legend_title.pack(side="left", padx=(0, 15))
        
        risk_levels = [
            ("Least", RISK_COLORS["least"]),
            ("Minimal", RISK_COLORS["minimal"]),
            ("Moderate", RISK_COLORS["moderate"]),
            ("Significant", RISK_COLORS["significant"]),
            ("Most", RISK_COLORS["most"])
        ]
        
        for level, color in risk_levels:
            level_frame = tk.Frame(legend_frame, bg="white")
            level_frame.pack(side="left", padx=10)
            
            color_indicator = tk.Frame(level_frame, bg=color, width=12, height=12)
            color_indicator.pack(side="left", padx=(0, 5))
            
            level_label = tk.Label(
                level_frame,
                text=level,
                font=("Arial", 10),
                bg="white",
                fg=COLORS["text"]
            )
            level_label.pack(side="left")

        # Initialize selected_containers list if needed
        if len(self.selected_containers) < len(DATA.IRP_Category5):
            for _ in range(len(DATA.IRP_Category5) - len(self.selected_containers)):
                self.selected_containers.append(None)

        # Get the questions from DATA and align them on screen
        for i, (key, value) in enumerate(DATA.IRP_Category5.items()):
            # Add to values list if not already there
            if i >= len(self.values):
                self.values.append(tk.IntVar())
                
            # Question card with shadow effect
            card_shadow = tk.Frame(middle_frame, bg="#dddddd")
            card_shadow.pack(fill="x", pady=10, padx=1)
            
            # Determine shadow color based on answer
            selected_value = self.values[i].get()
            if selected_value == 0:
                shadow_color = "#dddddd"  # Not answered
            else:
                risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                                   RISK_COLORS["significant"], RISK_COLORS["most"]]
                shadow_color = risk_colors_list[selected_value - 1]
            
            # Update the shadow color
            card_shadow.config(bg=shadow_color)
            
            # Create the question frame without a border highlight
            question_frame = tk.Frame(card_shadow, bg="white", padx=20, pady=15)
            question_frame.pack(fill="both", expand=True, padx=3, pady=3)  # Increased padding for shadow effect
            
            # Question number and text
            question_header = tk.Frame(question_frame, bg="white")
            question_header.pack(fill="x", anchor="w")
            
            question_num = tk.Label(
                question_header,
                text=f"Question {i+1}:",
                font=("Arial", 12, "bold"),
                bg="white",
                fg=COLORS["primary"],
                anchor="w"
            )
            question_num.pack(side="left", padx=(0, 10))
            
            question = tk.Label(
                question_header, 
                text=key, 
                wraplength=800, 
                justify=tk.LEFT, 
                font=("Arial", 12),
                bg="white",
                fg=COLORS["text"],
                anchor="w"
            )
            question.pack(side="left", fill="x", expand=True)
            
            # Radio button options in a horizontal layout
            radio_frame = tk.Frame(question_frame, bg="white", pady=15)
            radio_frame.pack(fill="x")
            
            # Create a grid for the answer options
            risk_levels = ["Least", "Minimal", "Moderate", "Significant", "Most"]
            risk_colors_list = [RISK_COLORS["least"], RISK_COLORS["minimal"], RISK_COLORS["moderate"], 
                               RISK_COLORS["significant"], RISK_COLORS["most"]]
            
            # Store containers for this question
            question_containers = []
            
            for j in range(5):
                option_frame = tk.Frame(radio_frame, bg="white", padx=5, pady=5)
                option_frame.grid(row=0, column=j, sticky="nsew")
                radio_frame.grid_columnconfigure(j, weight=1)  # Equal width columns
                
                # Create a container for the option with improved styling
                # Use a raised relief for better visibility
                radio_container = tk.Frame(option_frame, bg="white", padx=10, pady=5, relief="raised", bd=1)
                radio_container.pack(fill="both", expand=True)
                question_containers.append(radio_container)
                
                # Add the risk level header with color
                level_label = tk.Label(
                    radio_container,
                    text=risk_levels[j],
                    font=("Arial", 10, "bold"),
                    bg=risk_colors_list[j],
                    fg="white",
                    padx=5,
                    pady=2
                )
                level_label.pack(fill="x")
                
                # Add the answer text
                answer_text = tk.Label(
                    radio_container,
                    text=value[j],
                    font=("Arial", 10),
                    bg="white",
                    fg=COLORS["text"],
                    wraplength=150,
                    justify="center",
                    padx=5,
                    pady=10
                )
                answer_text.pack(fill="both", expand=True)
                
                # Add a hidden radio button for tracking the selection
                radio_var = self.values[i]
                radio_btn = tk.Radiobutton(
                    radio_container, 
                    variable=radio_var, 
                    value=j+1,
                    bg="white",
                    activebackground="white",
                    highlightthickness=0,
                    bd=0,
                    padx=0,
                    pady=0
                )
                
                # If this option is selected, update the container appearance
                if radio_var.get() == j+1:
                    radio_container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                    answer_text.config(bg=COLORS["bg"])
                    self.selected_containers[i] = radio_container
                
                # Make the entire container clickable with improved shadow effect
                def make_click_handler(radio_btn, container, question_idx, option_idx, containers):
                    def on_click(event):
                        # First reset all containers for this question
                        for c in containers:
                            c.config(relief="raised", bd=1, bg="white")
                            for widget in c.winfo_children():
                                if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                    widget.config(bg="white")
                        
                        # Then update the selected container
                        radio_btn.select()
                        container.config(relief="sunken", bd=2, bg=COLORS["bg"])
                        for widget in container.winfo_children():
                            if not isinstance(widget, tk.Label) or widget.cget("bg") not in risk_colors_list:
                                widget.config(bg=COLORS["bg"])
                        
                        # Update the selected container reference
                        self.selected_containers[question_idx] = container
                        
                        # Update the question card shadow color
                        nonlocal card_shadow
                        card_shadow.config(bg=risk_colors_list[option_idx])
                    return on_click
                
                # Bind click events to all elements
                radio_container.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                answer_text.bind("<Button-1>", make_click_handler(radio_btn, radio_container, i, j, question_containers))
                
                # Add hover effect that preserves the risk level colors
                def make_hover_handler(container, level_label):
                    def on_hover(event):
                        if container != self.selected_containers[i]:  # Only apply hover to non-selected containers
                            container.config(bg=COLORS["bg"])
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg=COLORS["bg"])
                    return on_hover
                
                def make_leave_handler(container, level_label):
                    def on_leave(event):
                        if container != self.selected_containers[i]:  # Only revert hover on non-selected containers
                            container.config(bg="white")
                            for widget in container.winfo_children():
                                if widget != level_label:  # Don't change the color label
                                    widget.config(bg="white")
                    return on_leave
                
                radio_container.bind("<Enter>", make_hover_handler(radio_container, level_label))
                radio_container.bind("<Leave>", make_leave_handler(radio_container, level_label))
                answer_text.bind("<Enter>", make_hover_handler(radio_container, level_label))
                answer_text.bind("<Leave>", make_leave_handler(radio_container, level_label))


""" Inherent Risk Profile - Score page """
class IRP_Final(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Inherent Risk Profile - Score")
        self.config(bg=COLORS["bg"])

        # Main container with padding
        main_container = tk.Frame(self, bg=COLORS["bg"], padx=40, pady=40)
        main_container.pack(fill="both", expand=True)
        
        # Header with title
        header_frame = tk.Frame(main_container, bg=COLORS["bg"])
        header_frame.pack(fill="x", pady=(0, 30))
        
        title_label = tk.Label(
            header_frame, 
            text="Inherent Risk Profile Results",
            font=("Arial", 24, "bold"),
            bg=COLORS["bg"],
            fg=COLORS["primary"]
        )
        title_label.pack(side="left")
        
        # Button frame
        button_frame = tk.Frame(header_frame, bg=COLORS["bg"])
        button_frame.pack(side="right")
        
        home_button = tk.Button(
            button_frame, 
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
        home_button.pack(side="left", padx=5)
        
        back_button = tk.Button(
            button_frame, 
            text="BACK", 
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
            command=lambda: master.switch_frame(IRP_Page)
        )
        back_button.pack(side="left", padx=5)
        
        # Results card with improved shadow effect
        results_shadow = tk.Frame(main_container, bg="#bbbbbb")
        results_shadow.pack(fill="x", pady=15, padx=1)
        
        results_card = tk.Frame(results_shadow, bg="white", padx=30, pady=30)
        results_card.pack(fill="both", expand=True, padx=3, pady=3)
        
        # Results title
        results_title = tk.Label(
            results_card,
            text="Assessment Results",
            font=("Arial", 18, "bold"),
            bg="white",
            fg=COLORS["primary"]
        )
        results_title.pack(pady=(0, 20))
        
        # Results content
        results_frame = tk.Frame(results_card, bg="white")
        results_frame.pack(fill="x")
        
        # Risk level counts
        risk_levels = [
            ("Least", calculate_total()[0], RISK_COLORS["least"]),
            ("Minimal", calculate_total()[1], RISK_COLORS["minimal"]),
            ("Moderate", calculate_total()[2], RISK_COLORS["moderate"]),
            ("Significant", calculate_total()[3], RISK_COLORS["significant"]),
            ("Most", calculate_total()[4], RISK_COLORS["most"])
        ]
        
        for level, count, color in risk_levels:
            level_frame = tk.Frame(results_frame, bg="white")
            level_frame.pack(fill="x", pady=5)
            
            # Color indicator
            color_indicator = tk.Frame(level_frame, bg=color, width=15, height=15)
            color_indicator.pack(side="left", padx=(0, 10))
            
            level_label = tk.Label(
                level_frame,
                text=f"{level}:",
                font=("Arial", 14, "bold"),
                bg="white",
                fg=COLORS["text"],
                width=12,
                anchor="w"
            )
            level_label.pack(side="left")
            
            count_label = tk.Label(
                level_frame,
                text=f"{count} Point(s)",
                font=("Arial", 14),
                bg="white",
                fg=COLORS["text"]
            )
            count_label.pack(side="left", padx=10)
        
        # Separator
        separator = tk.Frame(results_card, height=2, bg=COLORS["entry_bg"])
        separator.pack(fill="x", pady=20)
        
        # Final score
        final_score_frame = tk.Frame(results_card, bg="white")
        final_score_frame.pack(fill="x", pady=10)
        
        final_score_label = tk.Label(
            final_score_frame,
            text="Risk Level:",
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"],
            width=12,
            anchor="w"
        )
        final_score_label.pack(side="left")
        
        risk_level = IRP_Final.find_max()
        risk_color = RISK_COLORS.get(risk_level.lower(), "#dddddd") if risk_level else "#dddddd"
        
        final_score_value = tk.Label(
            final_score_frame,
            text=risk_level,
            font=("Arial", 16, "bold"),
            bg=risk_color,
            fg="white",
            padx=15,
            pady=5
        )
        final_score_value.pack(side="left", padx=10)
        
        # Save section
        save_frame = tk.Frame(results_card, bg="white", pady=20)
        save_frame.pack(fill="x")
        
        save_label = tk.Label(
            save_frame,
            text="Save Assessment:",
            font=("Arial", 14),
            bg="white",
            fg=COLORS["text"]
        )
        save_label.pack(side="left")
        
        # limit entry to alphanumeric characters only
        def only_alphanumeric(char):
            return char.isalnum()

        alpha_num_validation = self.register(only_alphanumeric)
        
        assessment_name_entry = tk.Entry(
            save_frame, 
            font=("Arial", 12),
            relief='flat',
            bd=1,
            highlightthickness=1,
            highlightbackground=COLORS["entry_bg"],
            bg=COLORS["bg"],
            fg=COLORS["text"],
            width=20,
            validate='key',
            validatecommand=(alpha_num_validation, '%S')
        )
        assessment_name_entry.pack(side="left", padx=10)
        
        # Add tooltip for the assessment name entry field
        ToolTip(widget=assessment_name_entry, text="Enter a unique name for the assessment")
        
        save_button = tk.Button(
            save_frame, 
            text='SAVE', 
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
            command=lambda: IRP_Final.save(master, assessment_name_entry.get())
        )
        save_button.pack(side="left", padx=5)

    # find the risk category with the maximum answers and return it as a String
    def find_max():
        max_value = max(calculate_total())
        indexes = [i for i, j in enumerate(calculate_total()) if j == max_value]
        if max_value == 0:
            return ''
        elif 4 in indexes:
            return 'Most'
        elif 3 in indexes:
            return 'Significant'
        elif 2 in indexes:
            return 'Moderate'
        elif 1 in indexes:
            return 'Minimal'
        elif 0 in indexes:
            return 'Least'

    # handles saving the results to the database with all the validations required
    def save(frame, name):
        name = name.lower()
        get_userInfo_query = """ SELECT uid,company FROM users WHERE username=%s; """
        u_value = [login.Login_Page.logged_in]

        db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA") # open db connection
        uInfo = db.read_query_data(db_connection, get_userInfo_query, u_value)

        insert_irp_query = """ 
        INSERT INTO irp (name, date, user, company, least, minimal, moderate, significant, most, risk_level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); 
        """
        values = [name, datetime.now(), uInfo[0][0], uInfo[0][1], calculate_total()[0], calculate_total()[1], calculate_total()[2], calculate_total()[3], calculate_total()[4], IRP_Final.find_max()]
        
        get_assessment_name_query = """ SELECT name FROM irp WHERE name=%s; """
        name_value = [name]
        assessment_name = db.read_query_data(db_connection, get_assessment_name_query, name_value)

        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to save your results?')

        if confirm:
            if name == "":
                messagebox.showwarning("Warning", "You need to enter a name for the assessment")
            elif assessment_name:
                messagebox.showwarning("Warning", "An assessment with this name already exists")
            else:
                db.execute_query_data(db_connection, insert_irp_query, values)
                reset_irp()
                frame.switch_frame(home.Home_Page)

        db_connection.close()


""" This class handles the display of the tooltip """
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
        tw.wm_overrideredirect(1) # window without border and no normal means of closing
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


# this function resets the answers of all the IRP categories
def reset_irp():
    clear_pressed(IRP_Cat1_Page.values, IRP_Cat1_Page.selected_containers)
    clear_pressed(IRP_Cat2_Page.values, IRP_Cat2_Page.selected_containers)
    clear_pressed(IRP_Cat3_Page.values, IRP_Cat3_Page.selected_containers)
    clear_pressed(IRP_Cat4_Page.values, IRP_Cat4_Page.selected_containers)
    clear_pressed(IRP_Cat5_Page.values, IRP_Cat5_Page.selected_containers)


# this function clears the answers of a category after a confirmation window
def clear_category(values, selected_containers):
    confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your answers?')
    if confirm:
        clear_pressed(values, selected_containers)


""" This function clears the selection of radio buttons and resets container styling
  @arg values = List[] | contains the variable that is a reference to the radio buttons 
  @arg selected_containers = List[] | contains references to the selected containers """
def clear_pressed(values, selected_containers):
    for i in range(len(values)):
        values[i].set(0)
        if i < len(selected_containers) and selected_containers[i] is not None:
            # Reset the container styling
            selected_containers[i].config(relief="raised", bd=1, bg="white")
            for widget in selected_containers[i].winfo_children():
                if not isinstance(widget, tk.Label) or widget.cget("bg") not in [RISK_COLORS["least"], RISK_COLORS["minimal"], 
                                                                               RISK_COLORS["moderate"], RISK_COLORS["significant"], 
                                                                               RISK_COLORS["most"]]:
                    widget.config(bg="white")
            selected_containers[i] = None


""" This function counts the number of answers in each risk level in every category independently
  @arg = List[] | contains the variable that is a reference to the radio buttons """
def calculate_total_per_category(values):
    least = minimal = moderate = significant = most = total_selected = 0
    
    for i in range(len(values)):
        if (values[i].get() == 1):
            least += 1
            total_selected += 1
        elif (values[i].get() == 2):
            minimal += 1
            total_selected += 1
        elif (values[i].get() == 3):
            moderate += 1
            total_selected += 1
        elif (values[i].get() == 4):
            significant += 1
            total_selected += 1
        elif (values[i].get() == 5):
            most += 1
            total_selected += 1

    return [least, minimal, moderate, significant, most, total_selected]


""" This functions calculates the total value of each risk level across all the categories of the Inherent Risk Profile """           
def calculate_total():
    least_total = calculate_total_per_category(IRP_Cat1_Page.values)[0] + calculate_total_per_category(IRP_Cat2_Page.values)[0] + calculate_total_per_category(IRP_Cat3_Page.values)[0] + calculate_total_per_category(IRP_Cat4_Page.values)[0] + calculate_total_per_category(IRP_Cat5_Page.values)[0]
    minimal_total = calculate_total_per_category(IRP_Cat1_Page.values)[1] + calculate_total_per_category(IRP_Cat2_Page.values)[1] + calculate_total_per_category(IRP_Cat3_Page.values)[1] + calculate_total_per_category(IRP_Cat4_Page.values)[1] + calculate_total_per_category(IRP_Cat5_Page.values)[1]
    moderate_total = calculate_total_per_category(IRP_Cat1_Page.values)[2] + calculate_total_per_category(IRP_Cat2_Page.values)[2] + calculate_total_per_category(IRP_Cat3_Page.values)[2] + calculate_total_per_category(IRP_Cat4_Page.values)[2] + calculate_total_per_category(IRP_Cat5_Page.values)[2]
    significant_total = calculate_total_per_category(IRP_Cat1_Page.values)[3] + calculate_total_per_category(IRP_Cat2_Page.values)[3] + calculate_total_per_category(IRP_Cat3_Page.values)[3] + calculate_total_per_category(IRP_Cat4_Page.values)[3] + calculate_total_per_category(IRP_Cat5_Page.values)[3]
    most_total = calculate_total_per_category(IRP_Cat1_Page.values)[4] + calculate_total_per_category(IRP_Cat2_Page.values)[4] + calculate_total_per_category(IRP_Cat3_Page.values)[4] + calculate_total_per_category(IRP_Cat4_Page.values)[4] + calculate_total_per_category(IRP_Cat5_Page.values)[4]

    return [least_total, minimal_total, moderate_total, significant_total, most_total]
