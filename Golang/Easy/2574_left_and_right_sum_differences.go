package main

import (
	"fmt"
	"slices"
)

// leftRightDifference returns answer[i] = |leftSum[i] - rightSum[i]|.
//
// Two-pass approach that reuses the answer slice as scratch:
//   - Forward pass writes the prefix sum (left of i) into ans[i].
//   - Backward pass rewrites each cell to |ans[i] - rightSum| while
//     accumulating rightSum.
//
// Inline absolute value avoids the float round-trip of math.Abs.
//
// Time complexity:  O(n)
// Space complexity: O(1) auxiliary (output excluded).
func leftRightDifference(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)

	leftSum := 0
	for i, v := range nums {
		ans[i] = leftSum
		leftSum += v
	}

	rightSum := 0
	for i := n - 1; i > -1; i-- {
		diff := ans[i] - rightSum
		if diff > 0 {
			ans[i] = diff
		} else {
			ans[i] = -diff
		}
		rightSum += nums[i]
	}

	return ans
}

// leftRightDifferenceSinglePass pre-computes the total sum, then walks
// once left to right: subtract the current element from rightSum (it is
// no longer "to the right"), write |leftSum - rightSum|, and fold the
// element into leftSum (it becomes "to the left" for the next index).
//
// Time complexity:  O(n)
// Space complexity: O(1) auxiliary (output excluded).
func leftRightDifferenceSinglePass(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)

	leftSum := 0
	rightSum := 0
	for _, v := range nums {
		rightSum += v
	}

	for i, v := range nums {
		rightSum -= v

		diff := leftSum - rightSum
		if diff > 0 {
			ans[i] = diff
		} else {
			ans[i] = -diff
		}

		leftSum += v
	}

	return ans
}

func main() {
	testCases := []struct {
		nums     []int
		expected []int
	}{
		{[]int{10, 4, 8, 3}, []int{15, 1, 11, 22}},
		{[]int{1}, []int{0}},
		{[]int{1, 2, 3, 4, 5}, []int{14, 11, 6, 1, 10}},
		{[]int{5, 5}, []int{5, 5}},
		{[]int{0, 0, 0}, []int{0, 0, 0}},
	}

	for _, approach := range []struct {
		label string
		fn    func([]int) []int
	}{
		{"leftRightDifference          ", leftRightDifference},
		{"leftRightDifferenceSinglePass", leftRightDifferenceSinglePass},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(append([]int(nil), tc.nums...))
			status := "PASS"
			if !slices.Equal(result, tc.expected) {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | Input: %v | Expected: %v | Result: %v | [%s]\n",
				i+1, tc.nums, tc.expected, result, status)
		}
	}
}
