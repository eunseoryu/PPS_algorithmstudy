#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    
    int p_n = 0, y_n = 0;
    for(auto x : s){
        if(x =='p' || x =='P'){
            p_n ++;
        }
        else if(x =='y' || x == 'Y'){
            y_n ++;
        }
    }
    if(p_n != y_n) answer = false;

    return answer;
}