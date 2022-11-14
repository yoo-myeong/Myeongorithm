import java.util.*;

class Main {

    public static int[] getNumbers(int b){
        int[] arr = new int[b];

        int num = 1;
        int p = 0;
        
        while(p<=b) {
            for(int i=0; i<num; i++) {
                arr[p] = num;
                p++;
                if(p == b) return arr;
            }
            num ++;
        }

        return arr;
    }
    
    public static int solution(int a, int b) {
        int sum = 0;
        int[] arr = getNumbers(b);
        for(int i=a-1; i<b; i++) {
            sum += arr[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int a = kb.nextInt();
        int b = kb.nextInt();

        System.out.println(T.solution(a,b));
    }
}