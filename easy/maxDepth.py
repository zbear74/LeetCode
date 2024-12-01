# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def printTreeNode(self):
        if self != None:
            print(self.val)
        if (self.left is not None):
            self.left.printTreeNode()
        if (self.right is not None):
            self.right.printTreeNode()

class Solution:
    
    left = 0
    right= 0
    
    
    def maxDepth(self, root: [TreeNode]) -> int:
                
        if root == None:
            return 0        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1 
        








xr3 = TreeNode(3,None,None)
xr4 = TreeNode(4,None,None)
xl4 = TreeNode(4,None,None)
xl3 = TreeNode(3,None,None)
xr2 = TreeNode(2,xr4,xr3)
xl2 = TreeNode(2,xl3,xl4)
x1 = TreeNode(1,xl2,xr2)

yl = TreeNode(2,None,None)
yr = TreeNode(2,None,None)
y1 = TreeNode(1,yl,yr)




ml9 = TreeNode(9,None,None)
mr9 = TreeNode(9,None,None)
ml8 = TreeNode(8,None,None)
mr8 = TreeNode(8,None,None)
ml6 = TreeNode(6,None,None)
mr6 = TreeNode(6,None,None)
ml5 = TreeNode(5,ml8,ml9)
mr5 = TreeNode(5,mr9,mr8)
ml4 = TreeNode(4,ml6,None)
mr4 = TreeNode(4,None,mr6)
ml3 = TreeNode(3,ml4,ml5)
mr3 = TreeNode(3,mr5,mr4)
m2 = TreeNode(2,ml3,mr3)




print("\nInput: ")
x1.printTreeNode()
sx = Solution().maxDepth(x1)     
print("Result: ",sx)


print("\nInput: ")
y1.printTreeNode()
sx = Solution().maxDepth(y1)     
print("Result: ",sx)


print("\nInput: ")
m2.printTreeNode()
sx = Solution().maxDepth(m2)     
print("Result: ",sx)

        
        
        
        
        
        
        
