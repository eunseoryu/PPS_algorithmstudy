#include <iostream>
//beakjoon 5622 다이얼

using namespace std;

int main(){
    int n, result = 0;
    string str;

    cin >> str;

    for(int i=0; i<str.length(); i++){
        result += 2+ ((str[i]-62)/3)*1;
        if(str[i] == 'S' ||str[i] == 'V' ||str[i]== 'Y' ||str[i] == 'Z' ) result--;
    }
    cout << result;
    return 0;
}