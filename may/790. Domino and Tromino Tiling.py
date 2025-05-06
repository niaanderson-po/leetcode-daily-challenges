from functools import cache

def numTilings(n):
    """
    :type n: int
    :rtype: int
    """
    #constant var
    MOD = 1_000_000_007
    
    @cache  
    def p(n):
        #2x1 board
        if n == 1:
            return 1
        return (p(n-1)+ f(n-2)) % MOD

    @cache
    def f(n):
        if n <= 2:
            return n
        return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % MOD
    
    return f(n)

n = 3
print(numTilings(n))

n = 1
print(numTilings(n))