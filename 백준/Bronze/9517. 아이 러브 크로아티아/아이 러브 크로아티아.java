import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());

        int timeTotal= 0;
        for (int i=1; i<n+1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int time = Integer.parseInt(st.nextToken());
            String c = st.nextToken();
            if (timeTotal + time > 210) {
                break;
            }
            if (c.equals("T")) {
                timeTotal += time;
                k++;
            } else {
                timeTotal += time;
            }
            
            if (k > 8) k = 1;
        }

        System.out.println(k);
        br.close();
    }
}