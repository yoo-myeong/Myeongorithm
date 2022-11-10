import java.util.*;

class Main {
    public static void solution(int[] arr) {
        Arrays.sort(arr);
        
        int sum = Arrays.stream(arr).sum();

        int idx1=0, idx2=0;
        
        for(int i=0; i<9; i++) {
            for(int j=1; j<9; j++) {
                if(sum-arr[i]-arr[j] == 100) {
                    idx1 = i;
                    idx2 = j;
                    break;
                }         
            }
        }

        for(int i=0; i<9; i++) {
            if(i == idx1 || i == idx2) continue;
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int[] arr = new int[9];
        for(int i=0; i<9; i++) {
            arr[i] = kb.nextInt();
        }
        T.solution(arr);
    }
}