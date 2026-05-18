package main

import "fmt"

// canJump returns whether the last index of nums is reachable from index 0,
// given that nums[i] is the maximum jump length from position i.
//
// Greedy, right-to-left. Track the leftmost index target from which the goal
// is known reachable. Any i with i + nums[i] >= target replaces target,
// dragging the frontier left. Reachable iff target collapses to 0.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func canJump(nums []int) bool {
	n := len(nums)
	target := n - 1

	for i := n - 1; i >= 0; i-- {
		maxJump := nums[i]
		if i+maxJump >= target {
			target = i
		}
	}

	return target == 0
}

// canJumpMemoisation is the top-down DP variant: canReach(i) tests every
// jump length and caches the result.
//
// Time complexity:  O(n^2)
// Space complexity: O(n)
func canJumpMemoisation(nums []int) bool {
	n := len(nums)
	memo := make(map[int]bool)
	memo[n-1] = true

	var canReach func(i int) bool
	canReach = func(i int) bool {
		if val, ok := memo[i]; ok {
			return val
		}

		for jump := 1; jump <= nums[i]; jump++ {
			if canReach(i + jump) {
				memo[i] = true
				return true
			}
		}
		memo[i] = false
		return false
	}

	return canReach(0)
}

// canJumpRecursive is the plain recursive baseline — exponential, kept to
// show what memoisation actually saves.
//
// Time complexity:  O(max(nums)^n)
// Space complexity: O(n) — recursion depth.
func canJumpRecursive(nums []int) bool {
	n := len(nums)

	var canReach func(i int) bool
	canReach = func(i int) bool {
		if i >= n-1 {
			return true
		}

		for jump := 1; jump <= nums[i]; jump++ {
			if canReach(i + jump) {
				return true
			}
		}
		return false
	}

	return canReach(0)
}

func main() {
	testCases := []struct {
		nums     []int
		expected bool
	}{
		{[]int{2, 3, 1, 1, 4}, true},
		{[]int{3, 2, 1, 0, 4}, false},
		{[]int{0}, true},
		{[]int{2, 0, 0}, true},
		{[]int{1, 0, 1, 0}, false},
	}

	funcs := []struct {
		label string
		fn    func([]int) bool
	}{
		{"canJump            ", canJump},
		{"canJumpMemoisation ", canJumpMemoisation},
		{"canJumpRecursive   ", canJumpRecursive},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			result := f.fn(append([]int(nil), tc.nums...))
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | Input: %v | Expected: %t | Result: %t | [%s]\n",
				f.label, i+1, tc.nums, tc.expected, result, status)
		}
	}
}
