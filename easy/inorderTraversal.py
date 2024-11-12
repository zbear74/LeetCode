# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

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
    def inorderTraversal(self, root:[TreeNode]) -> list[int]:
      
      result = []
      goDown = True     
      current = root
      prev_root = []          
      node = None
      
      if root == None: 
        return result
      
      
      while current.left != None or current.right != None or len(prev_root) != 0  or (current.left == None and current.right == None):
        
        # if left not None => go next
        if current.left != None and goDown == True:
          prev_root.append(current)   # save cur as prev_root
          current = current.left
          goDown = True
          continue # go next left
        
        if goDown == True:
          result.append(current.val)        
        
        if current.right != None:
          
          current = current.right
          goDown = True
          continue        
        
        else:
          if len(prev_root) > 0:
            node = prev_root.pop()
            current = node
            result.append(node.val)
            goDown = False
          else:
            break               
                
        
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

y = None


print("\nInput: ")
x1.printTreeNode()
sx = Solution().inorderTraversal(x1)     
print("Result: ",sx)

print("\nInput: ")
x9.printTreeNode()
sx = Solution().inorderTraversal(x9)     
print("Result: ",sx)


print("\nInput: None")
sx = Solution().inorderTraversal(y)     
print("Result: ",sx)

