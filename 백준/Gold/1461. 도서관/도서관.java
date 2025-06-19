import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 책 수
        int M = Integer.parseInt(st.nextToken()); // 한 번에 옮길 수 있는 최대 책 수

        // 양수/음수 리스트 구분
        List<Integer> pos = new ArrayList<>();
        List<Integer> neg = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(st.nextToken());
            if (x > 0) pos.add(x);
            else neg.add(-x); // 음수는 절댓값으로 저장
        }

        // 내림차순 정렬 (가장 먼 거리부터 처리)
        Collections.sort(pos, Collections.reverseOrder());
        Collections.sort(neg, Collections.reverseOrder());

        int maxDist = 0;
        if (!pos.isEmpty()) maxDist = Math.max(maxDist, pos.get(0));
        if (!neg.isEmpty()) maxDist = Math.max(maxDist, neg.get(0));

        int total = 0;

        // 양수 처리
        for (int i = 0; i < pos.size(); i += M) {
            total += pos.get(i) * 2;
        }

        // 음수 처리
        for (int i = 0; i < neg.size(); i += M) {
            total += neg.get(i) * 2;
        }

        // 가장 먼 거리만 편도로
        total -= maxDist;

        System.out.println(total);
    }
}
