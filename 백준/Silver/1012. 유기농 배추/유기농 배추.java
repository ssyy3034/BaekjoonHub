
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class Main {
    /*
    입력을 N으로 받음
    N만큼 반복하며 공백을 구분하여 밭 크기, 배추 갯수 받음
    배추 갯수만큼 반복하며 밭에 배추 위치 할당, 배추 위치는 1로 설정

    입력 완료된 밭을 순회하며 만약 배추를 만날경우, 0으로 바꾸고 count++
    인접 배추 전부 순회하는법을 모르겠음
    순회 끝나면 카운트 출력
     */
    public static void dfs(int[][] field, int x, int y, int M, int N) {
        // 범위를 벗어나면 리턴
        if (x < 0 || x >= M || y < 0 || y >= N) return;
        // 배추가 아니면 리턴
        if (field[x][y] == 0) return;

        field[x][y] = 0; // 방문 처리

        // 상하좌우 탐색
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        for (int i = 0; i < 4; i++) {
            dfs(field, x + dx[i], y + dy[i], M, N);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 갯수 받았음

        for(int i = 0; i < T; i++){ // 공백을 구분하여 테스트 밭 크기, 배추 갯수 받음.
            StringTokenizer st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            int[][] field = new int[M][N];
            for(int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                field[x][y] = 1;
            }

            int count = 0;
            for(int x = 0;x<M;x++){
                for(int y =0;y<N;y++){
                    if(field[x][y] == 1){
                        dfs(field, x, y,M,N);
                        count++;
                        }
                    }
                }
            System.out.println(count);
            }
        }
    }
