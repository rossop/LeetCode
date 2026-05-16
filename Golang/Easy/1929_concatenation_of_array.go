package main

import "fmt"

// getConcatenation returns nums concatenated with itself: ans of length 2n
// where ans[i] == ans[i+n] == nums[i].
//
// Allocate the 2n result up front, then fill both halves in a single pass.
//
// Time complexity:  O(n)
// Space complexity: O(n) — for the output array.
func getConcatenation(nums []int) []int {
	length := len(nums)
	ans := make([]int, 2*length)

	for i := 0; i < length; i++ {
		ans[i] = nums[i]
		ans[i+length] = nums[i]
	}
	return ans
}

func main() {
	testCases := []struct {
		nums     []int
		expected []int
	}{
		{[]int{1, 2, 1}, []int{1, 2, 1, 1, 2, 1}},
		{[]int{1, 3, 2, 1}, []int{1, 3, 2, 1, 1, 3, 2, 1}},
		{[]int{5}, []int{5, 5}},
		{[]int{9, 8, 7, 6}, []int{9, 8, 7, 6, 9, 8, 7, 6}},
	}

	for i, tc := range testCases {
		result := getConcatenation(tc.nums)
		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %v | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.nums, tc.expected, result, status)
	}
}
