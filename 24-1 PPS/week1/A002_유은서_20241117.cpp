class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        vector<int> v;
        vector<int> temp;

        while(triangle.size() < numRows){

            v.push_back(1);
            
            

            if(triangle.size() != 0) {
                temp = triangle.back();
                for(int i=0; i<(temp.size() - 1); i++){
                    if(temp.size() > 1)
                        v.push_back(temp[i] + temp[i+1]);
                }
                v.push_back(1);
            }
            

            triangle.push_back(v);
            v.clear();
        }
        return triangle;
    }
};