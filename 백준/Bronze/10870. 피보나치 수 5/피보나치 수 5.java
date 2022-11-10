import java.util.*;

class Main {
    public static int solution(int n) {
        int answer = 0;
        int[] nums = new int[n+1];

        if(n==0) return 0;
        if(n==1) return 1;
        
        nums[0] = 0;
        nums[1] = 1;
        for(int i=2; i<n+1; i++) {
            nums[i] = nums[i-2] + nums[i-1];
        }
        
        return nums[n];
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        System.out.println(T.solution(n));
        
    }
}