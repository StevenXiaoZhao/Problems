from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # find the max col index
        i = 0
        j = n - 1
        while i < j:
            k = int((i + j) / 2)
            if matrix[0][k] < target:
                if i == k:
                    break
                else:
                    i = k
            elif matrix[0][k] > target:
                j = k - 1
            else:
                return True

        if matrix[0][j] <= target:
            col_index_max = j
        else:
            col_index_max = i

        i = 0
        j = col_index_max

        # find the min col index
        while i < j:
            k = int((i + j) / 2)
            if matrix[m-1][k] < target:
                if i == k:
                    break
                else:
                    i = k+1
            elif matrix[m-1][k] > target:
                j = k
            else:
                return True

        if matrix[m-1][i] >= target:
            col_index_min = i
        else:
            col_index_min = j

        # find the max row index
        i = 0
        j = m - 1
        while i < j:
            k = int((i + j) / 2)
            if matrix[k][col_index_min] < target:
                if i == k:
                    break
                else:
                    i = k
            elif matrix[k][col_index_min] > target:
                j = k - 1
            else:
                return True

        if matrix[j][col_index_min] <= target:
            row_index_max = j
        else:
            row_index_max = i

        i = 0
        j = row_index_max

        # find the min row index
        while i < j:
            k = int((i + j) / 2)
            if matrix[k][col_index_max] < target:
                if i == k:
                    break
                else:
                    i = k + 1
            elif matrix[k][col_index_max] > target:
                j = k
            else:
                return True

        if matrix[i][col_index_max] >= target:
            row_index_min = i
        else:
            row_index_min = j

        for i in range(row_index_min, row_index_max+1):

            if col_index_max == col_index_min and matrix[i][col_index_max] == target:
                return True

            h = col_index_min
            j = col_index_max
            while h <= j:
                k = int((h+j)/2)
                if matrix[i][k] == target:
                    return True
                elif matrix[i][k] < target:
                    h = k+1
                else:
                    j = k-1

        return False




print(Solution().searchMatrix(
[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],
15
))