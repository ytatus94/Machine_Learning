class Solution(object):
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)

        head = 0
        tail = len(s) - 1
        while head < tail:
            while head < tail and s[head] not in vowels:
                head += 1
            while head < tail and s[tail] not in vowels:
                tail -= 1
            s[head], s[tail] = s[tail], s[head]

            head += 1
            tail -= 1


        return ''.join(s)

s = Solution()
print(s.reverseVowels('hello'))
