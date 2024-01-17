class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(s.begin(), s.end());
        sort(g.begin(), g.end());

        int res = 0;
        int i = 0, j = 0;
        
        while((i < g.size()) && (j < s.size())){
            if(s[j] >= g[i]){
                i++;
            }
            j++;
        }
        res = i;

        return res;
    }
};