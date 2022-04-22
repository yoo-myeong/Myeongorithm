import java.util.*;

class Main {
    public int solution(String str) {
        String answer = "";
        
        for(char c : str.toCharArray()) {
            if(Character.isDigit(c)) answer += c;
        }

        return Integer.valueOf(answer);
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.print(T.solution(str));
    }
}