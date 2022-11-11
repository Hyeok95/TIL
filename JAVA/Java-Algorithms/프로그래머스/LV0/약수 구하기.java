class Solution {
    public int[] solution(int n) {
        int[] arry = new int[10000];
        int index =0;
       
        for(int i = 1; i<=n; i++) {
			if(n%i ==0) {
				arry[index] = i;
				index++;
			}
		}
		int[] answer = new int [index];
		for(int i = 0; i<index; i++) {
			if(arry[i] != 0) {
				answer[i] = arry[i];

			}
		}
        
       
        return answer;
    }
}
