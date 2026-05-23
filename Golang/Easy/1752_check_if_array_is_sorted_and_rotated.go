package main

import "fmt"

// check returns true if nums could have been produced by rotating a
// non-decreasing array (rotation by 0 counts). Duplicates allowed.
//
// Walk the array as if it were circular: pair (curr, next) with modular
// indexing for 2n-1 steps. Track the longest non-decreasing run — reset
// to 1 on a drop. The array is a rotated sort iff some run reaches n.
//
// Why 2n - 1? The rotation pivot can be anywhere; walking around almost
// twice guarantees the full n-length non-decreasing run is seen no matter
// where it starts.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func check(nums []int) bool {
	n := len(nums)
	count := 1

	if n == 1 {
		return true
	}

	for idx := 0; idx < 2*n-1; idx++ {
		curr := nums[idx%n]
		next := nums[(idx+1)%n]

		if curr > next {
			count = 1
		} else {
			count++
		}

		if count == n {
			return true
		}
	}
	return n == 1
}

func main() {
	testCases := []struct {
		nums     []int
		expected bool
	}{
		{[]int{3, 4, 5, 1, 2}, true},
		{[]int{2, 1, 3, 4}, false},
		{[]int{1, 2, 3}, true},
		{[]int{1}, true},
		{[]int{1, 1, 1}, true},
		{[]int{7, 9, 1, 1, 1}, true},
		{[]int{2, 1}, true},
		{[]int{6, 10, 6}, true},
		{[]int{2, 4, 1, 3}, false},
	}

	for i, tc := range testCases {
		result := check(append([]int(nil), tc.nums...))
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %v | Expected: %t | Result: %t | [%s]\n",
			i+1, tc.nums, tc.expected, result, status)
	}
}
