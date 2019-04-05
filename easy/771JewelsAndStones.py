class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for lj in J:
            for ls in S:
                if lj==ls:
                    count+=1
        return count