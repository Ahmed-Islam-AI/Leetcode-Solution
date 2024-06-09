class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0

        cnt = defaultdict(int)
        cnt[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k

            if remain in cnt:
                res += cnt[remain]
            cnt[remain] += 1

        return res



        