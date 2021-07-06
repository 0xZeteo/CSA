package source;

import java.util.HashMap;

public class CSM {
    
    HashMap<String, HashMap<String,String[]>> questions;
    HashMap<String, String[]> domain1, domain2, domain3, domain4, domain5;

    public CSM() {
        Data data = new Data();
        questions = new HashMap<>();
        domain1 = new HashMap<>();
        domain2 = new HashMap<>();
        domain3 = new HashMap<>();
        domain4 = new HashMap<>();
        domain5 = new HashMap<>();

        questions.put("Domain 1: Cyber Risk Management and Oversight", domain1);
        questions.put("Domain 2: Threat Intelligence and Collaboration", domain2);
        questions.put("Domain 3: Cybersecurity Controls", domain3);
        questions.put("Domain 4: External Dependency Management", domain4);
        questions.put("Domain 5: Cyber Incident Management and Resilience", domain5);

        domain1.put("Oversight (Baseline)", data.domain1OversightBaseline);
        domain1.put("Oversight (Evolving)", data.domain1OversightEvolving);
        domain1.put("Oversight (Intermediate)", data.domain1OversightIntermediate);
        domain1.put("Oversight (Advanced)", data.domain1OversightAdvanced);
        domain1.put("Oversight (Innovative)", data.domain1OversightInnovative);

        domain1.put("Strategy & Policies (Baseline)", data.domain1StrategyPoliciesBaseline);
        domain1.put("Strategy & Policies (Evolving)", data.domain1StrategyPoliciesEvolving);
        domain1.put("Strategy & Policies (Intermediate)", data.domain1StrategyPoliciesIntermediate);
        domain1.put("Strategy & Policies (Advanced)", data.domain1StrategyPoliciesAdvanced);
        domain1.put("Strategy & Policies (Innovative)", data.domain1StrategyPoliciesInnovative);

        domain1.put("IT Asset Management (Baseline)", data.domain1ITAssetManagementBaseline);
        domain1.put("IT Asset Management (Evolving)", data.domain1ITAssetManagementEvolving);
        domain1.put("IT Asset Management (Intermediate)", data.domain1ITAssetManagementIntermediate);
        domain1.put("IT Asset Management (Advanced)", data.domain1ITAssetManagementAdvanced);
        domain1.put("IT Asset Management (Innovative)", data.domain1ITAssetManagementInnovative);

        domain1.put("Risk Management Program (Baseline)", data.domain1RiskManagementProgramBaseline);
        domain1.put("Risk Management Program (Evolving)", data.domain1RiskManagementProgramEvolving);
        domain1.put("Risk Management Program (Intermediate)", data.domain1RiskManagementProgramIntermediate);
        domain1.put("Risk Management Program (Advanced)", data.domain1RiskManagementProgramAdvanced);
        domain1.put("Risk Management Program (Innovative)", data.domain1RiskManagementProgramInnovative);

        domain1.put("Risk Assessment (Baseline)", data.domain1RiskAssessmentBaseline);
        domain1.put("Risk Assessment (Evolving)", data.domain1RiskAssessmentEvolving);
        domain1.put("Risk Assessment (Intermediate)", data.domain1RiskAssessmentIntermediate);
        domain1.put("Risk Assessment (Advanced)", data.domain1RiskAssessmentAdvanced);
        domain1.put("Risk Assessment (Innovative)", data.domain1RiskAssessmentInnovative);

        domain1.put("Audit (Baseline)", data.domain1AuditBaseline);
        domain1.put("Audit (Evolving)", data.domain1AuditEvolving);
        domain1.put("Audit (Intermediate)", data.domain1AuditIntermediate);
        domain1.put("Audit (Advanced)", data.domain1AuditAdvanced);
        domain1.put("Audit (Innovative)", data.domain1AuditInnovative);

        domain1.put("Staffing (Baseline)", data.domain1StaffingBaseline);
        domain1.put("Staffing (Evolving)", data.domain1StaffingEvolving);
        domain1.put("Staffing (Intermediate)", data.domain1StaffingIntermediate);
        domain1.put("Staffing (Advanced)", data.domain1StaffingAdvanced);
        domain1.put("Staffing (Innovative)", data.domain1StaffingInnovative);

        domain1.put("Training (Baseline)", data.domain1TrainingBaseline);
        domain1.put("Training (Evolving)", data.domain1TrainingEvolving);
        domain1.put("Training (Intermediate)", data.domain1TrainingIntermediate);
        domain1.put("Training (Advanced)", data.domain1TrainingAdvanced);
        domain1.put("Training (Innovative)", data.domain1TrainingInnovative);

        domain1.put("Culture (Baseline)", data.domain1CultureBaseline);
        domain1.put("Culture (Evolving)", data.domain1CultureEvolving);
        domain1.put("Culture (Intermediate)", data.domain1CultureIntermediate);
        domain1.put("Culture (Advanced)", data.domain1CultureAdvanced);
        domain1.put("Culture (Innovative)", data.domain1CultureInnovative);

        domain2.put("Threat Intelligence & Information (Baseline)", data.domain2ThreatIntelligenceAndInformationBaseline);
        domain2.put("Threat Intelligence & Information (Evolving)", data.domain2ThreatIntelligenceAndInformationEvolving);
        domain2.put("Threat Intelligence & Information (Intermediate)", data.domain2ThreatIntelligenceAndInformationIntermediate);
        domain2.put("Threat Intelligence & Information (Advanced)", data.domain2ThreatIntelligenceAndInformationAdvanced);
        domain2.put("Threat Intelligence & Information (Innovative)", data.domain2ThreatIntelligenceAndInformationInnovative);

        domain2.put("Monitoring & Analyzing (Baseline)", data.domain2MonitoringAndAnalyzingBaseline);
        domain2.put("Monitoring & Analyzing (Evolving)", data.domain2MonitoringAndAnalyzingEvolving);
        domain2.put("Monitoring & Analyzing (Intermediate)", data.domain2MonitoringAndAnalyzingIntermediate);
        domain2.put("Monitoring & Analyzing (Advanced)", data.domain2MonitoringAndAnalyzingAdvanced);
        domain2.put("Monitoring & Analyzing (Innovative)", data.domain2MonitoringAndAnalyzingInnovative);

        domain2.put("Information Sharing (Baseline)", data.domain2InformationSharingBaseline);
        domain2.put("Information Sharing (Evolving)", data.domain2InformationSharingEvolving);
        domain2.put("Information Sharing (Intermediate)", data.domain2InformationSharingIntermediate);
        domain2.put("Information Sharing (Advanced)", data.domain2InformationSharingAdvanced);
        domain2.put("Information Sharing (Innovative)", data.domain2InformationSharingInnovative);

        domain3.put("Infrastructure Management (Baseline)", data.domain3InfrastructureManagementBaseline);
        domain3.put("Infrastructure Management (Evolving)", data.domain3InfrastructureManagementEvolving);
        domain3.put("Infrastructure Management (Intermediate)", data.domain3InfrastructureManagementIntermediate);
        domain3.put("Infrastructure Management (Advanced)", data.domain3InfrastructureManagementAdvanced);
        domain3.put("Infrastructure Management (Innovative)", data.domain3InfrastructureManagementInnovative);

        domain3.put("Access & Data Management (Baseline)", data.domain3AccessAndDataManagementBaseline);
        domain3.put("Access & Data Management (Evolving)", data.domain3AccessAndDataManagementEvolving);
        domain3.put("Access & Data Management (Intermediate)", data.domain3AccessAndDataManagementIntermediate);
        domain3.put("Access & Data Management (Advanced)", data.domain3AccessAndDataManagementAdvanced);
        domain3.put("Access & Data Management (Innovative)", data.domain3AccessAndDataManagementInnovative);

        domain3.put("Device/End-Point Security (Baseline)", data.domain3DeviceEndPointSecurityBaseline);
        domain3.put("Device/End-Point Security (Evolving)", data.domain3DeviceEndPointSecurityEvolving);
        domain3.put("Device/End-Point Security (Intermediate)", data.domain3DeviceEndPointSecurityIntermediate);
        domain3.put("Device/End-Point Security (Advanced)", data.domain3DeviceEndPointSecurityAdvanced);
        domain3.put("Device/End-Point Security (Innovative)", data.domain3DeviceEndPointSecurityInnovative);

        domain3.put("Secure Coding (Baseline)", data.domain3SecureCodingBaseline);
        domain3.put("Secure Coding (Evolving)", data.domain3SecureCodingEvolving);
        domain3.put("Secure Coding (Intermediate)", data.domain3SecureCodingIntermediate);
        domain3.put("Secure Coding (Advanced)", data.domain3SecureCodingAdvanced);
        domain3.put("Secure Coding (Innovative)", data.domain3SecureCodingInnovative);

        domain3.put("Threat & Vulnerability Detection (Baseline)", data.domain3ThreatAndVulnerabilityDetectionBaseline);
        domain3.put("Threat & Vulnerability Detection (Evolving)", data.domain3ThreatAndVulnerabilityDetectionEvolving);
        domain3.put("Threat & Vulnerability Detection (Intermediate)", data.domain3ThreatAndVulnerabilityDetectionIntermediate);
        domain3.put("Threat & Vulnerability Detection (Advanced)", data.domain3ThreatAndVulnerabilityDetectionAdvanced);
        domain3.put("Threat & Vulnerability Detection (Innovative)", data.domain3ThreatAndVulnerabilityDetectionInnovative);

        domain3.put("Anomalous Activity Detection (Baseline)", data.domain3AnomalousActivityDetectionBaseline);
        domain3.put("Anomalous Activity Detection (Evolving)", data.domain3AnomalousActivityDetectionEvolving);
        domain3.put("Anomalous Activity Detection (Intermediate)", data.domain3AnomalousActivityDetectionIntermediate);
        domain3.put("Anomalous Activity Detection (Advanced)", data.domain3AnomalousActivityDetectionAdvanced);
        domain3.put("Anomalous Activity Detection (Innovative)", data.domain3AnomalousActivityDetectionInnovative);

        domain3.put("Event Detection (Baseline)", data.domain3EventDetectionBaseline);
        domain3.put("Event Detection (Evolving)", data.domain3EventDetectionEvolving);
        domain3.put("Event Detection (Intermediate)", data.domain3EventDetectionIntermediate);
        domain3.put("Event Detection (Advanced)", data.domain3EventDetectionAdvanced);
        domain3.put("Event Detection (Innovative)", data.domain3EventDetectionInnovative);
        
        domain3.put("Patch Management (Baseline)", data.domain3PatchManagementBaseline);
        domain3.put("Patch Management (Evolving)", data.domain3PatchManagementEvolving);
        domain3.put("Patch Management (Intermediate)", data.domain3PatchManagementIntermediate);
        domain3.put("Patch Management (Advanced)", data.domain3PatchManagementAdvanced);
        domain3.put("Patch Management (Innovative)", data.domain3PatchManagementInnovative);

        domain3.put("Remediation (Baseline)", data.domain3RemediationBaseline);
        domain3.put("Remediation (Evolving)", data.domain3RemediationEvolving);
        domain3.put("Remediation (Intermediate)", data.domain3RemediationIntermediate);
        domain3.put("Remediation (Advanced)", data.domain3RemediationAdvanced);
        domain3.put("Remediation (Innovative)", data.domain3RemediationInnovative);

        domain4.put("Connections (Baseline)", data.domain4ConnectionsBaseline);
        domain4.put("Connections (Evolving)", data.domain4ConnectionsEvolving);
        domain4.put("Connections (Intermediate)", data.domain4ConnectionsIntermediate);
        domain4.put("Connections (Advanced)", data.domain4ConnectionsAdvanced);
        domain4.put("Connections (Innovative)", data.domain4ConnectionsInnovative);

        domain4.put("Due Diligence (Baseline)", data.domain4DueDiligenceBaseline);
        domain4.put("Due Diligence (Evolving)", data.domain4DueDiligenceEvolving);
        domain4.put("Due Diligence (Intermediate)", data.domain4DueDiligenceIntermediate);
        domain4.put("Due Diligence (Advanced)", data.domain4DueDiligenceAdvanced);
        domain4.put("Due Diligence (Innovative)", data.domain4DueDiligenceInnovative);

        domain4.put("Contracts (Baseline)", data.domain4ContractsBaseline);
        domain4.put("Contracts (Evolving)", data.domain4ContractsEvolving);
        domain4.put("Contracts (Intermediate)", data.domain4ContractsIntermediate);
        domain4.put("Contracts (Advanced)", data.domain4ContractsAdvanced);
        domain4.put("Contracts (Innovative)", data.domain4ContractsInnovative);

        domain4.put("Ongoing Monitoring (Baseline)", data.domain4OngoingMonitoringBaseline);
        domain4.put("Ongoing Monitoring (Evolving)", data.domain4OngoingMonitoringEvolving);
        domain4.put("Ongoing Monitoring (Intermediate)", data.domain4OngoingMonitoringIntermediate);
        domain4.put("Ongoing Monitoring (Advanced)", data.domain4OngoingMonitoringAdvanced);
        domain4.put("Ongoing Monitoring (Innovative)", data.domain4OngoingMonitoringInnovative);

        domain5.put("Planning (Baseline)", data.domain5PlanningBaseline);
        domain5.put("Planning (Evolving)", data.domain5PlanningEvolving);
        domain5.put("Planning (Intermediate)", data.domain5PlanningIntermediate);
        domain5.put("Planning (Advanced)", data.domain5PlanningAdvanced);
        domain5.put("Planning (Innovative)", data.domain5PlanningInnovative);

        domain5.put("Testing (Baseline)", data.domain5TestingBaseline);
        domain5.put("Testing (Evolving)", data.domain5TestingEvolving);
        domain5.put("Testing (Intermediate)", data.domain5TestingIntermediate);
        domain5.put("Testing (Advanced)", data.domain5TestingAdvanced);
        domain5.put("Testing (Innovative)", data.domain5TestingInnovative);

        domain5.put("Detection (Baseline)", data.domain5DetectionBaseline);
        domain5.put("Detection (Evolving)", data.domain5DetectionEvolving);
        domain5.put("Detection (Intermediate)", data.domain5DetectionIntermediate);
        domain5.put("Detection (Advanced)", data.domain5DetectionAdvanced);
        domain5.put("Detection (Innovative)", data.domain5DetectionInnovative);

        domain5.put("Response & Mitigation (Baseline)", data.domain5ResponseAndMitigationBaseline);
        domain5.put("Response & Mitigation (Evolving)", data.domain5ResponseAndMitigationEvolving);
        domain5.put("Response & Mitigation (Intermediate)", data.domain5ResponseAndMitigationIntermediate);
        domain5.put("Response & Mitigation (Advanced)", data.domain5ResponseAndMitigationAdvanced);
        domain5.put("Response & Mitigation (Innovative)", data.domain5ResponseAndMitigationInnovative);
        
        domain5.put("Escalation & Reporting (Baseline)", data.domain5EscalationAndReportingBaseline);
        domain5.put("Escalation & Reporting (Evolving)", data.domain5EscalationAndReportingEvolving);
        domain5.put("Escalation & Reporting (Intermediate)", data.domain5EscalationAndReportingIntermediate);
        domain5.put("Escalation & Reporting (Advanced)", data.domain5EscalationAndReportingAdvanced);
        domain5.put("Escalation & Reporting (Innovative)", data.domain5EscalationAndReportingInnovative);
    }
}
