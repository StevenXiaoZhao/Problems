
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        previous = 0
        for token in tokens:
            if token.isnumeric():
                value = int(token)
                if value <= previous:
                    return False
                else:
                    previous =value

        return True
