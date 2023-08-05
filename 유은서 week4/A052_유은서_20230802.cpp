#include <iostream>
#include <vector>
//beakjoon 8958 OX퀴즈

using namespace std;

int main(){
    int n, plus, result;
    string str;
    bool check;

    cin >> n;

    for(int i=0; i<n; i++){
        cin >> str;
        result = 0;
        check = false;

        for(auto x: str){
            if(x == 'O' && check == false){
                check = true;
                plus = 1;          
            }
            else if(x == 'O' && check == true){
                plus ++;
            }
            else{
                check = false;
                plus = 0;
            }
            result += plus;
        }
        cout << result << '\n';
    }

    return 0;
}