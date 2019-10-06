# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class newList:
    def __init__(self):
        self.head=None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        current=A
        length=0
        while current!=None:
            length+=1
            current=current.next
        mid=length//2
        
        j=1
        current=A
        while j<mid:
            j+=1
            current=current.next
        halfList=current.next
        current.next= None
        
        
        
        current=halfList
        prev=None
        while current!=None:
            next=current.next
            current.next=prev
            prev=current
            current=next
            
        halfList=prev
            
        
        currentA=A
        currentHalf=halfList
        
        while currentA!=None and currentHalf!=None:
            print (currentA.val)
            temp=currentHalf.next
            currentHalf.next=currentA.next
            currentA.next=currentHalf
            currentA=currentHalf.next
            currentHalf=temp
            
        
        if currentA==None:
            currentA.next=currentHalf
        
        return A
            
        
