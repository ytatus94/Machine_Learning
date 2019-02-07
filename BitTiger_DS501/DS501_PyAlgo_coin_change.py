class Solution1(object):
    def coinChange(self, coins, amount):
        def change(remaining):
            if remaining <= 0:
                return 0

            min_coins = float('+inf')

            for c in coins:
                if c <= remaining:
                    num_coins = change(remaining-c) + 1
                    min_coins = min(min_coins, num_coins)
            return min_coins

        answer = change(amount)

        if answer != float('+inf'):
            return answer
        else:
            return -1

s1 = Solution1()
print(s1.coinChange([1, 2, 5], 11))
print(s1.coinChange([2], 3))
#print(s1.coinChange([118, 449, 61, 122, 133, 164, 336], 1702))

class Solution2(object):
    def coinChange(self, coins, amount):
        def change(remaining, memo):
            if remaining <= 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            min_coins = float('+inf')
            for c in coins:
                if c <= remaining:
                    min_coins = min(min_coins, change(remaining-c, memo)+1)
                    memo[remaining] = min_coins
            return min_coins

        answer = change(amount, {})
        if answer != float('+inf'):
            return answer
        else:
            return -1

s2 = Solution2()
print(s2.coinChange([1, 2, 5], 11))
print(s2.coinChange([2], 3))
print(s2.coinChange([118, 449, 61, 122, 133, 164, 336], 1702))

class Solution3(object):
    def coinChange(self, coins, amount):
        table = [float('+inf')] * (amount + 1)
        table[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    table[i] = min(table[i], table[i-c]+1)

        if table[amount] == float('+inf'):
            return -1
        return table[amount]

s3 = Solution3()
print(s3.coinChange([1, 2, 5], 11))
print(s3.coinChange([2], 3))
print(s3.coinChange([118, 449, 61, 122, 133, 164, 336], 1702))

class Solution4(object):
    def coinChange(self, coins, amount):
        def change(idx, remaining, count):
            if remaining <= 0:
                self.answer = min(self.answer, count)
                return

            for i in range(idx, len(coins)):
                if coins[i] <= remaining < coins[i] * (self.answer-count):
                    change(i, remaining-coins[i], count+1)

        coins.sort(reverse=True)
        self.answer = float('+inf')
        change(0, amount, 0)

        if self.answer != float('+inf'):
            return self.answer
        else:
            return -1

s4 = Solution4()
print(s4.coinChange([1, 2, 5], 11))
print(s4.coinChange([2], 3))
print(s4.coinChange([118, 449, 61, 122, 133, 164, 336], 1702))

