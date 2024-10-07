import java.util.*;


public class Main {
    static float solution(int n, int[] arr) {
        float result = 0;
        int max_score = 0;
        for (int i=0; i<n; i++) {
            if (arr[i] > max_score) max_score = arr[i];
        }
        for (int i=0; i<n; i++) {
            result += ((float)arr[i] / max_score * 100);
        }

        return result / n;
    }


    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        int n = scn.nextInt();
        int[] score = new int[n];
        for (int i=0; i<n; i++) {
            score[i] = scn.nextInt();
        }

        System.out.println(solution(n, score));
    }
}