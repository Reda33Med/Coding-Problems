class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) :
            return False
        listS = sorted(list(s))
        print(listS)

        listT = sorted(list(t))
        print(listT)

        if listS == listT:
            return True
        else:
            return False

        