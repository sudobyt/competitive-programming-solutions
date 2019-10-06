class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        length=len(A)//2
        
        max_ele=max(A)
        aux=[0]*(max_ele+1)
        for el in A:
            aux[el]+=1
        
        ma=max(aux)
        return aux.index(ma)
