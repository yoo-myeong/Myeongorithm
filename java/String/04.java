import java.util.*;

class Main {
    public String solution(String str) {
        StringBuffer sb = new StringBuffer(str);
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        String[] strArr = new String[n];
        for(int i=0; i<n; i++){
            strArr[i] = kb.next();
        }
        
        for(int i=0; i<n; i++){
            System.out.println(T.solution(strArr[i]));
        }
    }
}