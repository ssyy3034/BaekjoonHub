import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

/*
정렬한 다음, 1씩 증가하는 수 만들어서 절댓값 더함(불만도)
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        long sum = 0;
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        for(int i=0; i<N; i++){
            sum += Math.abs(arr[i]-(i+1));
        }
        System.out.println(sum);
    }
}
