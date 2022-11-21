//최대공약수
class GCD {
    public static int getGCD(int num1, int num2){
        if (num1 % num2== 0){
            return num2;
        }
        return getGCD(num2, num1%num2); //나머지가 있으면 다시 GCD메소드로 들어감 (재귀)
    }
}

class Solution {
    public int solution(int n) {
        int answer = 0;
        int gcd = GCD.getGCD(n,6);
        int lcm = n*6 / gcd; //최소공배수
        answer = lcm/6;
        return answer;
    }
}
