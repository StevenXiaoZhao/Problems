class Solution:
    def originalDigits(self, s: str) -> str:
        char_dict = {}
        numbers = [0] * 10
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        #  保证数字按顺序排列
        words = {'zero': 0,
                 'wto': 2,
                 'geiht': 8,
                 'xsi': 6,
                 'seven': 7,
                 'vfie': 5,
                 'four': 4,
                 'one': 1,
                 'three': 3,
                 'inne': 9}

        for word in words:
            char = word[0]
            if char in char_dict and char_dict[char]>0:
                count = char_dict[char]
                for char2 in word:
                    char_dict[char2] -= count
                numbers[words[word]] = count

        result = ''
        for i in range(len(numbers)):
            if numbers[i] > 0:
                result += str(i)*numbers[i]
        return result


print(Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine"))
