def numEquivDominoPairs(dominoes):
    """
    :type dominoes: List[List[int]]
    :rtype: int
    """
    num = [0] * 100
    ret = 0

    for x, y in dominoes:
        if x <= y:
            val = x * 10 + y 
        else:
            val = y * 10 + x
        
        ret += num[val]
        num[val] += 1

    return ret

dominoes = [[1,2],[2,1],[3,4],[5,6]]
print(numEquivDominoPairs(dominoes))

dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(numEquivDominoPairs(dominoes))