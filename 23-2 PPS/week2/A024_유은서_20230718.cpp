class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0, twenty = 0;
        for (auto x: bills){
            if(x == 5) five ++;
            else if(x == 10) {
                ten ++;
                if(five > 0) five --;
                else return false;
            }
            else{
                if(five > 0 && ten > 0){
                    five --;
                    ten --;
                } 
                else if(five > 2){
                    five = five -3;
                }
                else return false;
            }
        }
        return true;
    }
};