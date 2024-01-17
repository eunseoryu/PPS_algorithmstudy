#include <string>
#include <vector>
#include <stack>
//#include <iostream>
//programmers 크레인 인형뽑기 게임

using namespace std;

int find_top(int n, vector<vector<int>>& board){
    int value;
    for(int i=0; i<board.size(); i++){
        if(board[i][n] != 0) {
            value = board[i][n];
            board[i][n] = 0;
            return value;
        }
    }
    return 0;
}

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0, temp;
    stack<int> s;
    for(int i=0; i<moves.size(); i++){
        temp = find_top((moves[i]-1),board);
        if(temp !=0 && !s.empty() && s.top() == temp){
            s.pop();
            //cout << temp << ":pop!" << endl;
            answer += 2;
        }
        else if(temp !=0){
            s.push(temp);
            //cout << s.top() << endl;
        }
    }
    
    
    return answer;
}