class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap =[0]*256
        tmap=[0]*256
        n=len(s)
        for i in range(n):
            if smap[ord(s[i])]!=tmap[ord(t[i])]:
                return False
            smap[ord(s[i])]=i+1
            tmap[ord(t[i])]=i+1
        return True        