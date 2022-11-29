import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int index = 0 ;
        
        Arrays.sort(array);
        
        for (int i=0; i<array.length; i++){
            if (Math.abs(n-array[index]) > Math.abs(n-array[i])){
                index = i;
            }
        }
        
        return array[index];
    }
}
