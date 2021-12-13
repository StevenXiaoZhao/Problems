from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        flag = -newColor
        curr = image[sr][sc]
        ready_to_flag = [(sr, sc)]
        row_num = len(image)
        col_num = len(image[0])

        while len(ready_to_flag) > 0:
            row_index, col_index = ready_to_flag.pop()
            image[row_index][col_index] = flag
            if row_index-1 >= 0 and image[row_index-1][col_index] == curr and image[row_index-1][col_index] != flag:
                ready_to_flag.append((row_index-1, col_index))

            if col_index-1 >= 0 and image[row_index][col_index-1] == curr and image[row_index][col_index-1] != flag:
                ready_to_flag.append((row_index, col_index-1))

            if row_index+1 < row_num and image[row_index+1][col_index] == curr and image[row_index+1][col_index] != flag:
                ready_to_flag.append((row_index+1, col_index))

            if col_index+1 < col_num and image[row_index][col_index+1] == curr and image[row_index][col_index+1] != flag:
                ready_to_flag.append((row_index, col_index+1))

        for row_index in range(row_num):
            for col_index in range(col_num):
                if image[row_index][col_index] == flag:
                    image[row_index][col_index] = -flag

        return image

print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]]
,sr = 1, sc = 1, newColor = 2))