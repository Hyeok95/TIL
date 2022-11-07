class Solution {
    public String solution(String rsp) {
        String answer = "";
        
        for (int i = 0; i<rsp.length(); i++){
            answer += (rsp.split("")[i].equals("0") ? "5"
                       : rsp.split("")[i].equals("2") ? "0"
                        : rsp.split("")[i].equals("5") ? "2" : "9");
        }
        
        return answer;
    }
}
