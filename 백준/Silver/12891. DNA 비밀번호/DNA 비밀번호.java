import java.util.*;


public class Main {
    static int solution(int n, int m, char[] s, int[] arr) {
        int result = 0;
        int[] checkArr = {0, 0, 0, 0};
        int idx = m;
        for (int i=0; i<m; i++) {
            if (s[i] == 'A') checkArr[0]++;
            else if (s[i] == 'C') checkArr[1]++;
            else if (s[i] == 'G') checkArr[2]++;
            else if (s[i] == 'T') checkArr[3]++;
        }

        while (true) {
            boolean pwOk = true;
            for (int i=0; i<4; i++) {
                if (checkArr[i] < arr[i]) {
                    pwOk = false;
                    break;
                }
            }
            if (pwOk) {
                result++;
            }

            if (idx == n) break;

            if (s[idx-m] == 'A') checkArr[0]--;
            else if (s[idx-m] == 'C') checkArr[1]--;
            else if (s[idx-m] == 'G') checkArr[2]--;
            else if (s[idx-m] == 'T') checkArr[3]--;

            if (s[idx] == 'A') checkArr[0]++;
            else if (s[idx] == 'C') checkArr[1]++;
            else if (s[idx] == 'G') checkArr[2]++;
            else if (s[idx] == 'T') checkArr[3]++;

            idx++;
        }
        
        return result;
    }


    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        int n = scn.nextInt();
        int m = scn.nextInt();
        char[] s = scn.next().toCharArray();
        int[] dnaPart = new int[4];
        for (int i=0; i<4; i++) {
            dnaPart[i] = scn.nextInt();
        }

        System.out.println(solution(n, m, s, dnaPart));
    }
}