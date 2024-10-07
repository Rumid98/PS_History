import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i=0; i<n; i++) {
            heap.offer(Integer.parseInt(br.readLine()));
        }

        int answer = 0;
        for (int i=0; i<n; i++) {
            int curMaxWeight = heap.poll() * (n - i);
            if (curMaxWeight > answer) {
                answer = curMaxWeight;
            }
        }
        System.out.println(answer);
        br.close();
    }
}