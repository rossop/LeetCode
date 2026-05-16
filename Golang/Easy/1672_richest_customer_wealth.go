package main

import "fmt"

func sum(list []int) int {
	ans := 0
	for _, val := range list {
		ans += val
	}
	return ans
}

// maximumWealth returns the largest row-sum in accounts — i.e., the wealth of
// the richest customer.
//
// Sum each row and keep the running max. No materialized totals needed.
//
// Time complexity:  O(m * n)
// Space complexity: O(1)
func maximumWealth(accounts [][]int) int {
	ans := 0

	for _, acc := range accounts {
		ans = max(sum(acc), ans)
	}
	return ans
}

func main() {
	testCases := []struct {
		accounts [][]int
		expected int
	}{
		{[][]int{{1, 2, 3}, {3, 2, 1}}, 6},
		{[][]int{{1, 5}, {7, 3}, {3, 5}}, 10},
		{[][]int{{2, 8, 7}, {7, 1, 3}, {1, 9, 5}}, 17},
		{[][]int{{100}}, 100},
	}

	for i, tc := range testCases {
		result := maximumWealth(tc.accounts)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %v | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.accounts, tc.expected, result, status)
	}
}
