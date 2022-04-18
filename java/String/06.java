import java.util.*;

class Main {
    public String solution(String str) {
        String answer = "";

        for(int i=0; i<str.length(); i++){
            char c = str.charAt(i);
            if(str.indexOf(c) == i) answer+= c;
        }
        
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.print(T.solution(str));
    }
}