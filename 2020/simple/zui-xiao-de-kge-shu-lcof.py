from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        i = 0
        j = len(arr) - 1
        if j < 0 or k == 0:
            return []
        if k == len(arr):
            return arr

        while True:
            compare = min(arr[i], arr[j])
            if i < j - 1 and (arr[i] == arr[j]):  # 如果 arr[i]和 arr[j]是最大值且相同，则会出现问题
                compare = min(arr[i:j])
                if compare == arr[i]: #所有值都一样了，再继续下去不会有顺序改变
                    return arr[0: k]
            copy_i = i
            copy_j = j
            while i < j:
                if arr[i] > compare >= arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                if arr[i] <= compare:
                    i += 1
                if arr[j] > compare:
                    j -= 1

            if k == i-1:
                return arr[0:k]
            elif k < i:
                i = copy_i
            else:
                j = copy_j


print(Solution().getLeastNumbers([3,2,1],2))
