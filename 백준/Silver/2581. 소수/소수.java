import java.util.*;

class Main {

    public static boolean isPrime(int num) {
        if(num == 1) return false;
        for(int i=2; i<num; i++) {
            if(num%i == 0) return false;
        }
        return true;
    }

    public static void solution(int m, int n) {
        int sum = 0;
        int minVal = Integer.MAX_VALUE;
        for (int i = m; i <= n; i++) {
            if (isPrime(i)) {
                sum += i;
                minVal = Math.min(minVal, i);
            }
        }

        if (sum == 0) {
            System.out.print(-1);
        } else {
            System.out.println(sum);
            System.out.println(minVal);
        }

        return;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int m = kb.nextInt();
        int n = kb.nextInt();

        T.solution(m, n);
    }
}