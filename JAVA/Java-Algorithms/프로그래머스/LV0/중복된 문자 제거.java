class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for (int i=0; i<my_string.length(); i++){
            char temp = my_string.charAt(i);
                
            if (my_string.indexOf(temp) == i){
                    answer += temp;
            }
        }
        
        return answer;
    }
}
