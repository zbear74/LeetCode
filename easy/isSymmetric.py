# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
 
 
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
    ## symmetric node
    def isSymmetricNode(self,a:[TreeNode],b:[TreeNode]) -> bool:
        if a == None and b == None:
            return True
        if (a.val == b.val) and ( 
                                 (a.left == None and b.right == None and a.right == None and b.left == None ) or  
                                 (a.left == None and b.right == None and a.right != None and b.left != None) or 
                                 (a.left != None and b.right != None and a.right == None and b.left == None ) or  
                                 (a.left != None and b.right != None and a.right != None and b.left != None)
                                 ):
            return True
        else : 
            return False
    
    def isSymmetric(self, root:TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        elif root.left != None and root.right != None:
            ## go to by tree
            curr_left = root.left
            curr_right = root.right
            next_path_left = []
            next_path_right = []
            flag_down = True
            flag_left = True
            flag_right = False
               
            l = 0
            r = 0
            ## symmetric path
            while (curr_left != None and curr_right !=None) or len(next_path_left) > 0:               
                
                if self.isSymmetricNode(curr_left,curr_right) == False:
                    return False
                
                if curr_left.right != None and curr_right.left != None:
                    next_path_left.append(curr_left.right)
                    next_path_right.append(curr_right.left)    
                                                
                if curr_left.left != None and curr_right.right != None :
                    curr_left = curr_left.left
                    curr_right = curr_right.right
                    continue
                
                if len(next_path_left) > 0:
                    curr_left = next_path_left.pop()
                    curr_right = next_path_right.pop()
                    continue
                
                return True
                
        else:
            return False
        ### finaly
        return True

     


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
sx = Solution().isSymmetric(x1)     
print("Result: ",sx)


print("\nInput: ")
y1.printTreeNode()
sx = Solution().isSymmetric(y1)     
print("Result: ",sx)


print("\nInput: ")
m2.printTreeNode()
sx = Solution().isSymmetric(m2)     
print("Result: ",sx)

