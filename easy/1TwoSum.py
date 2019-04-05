class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        size=len(nums)
        d={nums[i] :i for i in range(size)  }
        
        for i in range(size):
            tmp=target-nums[i]
            if(tmp in d):
                if (d[tmp]!=i):
                    return [i,d[tmp]]