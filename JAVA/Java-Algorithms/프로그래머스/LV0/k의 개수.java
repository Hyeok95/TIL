class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for (int a = i; a <= j; a++ ){
            StringBuilder sb = new StringBuilder();
            sb.append(a);

            for (int b = 0; b < sb.length(); b++) {
                if ((sb.charAt(b) - '0') == k) {
                    answer++;
                }
            }
        }
        return answer;
    }
}
