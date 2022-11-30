class Solution {
    public int solution(int num, int k) {
        int answer = 0;
        String strNum = String.valueOf(num);
        String strK = String.valueOf(k);
        
        if(strNum.indexOf(strK) == -1){
            return -1;
        } else {
            return strNum.indexOf(strK) +1;
        }
    }
}
