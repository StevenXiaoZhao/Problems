class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<2:
            return True
        is_first_lower = word[0].islower()
        is_follow_lower = word[1].islower()
        for i in range(1, len(word)):
            if is_first_lower and word[i].isupper():
                return False
            else:
                if is_follow_lower and word[i].isupper():
                    return False
                if not is_follow_lower and word[i].islower():
                    return False

        return True

print(Solution().detectCapitalUse("uSa"))
