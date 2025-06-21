
/*
1. 주식을 사거나
2. 주식을 팔거나
3. 아무것도 안하거나

입력 받는건
총 테스트 갯수 받기

테스트 갯수만큼 반복
{ 테스트 갯수 입력
태스트 케이스 입력
차익 계산 후 출력 }


리스트로 받고 순회하면서 a[i]가 a[i+1]보다 작거나 같다면 주식을 산다.(같으면 count로 주식 수 더함)
더 크다면 차익 실현
차익 계산후 출력

 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int testCount = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            int[] prices = new int[testCount];
            for (int j = 0; j < testCount; j++) {
                prices[j] = Integer.parseInt(st.nextToken());
            }
            long profit = 0;
            long maxPrice = 0;
            for (int j = testCount - 1; j >= 0; j--) {
                if (prices[j] > maxPrice) {
                    maxPrice = prices[j];
                } else {
                    profit += maxPrice - prices[j];
                }
            }
            System.out.println(profit);
        }
    }
}
