    import java.io.BufferedReader;
    import java.io.IOException;

    /*
    2500이기 때문에 그냥 세면 됨
    단어를 substring으로 비교하고, 맞으면 index = index+word.length 해서 점프해버리면 됨
     */
    public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new java.io.InputStreamReader(System.in));

            String doc = br.readLine();
            String word = br.readLine();

            int index = 0;
            int count = 0;
            while(index <= doc.length() - word.length()){
                if(doc.startsWith(word, index)){
                    index += word.length();
                    count++;
                }
                else{
                    index++;
                }
            }
            System.out.println(count);
        }

    }
