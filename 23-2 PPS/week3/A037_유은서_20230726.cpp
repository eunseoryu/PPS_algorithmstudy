class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> v;
        int temp, a;
        bool isselfdiv = true;
        for(int i= left; i<= right; i++){
            isselfdiv = true;
            a = i;
            while(a > 0){
                temp = a%10;
                a = a/10;
                if(temp == 0 ||i%temp != 0) {
                    isselfdiv = false;
                    break;
                }
            }
            if(isselfdiv == true) v.push_back(i);
        }
        return v;
    }
};