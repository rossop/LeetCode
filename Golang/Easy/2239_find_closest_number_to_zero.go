package main

import (
	"fmt";
	"cmp";
	"slices";
)

// Solution groups all approaches for 2239. Find Closest Number to Zero.
//
// Given an integer array nums of size n, return the number closest to 0 in
// nums. If there are multiple answers, return the number with the largest value.
type Solution struct{}

// findClosestNumber returns the element in nums with the smallest absolute
// value, breaking ties in favour of the positive value.
//
// Single pass: tracks the best candidate seen so far. The abs helper is
// defined as a closure to avoid shadowing the built-in. Updates closest when
// a strictly smaller absolute value is found, or when the absolute values are
// equal but the current element is larger (positive beats negative on a tie).
//
// Time complexity:  O(n)
// Space complexity: O(1)
func (s Solution) findClosestNumber(nums []int) int {
	closest := nums[0]
	abs := func(n int) int {
		if n < 0 {
			return -n
		}
		return n
	}
	for _, num := range nums {
		val := abs(num)
		if val < abs(closest) {
			closest = num
		} else if val == abs(closest) && num > closest {
			closest = num
		}
	}
	return closest
}

// findClosestNumberMap returns the element in nums closest to zero using
// slices.MinFunc — the idiomatic Go equivalent of Python's min(key=...).
//
// slices.MinFunc accepts a comparator func(a, b T) int that must return:
//   - negative if a should be considered smaller (wins)
//   - zero     if a and b are equal
//   - positive if b should be considered smaller (wins)
//
// Use cmp.Compare(x, y) to produce a negative/zero/positive integer for
// ordered types instead of writing the comparison manually. The exact value
// is unspecified — only the sign matters to the comparator contract.
//
// When to use slices.MinFunc:
//   - Production code or take-home assignments — it is expressive and safe.
//   - Interviews where you can use the stdlib freely (some allow it).
//
// When NOT to use slices.MinFunc:
//   - LeetCode submissions — slices/cmp packages require Go 1.21+; older
//     judge versions will reject the import.
//   - Interviews where you are expected to demonstrate the algorithm itself
//     rather than delegate to a helper.
//
// Requires: "cmp" and "slices" imports (Go 1.21+).
//
// Time complexity:  O(n)
// Space complexity: O(1)
func (s Solution) findClosestNumberMap(nums []int) int {
	abs := func(n int) int {
		if n < 0 {
			return -n
		}
		return n
	}
	return slices.MinFunc(nums, func(a, b int) int {
		absA, absB := abs(a), abs(b)
		if absA != absB {
			return cmp.Compare(absA, absB)
		}
		return cmp.Compare(b, a) // larger value wins on tie
	})
}

func main() {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{nums: []int{-4, -2, 1, 4, 8}, expected: 1},
		{nums: []int{2, -1, 1}, expected: 1},
		{nums: []int{-10, -5, 5, 10}, expected: 5},
		{nums: []int{0, -1, 1}, expected: 0},
		{nums: []int{-2, -3, 3, 2}, expected: 2},
	}

	sol := Solution{}

	for _, approach := range []struct {
		label string
		fn    func([]int) int
	}{
		{"findClosestNumber   ", sol.findClosestNumber},
		{"findClosestNumberMap", sol.findClosestNumberMap},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.nums)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | Input: nums=%v | Expected: %d | Result: %d | [%s]\n",
				i+1, tc.nums, tc.expected, result, status)
		}
	}
}
