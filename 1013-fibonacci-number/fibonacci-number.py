class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        last = 1
        slast = 0

        for i in range(2, n + 1):
            curr = last + slast
            slast = last
            last = curr

        return last
        