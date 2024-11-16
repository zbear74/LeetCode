# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        
        
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
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        result = True
        if p == None and q == None:
            return True
        if (p == None and q != None) or ( p != None and q == None):
            return False
        
        # cur1 = p
        # cur2 = q
        
        if (p.val == q.val): #or ( p.val is None and q.val is None):
            if p.left != None and q.left != None:
                result = self.isSameTree(p.left,q.left)
                if result == False:
                    return False
            if p.right != None and q.right != None:
                result = self.isSameTree(p.right,q.right)
                if result == False:
                    return False             
            if (p.left == None and q.left != None) or (p.left != None and q.left == None) or (p.right == None and q.right != None) or (p.right != None and q.right == None):
                return False    
            
        else:
            return False
        
        return result 
        
      
      
      
        
        
x1 = TreeNode(1,None,None)
x2 = TreeNode(9,x1,None)
x3 = TreeNode(3,None,x2)
x4 = TreeNode(2,x3,None)
x5 = TreeNode(8,None,None)
x6 = TreeNode(6,x5,None)
x7 = TreeNode(7,None,None)
x8 = TreeNode(5,x7,x6)
x9 = TreeNode(4,x4,x8)

k1 = TreeNode(2,None,None)
k2 = TreeNode(1,k1,None)

y1 = TreeNode(2,None,None)
y2 = TreeNode(1,None,y1)

z = None

# case 4
l2 = TreeNode(2,None,None)
l3 = TreeNode(3,None,None)
l1 = TreeNode(1,l2,l3)


m2 = TreeNode(2,None,None)
m3 = TreeNode(3,None,None)
m1 = TreeNode(1,m2,m3)


# case 5
n5 = TreeNode(5,None,None)
n4 = TreeNode(4,n5,None)
n3 = TreeNode(3,None,None)
n2 = TreeNode(2,n3,n4)
n1 = TreeNode(1,n2,None)

o3 = TreeNode(3,None,None)
o2 = TreeNode(2,o3,None)
o1 = TreeNode(1,o2,None)




# print("\nInput: ")
# k2.printTreeNode()
# print("\nInput: ")
# y2.printTreeNode()

sx = Solution().isSameTree(n1,o1)     
print("Result: ",sx)

