
# Employee info
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_dict = dict()
        for employee in employees:
            employees_dict[employee.id] = employee

        if id not in employees_dict:
            return 0

        queue = [id]
        total_importance = 0
        while len(queue)>0:
            id = queue.pop(0)
            employee = employees_dict[id]
            total_importance += employee.importance
            for sub in employee.subordinates:
                queue.append(sub)

        return total_importance

print(Solution().getImportance())