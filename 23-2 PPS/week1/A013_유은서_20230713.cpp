#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> countMap;

        for (int num : nums) {
            countMap[num]++;
        }

        for (auto pair : countMap) {
            if (pair.second == 1) {
                return pair.first;
            }
        }

        return -1; // 에러 처리
    }
};
