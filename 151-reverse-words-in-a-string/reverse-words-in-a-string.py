class Solution:
    def reverseWords(self, s: str) -> str:
        prem = s.split()
        left = 0
        right = len(prem)-1
        while left < right :
            prem[left],prem[right]=prem[right],prem[left]
            left +=1
            right -=1
        return " ".join(prem)
       
        