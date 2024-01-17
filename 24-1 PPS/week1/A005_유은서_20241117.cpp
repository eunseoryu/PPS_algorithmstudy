#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    for (int i = 0; i < skill_trees.size(); i++) {
        bool valid = true;
        int prev_idx = -1;

        for (auto x : skill_trees[i]) {
            int curr_idx = skill.find(x);

            if (curr_idx != string::npos) {
                if (curr_idx != prev_idx + 1) {
                    valid = false;
                    break;
                }

                prev_idx = curr_idx;
            }
        }

        if (valid) {
            answer++;
        }
    }

    return answer;
}