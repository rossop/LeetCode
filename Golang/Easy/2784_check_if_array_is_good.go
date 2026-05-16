package main

import (
	"fmt"
	"slices"
	"sort"
)

// isGood reports whether nums is a permutation of base[n] = [1..n-1, n, n],
// where n = max(nums).
//
// Single pass with a mask of size n: each value v < n must appear exactly
// once; v == n is allowed twice. After the pass, max must have landed twice
// and every slot must be filled (sum == n + 1).
//
// Time complexity:  O(n)
// Space complexity: O(n)
func isGood(nums []int) bool {
	n := slices.Max(nums)
	mask := make([]int, n)

	for _, v := range nums {
		if v < n {
			if mask[v-1] == 0 {
				mask[v-1]++
			} else {
				return false
			}
		} else if v == n {
			mask[v-1]++
		}
	}

	return mask[n-1] == 2 && sum(mask) == n+1
}

// isGoodSort verifies the shape after sorting: length is max + 1, the last
// two entries are equal, and the leading prefix is 1..n-1 in order.
//
// Time complexity:  O(n log n)
// Space complexity: O(1) — in-place sort.
func isGoodSort(nums []int) bool {
	sort.Ints(nums)
	n := len(nums)

	if n < 2 {
		return false
	}
	if nums[n-1] != n-1 {
		return false
	}
	if nums[n-2] != nums[n-1] {
		return false
	}

	for i := 0; i < n-2; i++ {
		if nums[i] != i+1 {
			return false
		}
	}

	return true
}

func sum(arr []int) int {
	s := 0
	for _, v := range arr {
		s += v
	}
	return s
}

func main() {
	testCases := []struct {
		nums     []int
		expected bool
	}{
		{[]int{2, 1, 3}, false},
		{[]int{1, 3, 3, 2}, true},
		{[]int{1, 1}, true},
		{[]int{3, 4, 4, 1, 2, 1}, false},
		{[]int{1, 2, 3, 4, 4}, true},
	}

	funcs := []struct {
		label string
		fn    func([]int) bool
	}{
		{"isGood    ", isGood},
		{"isGoodSort", isGoodSort},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			input := append([]int(nil), tc.nums...)
			result := f.fn(input)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | Input: %v | Expected: %t | Result: %t | [%s]\n",
				f.label, i+1, tc.nums, tc.expected, result, status)
		}
	}
}
