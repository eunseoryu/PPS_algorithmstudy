//programmers - 쿠키구입
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> cookie) {
    int answer = 0;
    
    int left_sum, right_sum, l_idx, r_idx;
    for(int i = 0; i < cookie.size() - 1; i++){
        left_sum = cookie[i];
        right_sum = cookie[i + 1];
        l_idx = i;
        r_idx = i + 1;

        while(true){

            if(left_sum == right_sum)
                answer = max(answer, left_sum);

            if(left_sum > right_sum){
                if(r_idx + 1 == cookie.size()) break;
                right_sum += cookie[++r_idx];
            }
            else{
                if(l_idx - 1 < 0) break;
                left_sum += cookie[--l_idx];
            }            

        }
    }

    return answer;
}