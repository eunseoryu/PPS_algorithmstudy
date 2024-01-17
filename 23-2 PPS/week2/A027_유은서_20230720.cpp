#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    vector<char> v;

    for (auto x : number) {
        v.push_back(x);
    }

    int idx = 0;
    int len = number.size() - k;

    for (int i = 0; i < len; i++) {
        char maxNum = v[idx];
        int maxIdx = idx;

        for (int j = idx; j <= k + i; j++) {
            if (maxNum < v[j]) {
                maxNum = v[j];
                maxIdx = j;
            }
        }

        idx = maxIdx + 1;
        answer += maxNum;
    }

    return answer;
}
