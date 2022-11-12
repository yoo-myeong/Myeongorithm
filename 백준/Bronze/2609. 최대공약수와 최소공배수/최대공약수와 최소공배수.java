import java.util.*;

class Main {
    public static void solution(int x, int y) {
        int bigger = Math.max(x, y);
        int smaller = Math.min(x, y);

        int gcd;
        int lcm;
        
        while(true){
            int tmp = smaller;
            smaller = bigger % smaller;
            bigger = tmp;
            if (smaller == 0) {
                gcd = tmp;
                break;
            }
        }

        lcm = x*y / gcd;

        System.out.println(Integer.toString(gcd));
        System.out.println(Integer.toString(lcm));
        
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int x = kb.nextInt();
        int y = kb.nextInt();
        T.solution(x,y);
    }
}