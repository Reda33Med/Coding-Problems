class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Main Variable
        longest = 0

        #Pointers of the window
        left_pointer = 0
        right_pointer = 0

        #Keeping Characters
        characters_set = set()

        #The main logic
        while right_pointer < len(s) :

            if s[right_pointer] in characters_set:

                characters_set.remove(s[left_pointer])
                left_pointer += 1

            else:

                characters_set.add(s[right_pointer])
                longest = max( longest , ((right_pointer - left_pointer) + 1) )
                right_pointer += 1

        #Return of the main variable
        return longest