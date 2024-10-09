import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        long answer = 1;
        for (int i=2; i<n+1; i++) {
            answer = answer * i % p;
        }

        System.out.println(answer);
        br.close();
    }
}