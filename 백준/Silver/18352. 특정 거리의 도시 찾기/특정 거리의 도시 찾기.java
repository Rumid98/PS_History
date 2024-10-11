import java.util.*;
import java.io.*;


public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        ArrayList<Integer> answer = new ArrayList<>();

        graph = new ArrayList[n+1];
        visited = new boolean[n+1];
        for (int i=1; i<n+1; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(x);
        visited[x] = true;
        int count = 0;
        while (!queue.isEmpty()) {
            if (count == k) {
                while (!queue.isEmpty()) {
                    answer.add(queue.poll());
                }
                break;
            }
            int loopLen = queue.size();
            for (int j=0; j<loopLen; j++) {
                int curNode = queue.poll();
                for (int o=0; o<graph[curNode].size(); o++) {
                    int nextNode = graph[curNode].get(o);
                    if (!visited[nextNode]) {
                        queue.offer(nextNode);
                        visited[nextNode] = true;
                    }
                }
            }
            count++;
        }

        if (answer.isEmpty()) {
            System.out.println(-1);
        } else {
            Collections.sort(answer);
            for (int i=0; i<answer.size(); i++) {
                System.out.println(answer.get(i));
            }
        }

        br.close();
    }
}