class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Two pointer and swapping Technique 
        """
        n= len(s)
        left = 0 
        right = n-1
        while left<right:
            ch = s[left]
            s[left]= s[right]
            s[right] = ch
            left += 1
            right -= 1




        