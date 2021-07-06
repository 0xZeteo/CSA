package source;

import java.util.HashMap;

public class CSM {
    
    HashMap<String, HashMap<String,String[]>> questions;
    HashMap<String, String[]> domain1, domain2, domain3, domain4, domain5;

    public CSM() {
        Data data = new Data();
        questions = new HashMap<>();
        domain1 = new HashMap<>();

        domain1.put("Oversight / Baseline", data.domain1OversightBaseline);
        domain1.put("Oversight / Evolving", data.domain1OversightEvolving);
        domain1.put("Oversight / Intermediate", data.domain1OversightIntermediate);
        domain1.put("Oversight / Advanced", data.domain1OversightAdvanced);
        domain1.put("Oversight / Innovative", data.domain1OversightInnovative);

        domain1.put("Strategy & Policies / Baseline", data.domain1StrategyPoliciesBaseline);
        domain1.put("Strategy & Policies / Evolving", data.domain1StrategyPoliciesEvolving);
        domain1.put("Strategy & Policies / Intermediate", data.domain1StrategyPoliciesIntermediate);
        domain1.put("Strategy & Policies / Advanced", data.domain1StrategyPoliciesAdvanced);
        domain1.put("Strategy & Policies / Innovative", data.domain1StrategyPoliciesInnovative);

        domain1.put("IT Asset Management / Baseline", data.domain1ITAssetManagementBaseline);
        domain1.put("IT Asset Management / Evolving", data.domain1ITAssetManagementEvolving);
        domain1.put("IT Asset Management / Intermediate", data.domain1ITAssetManagementIntermediate);
        domain1.put("IT Asset Management / Advanced", data.domain1ITAssetManagementAdvanced);
        domain1.put("IT Asset Management / Innovative", data.domain1ITAssetManagementInnovative);

        domain1.put("Risk Management Program / Baseline", data.domain1RiskManagementProgramBaseline);
        domain1.put("Risk Management Program / Evolving", data.domain1RiskManagementProgramEvolving);
        domain1.put("Risk Management Program / Intermediate", data.domain1RiskManagementProgramIntermediate);
        domain1.put("Risk Management Program / Advanced", data.domain1RiskManagementProgramAdvanced);
        domain1.put("Risk Management Program / Innovative", data.domain1RiskManagementProgramInnovative);

        domain1.put("Risk Assessment / Baseline", data.domain1RiskAssessmentBaseline);
        domain1.put("Risk Assessment / Evolving", data.domain1RiskAssessmentEvolving);
        domain1.put("Risk Assessment / Intermediate", data.domain1RiskAssessmentIntermediate);
        domain1.put("Risk Assessment / Advanced", data.domain1RiskAssessmentAdvanced);
        domain1.put("Risk Assessment / Innovative", data.domain1RiskAssessmentInnovative);

        domain1.put("Audit / Baseline", data.domain1AuditBaseline);
        domain1.put("Audit / Evolving", data.domain1AuditEvolving);
        domain1.put("Audit / Intermediate", data.domain1AuditIntermediate);
        domain1.put("Audit / Advanced", data.domain1AuditAdvanced);
        domain1.put("Audit / Innovative", data.domain1AuditInnovative);

        domain1.put("Staffing / Baseline", data.domain1StaffingBaseline);
        domain1.put("Staffing / Evolving", data.domain1StaffingEvolving);
        domain1.put("Staffing / Intermediate", data.domain1StaffingIntermediate);
        domain1.put("Staffing / Advanced", data.domain1StaffingAdvanced);
        domain1.put("Staffing / Innovative", data.domain1StaffingInnovative);

        questions.put("Domain 1: Cyber Risk Management and Oversight", domain1);
    }
}
