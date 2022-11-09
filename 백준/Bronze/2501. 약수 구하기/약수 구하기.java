import java.util.*;

class Main {
    public int solution(int n, int k) {
        int cnt = 1;
        for(int i=1; i<n+1; i++) {
            if(n%i==0 && cnt!=k) cnt++;
            else if(n%i == 0 && cnt == k) return i;
        }

        return 0;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int k = kb.nextInt();
        System.out.print(T.solution(n,k));
    }
}