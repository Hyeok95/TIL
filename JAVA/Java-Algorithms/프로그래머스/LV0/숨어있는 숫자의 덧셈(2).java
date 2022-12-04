class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        String[] num = my_string.replaceAll("[^0-9]", " ").split(" ");
        System.out.print(num);
        
        for (int i = 0; i<num.length; i++){
            if(num[i].equals("")){
                continue;
            } else {
                answer += Integer.parseInt(num[i]);
            }
        }
        
        return answer;
    }
}
