class Solution:
    def isPalindrome(self, s: str) -> bool:

        pure_string = s.lower()
        ansr = []

        for i in pure_string:
            if i>="a" and i<="z" or i >= "0" and i <="9":
                ansr.append(i)

        for i in range(len(ansr)):
            if ansr[i] != ansr[len(ansr)-i-1]:
                return False

        return True