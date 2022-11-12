import java.util.*;

class Main {
    public static boolean checkIsPrime(int num) {
        if(num == 1) return false;
        // System.out.println("num="+num);
        for(int i=2; i<num; i++) {
            // System.out.println("i="+i);
            if(num%i == 0) {
                return false;   
            }
        }
        return true;
    }
    
    public static int solution(int[] arr) {
        int cnt = 0;
        for(int num : arr) {
            if(checkIsPrime(num)) cnt++;
        }
        return cnt;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = kb.nextInt();
        }

        System.out.println(T.solution(arr));
    }
}