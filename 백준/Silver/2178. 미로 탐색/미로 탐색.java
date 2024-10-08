import java.util.*;
import java.io.*;


public class Main {
    static int[][] graph;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            String line = st.nextToken();
            for (int j=0; j<m; j++) {
                graph[i][j] = Integer.parseInt(String.valueOf(line.charAt(j)));
            }
        }

        System.out.println(BFS(n, m));
    }

    static int BFS(int n, int m) {
        int answer = 1;
        boolean end = false;

        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];
        queue.offer(new int[] {0, 0});
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int loopLen = queue.size();
            for (int i = 0; i < loopLen; i++) {
                int[] curNode = queue.poll();
                if (curNode[0] == n-1 && curNode[1] == m-1) {
                    end = true;
                    break;
                }
                for (int k=0; k<4; k++) {
                    int nx = curNode[0] + dx[k];
                    int ny = curNode[1] + dy[k];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && graph[nx][ny] == 1) {
                        queue.offer(new int[] {nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
            if (end) break;
            answer++;
        }

        return answer;
    }

};