from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S is None:
            return None
        elif len(S) == 1:
            return [S[0].lower(), S[0].upper()] if str.isalpha(S[0]) else S[0]

        curr = S[0]
        strs = self.letterCasePermutation(S[1:])
        new_strs = []
        if str.isnumeric(curr):
            for x in range(len(strs)):
                new_strs.append(curr + strs[x])
        else:
            curr_copy = curr.upper() if curr.islower() else curr.lower()

            for x in range(len(strs)):
                new_strs.append(curr + strs[x])

            for x in range(len(strs)):
                new_strs.append(curr_copy + strs[x])

        return new_strs

print(Solution().letterCasePermutation('a1b2weurowoe'))