package main

import (
	"fmt"
	"slices"
)

// kidsWithCandies returns, for each kid, whether candy + extraCandies meets
// or exceeds the current maximum.
//
// The threshold (slices.Max) is computed once — adding candy never lowers it
// for anyone else, so the check is a simple linear pass.
//
// Time complexity:  O(n)
// Space complexity: O(n) — for the output slice.
func kidsWithCandies(candies []int, extraCandies int) []bool {
	target := slices.Max(candies)
	ans := make([]bool, len(candies))

	for i, candy := range candies {
		ans[i] = candy+extraCandies >= target
	}
	return ans
}

func main() {
	testCases := []struct {
		candies      []int
		extraCandies int
		expected     []bool
	}{
		{[]int{2, 3, 5, 1, 3}, 3, []bool{true, true, true, false, true}},
		{[]int{4, 2, 1, 1, 2}, 1, []bool{true, false, false, false, false}},
		{[]int{12, 1, 12}, 10, []bool{true, false, true}},
		{[]int{1, 1}, 1, []bool{true, true}},
	}

	for i, tc := range testCases {
		result := kidsWithCandies(tc.candies, tc.extraCandies)
		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: candies=%v extra=%d | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.candies, tc.extraCandies, tc.expected, result, status)
	}
}
