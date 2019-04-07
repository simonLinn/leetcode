class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        x=str(x)
        size=len(x)

        if x[0:int(size/2)]==x[-int(size/2):][::-1]:
            return True


        return False
        
