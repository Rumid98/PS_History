import java.util.*;
import java.io.*;


public class Main {
    static int n;
    static int m;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static int[][] graph;
    static boolean[][] visited;

    static class Node {
        public int x;
        public int y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static int bfs(int x, int y) {
        int count = 1;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(x, y));
        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            for (int k=0; k<4; k++) {
                int nx = curNode.x + dx[k];
                int ny = curNode.y + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < m && graph[nx][ny] == 1 && !visited[nx][ny]) {
                    count++;
                    visited[nx][ny] = true;
                    queue.offer(new Node(nx, ny));
                }
            }
        }

        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int answer = 0;
        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i=0; i<k; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[r-1][c-1] = 1;
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (graph[i][j] == 1) {
                    visited[i][j] = true;
                    int result = bfs(i, j);
                    if (result > answer) answer = result;
                }
            }
        }

        System.out.println(answer);
        br.close();
    }
}