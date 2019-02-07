# 先處理數字
class SolutionEX1(object):
    def decodeString(self, s):
        multiplier = ''
        stack = []

        for c in s:
            if c.isdigit():
                multiplier += c
            elif c == '[':
                pattern = ''
                record = [int(multiplier), pattern]
                stack.append(record)

                multiplier = ''
                print(record)

# s1 = SolutionEX1()
# s1.decodeString('10[ab]2[cd]')


# 再處理 pattern
class SolutionEX2(object):
    def decodeString(self, s):
        stack = []
        multiplier = ''

        for c in s:
            if c.isdigit():
                multiplier += c
            elif c == '[':
                pattern = ''
                record = [int(multiplier), pattern]
                stack.append(record)
                multiplier = ''
            else:
                # 開始累積 pattern chars
                # 把目前的 record 拿出來
                curr_record = stack[-1]
                curr_record[1] += c

                # 看 pattern 有沒有累積的效果
                print(c, curr_record)

# 檢查有沒有成功累積 pattern 字串
# s2 = SolutionEX2()
# s2.decodeString('10[ab]2[cd]')


class SolutionEX3(object):
    def decodeString(self, s):
        stack = []
        multiplier = ''

        stack.append([0, ''])

        for c in s:
            if c.isdigit():
                multiplier += c
            elif c == '[':
                pattern = ''
                record = [int(multiplier), pattern]
                stack.append(record)
                multiplier = ''
            elif c == ']':
                # 停止累積 pattern 開始 decode
                mul, pattern = stack.pop()
                decoded = pattern * mul
                print('%s[%s]=>%s' % (mul, pattern, decoded))

                # decoded string 成為上一層括號的 pattern
                last_record = stack[-1]
                last_record[1] += decoded
                print(last_record)
                # 初始化的階段，要加一個空的 record 給最後一筆 decoded string 往前放
            else:
                curr_record = stack[-1]
                curr_record[1] += c

        # final decoded string = stack 最後一筆 record 裡的 pattern
        return stack[0][1]

# s3 = SolutionEX3()
# s3.decodeString('10[ab]2[cd]')
# s3.decodeString('3[2[ab]]')

# Final version
class Solution(object):
    def decodeString(self, s):
        stack = []
        multiplier = ''
        stack.append([0, ''])

        for c in s:
            if c.isdigit():
                multiplier += c
            elif c == '[':
                pattern = ''
                record = [int(multiplier), pattern]
                stack.append(record)
                multiplier = ''
            elif c == ']':
                mul, pattern = stack.pop()
                decoded = pattern * mul
                last_record = stack[-1]
                last_record[1] += decoded
            else:
                curr_record = stack[-1]
                curr_record[1] += c

        return stack[0][1]

s = Solution()
print(s.decodeString('3[a]2[bc]'))
print(s.decodeString('2[abc]3[cd]ef'))
print(s.decodeString('2[3[ab]]'))
