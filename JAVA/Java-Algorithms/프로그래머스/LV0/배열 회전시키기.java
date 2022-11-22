class Solution {
    public int[] solution(int[] numbers, String direction) {
        int[] answer = new int[numbers.length];
        int first = numbers[0];
        int last = numbers[numbers.length-1];
        
        if (direction.equals("right")){
            answer[0] = last;
            for (int i=numbers.length-2; i>=0; i--){
                answer[i+1] = numbers[i];
            }
        } else {
            answer[0] = numbers[1];
            for (int i=numbers.length-2; i>=1; i--){
                answer[i] = numbers[i+1];
            }
            answer[numbers.length-1] = first;
        }
        
        return answer;
    }
}
