/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void solve(TreeNode* root, vector<int> &bst){
        if(root==NULL){
            return;
        }
        solve(root->left, bst);
        bst.push_back(root->val);
        solve(root->right, bst);
    }
    bool findTarget(TreeNode* root, int k) {
        vector<int>bst;
        solve(root, bst);
        int s=0,e=bst.size()-1;
        int sum=0;
        while(s<e)
        {
            sum=bst[s]+bst[e];
            if(sum==k)
                return true;
            else if (sum>k)
                e--;
            else
                s++;
        }
        return false;
    }
};