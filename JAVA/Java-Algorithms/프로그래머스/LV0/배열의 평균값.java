class Solution {
    public double solution(int[] numbers) {
        double Sum = 0;
        double avg = 0;
        for (int i = 0; i < numbers.length; i++){
            Sum += numbers[i];
        }
        avg = Sum / (numbers.length);
        return avg;
    }
}
