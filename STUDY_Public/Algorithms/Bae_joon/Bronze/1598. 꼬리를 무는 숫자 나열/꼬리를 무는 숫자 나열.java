import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        final int n1 = Integer.parseInt(st.nextToken());
        final int n2 = Integer.parseInt(st.nextToken());

        // 계산
        final int x1 = (n1 - 1) / 4 + 1;
        final int x2 = (n2 - 1) / 4 + 1;
        final int y1 = (n1 - 1) % 4;
        final int y2 = (n2 - 1) % 4;
        final int distance = (Math.abs(x2 - x1) + Math.abs(y2 - y1));

        // 출력
        System.out.println(distance);

        br.close();
    }
}