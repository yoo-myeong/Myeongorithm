import java.util.*;

class Main {
    public String solution(String str) {
        int strLength = str.length();

        int lt = 0, rt = strLength-1;

        while(lt <  rt){
            if(!Character.isAlphabetic(str.charAt(lt))) lt++;
            else if(!Character.isAlphabetic(str.charAt(rt))) rt--;
            else {
                char leftCh = Character.toLowerCase(str.charAt(lt));
                char rightCh = Character.toLowerCase(str.charAt(rt));
                if(leftCh != rightCh) return "NO";
                lt ++;
                rt --;
            }
        }

        return "YES";
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.print(T.solution(str));
    }
}