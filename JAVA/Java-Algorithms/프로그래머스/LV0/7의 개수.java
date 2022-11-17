class Solution {
    public int solution(int[] array) {
        int answer = 0;
        String num = "";
        
        for (int i=0; i<array.length; i++){
            num += array[i];
        }
        char[] strChar = num.toCharArray();
        
        for (int i=0; i<strChar.length; i++){
            if (strChar[i] == '7'){
                answer +=1;
            }
        }
        
        return answer;
    }
}
