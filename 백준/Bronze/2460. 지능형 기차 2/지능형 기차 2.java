import java.util.*;

class Main {
    public static int solution(Scanner kb) {
        int max = Integer.MIN_VALUE;

        int people = 0;
        for(int i=0; i<10; i++) {
            int pout = kb.nextInt();
            int pin = kb.nextInt();
            people -= pout;
            people += pin;
            max = Math.max(max, people);
        }
        
        return max;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        System.out.println(T.solution(kb));
        
    }
}