import java.util.*;
import java.io.*;


public class Main {
    public static long counter(char[] word) {
        long result = 1;
        int count = 0;
        boolean prev = false;

        for (int i=0; i<word.length; i++) {
            count++;
            if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') {
                if (prev) {
                    result = (result * count % 1000000007);
                } else {
                    prev = true;
                }
                count = 0;
            }
        }

        if (!prev) {
            result = -1;
        }

        return result % (1000000007);
    }


    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            char[] word = br.readLine().toCharArray();
            bw.write(counter(word) + "\n");
        }

        br.close();
        bw.flush();
        bw.close();
    }
}