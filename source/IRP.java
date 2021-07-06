package source;

import java.util.HashMap;

/**
 * Inherent Risk Profile
 * @Function void getAnswers()  - fills the answers submitted by the user to each question
 * @Function void score()       - counts the answers to determine the number in each risk level and updates their variables
 * @Function String riskLevel() - returns the final risk level as a String (least, minimal, moderate, significant, most)
 */
public class IRP {

    HashMap<String, String[]> questions;                // @key = Category (String) || @value = Questions (String[])
    HashMap<String, String> answers;                    // @key = Question (String) || @value = Answer (String)
    int least, minimal, moderate, significant, most;    // Integers to count the number of answers in each Risk Level

    /**
     * @Constructor
     * Initializes all the variables 
     * Fills the arrays of questions under their relative categories in the hashmap
     */
    public IRP() {
        Data data = new Data();
        questions = new HashMap<>();
        answers = new HashMap<>();
        least = minimal = moderate = significant = most = 0;
        questions.put("Technologies and Connection Types", data.questionsCategory1);
        questions.put("Delivery Channels", data.questionsCategory2);
        questions.put("Online/Mobile Products and Technology Services", data.questionsCategory3);
        questions.put("Organizational Characteristics", data.questionsCategory4);
        questions.put("External Threats", data.questionsCategory5);
    }

    /**
     * @Function getAnswers() - Gets the answer for each question from the user (possible answers: least, minimal, moderate, significant, most)
     * @ToDo replace null with answers from the user
     */
    public void getAnswers() {

        for (String key : questions.keySet()) {
            for (int i = 0; i < questions.get(key).length; i++) {
                answers.put(questions.get(key)[i], null);
            }
        }
    }

    /**
     * @Function score() - Counts the entries in each risk level and updates the variables (least, minimal, moderate, significant, most)
     */
    public void score() {

        for (String key : answers.keySet()) {
            switch (answers.get(key)) {
                case "Least"      : least++;       break;
                case "Minimal"    : minimal++;     break;
                case "Moderate"   : moderate++;    break;
                case "Significant": significant++; break;
                case "Most"       : most++;        break;
            }
        }
    }

    /**
     * @Function riskLevel() - Calculates the final risk level
     * @Return String        - representing the final risk level (least, minimal, moderate, significant, most)
     * @ToDo update the formula to calculate the risk level
     * @ToDo what happens if 2 risk levels have same number of answers ?
     */
    public String riskLevel() {
        String risk = "";
        return risk;
    }
}
