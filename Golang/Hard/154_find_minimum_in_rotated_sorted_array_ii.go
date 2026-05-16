package main

import "fmt"

// findMin returns the smallest element of a rotated sorted array that may
// contain duplicates.
//
// Binary search against the right end. nums[mid] > nums[right] places the
// minimum strictly to the right of mid. nums[mid] < nums[right] keeps the
// minimum at mid or earlier. On equality the side is ambiguous, but
// nums[mid] still equals nums[right], so dropping right by one is safe and
// cannot skip the minimum.
//
// Time complexity:  O(log n) average, O(n) worst case (all equal).
// Space complexity: O(1)
func findMin(nums []int) int {
	left, right := 0, len(nums)-1

	for left < right {
		mid := left + (right-left)/2

		if nums[mid] > nums[right] {
			left = mid + 1
		} else if nums[mid] < nums[right] {
			right = mid
		} else {
			right--
		}
	}
	return nums[left]
}

func main() {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{[]int{1, 3, 5}, 1},
		{[]int{2, 2, 2, 0, 1}, 0},
		{[]int{3, 1, 3}, 1},
		{[]int{1, 1, 1, 1}, 1},
		{[]int{10, 1, 10, 10, 10}, 1},
		{[]int{1}, 1},
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
