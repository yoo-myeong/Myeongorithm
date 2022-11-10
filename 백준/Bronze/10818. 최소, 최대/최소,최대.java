import java.util.*;

class Main {

    public static String solution(int n, int[] nums) {

        String answer = "";

        int max = Integer.MIN_VALUE;

        int min = Integer.MAX_VALUE;

        for (int num : nums) {

            if(num > max) max=num;

            if(num < min) min=num;

        }

        answer=Integer.toString(min)+" "+Integer.toString(max);

        return answer;

    }

    public static void main(String[] args) {

        Main T = new Main();

        Scanner kb = new Scanner(System.in);

        int n = kb.nextInt();

        int[] nums = new int[n];

        for(int i=0;i<n;i++){

            nums[i]=kb.nextInt();

        }

        System.out.println(T.solution(n,nums));

        

    }

}
