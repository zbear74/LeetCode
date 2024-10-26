# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
     

   
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        #print("define = ",val)
    
    def printListNode(self):
        print(self.val)
        if ( self.next is not None):
            self.next.printListNode()
    

class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        start = head
        if head == None:
            return start 
        
        while head.next is not None:                      
            if head.val == head.next.val:                
                head.next = head.next.next
            else: 
                head = head.next
            if head == None:
                return start 
        return start


# EXAMPLES TEST

a3=ListNode(2)       
a2=ListNode(1,a3)        
a1=ListNode(1,a2)  


x5=ListNode(3)
x4=ListNode(3,x5)
x3=ListNode(2,x4)
x2=ListNode(1,x3)
x1=ListNode(1,x2)

y3=ListNode(2)       
y2=ListNode(2,y3)        
y1=ListNode(1,y2)  


print("**********")


a1.printListNode()    
print("==")
x1.printListNode() 
print("==")
y1.printListNode() 

d = Solution().deleteDuplicates(a1)
print("= RESULT =")
d.printListNode() 

d = Solution().deleteDuplicates(x1)
print("= RESULT =")
d.printListNode() 


d = Solution().deleteDuplicates(a3)
print("= RESULT =")
d.printListNode() 

d = Solution().deleteDuplicates(y1)
print("= RESULT =")
d.printListNode() 
 
    
    
       
        
    
    

            
        
        