
# 13. Convert String to matrix having K characters per row Using list comprehension + slicing.
# Input : test_str = ‘GeeksforGeeks is best’, K = 7 
# Explanation : Each character is assigned to 7 element row in matrix.
# Input string and value for K
test_str = 'GeeksforGeeks is best'
K = 7
matrix = [list(test_str[i:i + K]) for i in range(0, len(test_str), K)]
print(matrix)


# Output : [[‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’], [‘r’, ‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘ ‘], [‘i’, ‘s’, ‘ ‘, ‘b’, ‘e’, ‘s’, ‘t’]] 
