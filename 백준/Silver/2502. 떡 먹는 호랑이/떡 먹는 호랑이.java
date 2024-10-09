import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int day = Integer.parseInt(st.nextToken());
        int val = Integer.parseInt(st.nextToken());
        int[] dp = new int[31];
        dp[1] = 1; dp[2] = 1;

        while (true) {
            for (int i=3; i<day+1; i++) {
                dp[i] = dp[i-1] + dp[i-2];
            }

            if (dp[day] == val) {
                break;
            } else if (dp[day] > val) {
                dp[1]++;
                dp[2] = dp[1];
            } else {
                dp[2]++;
            }
        }

        System.out.println(dp[1]);
        System.out.println(dp[2]);
        br.close();
    }
}