class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -(2**31)   # -2147483648

        sign = -1 if x < 0 else 1
        n = abs(x)
        rev = 0

        # Max allowed popped digit when rev == 214748364
        max_last_digit = 8 if sign == -1 else 7

        while n != 0:
            pop = n % 10
            n //= 10

            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > max_last_digit):
                return 0

            rev = rev * 10 + pop

        result = sign * rev
        return result if INT_MIN <= result <= INT_MAX else 0
