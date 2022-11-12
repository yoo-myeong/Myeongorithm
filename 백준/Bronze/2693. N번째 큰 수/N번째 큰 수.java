import java.util.*;

class Main {
    public static int solution(Integer[] arr) {
        Arrays.sort(arr, Collections.reverseOrder());
        return arr[2];
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String t = kb.nextLine();

        for (int i = 0; i < Integer.valueOf(t); i++) {
            String str = kb.nextLine();
            String[] strArr = str.split(" ");
            Integer[] intArr = new Integer[10];
            for (int j = 0; j < 10; j++) {
                int strToInt = Integer.valueOf(strArr[j]);
                intArr[j] = strToInt;
            }
            System.out.println(T.solution(intArr));
        }
    }
}