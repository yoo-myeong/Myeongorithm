import java.util.*;

class Main {
    public String solution(String str) {
        int lt = 0;
        int rt = str.length()-1;
        char[] strToChar = str.toCharArray();
        
        while(lt<rt) {
            if(!Character.isAlphabetic(strToChar[lt])) lt++;
            else if(!Character.isAlphabetic(strToChar[rt])) rt--;
            else {
                char tmp = strToChar[lt];
                strToChar[lt] = strToChar[rt];
                strToChar[rt] = tmp;
                lt++;
                rt--;
            }
        }

        return String.valueOf(strToChar);
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.print(T.solution(str));
    }
}