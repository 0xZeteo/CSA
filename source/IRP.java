package source;
import java.util.HashMap;

public class IRP {
    
    HashMap<String, String[]> questions; // HashMap containing the category (String) as key and its relevant questions (String[]) as values

    // Questions under the category "Technologies and Connection Types"
    String[] questionsCategory1 = {
        "Total number of Internet service provider (ISP) connections",  
                    // Least(0), Minimal(1-20), Moderate(21-100), Significant(101-200), Most(>200)
        "Unsecured external connections, number of connections not users",
                    // Least(0), Minimal(1-5), Moderate(6-10), Significant(11-25), Most(>25)
        "Wireless network access",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Personal devices allowed to connect to the corporate network",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Third parties, including number of organizations and number of individuals from vendors and subcontractors, with access to internal systems",
                    // Least(0)(0), Minimal(1-5)(<50), Moderate(6-10)(50-500), Significant(11-25)(501-1,500), Most(>25)(>1,500)
        "Wholesale customers with dedicated connections",
                    // Least(0), Minimal(1-5), Moderate(6-10), Significant(11-25), Most(>25)
        "Internally hosted and developed or modified vendor applications supporting critical activities",
                    // Least(0), Minimal(1-5), Moderate(6-10), Significant(11-25), Most(>25)
        "Internally hosted, vendor-developed applications supporting critical activities",
                    // Least(0-5), Minimal(6-30), Moderate(31-75), Significant(76-200), Most(>200)
        "User-developed technologies and user computing that support critical activities",
                    // Least(0), Minimal(1-100), Moderate(101-500), Significant(501-2,500), Most(>2,500)
        "End-of-life (EOL) systems",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Open Source Software (OSS)",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Network devices",
                    // Least(0-250), Minimal(250-1,500), Moderate(1,501–25,000), Significant(25,001-50,000), Most(>50,000)
        "Third-party service providers storing and/or processing information that support critical activities (Do not have access to internal systems, but the institution relies on their services)",
                    // Least(0), Minimal(1-25), Moderate(26-100), Significant(101-200)(1 or more are foreign-based), Most(>200)(1 or more are foreign-based)
        "Cloud computing services hosted externally to support critical activities"
                    // Least(0), Minimal(1-3), Moderate(4-7), Significant(8-10), Most(>10)
    };

    // Questions under the category "Delivery Channels"
    String[] questionsCategory2 = {
        "Online presence (customer)", 
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Mobile presence",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Automated Teller Machines (ATM) (Operation)"
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
    };

    // Questions under the category "Online/Mobile Products and Technology Services"
    String[] questionsCategory3 = {
        "Issue debit or credit cards",
                    // Least(0), Minimal(<10,000), Moderate(10,000-50,000), Significant(50,000-100,000), Most(>100,000)
        "Prepaid cards",
                    // Least(0), Minimal(<5,000), Moderate(5,000-10,000), Significant(10,001-20,000), Most(>20,000)
        "Emerging payments technologies (e.g., digital wallets, mobile wallets)",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Person-to-person payments (P2P)",
                    // Least(0), Minimal(<1,000)(<50,000), Moderate(1,000-5,000)(50,000-100,000), Significant(5,001–10,000)(100,001–1 million), Most(>10,000)(>1 million)
        "Originating ACH payments",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Originating wholesale payments",
                    // Least(0), Minimal(< 3% of total assets), Moderate(3% - 5%), Significant(6% - 25%), Most(> 25%)
        "Wire transfers",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Merchant remote deposit capture (RDC)",
                    // Least(0), Minimal(<100)(< 3% of total assets), Moderate(100–500)(3% - 5%), Significant(501–1,000)(6% - 25%), Most(>1,000)(> 25%)
        "Global remittances",
                    // Least(0), Minimal(< 3%), Moderate(3% - 5%), Significant(6% - 25%), Most(> 25%)
        "Treasury services and clients",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Trust services",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Act as a correspondent bank (Interbank transfers)",
                    // Least(0), Minimal(<100), Moderate(100–250), Significant(251–500), Most(>500)
        "Merchant acquirer (sponsor merchants or card processor activity into the payment system)",
                    // Least(0), Minimal(<1,000), Moderate(1,000-10,000), Significant(10,001–100,000), Most(>100,000)
        "Host IT services for other organizations (either through joint systems or administrative support)"
                    // Least(0), Minimal(only affiliated organizations), Moderate(up to 25 unaffiliated organizations), Significant(26–50), Most(>50)
    };

    // Questions under the category "Organizational Characteristics"
    String[] questionsCategory4 = {
        "Mergers and acquisitions (including divestitures and joint ventures)",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Direct employees (including information technology and cybersecurity contractors)",
                    // Least(<50), Minimal(50-2,000), Moderate(2,001–10,000), Significant(10,001–50,000), Most(>50,000)
        "Changes in IT and information security staffing",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Privileged access (Administrators, network, database, applications, systems, etc.)",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Changes in IT environment (e.g., network, infrastructure, critical applications, technologies supporting new products or services)",
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
        "Locations of branches/business presence",
                    // Least(1 state), Minimal(1 region), Moderate(1 country), Significant(1–20 countries), Most(>20 countries)
        "Locations of operations/data centers"
                    // Least(1 state), Minimal(1 region), Moderate(1 country), Significant(1–10 countries), Most(>10 countries)
    };

    // Questions under the category "External Threats"
    String[] questionsCategory5 = {
        "Attempted cyber attacks"
                    // Least(), Minimal(), Moderate(), Significant(), Most() ---------------------------------
    };

    /**
     * Constructor
     * Initializes the questions and their categories
     */
    public IRP() {
        questions = new HashMap<>();

        questions.put("Technologies and Connection Types", questionsCategory1);
        questions.put("Delivery Channels", questionsCategory2);
        questions.put("Online/Mobile Products and Technology Services", questionsCategory3);
        questions.put("Organizational Characteristics", questionsCategory4);
        questions.put("External Threats", questionsCategory5);
    }

    

}
