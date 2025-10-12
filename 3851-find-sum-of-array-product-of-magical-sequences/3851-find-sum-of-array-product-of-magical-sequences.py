class Solution(object):
    def magicalSum(self, m, k, nums):
        """
        :type m: int
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            num = den = 1
            for i in range(r):
                num = (num * (n - i)) % MOD
                den = (den * (i + 1)) % MOD
            return num * pow(den, MOD - 2, MOD) % MOD

        pow_nums = [[1] * (m + 1) for _ in range(n)]
        for j in range(n):
            for c in range(1, m + 1):
                pow_nums[j][c] = (pow_nums[j][c - 1] * nums[j]) % MOD

        from collections import defaultdict

        dp = defaultdict(int)
        dp[(m, 0, 0)] = 1  

        for j in range(n):
            newdp = defaultdict(int)
            for (r, carry_in, ones_so_far), val in dp.items():
                if val == 0:
                    continue
                for c in range(r + 1):
                    comb = nCr(r, c)
                    weight = val * comb % MOD
                    weight = weight * pow_nums[j][c] % MOD

                    total = c + carry_in
                    bit = total & 1
                    carry_out = total >> 1
                    newr = r - c
                    newones = ones_so_far + bit
                    key = (newr, carry_out, newones)
                    newdp[key] = (newdp[key] + weight) % MOD
            dp = newdp

        ans = 0
        for (r, carry, ones), val in dp.items():
            if r != 0:
                continue
            total_ones = ones + bin(carry).count('1')
            if total_ones == k:
                ans = (ans + val) % MOD

        return ans
