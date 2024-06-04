class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = k% len(nums)

        temp = nums[-x :]
        del nums[-x:]

        nums[:0] = temp