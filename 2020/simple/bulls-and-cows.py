class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls_count = 0
        cows_count = 0
        num_count = dict()
        count = len(secret)

        for i in range(count):
            secret_num = secret[i]
            if secret_num != guess[i]:
                if secret_num not in num_count:
                    num_count[secret_num] = 0
                num_count[secret_num] += 1

        for i in range(count):
            guess_num = guess[i]
            if secret[i] == guess_num:
                bulls_count += 1
            elif guess_num in num_count:
                if num_count[guess_num] > 0:
                    num_count[guess_num] -= 1
                    cows_count += 1
        return str(bulls_count)+'A'+str(cows_count)+'B'

print(Solution().getHint(secret = "1123", guess = "0111"))