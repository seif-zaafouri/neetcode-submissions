class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        fn_2 = 1 #f(1) 
        fn_1 = 2 #f(2)
        for i in range(3, n+1):
            fn = fn_2 + fn_1
            fn_2 = fn_1
            fn_1 = fn

        return fn



        