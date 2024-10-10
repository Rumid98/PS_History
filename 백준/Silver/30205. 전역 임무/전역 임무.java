import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long p = Integer.parseInt(st.nextToken());
        boolean end = false;

        for (int i=0; i<n; i++) {
            int itemCount = 0;
            PriorityQueue<Integer> heap = new PriorityQueue<>();

            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                int curFloor = Integer.parseInt(st.nextToken());
                if (curFloor == -1) {
                    itemCount++;
                } else {
                    heap.add(curFloor);
                }
            }

            while (!heap.isEmpty()) {
                if (heap.peek() <= p) {
                    p += heap.poll();
                } else {
                    if (itemCount > 0) {
                        if (p*2 > 1000000001) {
                            p = 1000000001;
                        } else {
                            p *= 2;
                        }
                        itemCount--;
                    } else {
                        end = true;
                        break;
                    }
                }
            }
            while (itemCount > 0) {
                p *= 2;
                itemCount--;
            }

            if (end) {
                break;
            }
        }

        if (end) {
            System.out.println(0);
        } else {
            System.out.println(1);
        }

        br.close();
    }
}