def longestSubstring(x, y):
    lx, ly = len(x) + 1, len(y) + 1
    dp_matrix = [[0 for i in range(ly)] for j in range(lx)]
    result = 0
    for i in range(lx):
        for j in range(ly):
            if (i == 0 or j == 0):
                dp_matrix[i][j] = 0
            elif (x[i - 1] == y[j - 1]):
                dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                result = max(result, dp_matrix[i][j])
            else:
                dp_matrix[i][j] = 0
    return result

n = longestSubstring("CABAS", "FDFABASDS")
print(n)
 
