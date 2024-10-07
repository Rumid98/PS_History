import java.util.*;
import java.io.*;


public class Main {
    static class Node {
        public int idx;
        public int val;

        Node(int idx, int val) {
            this.idx = idx;
            this.val = val;
        }
    }

    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        Deque<Node> queue = new LinkedList();
        ArrayList<Integer> answer = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i=0; i<n; i++) {
            // deque 좌측 idx 값이 i-L+1을 벗어난 경우 -> remove
            if (!queue.isEmpty() && queue.getFirst().idx < i-l+1) {
                queue.removeFirst();
            }
            // i번째 idx값 받기
            int curNode = Integer.parseInt(st.nextToken());
            // 현재 idx에 해당하는 값보다 큰 값이 deque에 있는 경우 -> remove / 작거나 같은 경우 -> add
            while (!queue.isEmpty()) {
                if (curNode < queue.getLast().val) {
                    queue.removeLast();
                } else {
                    break;
                }
            }
            queue.addLast(new Node(i, curNode));

            // deque 좌측 Node의 val 값이 Di
            bw.write(queue.getFirst().val + " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}