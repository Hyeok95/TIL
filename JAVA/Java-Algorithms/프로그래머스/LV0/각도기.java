class Solution {
    public int solution(int angle) {
        if (angle < 90){
            return 1;
        } if (angle == 90) {
            return 2;
        } if (angle < 180 && angle > 90) {
            return 3;
        } else {
            return 4;
        }
    }
}
