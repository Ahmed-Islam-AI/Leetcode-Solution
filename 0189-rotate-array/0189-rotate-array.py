class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = k% len(nums)

        def rev(s,e):
            while s<e:
                nums[s],nums[e] = nums[e],nums[s]
                s+=1
                e-=1
            
        nums.reverse()
        rev(0,x-1)
        rev(x , len(nums)-1)