class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution=[0,0]
        size=len(nums)
        d={nums[i] :i for i in range(size)  }
        tmp=0
        for i in range(size):
            tmp=target-nums[i]
            if(tmp in d):
                if(d[tmp]!=i):
                    solution[0]=i
                    solution[1]=d[tmp]
                    break

        return solution