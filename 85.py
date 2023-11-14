'''
https://leetcode.com/problems/validate-binary-search-tree/
'''


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sortedArray = []
        self.LCP(root, sortedArray)
        if sortedArray == sorted(list(set(sortedArray))):
            return True
        else:
            return False

    def LCP(self, root, sortedArray):
        if root.left != None:
            self.LCP(root.left, sortedArray)
        sortedArray.append(root.val)
        if root.right != None:
            self.LCP(root.right, sortedArray)