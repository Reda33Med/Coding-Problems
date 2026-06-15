class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        size = 1
        left_pointer = 0
        right_pointer = len(s)

        while left_pointer < right_pointer:

            character_set = {}

            for i in range(left_pointer, right_pointer):

                if s[i] in character_set :
                    right_pointer = i
                    break
                else:
                    character_set[s[i]] = 1
            
            size = max(size , len(character_set))
            left_pointer += 1
            right_pointer = len(s)
            

        return size
