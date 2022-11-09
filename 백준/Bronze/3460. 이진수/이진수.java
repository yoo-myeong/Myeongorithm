import java.util.*;

class Main {
    public static String solution(int n) {
        String answer = "";

        String binary = Integer.toBinaryString(n);
        char[] charArr = binary.toCharArray();

        for(int i=charArr.length-1; i>=0; i--) {
            if(charArr[i] == '1') {
                answer += Integer.toString(charArr.length-i-1) + ' ';
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int t = kb.nextInt();

        for(int i=0; i<t; i++) {
            int n = kb.nextInt();
            System.out.println(T.solution(n));   
        }
    }
}