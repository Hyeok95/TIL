import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
            
        for (int i=0; i<numbers.length; i++){
            answer = numbers[numbers.length-1] * numbers[numbers.length-2];
        }
        return answer;
    }
}
