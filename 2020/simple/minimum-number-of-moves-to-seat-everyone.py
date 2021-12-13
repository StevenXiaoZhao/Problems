from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count = len(seats)
        moves = 0
        for i in range(count):
            moves += abs(students[i] - seats[i])

        return moves
