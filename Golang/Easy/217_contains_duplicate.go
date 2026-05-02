package main

import "fmt"

// containsDuplicate reports whether any value in nums appears at least twice.
//
// Inserts every element into a map[int]struct{} (an idiomatic Go set), then
// compares the map length to the slice length. Always processes the entire
// slice even if a duplicate is found early.
//
// Time complexity:  O(n)
// Space complexity: O(n)
func containsDuplicate(nums []int) bool {
	set := make(map[int]struct{}, len(nums))
	for _, item := range nums {
		set[item] = struct{}{}
	}
	return len(nums) != len(set)
}

// containsDuplicateEarlyExit reports whether any value in nums appears at
// least twice, returning true as soon as the first duplicate is found.
//
// Time complexity:  O(n) worst case; faster in practice with early exit
// Space complexity: O(n)
func containsDuplicateEarlyExit(nums []int) bool {
	seen := make(map[int]bool)
	for _, n := range nums {
		if seen[n] {
			return true
		}
		seen[n] = true
	}
	return false
}

func main() {
	testCases := []struct {
		nums     []int
		expected bool
	}{
		{[]int{1, 2, 3, 1}, true},
		{[]int{1, 2, 3, 4}, false},
		{[]int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
		{[]int{1}, false},
	}

	for i, tc := range testCases {
		r1, r2 := containsDuplicate(tc.nums), containsDuplicateEarlyExit(tc.nums)
		s1, s2 := "PASS", "PASS"
		if r1 != tc.expected {
			s1 = "FAIL"
		}
		if r2 != tc.expected {
			s2 = "FAIL"
		}
		fmt.Printf("Example %d | Expected: %v | set: %v [%s] | earlyExit: %v [%s]\n",
			i+1, tc.expected, r1, s1, r2, s2)
	}
}
