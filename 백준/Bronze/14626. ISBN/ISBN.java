

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String isbn = br.readLine();


        int missingIndex = isbn.indexOf('*');

        for(int i = 0; i <=9; i++) {
            StringBuilder sb = new StringBuilder(isbn);
            sb.setCharAt(missingIndex,(char)(i+'0'));

            int sum = 0;
            for (int j = 0; j < 13; j++) {
                int digit = sb.charAt(j) - '0';
                if (j % 2 == 0) {
                    sum += digit;         // 짝수 인덱스: 1 × digit
                } else {
                    sum += 3 * digit;     // 홀수 인덱스: 3 × digit
                }

            }
            if (sum % 10 == 0) {
                System.out.println(i);
                break;
            }


        }
    }
}
