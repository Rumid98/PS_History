import java.util.*;
import java.io.*;


public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[] numbers;
    static int n;
    static int m;

    public static void recursion(int count, int[] result) throws IOException {
        if (count == m) {
            for(int i=0 ; i<m; i++) {
                bw.write(result[i] + " ");
            }
            bw.write("\n");
            return;
        }
        for (int i=1; i<n+1; i++) {
            result[count] = i;
            recursion(count + 1, result);
        }
    }

    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        numbers = new int[n+1];
        for (int i=1; i<n+1; i++) {
            numbers[i] = i;
        }

        recursion(0, new int[8]);
        br.close();
        bw.flush();
        bw.close();
    }
}