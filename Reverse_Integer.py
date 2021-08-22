class Solution(object):

      def reverse(self, x):
             isnegative = x< 0
             reverse_num = 0
             x = abs(x)
             while (x > 0):
                    reminder = x % 10
                    reverse_num = (reverse_num * 10) + reminder
                    x = x // 10
                    if (reverse_num >= 2147483647 or reverse_num <= -2147483648 ):
                       reverse_num = 0

             if isnegative:
                 reverse_num = reverse_num *(-1)
             return reverse_num


solution = Solution()
print(solution.reverse(123))
