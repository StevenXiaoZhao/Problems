class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse_x =0
        x_copy =x
        while x > 0:
            t=x%10
            reverse_x = reverse_x*10+t
            x=int(x/10)
        return reverse_x == x_copy

print(Solution().isPalindrome(8))