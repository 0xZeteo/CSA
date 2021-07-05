
public class Main{

public static void main(String[] args){
    IRP test = new IRP();
    
    for (String key : test.questions.keySet()) {
        for (int i = 0; i < test.questions.get(key).length; i++) {
            System.out.println(key + " : " + test.questions.get(key)[i]);
        }
    }
}}