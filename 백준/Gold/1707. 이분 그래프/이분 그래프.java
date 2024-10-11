import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            ArrayList<Integer>[] graph = new ArrayList[v+1];
            int[] graphCheck = new int[v+1];
            boolean[] visited = new boolean[v+1];
            Queue<Integer> queue = new LinkedList<>();
            boolean end = false;

            for (int j=1; j<v+1; j++) {
                graph[j] = new ArrayList<Integer>();
            }
            for (int j=0; j<e; j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph[a].add(b);
                graph[b].add(a);
            }

            for (int x=1; x<v+1; x++) {
                if (!visited[x]) {
                    queue.offer(x);
                    graphCheck[x] = 1;
                    visited[x] = true;

                    while (!queue.isEmpty()) {
                        int curNode = queue.poll();
                        for (int k=0; k<graph[curNode].size(); k++) {
                            int nextNode = graph[curNode].get(k);
                            if (visited[nextNode]) {
                                if (graphCheck[curNode] == graphCheck[nextNode]) {
                                    end = true;
                                    break;
                                }
                            } else {
                                if (graphCheck[curNode] == 1) {
                                    graphCheck[nextNode] = 2;
                                } else {
                                    graphCheck[nextNode] = 1;
                                }
                                queue.offer(nextNode);
                                visited[nextNode] = true;
                            }
                        }
                        if (end) {
                            break;
                        }
                    }
                }
                if (end) {
                    break;
                }
            }
            if (end) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }

        br.close();
    }
}