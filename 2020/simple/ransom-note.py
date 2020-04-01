class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = dict()
        for char in magazine:
            if char not in magazine_dict:
                magazine_dict[char] =1
            else:
                magazine_dict[char]+=1

        for char in ransomNote:
            if char not in magazine_dict or magazine_dict[char]==0:
                return False
            magazine_dict[char]-=1

        return True

print(Solution().canConstruct("aa", "ab"))