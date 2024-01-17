#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    sort(arr.begin(), arr.end());
    
    for(auto x : arr){
        if(x % divisor == 0){
            answer.push_back(x);
        }
    }
    if(answer.empty()) answer.push_back(-1);
    
    return answer;
}