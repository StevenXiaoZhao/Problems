from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate_dict = {}
        for s in licensePlate:
            if s.isalpha():
                ss = s.lower()
                if ss in plate_dict:
                    plate_dict[ss] += 1
                else:
                    plate_dict[ss] = 1

        result = None
        for word in words:
            my_dict = {}
            for char in word:
                if char in plate_dict:
                    if char in my_dict:
                        my_dict[char] +=1
                    else:
                        my_dict[char] = 1

            is_completing = True
            for char in plate_dict:
                if char not in my_dict or my_dict[char] < plate_dict[char]:
                    is_completing = False
                    break

            if is_completing is True:
                if result is None or len(result) > len(word):
                    result = word

        return result


print(Solution().shortestCompletingWord(licensePlate = "iMSlpe4", words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
))