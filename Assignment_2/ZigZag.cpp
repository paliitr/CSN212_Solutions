#include<iostream>
#include<cstring>

#define endl "\n"

using namespace std;

class ZigZag {
  public:
    int longestSequence(int A[]) {
      int result = 1;
      int len = sizeof(A)/sizeof(A[0]);
      int dp[len][2];
      for(int i = 0; i < len; i++) {
        dp[i][0] = 0;
        dp[i][1] = 0;
      }
      for(int i = 0; i < len; i++) {
        int j = i - 1;
        while(j >= 0) {
          if(A[j] < A[i]) {
            dp[i][0] = (dp[j][1] + 1 >= dp[i][0])? dp[j][1] + 1 : dp[i][0];
          }
          if(A[j] > A[i]) {
            dp[i][1] = (dp[j][0] + 1 >= dp[i][1])? dp[j][0] + 1 : dp[i][1];
          }
          j--;
        }
        int result0 = (dp[i][0] >= dp[i][1])? dp[i][0] : dp[i][1];
        result = (result0 >= result)? result0 : result;
      }
      return result;
    }
}

int main() {
  ios::sync_with_stdio(false);
  ZigZag problem;
  int sequence = { 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 };
  cout<<problem.longestSequence(sequence)<<endl;
}
