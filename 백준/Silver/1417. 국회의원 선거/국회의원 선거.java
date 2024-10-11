import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int dasom = Integer.parseInt(br.readLine());
        
        if (n==1) {
            System.out.println(0);
        } else {
            int answer = 0;
            PriorityQueue<Integer> heap = new PriorityQueue<>();
            for (int i=0; i<n-1; i++) {
                heap.offer(-Integer.parseInt(br.readLine()));
            }

            while (true) {
                if (dasom > -heap.peek()) {
                    break;
                } else {
                    dasom++;
                    answer++;
                    heap.offer(heap.poll()+1);
                }
            }

            System.out.println(answer);
        }
        
        br.close();
    }
}