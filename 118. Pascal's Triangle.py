def generate1(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    all_result = [[1], [1, 1]]
    if numRows == 2:
        return all_result
    line = [1, 1]
    for t in range(2, numRows):
        r = []
        for i in range(0, len(line)-1):
            r.append(line[i]+line[i+1])
        line = [1] + r + [1]
        all_result.append(line)
    return all_result


def generate(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle


print(generate1(7))
yang_hui_1 = [1]
yang_hui_2 = [1, 1]



