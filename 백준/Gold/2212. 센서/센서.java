
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        if (K >= N) {
            System.out.println(0);
            return;
        }


        String[] str = br.readLine().split(" ");
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
        Arrays.sort(arr);
        int[] distanceBetween = new int[N - 1];
        for (int i = 0; i < N-1; i++) {
            distanceBetween[i] = Math.abs(arr[i] - arr[i+1]);
        }

        Arrays.sort(distanceBetween);
        int result = 0;
        for (int i = 0; i < N-K; i++) {
            result += distanceBetween[i];
        }
        System.out.println(result);
    }

}
