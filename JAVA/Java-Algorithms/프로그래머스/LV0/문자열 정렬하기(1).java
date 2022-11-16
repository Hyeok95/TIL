import java.util.*;
class Solution {
    public int[] solution(String my_string) {
      char[] arry = my_string.toCharArray();
		String filter = "";
		
		//a ~ z = 97 ~ 122
		//0~9 = 48 ~ 57
		for(int i = 0; i<arry.length; i++) {
			if(arry[i] >=48 &&  arry[i] <= 57) {
				filter += arry[i];
			}
		}
		int[] answer = new int [filter.length()];
		String [] transfer = new String [filter.length()];
		for(int i = 0; i<filter.length(); i++) {
			transfer[i]= filter.charAt(i) + "";
			answer[i] = Integer.parseInt(transfer[i]);
		}  
        
        Arrays.sort(answer);
        return answer;
    }
}
