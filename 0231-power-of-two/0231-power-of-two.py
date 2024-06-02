class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power =1
        counter =1
        while power<=n:
            if power == n:
                return True
            power = 2**counter
            counter += 1

        return False

        