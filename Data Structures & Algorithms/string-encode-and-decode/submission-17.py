class Solution:

    def encode(self , strs: List[str]) -> str:
        
        finalestring = ""

        for word in strs:
            finalestring = finalestring + str(len(word))+ "#"+str(word) 

        return finalestring


    def decode(self, s: str) -> List[str]:
        
        finale_solution = []
        i = 0
        
        while i < len(s) :
            semi_solution = ""
            word_string = ""
            word_length = 0
            
            while s[i] != "#" :
                word_string = word_string + s[i]
                i = i + 1
                
            word_length = int(word_string)
            j = i + 1
            while j < word_length + i +1:
                semi_solution = semi_solution + s[j]
                j = j + 1
                
            finale_solution.append(str(semi_solution))
            
            i = j
            

        return finale_solution