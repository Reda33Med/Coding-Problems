class Solution:
    def isValid(self, s: str) -> bool:

        G = {"}" : "{" , ")" : "(" , "]" : "["}
        L = []

        for i in s:
            if i not in G:
                L.append(i)
            else:
                if not L or L[-1] != G.get(i):
                    return False
                
                L.pop()
        
        return not L

        