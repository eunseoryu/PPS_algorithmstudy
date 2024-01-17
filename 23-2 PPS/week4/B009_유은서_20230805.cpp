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
    int height_find(TreeNode* root) {
        if (root == nullptr)
            return 0;

        int left_height = height_find(root->left);
        int right_height = height_find(root->right);

        return max(left_height, right_height) + 1;
    }

    bool isBalanced(TreeNode* root) {
        if (root == nullptr)
            return true;

        int left_height = height_find(root->left);
        int right_height = height_find(root->right);

        if (abs(left_height - right_height) <= 1 && isBalanced(root->left) && isBalanced(root->right))
            return true;

        return false;
    }
};