from typing import List


class Solution:
    def k_line(self, lines: List[int], k: int) -> float:
        if lines is None:
            return 0

        lines.sort(reverse=True)
        count = len(lines)
        i = 0
        j = count-1
        while i<j:
            mid = int((i+j)/2)
            line_count = self.get_line_count(lines, mid)
            if line_count > k:
                j = line_count
            elif line_count <k:
                i = line_count



    def get_line_count(self, lines: List[int], mid):
        num = 0
        for i in range(mid+1):
            num += int(lines[i]/lines[mid])
        return num