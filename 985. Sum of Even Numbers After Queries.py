def sumEvenAfterQueries(A:'List[int]', queries: 'List[List[int]]') -> 'List[int]':
    ans = []
    for query in queries:
        A[query[1]] += query[0]
        result = 0
        for item in A:
            if item % 2 == 0:
                result += item
        ans.append(result)
    return ans


def sumEvenAfterQueries2(A:'List[int]', queries: 'List[List[int]]') -> 'List[int]':
    ans = []
    ret = sum(x for x in A if x % 2 == 0)
    for query in queries:
        if A[query[1]] % 2 == 0:
            if query[0] % 2 == 0:
                ret += query[0]
            else:
                ret -= A[query[1]]
        else:
            if query[0] % 2:
                ret += query[0] + A[query[1]]
        A[query[1]] += query[0]
        ans.append(ret)
    return ans


def sumEvenAfterQueries3(A:'List[int]', queries: 'List[List[int]]') -> 'List[int]':
    ans = []
    ret = sum(x for x in A if x % 2 == 0)
    for val, pos in queries:
        if A[pos] % 2 == 0:
            if val % 2 == 0:
                ret += val
            else:
                ret -= A[pos]
        else:
            if val % 2:
                ret += val + A[pos]
        A[pos] += val
        ans.append(ret)
    return ans


def sumEvenAfterQueries4(A:'List[int]', queries: 'List[List[int]]') -> 'List[int]':
    ans = []
    ret = sum(x for x in A if x % 2 == 0)
    for val, pos in queries:
        # 第一步 计算出其余未修改项中的偶数和
        if A[pos] % 2 == 0:
            ret -= A[pos]
        # 第二步 进行更新
        A[pos] += val
        if A[pos] % 2 == 0:
            ret += A[pos]
        ans.append(ret)
    return ans


A_list = [1, 2, 3, 4]
query_list = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(sumEvenAfterQueries4(A_list, query_list))