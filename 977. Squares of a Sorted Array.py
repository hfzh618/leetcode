def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    print([x * x for x in A].sort())
    return sorted([x * x for x in A])


def sortedSquares2(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    ans = []
    N = len(A)
    j = 0
    while j < N and A[j] < 0:
        j += 1
    i = j - 1
    while 0 < i and j < N:
        if A[i] ** 2 < A[j] ** 2:
            ans.append(A[i] ** 2)
            i -= 1
        else:
            j += 1
    while 0 < i:
        ans.append(A[i])
        i -= 1
    while j < N:
        ans.append(A[j])
        j += 1
    return ans


li = [-4, -1, 0, 3, 10]
print(sortedSquares(li))