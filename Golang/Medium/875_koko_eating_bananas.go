package main

import "fmt"

// calcHours returns the total hours needed to eat every pile at speed k,
// using ceiling division per pile.
func calcHours(piles []int, k int) int {
	totalHours := 0
	for _, p := range piles {
		totalHours += (p + k - 1) / k
	}
	return totalHours
}

// minEatingSpeed returns the minimum integer eating speed k that lets Koko
// finish all piles within h hours.
//
// The predicate "hours(k) <= h" is monotonic in k, so binary search over
// k in [1, max(piles)] finds the lower bound where it first holds.
//
// Time complexity:  O(n log m), n = len(piles), m = max(piles).
// Space complexity: O(1)
func minEatingSpeed(piles []int, h int) int {
	maxPile := 0
	for _, p := range piles {
		if p > maxPile {
			maxPile = p
		}
	}

	left, right := 1, maxPile
	res := right

	for left <= right {
		mid := left + (right-left)/2
		if calcHours(piles, mid) <= h {
			res = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return res
}

func main() {
	testCases := []struct {
		piles    []int
		h        int
		expected int
	}{
		{[]int{3, 6, 7, 11}, 8, 4},
		{[]int{30, 11, 23, 4, 20}, 5, 30},
		{[]int{30, 11, 23, 4, 20}, 6, 23},
		{[]int{1}, 1, 1},
		{[]int{1000000000}, 2, 500000000},
	}

	for i, tc := range testCases {
		result := minEatingSpeed(append([]int(nil), tc.piles...), tc.h)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: piles=%v h=%d | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.piles, tc.h, tc.expected, result, status)
	}
}
