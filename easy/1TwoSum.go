package main
import "fmt"

 func twoSum(nums []int, target int) []int {
    hash := make(map[int]int)
	size:=len(nums)
	i:=0
	tmp:=0
	for i=0;i<size;i++{
		hash[nums[i]]=i
	} 

	for i=0;i<size;i++{
		tmp=target-nums[i]
		key,prs:=hash[tmp]
		if(prs==true && key!=i){
			return ([]int{i,key})
		}
			
	}
	return ([]int{0,0})

 }

func main() {
	nums:=[]int{2, 7, 11, 15}
	target:=9
	
	

	fmt.Println(twoSum(nums,target))
	

	
	
}