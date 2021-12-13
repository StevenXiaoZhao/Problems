from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        right_side_max = [0] * len(height)
        right_max = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_side_max[i] = right_max
            if height[i] > right_max:
                right_max = height[i]

        total_rain = 0
        left_max = height[0]
        for i in range(1, len(height)):
            if height[i] < left_max and height[i] < right_side_max[i]:  # this is a vally
                # choose the small hill as the level
                rain_level = min(left_max, right_side_max[i])
                total_rain += rain_level - height[i]
                height[i] = rain_level
            elif height[i] > left_max:
                left_max = height[i]
        return total_rain


print(Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(Solution().trap(height=[4, 2, 0, 3, 2, 5]))  # 9
