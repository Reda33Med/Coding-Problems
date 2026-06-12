class Solution:
    def isValid(self, s: str) -> bool:

        G = {"}" : "{" , ")" : "(" , "]" : "["}
        L = []

        for i in s:
            if i not in G:
                L.append(i)
            else:
                if (len(L) == 0) or (L[-1] != G.get(i)):
                    return False
                
                L.pop()
        
        if len(L)>0:
            return False
        else:
            return True

        