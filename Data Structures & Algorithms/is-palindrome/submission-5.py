class Solution:
    def isPalindrome(self, s: str) -> bool:

        pure_string = s.lower()
        ansr = []

        for i in pure_string:
            if i>="a" and i<="z" or i >= "0" and i <="9":
                ansr.append(i)

        if len(ansr) == 1 and ansr[0] >= "a" and ansr[0] <= "z":
            return True
        elif len(ansr) == 1:
            return False

        for i in range(len(ansr)):
            if ansr[i] != ansr[len(ansr)-i-1]:
                return False

        return True