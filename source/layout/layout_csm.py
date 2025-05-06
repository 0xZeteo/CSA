""" Here is the layout of the CSM home page which contains all 5 domains """

import layout.layout_home as home
import layout.layout_login as login
import layout.layout_csm_domain1 as d1
import layout.layout_csm_domain2 as d2
import layout.layout_csm_domain3 as d3
import layout.layout_csm_domain4 as d4
import layout.layout_csm_domain5 as d5
import DATA
import db

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Update the COLORS dictionary to include more vibrant options
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

""" This class is responsible for the layout of the Cybersecurity Maturity's Main page
    Contains all the categories and links to each one """
class CSM_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Cybersecurity Maturity")

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
            text="Cybersecurity Maturity Assessment",
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
            text="Select a domain to begin your assessment",
            font=("Arial", 12),
            bg=COLORS["bg"],
            fg=COLORS["text"]
        )
        subtitle_label.pack(side="left", padx=(65, 0))
        
        # Content area with a subtle border
        content_frame = tk.Frame(main_container, bg=COLORS["bg"], bd=0)
        content_frame.pack(fill="both", expand=True)
        
        # Categories section with a subtle shadow
        categories_shadow = tk.Frame(content_frame, bg="#bbbbbb")
        categories_shadow.pack(fill="both", expand=True, padx=1, pady=1)

        categories_frame = tk.Frame(categories_shadow, bg="white", padx=15, pady=15)
        categories_frame.pack(fill="both", expand=True, padx=2, pady=2)

        # Create a grid layout for the domains
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

        # Create domain cards with integrated question count
        self.create_domain_card(
            col1_frame, 
            "Cyber Risk Management and Oversight", 
            submit_pressed(d1.CSM_Domain1_Governance_Page.values)[3] + 
            submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[3] + 
            submit_pressed(d1.CSM_Domain1_Resources_Page.values)[3] + 
            submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[3],
            sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance]) + 
            sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement]) + 
            sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources]) + 
            sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture]),
            lambda: master.switch_frame(d1.CSM_Domain1_Page)
        )

        self.create_domain_card(
            col2_frame, 
            "Threat Intelligence and Collaboration", 
            submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[3] + 
            submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[3] + 
            submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[3],
            sum([len(DATA.CSM_Domain2_ThreatIntelligence[i]) for i in DATA.CSM_Domain2_ThreatIntelligence]) + 
            sum([len(DATA.CSM_Domain2_MonitoringAndAnalyzing[i]) for i in DATA.CSM_Domain2_MonitoringAndAnalyzing]) + 
            sum([len(DATA.CSM_Domain2_InformationSharing[i]) for i in DATA.CSM_Domain2_InformationSharing]),
            lambda: master.switch_frame(d2.CSM_Domain2_Page)
        )

        self.create_domain_card(
            col3_frame, 
            "Cybersecurity Controls", 
            submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[3] + 
            submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[3] + 
            submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[3],
            sum([len(DATA.CSM_Domain3_PreventiveControls[i]) for i in DATA.CSM_Domain3_PreventiveControls]) + 
            sum([len(DATA.CSM_Domain3_DetectiveControls[i]) for i in DATA.CSM_Domain3_DetectiveControls]) + 
            sum([len(DATA.CSM_Domain3_CorrectiveControls[i]) for i in DATA.CSM_Domain3_CorrectiveControls]),
            lambda: master.switch_frame(d3.CSM_Domain3_Page)
        )

        self.create_domain_card(
            col4_frame, 
            "External Dependency Management", 
            submit_pressed(d4.CSM_Domain4_Connections_Page.values)[3] + 
            submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[3],
            sum([len(DATA.CSM_Domain4_Connections[i]) for i in DATA.CSM_Domain4_Connections]) + 
            sum([len(DATA.CSM_Domain4_RelationshipManagement[i]) for i in DATA.CSM_Domain4_RelationshipManagement]),
            lambda: master.switch_frame(d4.CSM_Domain4_Page)
        )

        self.create_domain_card(
            col5_frame, 
            "Cyber Incident Management and Resilience", 
            submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[3] + 
            submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[3] + 
            submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[3],
            sum([len(DATA.CSM_Domain5_IncidentPlanningAndStrategy[i]) for i in DATA.CSM_Domain5_IncidentPlanningAndStrategy]) + 
            sum([len(DATA.CSM_Domain5_DetectionResponseAndMitigation[i]) for i in DATA.CSM_Domain5_DetectionResponseAndMitigation]) + 
            sum([len(DATA.CSM_Domain5_EscalationAndReporting[i]) for i in DATA.CSM_Domain5_EscalationAndReporting]),
            lambda: master.switch_frame(d5.CSM_Domain5_Page)
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
            command=lambda: CSM_Page.reset_switch_csm(master)
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
            command=lambda: master.switch_frame(CSM_Final), 
            state="disabled"
        )
        final_score_button.pack(side="right", padx=5)

        # adds a tooltip to the final score button
        ToolTip(widget=final_score_button, text="Answer all the questions to proceed")

        # contains all the dictionaries for the CSM in the DATA file
        dicts = [DATA.CSM_Domain1_Governance, DATA.CSM_Domain1_RiskManagement, DATA.CSM_Domain1_Resources, DATA.CSM_Domain1_TrainingAndCulture,
                 DATA.CSM_Domain2_ThreatIntelligence, DATA.CSM_Domain2_MonitoringAndAnalyzing, DATA.CSM_Domain2_InformationSharing,
                 DATA.CSM_Domain3_PreventiveControls, DATA.CSM_Domain3_DetectiveControls, DATA.CSM_Domain3_CorrectiveControls,
                 DATA.CSM_Domain4_Connections, DATA.CSM_Domain4_RelationshipManagement,
                 DATA.CSM_Domain5_IncidentPlanningAndStrategy, DATA.CSM_Domain5_DetectionResponseAndMitigation, DATA.CSM_Domain5_EscalationAndReporting]

        # count the total number of questions
        count = 0
        for i in range(len(dicts)):
            for list in dicts[i].values():
                count += len(list)

        # if all answers are filled, enable the final score button
        if (calculate_total()[0] + calculate_total()[1] + calculate_total()[2] == count):
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

    def create_domain_card(self, parent, text, answered, total, command):
        """Create a styled card for domains with question count"""
        # Card with shadow effect
        card_shadow = tk.Frame(parent, bg="#bbbbbb")
        card_shadow.pack(fill="x", pady=5, padx=1)
        
        # Calculate completion percentage
        completion_pct = (answered / total) * 100 if total > 0 else 0
        
        # Determine card border color based on completion
        border_color = COLORS["primary"] if completion_pct == 100 else (
            COLORS["accent"] if completion_pct > 0 else "#dddddd"
        )
        
        card = tk.Frame(card_shadow, bg=COLORS["card_bg"], padx=15, pady=10)
        card.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Left side - text and count
        info_frame = tk.Frame(card, bg=COLORS["card_bg"])
        info_frame.pack(side="left", fill="both", expand=True)
        
        # Domain name with icon based on completion
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
        
        # Domain name
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
        
        # Progress bar
        progress_frame = tk.Frame(info_frame, bg=COLORS["card_bg"], pady=5)
        progress_frame.pack(fill="x")
        
        progress_bg = tk.Frame(progress_frame, bg=COLORS["entry_bg"], height=8)
        progress_bg.pack(fill="x", padx=20)
        
        if completion_pct > 0:
            progress_fg = tk.Frame(progress_bg, bg=icon_color, height=8, width=int(completion_pct * progress_bg.winfo_reqwidth() / 100))
            progress_fg.place(x=0, y=0)
        
        # Button with hover effect
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

    # resets the answers of all the CSM domains and categories
    def reset_switch_csm(frame):
        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your answers?')
        if confirm:
            reset_csm()
            frame.switch_frame(CSM_Page)


""" This class handles the scoring of the Cybersecurity maturity """
class CSM_Final(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Cybersecurity Maturity - Score")
        self.config(bg=COLORS["bg"])

        # Main container with padding
        main_container = tk.Frame(self, bg=COLORS["bg"], padx=40, pady=40)
        main_container.pack(fill="both", expand=True)
        
        # Header with title
        header_frame = tk.Frame(main_container, bg=COLORS["bg"])
        header_frame.pack(fill="x", pady=(0, 30))
        
        title_label = tk.Label(
            header_frame, 
            text="Cybersecurity Maturity Results",
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
            command=lambda: master.switch_frame(CSM_Page)
        )
        back_button.pack(side="left", padx=5)
        
        # Results card
        results_shadow = tk.Frame(main_container, bg="#dddddd")
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
        
        # Maturity level counts
        maturity_levels = [
            ("Baseline", maturity_total()[0][0], maturity_total()[1][0], maturity_total()[2][0]),
            ("Evolving", maturity_total()[0][1], maturity_total()[1][1], maturity_total()[2][1]),
            ("Intermediate", maturity_total()[0][2], maturity_total()[1][2], maturity_total()[2][2]),
            ("Advanced", maturity_total()[0][3], maturity_total()[1][3], maturity_total()[2][3]),
            ("Innovative", maturity_total()[0][4], maturity_total()[1][4], maturity_total()[2][4])
        ]
        
        for i, (level, yes, compensating, no) in enumerate(maturity_levels):
            level_frame = tk.Frame(results_frame, bg="white")
            level_frame.pack(fill="x", pady=5)
            
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
                text=f"Yes ({yes})  -  Compensating ({compensating})  -  No ({no})",
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
            text="Maturity Level:",
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"],
            width=12,
            anchor="w"
        )
        final_score_label.pack(side="left")
        
        final_score_value = tk.Label(
            final_score_frame,
            text=CSM_Final.find_max(),
            font=("Arial", 16, "bold"),
            bg="white",
            fg=COLORS["primary"]
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
            command=lambda: CSM_Final.save(master, assessment_name_entry.get())
        )
        save_button.pack(side="left", padx=5)

    # finds the total number of answers for all the categories (yes, yes_c, no) and returns the risk maturity level as a String
    def find_max():
        yes_max = max(maturity_total()[0])
        #yes_c_max = max(maturity_total()[1])
        #no_max = max(maturity_total()[2])

        yes_indexes = [i for i, j in enumerate(maturity_total()[0]) if j == yes_max]
        if yes_max == 0:
            return ''
        elif 0 in yes_indexes:
            return 'Baseline'
        elif 1 in yes_indexes:
            return 'Evolving'
        elif 2 in yes_indexes:
            return 'Intermediate'
        elif 3 in yes_indexes:
            return 'Advanced'
        elif 4 in yes_indexes:
            return 'Innovative'

    # handles the validation and querying of the database before saving the CSM results
    def save(frame, name):
        name = name.lower()
        get_userInfo_query = """ SELECT uid,company FROM users WHERE username=%s; """
        u_value = [login.Login_Page.logged_in]

        db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA") # open db connection
        uInfo = db.read_query_data(db_connection, get_userInfo_query, u_value)

        insert_csm_query = """ 
        INSERT INTO csm (name, date, user, company, baseline_yes, baseline_compensating, baseline_no, 
                         evolving_yes, evolving_compensating, evolving_no, intermediate_yes, intermediate_compensating, intermediate_no, 
                         advanced_yes, advanced_compensating, advanced_no, innovative_yes, innovative_compensating, innovative_no, maturity_level) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); 
        """
        values = [name, datetime.now(), uInfo[0][0], uInfo[0][1], maturity_total()[0][0], maturity_total()[1][0], maturity_total()[2][0], 
                  maturity_total()[0][1], maturity_total()[1][1], maturity_total()[2][1], maturity_total()[0][2], maturity_total()[1][2], maturity_total()[2][2], 
                  maturity_total()[0][3], maturity_total()[1][3], maturity_total()[2][3], maturity_total()[0][4], maturity_total()[1][4], maturity_total()[2][4], 
                  CSM_Final.find_max()]

        get_assessment_name_query = """ SELECT name FROM csm WHERE name=%s; """
        name_value = [name]
        assessment_name = db.read_query_data(db_connection, get_assessment_name_query, name_value)

        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to save your results?')

        if confirm:
            if name == "":
                messagebox.showwarning("Warning", "You need to enter a name for the assessment")
            elif assessment_name:
                messagebox.showwarning("Warning", "An assessment with this name already exists")
            else:
                db.execute_query_data(db_connection, insert_csm_query, values)
                reset_csm()
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


# confirmation box before clearing the answers of a single category
def clear_category(values):
    confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your answers?')
    if confirm:
        clear_pressed(values)

# clear the answers the given list of values
def clear_pressed(values):
    for i in range(len(values)):
        values[i].set(0)


# this function the number of answers under each possible answers and their total for a single category
def submit_pressed(values):
    y = y_c = n = total_selected = 0

    for i in range(len(values)):
        if (str(values[i].get()).startswith('1')):
            y += 1
            total_selected += 1
        elif (str(values[i].get()).startswith('2')):
            y_c += 1
            total_selected += 1
        elif (str(values[i].get()).startswith('3')):
            n += 1
            total_selected += 1

    return [y, y_c, n, total_selected]


# this function resets the answers of all the CSM Domains
def reset_csm():
    clear_pressed(d1.CSM_Domain1_Governance_Page.values)
    clear_pressed(d1.CSM_Domain1_RiskManagement_Page.values)
    clear_pressed(d1.CSM_Domain1_Resources_Page.values)
    clear_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)
    clear_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)
    clear_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)
    clear_pressed(d2.CSM_Domain2_InformationSharing_Page.values)  
    clear_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)
    clear_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)
    clear_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values) 
    clear_pressed(d4.CSM_Domain4_Connections_Page.values)
    clear_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)
    clear_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)
    clear_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)
    clear_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)


# calculate the total number of answers for the 3 possible answers (yes, yes(compensating), no)
# returns them as a list
def calculate_total():
    yes_total = (submit_pressed(d1.CSM_Domain1_Governance_Page.values)[0] + submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[0]
                + submit_pressed(d1.CSM_Domain1_Resources_Page.values)[0] + submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[0]
                + submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[0] + submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[0]
                + submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[0] 
                + submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[0] + submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[0] 
                + submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[0]
                + submit_pressed(d4.CSM_Domain4_Connections_Page.values)[0] + submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[0]
                + submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[0] + submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[0]
                + submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[0])

    yes_compensating_total = (submit_pressed(d1.CSM_Domain1_Governance_Page.values)[1] + submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[1]
                + submit_pressed(d1.CSM_Domain1_Resources_Page.values)[1] + submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[1]
                + submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[1] + submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[1]
                + submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[1] 
                + submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[1] + submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[1] 
                + submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[1]
                + submit_pressed(d4.CSM_Domain4_Connections_Page.values)[1] + submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[1]
                + submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[1] + submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[1]
                + submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[1])

    no_total = (submit_pressed(d1.CSM_Domain1_Governance_Page.values)[2] + submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[2]
                + submit_pressed(d1.CSM_Domain1_Resources_Page.values)[2] + submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[2]
                + submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[2] + submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[2]
                + submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[2] 
                + submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[2] + submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[2] 
                + submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[2]
                + submit_pressed(d4.CSM_Domain4_Connections_Page.values)[2] + submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[2]
                + submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[2] + submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[2]
                + submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[2])

    return [yes_total, yes_compensating_total, no_total]


# get the total for the maturity levels under each category (Baseline, Evolving, Intermediate, Advanced, Innovative)
def maturity_total():
    pages = [d1.CSM_Domain1_Governance_Page, d1.CSM_Domain1_RiskManagement_Page, d1.CSM_Domain1_Resources_Page, d1.CSM_Domain1_TrainingAndCulture_Page,
         d2.CSM_Domain2_ThreatIntelligence_Page, d2.CSM_Domain2_MonitoringAndAnalyzing_Page, d2.CSM_Domain2_InformationSharing_Page,
         d3.CSM_Domain3_PreventiveControls_Page, d3.CSM_Domain3_DetectiveControls_Page, d3.CSM_Domain3_CorrectiveControls_Page,
         d4.CSM_Domain4_Connections_Page, d4.CSM_Domain4_RelationshipManagement_Page,
         d5.CSM_Domain5_IncidentPlanningAndStrategy_Page, d5.CSM_Domain5_DetectionResponseAndMitigation_Page, d5.CSM_Domain5_EscalationAndReporting_Page]

    baseline_yes = evolving_yes = intermediate_yes = advanced_yes = innovative_yes = 0
    baseline_yes_c = evolving_yes_c = intermediate_yes_c = advanced_yes_c = innovative_yes_c = 0
    baseline_no = evolving_no = intermediate_no = advanced_no = innovative_no = 0

    for j in range(len(pages)):

        for i in range(len(pages[j].values)):

            if str(pages[j].values[i].get()).startswith('1'):    # yes answers

                if str(pages[j].values[i].get()).endswith('1'):  # baseline
                    baseline_yes += 1
                if str(pages[j].values[i].get()).endswith('2'):  # evolving
                    evolving_yes += 1
                if str(pages[j].values[i].get()).endswith('3'):  # intermediate
                    intermediate_yes += 1
                if str(pages[j].values[i].get()).endswith('4'):  # advanced
                    advanced_yes += 1
                if str(pages[j].values[i].get()).endswith('5'):  # innovative
                    innovative_yes += 1

            if str(pages[j].values[i].get()).startswith('2'):    # yes_c answers

                if str(pages[j].values[i].get()).endswith('1'):  # baseline
                    baseline_yes_c += 1
                if str(pages[j].values[i].get()).endswith('2'):  # evolving
                    evolving_yes_c += 1
                if str(pages[j].values[i].get()).endswith('3'):  # intermediate
                    intermediate_yes_c += 1
                if str(pages[j].values[i].get()).endswith('4'):  # advanced
                    advanced_yes_c += 1
                if str(pages[j].values[i].get()).endswith('5'):  # innovative
                    innovative_yes_c += 1

            if str(pages[j].values[i].get()).startswith('3'):    # no answers

                if str(pages[j].values[i].get()).endswith('1'):  # baseline
                    baseline_no += 1
                if str(pages[j].values[i].get()).endswith('2'):  # evolving
                    evolving_no += 1
                if str(pages[j].values[i].get()).endswith('3'):  # intermediate
                    intermediate_no += 1
                if str(pages[j].values[i].get()).endswith('4'):  # advanced
                    advanced_no += 1
                if str(pages[j].values[i].get()).endswith('5'):  # innovative
                    innovative_no += 1

    return [    
            [baseline_yes, evolving_yes, intermediate_yes, advanced_yes, innovative_yes],
            [baseline_yes_c, evolving_yes_c, intermediate_yes_c, advanced_yes_c, innovative_yes_c],
            [baseline_no, evolving_no, intermediate_no, advanced_no, innovative_no]
           ]