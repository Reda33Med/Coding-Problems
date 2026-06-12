class Solution:
    def isPalindrome(self, s: str) -> bool:

        index_left = 0
        index_right = len(s) - 1
        s = s.lower()

        while index_left < index_right:
            while index_left < index_right and not s[index_left].isalnum():
                index_left += 1

            while index_left < index_right and not s[index_right].isalnum():
                index_right -= 1

            if index_left >= index_right:
                break

            if s[index_left] != s[index_right]:
                return False

            index_left += 1
            index_right -= 1
        return True