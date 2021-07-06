package source;

public class Data {

    public Data(){}

    /**
     * Arrays containing the questions of the Inherent Risk Profile with 5 different categories
     */

    /* #region */
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
            // Least(0), Minimal(< 3%), Moderate(3% - 5%), Significant(6% - 25%), Most(>25%)
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
    /* #endregion */


    /**
     * Arrays containing the questions of the Risk Maturity Level 
     * Names of the arrays represent the domain, the category and the level
     */

    String[] domain1OversightBaseline = {
            "Designated members of management are held accountable by the board or an appropriate board committee for implementing and managing the information security and business continuity programs. (FFIEC Information Security Booklet, page 3)",
            "Information security risks are discussed in management meetings when prompted by highly visible cyber events or regulatory alerts. (FFIEC Information Security Booklet, page 6)",
            "Management provides a written report on the overall status of the information security and business continuity programs to the board or an appropriate board committee at least annually. (FFIEC Information Security Booklet, page 5)",
            "The budgeting process includes information security related expenses and tools. (FFIEC E-Banking Booklet, page 20)",
            "Management considers the risks posed by other critical infrastructures (e.g., telecommunications, energy) to the institution. (FFIEC Business Continuity Planning Booklet, page J-12)" 
    };

    String[] domain1OversightEvolving = {
            "At least annually, the board or an appropriate board committee reviews and approves the institution’s cybersecurity program.",
            "Management is responsible for ensuring compliance with legal and regulatory requirements related to cybersecurity.",
            "Cybersecurity tools and staff are requested through the budget process.",
            "There is a process to formally discuss and estimate potential expenses associated with cybersecurity incidents as part of the budgeting process." 
    };

    String[] domain1OversightIntermediate = {
            "The board or an appropriate board committee has cybersecurity expertise or engages experts to assist with oversight responsibilities.",
            "The standard board meeting package includes reports and metrics that go beyond events and incidents to address threat intelligence trends and the institution’s security posture.",
            "The institution has a cyber risk appetite statement approved by the board or an appropriate board committee.",
            "Cyber risks that exceed the risk appetite are escalated to management.",
            "The board or an appropriate board committee ensures management’s annual cybersecurity self-assessment evaluates the institution’s ability to meet its cyber risk management standards.",
            "The board or an appropriate board committee reviews and approves management’s prioritization and resource allocation decisions based on the results of the cyber assessments.",
            "The board or an appropriate board committee ensures management takes appropriate actions to address changing cyber risks or significant cybersecurity issues.",
            "The budget process for requesting additional cybersecurity staff and tools is integrated into business units’ budget processes." 
    };

    String[] domain1OversightAdvanced = {
            "The board or board committee approved cyber risk appetite statement is part of the enterprise-wide risk appetite statement.",
            "Management has a formal process to continuously improve cybersecurity oversight.",
            "The budget process for requesting additional cybersecurity staff and tools maps current resources and tools to the cybersecurity strategy.",
            "Management and the board or an appropriate board committee hold business units accountable for effectively managing all cyber risks associated with their activities.",
            "Management identifies root cause(s) when cyber attacks result in material loss.",
            "The board or an appropriate board committee ensures that management’s actions consider the cyber risks that the institution poses to the financial sector." 
    };

    String[] domain1OversightInnovative = {
            "The board or an appropriate board committee discusses ways for management to develop cybersecurity improvements that may be adopted sector-wide.",
            "The board or an appropriate board committee verifies that management’s actions consider the cyber risks that the institution poses to other critical infrastructures (e.g., telecommunications, energy)." 
    };

    String[] domain1StrategyPoliciesBaseline = {
            "The institution has an information security strategy that integrates technology, policies, procedures, and training to mitigate risk. (FFIEC Information Security Booklet, page 3)",
            "The institution has policies commensurate with its risk and complexity that address the concepts of information technology risk management. (FFIEC Information Security Booklet, page, 16)",
            "The institution has policies commensurate with its risk and complexity that address the concepts of threat information sharing. (FFIEC E-Banking Booklet, page 28)",
            "The institution has board-approved policies commensurate with its risk and complexity that address information security. (FFIEC Information Security Booklet, page 16)",
            "The institution has policies commensurate with its risk and complexity that address the concepts of external dependency or third-party management. (FFIEC Outsourcing Booklet, page 2)",
            "The institution has policies commensurate with its risk and complexity that address the concepts of incident response and resilience. (FFIEC Information Security Booklet, page 83)",
            "All elements of the information security program are coordinated enterprise-wide. (FFIEC Information Security Booklet, page 7)" 
    };

    String[] domain1StrategyPoliciesEvolving = {
            "The institution augmented its information security strategy to incorporate cybersecurity and resilience.",
            "The institution has a formal cybersecurity program that is based on technology and security industry standards or benchmarks.",
            "A formal process is in place to update policies as the institution’s inherent risk profile changes." 
    };

    String[] domain1StrategyPoliciesIntermediate = {
            "The institution has a comprehensive set of policies commensurate with its risk and complexity that address the concepts of threat intelligence.",
            "Management periodically reviews the cybersecurity strategy to address evolving cyber threats and changes to the institution’s inherent risk profile.",
            "The cybersecurity strategy is incorporated into, or conceptually fits within, the institution’s enterprise-wide risk management strategy.",
            "Management links strategic cybersecurity objectives to tactical goals.",
            "A formal process is in place to cross-reference and simultaneously update all policies related to cyber risks across business lines." 
    };

    String[] domain1StrategyPoliciesAdvanced = {
            "The cybersecurity strategy outlines the institution’s future state of cybersecurity with short-term and long-term perspectives.",
            "Industry-recognized cybersecurity standards are used as sources during the analysis of cybersecurity program gaps.",
            "The cybersecurity strategy identifies and communicates the institution’s role as a component of critical infrastructure in the financial services industry.",
            "The risk appetite is informed by the institution’s role in critical infrastructure.",
            "Management is continuously improving the existing cybersecurity program to adapt as the desired cybersecurity target state changes." 
    };

    String[] domain1StrategyPoliciesInnovative = {
            "The cybersecurity strategy identifies and communicates the institution’s role as it relates to other critical infrastructures." 
    };

    String[] domain1ITAssetManagementBaseline = {
        "An inventory of organizational assets (e.g., hardware, software, data, and systems hosted externally) is maintained. (FFIEC Information Security Booklet, page 9)",
        "Organizational assets (e.g., hardware, systems, data, and applications) are prioritized for protection based on the data classification and business value. (FFIEC Information Security Booklet, page 12)",
        "Management assigns accountability for maintaining an inventory of organizational assets. (FFIEC Information Security Booklet, page 9)",
        "A change management process is in place to request and approve changes to systems configurations, hardware, software, applications, and security tools. (FFIEC Information Security Booklet, page 56)"
    };

    String[] domain1ITAssetManagementEvolving = {
        "The asset inventory, including identification of critical assets, is updated at least annually to address new, relocated, re-purposed, and sunset assets.",
        "The institution has a documented asset life-cycle process that considers whether assets to be acquired have appropriate security safeguards.",
        "The institution proactively manages system EOL (e.g., replacement) to limit security risks.",
        "Changes are formally approved by an individual or committee with appropriate authority and with separation of duties."
    };

    String[] domain1ITAssetManagementIntermediate = {
        "Baseline configurations cannot be altered without a formal change request, documented approval, and an assessment of security implications.",
        "A formal IT change management process requires cybersecurity risk to be evaluated during the analysis, approval, testing, and reporting of changes."
    };

    String[] domain1ITAssetManagementAdvanced = {
        "Supply chain risk is reviewed before the acquisition of mission-critical information systems including system components.",
        "Automated tools enable tracking, updating, asset prioritizing, and custom reporting of the asset inventory.",
        "Automated processes are in place to detect and block unauthorized changes to software and hardware.",
        "The change management system uses thresholds to determine when a risk assessment of the impact of the change is required."
    };

    String[] domain1ITAssetManagementInnovative = {
        "A formal change management function governs decentralized or highly distributed change requests and identifies and measures security risks that may cause increased exposure to cyber attack.",
        "Comprehensive automated enterprise tools are implemented to detect and block unauthorized changes to software and hardware."
    };

    String[] domain1RiskManagementProgramBaseline = {
        "An information security and business continuity risk management function(s) exists within the institution. (FFIEC Information Security Booklet, page 68)"
    };

    String[] domain1RiskManagementProgramEvolving = {
        "The risk management program incorporates cyber risk identification, measurement, mitigation, monitoring, and reporting.",
        "Management reviews and uses the results of audits to improve existing cybersecurity policies, procedures, and controls.",
        "Management monitors moderate and high residual risk issues from the cybersecurity risk assessment until items are addressed."
    };

    String[] domain1RiskManagementProgramIntermediate = {
        "The cybersecurity function has a clear reporting line that does not present a conflict of interest.",
        "The risk management program specifically addresses cyber risks beyond the boundaries of the technological impacts (e.g., financial, strategic, regulatory, compliance).",
        "Benchmarks or target performance metrics have been established for showing improvements or regressions of the security posture over time.",
        "Management uses the results of independent audits and reviews to improve cybersecurity.",
        "There is a process to analyze and assign potential losses and related expenses, by cost center, associated with cybersecurity incidents."
    };

    String[] domain1RiskManagementProgramAdvanced = {
        "Cybersecurity metrics are used to facilitate strategic decision-making and funding in areas of need.",
        "Independent risk management sets and monitors cyber-related risk limits for business units.",
        "Independent risk management staff escalates to management and the board or an appropriate board committee significant discrepancies from business unit’s assessments of cyber-related risk.",
        "A process is in place to analyze the financial impact cyber incidents have on the institution’s capital.",
        "The cyber risk data aggregation and real-time reporting capabilities support the institution’s ongoing reporting needs, particularly during cyber incidents."
    };

    String[] domain1RiskManagementProgramInnovative = {
        "The risk management function identifies and analyzes commonalities in cyber events that occur both at the institution and across other sectors to enable more predictive risk management.",
        "A process is in place to analyze the financial impact that a cyber incident at the institution may have across the financial sector."
    };

    String[] domain1RiskAssessmentBaseline = {
        "A risk assessment focused on safeguarding customer information identifies reasonable and foreseeable internal and external threats, the likelihood and potential damage of threats, and the sufficiency of policies, procedures, and customer information systems. (FFIEC Information Security Booklet, page 8)",
        "The risk assessment identifies internet-based systems and high-risk transactions that warrant additional authentication controls. (FFIEC Information Security Booklet, page 12)",
        "The risk assessment is updated to address new technologies, products, services, and connections before deployment. (FFIEC Information Security Booklet, page 13)"
    };

    String[] domain1RiskAssessmentEvolving = {
        "Risk assessments are used to identify the cybersecurity risks stemming from new products, services, or relationships.",
        "The focus of the risk assessment has expanded beyond customer information to address all information assets.",
        "The risk assessment considers the risk of using EOL software and hardware components."
    };

    String[] domain1RiskAssessmentIntermediate = {
        "The risk assessment is adjusted to consider widely known risks or risk management practices."
    };

    String[] domain1RiskAssessmentAdvanced = {
        "An enterprise-wide risk management function incorporates cyber threat analysis and specific risk exposure as part of the enterprise risk assessment."
    };

    String[] domain1RiskAssessmentInnovative = {
        "The risk assessment is updated in real time as changes to the risk profile occur, new applicable standards are released or updated, and new exposures are anticipated.",
        "The institution uses information from risk assessments to predict threats and drive real-time responses.",
        "Advanced or automated analytics offer predictive information and real-time risk metrics."
    };

    String[] domain1AuditBaseline = {
        "Independent audit or review evaluates policies, procedures, and controls across the institution for significant risks and control issues associated with the institution's operations, including risks in new products, emerging technologies, and information systems. (FFIEC Audit Booklet, page 4)",
        "The independent audit function validates controls related to the storage or transmission of confidential data. (FFIEC Audit Booklet, page 1)",
        "Logging practices are independently reviewed periodically to ensure appropriate log management (e.g., access controls, retention, and maintenance). (FFIEC Operations Booklet, page 29)",
        "Issues and corrective actions from internal audits and independent testing/assessments are formally tracked to ensure procedures and control lapses are resolved in a timely manner. (FFIEC Information Security Booklet, page 6)"
    };

    String[] domain1AuditEvolving = {
        "The independent audit function validates that the risk management function is commensurate with the institution’s risk and complexity.",
        "The independent audit function validates that the institution’s threat information sharing is commensurate with the institution’s risk and complexity.",
        "The independent audit function validates that the institution’s cybersecurity controls function is commensurate with the institution’s risk and complexity.",
        "The independent audit function validates that the institution’s third-party relationship management is commensurate with the institution’s risk and complexity.",
        "The independent audit function validates that the institution’s incident response program and resilience are commensurate with the institution’s risk and complexity."
    };

    String[] domain1AuditIntermediate = {
        "A formal process is in place for the independent audit function to update its procedures based on changes to the institution’s inherent risk profile.",
        "The independent audit function validates that the institution’s threat intelligence and collaboration are commensurate with the institution’s risk and complexity.",
        "The independent audit function regularly reviews management’s cyber risk appetite statement.",
        "Independent audits or reviews are used to identify gaps in existing security capabilities and expertise."
    };

    String[] domain1AuditAdvanced = {
        "A formal process is in place for the independent audit function to update its procedures based on changes to the evolving threat landscape across the sector.",
        "The independent audit function regularly reviews the institution’s cyber risk appetite statement in comparison to assessment results and incorporates gaps into the audit strategy.",
        "Independent audits or reviews are used to identify cybersecurity weaknesses, root causes, and the potential impact to business units."
    };

    String[] domain1AuditInnovative = {
        "A formal process is in place for the independent audit function to update its procedures based on changes to the evolving threat landscape across other sectors the institution depends upon.",
        "The independent audit function uses sophisticated data mining tools to perform continuous monitoring of cybersecurity processes or controls."
    };

    String[] domain1StaffingBaseline = {
        "Information security roles and responsibilities have been identified. (FFIEC Information Security Booklet, page 7)",
        "Processes are in place to identify additional expertise needed to improve information security defenses. (FFIEC Information Security Work Program, Objective I: 2-8)"
    };

    String[] domain1StaffingEvolving = {
        "A formal process is used to identify cybersecurity tools and expertise that may be needed.",
        "Management with appropriate knowledge and experience leads the institution's cybersecurity efforts.",
        "Staff with cybersecurity responsibilities have the requisite qualifications to perform the necessary tasks of the position.",
        "Employment candidates, contractors, and third parties are subject to background verification proportional to the confidentiality of the data accessed, business requirements, and acceptable risk."
    };

    String[] domain1StaffingIntermediate = {
        "The institution has a program for talent recruitment, retention, and succession planning for the cybersecurity and resilience staffs."
    };

    String[] domain1StaffingAdvanced = {
        "The institution benchmarks its cybersecurity staffing against peers to identify whether its recruitment, retention, and succession planning are commensurate.",
        "Dedicated cybersecurity staff develops, or contributes to developing, integrated enterprise-level security and cyber defense strategies."
    };

    String[] domain1StaffingInnovative = {
        "The institution actively partners with industry associations and academia to inform curricula based on future cybersecurity staffing needs of the industry."
    };
}
