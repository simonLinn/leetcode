func jump(nums []int) int {
	size, now, after, i, step := len(nums), 0, 0, 0, 0

	for now < size-1 {
		after = now
		for ; i <= after; i++ {
			if now < i+nums[i] {
				now = i + nums[i]
			}
		}
		step++
	}
	return step
}