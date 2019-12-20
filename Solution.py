class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        output = 0

        foo = []
        for j in range(len(s)):
            foo.append(s[j])
            if len(list(set(foo))) == len(foo):
                output = len(foo)
            else :
                output = len(foo)-1
                foo.pop(0)
                if len(list(set(foo))) == len(foo) :
                    output = len(foo)
        return output
