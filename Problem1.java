// write a function : 
// class Solution { public int soultion (int N );}
// that , given an integer N < returns the smallest integer greater than N , the sum of whose digits is twice as big as the sum of digits of N.

// Examples : 
// 1. Given N = 14, the function should return 19 . The sum of digits of 19(1 + 9 = 10) is twice as big as sum of digits of 14 (1 + 4 = 5 ).
// 2. Given N = 10 , The function should return 11. The sum of digits of 11( 1 + 1 = 2)
// 3. Given N = 99, the function should return 9999
// Assume that :  N is an integer within the range[1.. 500].
// in your solution , foucs on correctness. The performance of your solution will not be the focus of the assesment .

class Problem1 {
   
    public static int solution(int N) {
        int normalSum = sum(N);
        int DoubleSum = 2 * normalSum;
        int result = N;
        while(true){
            result++;
            int resultSum = sum(result);
            if (resultSum == DoubleSum & result > N) {  // the second condition was not necessary since we are starting to increment from the N so it will be grater than N from the begining .
                return result;
            }
        }
    }

    public static int sum(int N) {
        int temp = N;
        int sum = 0;
        while (temp > 0) {
            int q = temp % 10;
            sum += q;
            temp = temp / 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        int n = 99;
        int result = solution(n);
        System.out.println("the result is : "+ result);
    }
}