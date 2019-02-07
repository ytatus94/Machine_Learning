class Solution(object):
    def lengthOfLongestSubstring(self, s):
        def valid(substr):
            return len(substr) == len(set(substr))

        longest = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]

                if valid(substr):
                    sz = len(substr)
                    if sz > longest:
                        longest = sz

        return longest

s = Solution()
print(s.lengthOfLongestSubstring('anappleaday'))

class Solution2():
    def lengthOfLongestSubstring(self, s):
        location = {}
        for c in s:
            location[c] = -1 # initialization

        longest = 0
        curr_str = ''
        for i in range(0, len(s)):
            c= s[i]
            at = location[c]

            #1. the current char appears for the first
            #2. the current char is not part of the current substring
            #3. the current char is part of the current substring

            if at == -1:
                curr_str += c
                location[c] = i
                continue

            idx = curr_str.find(c)
            if idx == -1:
                curr_str += c
                location[c] = i
            else:
                if longest < len(curr_str):
                    longest = len(curr_str)
                # position: posit +i
                # position: ti
                curr_str = curr_str[idx+1:] +c
                location[c] = i

        if len(curr_str) > longest:
            longest = len(curr_str)

        return longest

s2 = Solution2()
print(s2.lengthOfLongestSubstring('anappleaday'))
                
