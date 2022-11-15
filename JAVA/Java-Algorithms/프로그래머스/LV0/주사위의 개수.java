class Solution {
    public int solution(int[] box, int n) {
        
        int a = box[0] / n;
        int b = box[1] / n;
        int c = box[2] / n;
        
        int answer = a*b*c;
        
        return answer;
    }
}
