class Solution:
    def checkRecord(self, s: str) -> bool:
        reward = True
        absent_count = 0
        continue_late_count = 0
        for char in s:
            if char == 'A':
                absent_count += 1
                continue_late_count = 0
            elif char == 'L':
                continue_late_count += 1
            elif continue_late_count > 0:
                continue_late_count = 0

            if absent_count > 1 or continue_late_count > 2:
                reward = False
                break
        return reward

print(Solution().checkRecord("LALL"))