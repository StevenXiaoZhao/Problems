from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        hour_max = 3
        minute_max = 5
        if num < 0 or num > 8:
            return []

        result = []
        if num == 0:
            return ['0:00']
        for i in range(0, hour_max + 1):
            if num - i > minute_max:
                continue
            if i> num:
                break
            hours_situation = self.getHour(hours, i, 12)
            minutes_situation = self.getHour(minutes, num - i, 60)

            for hour in hours_situation:
                hour_str = str(hour)
                for minute in minutes_situation:
                    minute_str = ('0' if minute < 10 else '') + str(minute)
                    result.append(hour_str + ':' + minute_str)

        return result

    def getHour(self, hours: List[int], select_count: int, max_val: int) -> List[int]:
        if select_count == 0:
            return [0]
        elif select_count == 1:
            return hours
        elif len(hours) == select_count:
            result = sum(hours)
            return [result] if result<max_val else []
        else:
            # select index 0
            hours_copy = hours.copy()
            curr = hours_copy.pop(-1)
            data = self.getHour(hours_copy, select_count - 1, max_val - curr)
            for i in range(len(data)):
                t = data[i] + curr
                if t < max_val:
                    data[i] = t
            # Do not select index 0
            hours_copy = hours.copy()
            hours_copy.pop(-1)
            data2 = self.getHour(hours_copy, select_count, max_val)
            data.extend(data2)
            return data


print(Solution().readBinaryWatch(9))
