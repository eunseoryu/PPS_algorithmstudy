#include <iostream>
using namespace std;

int main(){
    int num;
    int cnt[26] = {0}, count=0;
    string temp, result;
    cin>> num;

    for(int i=0; i<num; i++){
        cin >> temp;
        if(temp[0]<97) cnt[temp[0] - 65]++; 
        else cnt[temp[0] - 97]++; 
    }

    for(int i=0; i<26; i++){
        if(cnt[i] >= 5){
            result += (char)(i+'a');
            count ++;
        }
    }
    if(count != 0) cout << result;
    else cout << "PREDAJA";
    

    return 0;
}