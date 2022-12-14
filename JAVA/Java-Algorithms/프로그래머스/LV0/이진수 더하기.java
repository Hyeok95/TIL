class Solution {
    public String solution(String bin1, String bin2) {
        long answer = Long.parseLong(bin1, 2) + Long.parseLong(bin2, 2);

        return Long.toBinaryString(answer);
    }
}
