#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 1;
    
    int temp = section[0];
    
    for (const auto v: section){
        if (v < temp + m){
            continue;
        }
    
        else{
            temp = v;
            answer+=1;
        }
    }
    return answer;
}