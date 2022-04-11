import java.util.*;

class Main {
    public int solution(String str, char t) {
        int answer = 0;
        
        for(char c : str.toUpperCase().toCharArray()){
            if(c==Character.toUpperCase(t)) answer ++;
        }
        
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        char c = kb.next().charAt(0);
        System.out.print(T.solution(str, c));
    }
}