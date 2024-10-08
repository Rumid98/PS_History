import java.util.*;
import java.io.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int answer = 0;

        ArrayList<Integer>[] arr = new ArrayList[n+1];
        boolean[] visited = new boolean[n+1];

        for (int i=1; i<n+1; i++) {
            arr[i] = new ArrayList<Integer>();
        }

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b); arr[b].add(a);
        }

        for (int i=1; i<n+1; i++) {
            if (!visited[i]) {
                answer++;
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);
                visited[i] = true;
                while (!queue.isEmpty()) {
                    int curNode = queue.poll();
                    for (int x: arr[curNode]) {
                        if (!visited[x]) {
                            queue.offer(x);
                            visited[x] = true;
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}