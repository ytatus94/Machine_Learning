class Solution(object):
    def isValid(self, s):
        # prepare paranthesis table
        brackets = set()
        brackets.add('(')
        brackets.add('[')
        brackets.add('{')

        pairs = set()
        pairs.add('()')
        pairs.add('[]')
        pairs.add('{}')

        stack = []

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                left = stack.pop()
                if left + c not in pairs:
                    return False

        return len(stack) == 0

s = Solution()

print(s.isValid('(())'))
print(s.isValid('([][])'))
print(s.isValid('([)'))
