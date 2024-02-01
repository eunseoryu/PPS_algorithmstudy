#include <bits/stdc++.h>

using namespace std;

string solution(string s) {
    string answer = "", tmp;
    vector<string> v;
    
    for(int i=0; i<s.length(); i++){
        tmp = s[i];

        if(islower(s[i])){
            if(i==0) tmp = toupper(s[i]);
            if(i>0&&s[i-1]==' ') tmp = toupper(s[i]);
        }
        else if(i>0&&isupper(s[i])&&(s[i-1]!=' ')){
            tmp = tolower(s[i]);
        } 

        v.push_back(tmp);
    }
    while(!v.empty()){
        answer += v.back();
        v.pop_back();
    }
    reverse(answer.begin(), answer.end());
           
    return answer;
}