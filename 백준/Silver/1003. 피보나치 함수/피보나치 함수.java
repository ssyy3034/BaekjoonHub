

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        int[][] dp = new int[41][2]; // dp[n][0]: 0 호출 횟수, dp[n][1]: 1 호출 횟수

        dp[0][0] = 1; dp[0][1] = 0;
        dp[1][0] = 0; dp[1][1] = 1;

        for (int i = 2; i <= 40; i++) {
            dp[i][0] = dp[i-1][0] + dp[i-2][0];
            dp[i][1] = dp[i-1][1] + dp[i-2][1];
        }
        for(int i =0;i<testCase;i++){
            int num = Integer.parseInt(br.readLine());
            System.out.println(dp[num][0]+" "+dp[num][1]);
        }
    }
}
