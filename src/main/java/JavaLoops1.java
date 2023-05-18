
        import java.io.*;

public class JavaLoops1 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());

        for (int i = 1; i < 11; i++) {

            int multp = N*i;
            System.out.println(N + " x " + i + " = "+ multp);
        }

        bufferedReader.close();
    }
}
