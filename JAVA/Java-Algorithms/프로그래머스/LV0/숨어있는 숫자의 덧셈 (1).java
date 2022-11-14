import java.util.Arrays;

class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String intStr = my_string.replaceAll("[^\\d]", "");
        
        for (int i = 0; i<intStr.length(); i++){
            answer += (intStr.charAt(i) - '0');
        }
        
        return answer;
    }
}
