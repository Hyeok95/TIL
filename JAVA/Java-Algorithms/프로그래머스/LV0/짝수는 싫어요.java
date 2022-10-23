class Solution {
    public int[] solution(int n) {
        int[] answer = new int[n/2];
        
        int cnt = 0;
        
        for (int i = 0; i <n; i++){
            if (i % 2 == 1){
                answer[cnt] = i;
                cnt++;
            }
        }
        
        return answer;
    }
}
