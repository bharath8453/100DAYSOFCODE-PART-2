class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        # If lengths mismatch, cannot follow pattern
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):
            # Check char -> word mapping
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word

            # Check word -> char mapping
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch

        return True

solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog")) 
print(solution.wordPattern("abba", "dog cat cat fish")) 
print(solution.wordPattern("aaaa", "dog cat cat dog"))  
print(solution.wordPattern("abba", "dog dog dog dog")) 