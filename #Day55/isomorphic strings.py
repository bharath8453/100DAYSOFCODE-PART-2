class Solution(object):
    def isIsomorphic(self, s, t):
        # If lengths differ, cannot be isomorphic
        if len(s) != len(t):
            return False

        # Maps for both directions
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check s -> t mapping
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # Check t -> s mapping
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True


solution = Solution()
print(solution.isIsomorphic("egg", "add"))   
print(solution.isIsomorphic("foo", "bar"))   
print(solution.isIsomorphic("paper", "title")) 