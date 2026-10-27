def solution(triangle):
    result = [[x for x in triangle[i]] for i in range(len(triangle))]

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            result[i+1][j] = max(result[i+1][j], triangle[i+1][j] + result[i][j])
            result[i+1][j+1] = max(result[i+1][j+1], triangle[i+1][j+1] + result[i][j])

    return max(result[-1])