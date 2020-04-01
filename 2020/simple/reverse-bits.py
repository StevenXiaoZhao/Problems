class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:]
        bits_count = len(binary)
        prefix_zero_counts = 32 - bits_count
        binary = '0'*prefix_zero_counts + binary
        reverse_binary = ''
        for bit in binary:
            reverse_binary = bit + reverse_binary
        result = int(reverse_binary, 2)
        return result

print(Solution().reverseBits(4294967293))
