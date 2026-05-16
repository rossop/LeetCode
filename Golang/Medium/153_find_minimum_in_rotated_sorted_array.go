package main

import "fmt"

// findMin returns the smallest element of a rotated sorted array of unique
// integers in O(log n).
//
// Binary search on the pivot: compare nums[m] with nums[r]. If nums[m] >
// nums[r], the rotation point lies strictly to the right of m, so move l
// past m. Otherwise the minimum is at m or to its left, so pull r down to m.
// When l == r, that index holds the minimum.
//
// Time complexity:  O(log n)
// Space complexity: O(1)
func findMin(nums []int) int {
	l, r := 0, len(nums)-1

	for l < r {
		m := l + (r-l)/2
		if nums[m] > nums[r] {
			l = m + 1
		} else {
			r = m
		}
	}
	return nums[l]
}

func main() {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{[]int{3, 4, 5, 1, 2}, 1},
		{[]int{4, 5, 6, 7, 0, 1, 2}, 0},
		{[]int{11, 13, 15, 17}, 11},
		{[]int{1}, 1},
		{[]int{2, 1}, 1},
		{[]int{5, 1, 2, 3, 4}, 1},
	}

	for i, tc := range testCases {
		result := findMin(append([]int(nil), tc.nums...))
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %v | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.nums, tc.expected, result, status)
	}
}
