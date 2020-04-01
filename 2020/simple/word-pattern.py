class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if pattern is None and str is None:
            return True

        if pattern is None or str is None:
            return False

        words = str.split(" ")
        count = len(pattern)
        if len(words) != count:
            return False

        change_str = ''
        mapping = dict()
        pattern_set = set()
        for i in range(count):
            if words[i] not in mapping:
                mapping[words[i]] = pattern[i]
                pattern_set.add(pattern[i])

            change_str += mapping[words[i]]

        return pattern == change_str and len(mapping.keys()) == len(pattern_set)

print(Solution().wordPattern(pattern = "abbc", str = "dog cat cat fish"))


