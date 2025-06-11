
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

/*
입력은 최대 10000개, 팀 수는 5000개
공백으로 분리돼서 주어짐
정렬후 조 갯수에 따라 맨앞+맨끝 평균 전부 구하고, 최소값 min으로 놓고 갱신


 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] numbers = new int[input.length];

        for (int i = 0; i < input.length; i++) {
            numbers[i] = Integer.parseInt(input[i]);
        }
        Arrays.sort(numbers);
        int min = numbers[0]+numbers[numbers.length-1];
        for(int i=0; i<n; i++){
            int score = numbers[numbers.length-1-i]+numbers[i];
            if(score<min){
                min = score;
            }
        }
        System.out.println(min);
    }
}
