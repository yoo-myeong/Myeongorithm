import java.util.*;

class Main {
    public String solution(String str) {
        String answer = "";
        int maxLen = Integer.MIN_VALUE;

        String[] splited = str.split("\\s");
        for (String s: splited){
            if(s.length() > maxLen) {
                maxLen = s.length();
                answer = s;
            }
        }
        
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.print(T.solution(str));
    }
}