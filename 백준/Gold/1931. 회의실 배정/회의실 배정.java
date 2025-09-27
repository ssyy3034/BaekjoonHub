
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    static class Meeting implements Comparable<Meeting> {
        int start;
        int end;

        public Meeting(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Meeting other) {
            if (this.end == other.end) {
                return this.start - other.start;
            }
            return this.end - other.end;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Meeting[] meetings = new Meeting[n];

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            int start = Integer.parseInt(input[0]);
            int end = Integer.parseInt(input[1]);
            meetings[i] = new Meeting(start, end);
        }

        Arrays.sort(meetings); // 종료 시간 기준 정렬

        int count = 0;
        int lastEnd = 0;

        for (Meeting m : meetings) {
            if (m.start >= lastEnd) {
                count++;
                lastEnd = m.end;
            }
        }

        System.out.println(count);
    }
}
