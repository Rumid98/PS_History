import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for (int i=n; i>0; i--) {
            System.out.print(i + " ");
        }
    }
}