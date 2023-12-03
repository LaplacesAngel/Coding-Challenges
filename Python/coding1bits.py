class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        for i in bin(n):
            if i == '1':
                count += 1
        
        return count
    

solution = Solution()

print(solution.hammingWeight(0b11111111111111111111111111111101))