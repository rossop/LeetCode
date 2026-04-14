package main

import "fmt"

// getMinDistance returns the minimum absolute distance between start and any
// index i where nums[i] == target.
//
// It iterates through nums once, computing abs(i - start) for each occurrence
// of target and tracking the running minimum.
//
// Parameters:
//   - nums:   the input slice of integers
//   - target: the value to search for in nums
//   - start:  the index to measure distance from
//
// Returns the minimum value of abs(i - start) across all i where nums[i] == target.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func getMinDistance(nums []int, target int, start int) int {
	res := len(nums)
	for i, num := range nums {
		if num == target {
			diff := i - start
			if diff < 0 {
				diff = -diff
			}
			if diff < res {
				res = diff
			}
		}
	}
	return res
}

func main() {
	testCases := []struct {
		nums     []int
		target   int
		start    int
		expected int
	}{
		{nums: []int{1, 2, 3, 4, 5}, target: 5, start: 3, expected: 1},
		{nums: []int{1}, target: 1, start: 0, expected: 0},
		{nums: []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, target: 1, start: 0, expected: 0},
	}

	for i, tc := range testCases {
		result := getMinDistance(tc.nums, tc.target, tc.start)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: nums=%v target=%d start=%d | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.nums, tc.target, tc.start, tc.expected, result, status)
	}
}
