class Solution:
    def frequencySort(self, s: str) -> str:

        count = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        ans = ""

        for i in sorted(count, key=lambda x: count[x], reverse=True):
            ans += i * count[i]

        return ans