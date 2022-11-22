import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String str = my_string.toLowerCase();
        char[] arr = str.toCharArray();
        
        Arrays.sort(arr);
        String str2 = new String(arr);
        
        return str2;
    }
}
