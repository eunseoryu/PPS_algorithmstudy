#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    string str = "";
    int count[2] = {};
    cin >> str;

    for(int i=0; i<str.size(); i++){
        if(str[i] != str[i+1]){
            count[str[i]-'0']++;
        }
    }

    cout << min(count[0], count[1]);
    return 0;
}