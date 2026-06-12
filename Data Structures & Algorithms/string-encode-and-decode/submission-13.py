class Solution:

    def encode(self, strs: List[str]) -> str:

        returned_word = ""

        for s in strs:
            returned_word += f"{len(s)}#{s}"

        return returned_word

    def decode(self, s: str) -> List[str]:

        i = 0
        list_words = []

        while i < len(s):

            j=i
            number = 0

            while s[j] != "#":
                j+=1

            number = int(s[i:j])

            list_words.append(s[j+1:j+number+1])
        
            i = j + number + 1

        return list_words