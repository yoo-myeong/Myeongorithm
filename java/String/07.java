import java.util.*;

class Main {
    public String solution(String str) {
        int strLength = str.length();

        for (int i = 0; i < strLength/2; i++) {
            char leftCh = Character.toLowerCase(str.charAt(i));
            char rightCh = Character.toLowerCase(str.charAt(strLength - 1 - i));

            if (leftCh != rightCh)
                return "NO";
        }

        return "YES";
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.print(T.solution(str));
    }
}