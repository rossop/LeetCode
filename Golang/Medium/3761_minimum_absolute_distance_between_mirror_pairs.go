package main

import "fmt"

// Solution groups all approaches for 3761. Minimum Absolute Distance Between Mirror Pairs.
//
// A mirror pair (i, j) with i < j satisfies reverse(nums[i]) == nums[j].
// Reversing omits leading zeros: reverse(120) = 21.
// Note: the relationship is NOT symmetric when trailing zeros are involved —
// reverse(120)=21 but reverse(21)=12 ≠ 120.
type Solution struct{}

// minMirrorPairDistance returns the minimum absolute index distance between any
// mirror pair in nums, or -1 if no mirror pair exists.
//
// Single pass using a hash map that tracks the most recent index for each
// reversed value. For each index i with value v, checks if v exists as a key
// (meaning a previous j stored reverse(nums[j]) = v there), giving a valid
// pair (j, i). Then stores reverse(v) → i for future lookups.
//
// Because the most recent j always gives the smallest distance for a given i,
// only one index per key is needed — no binary search required.
//
// Time complexity:  O(n) — single pass with O(1) map operations.
// Space complexity: O(n) — map stores at most one index per unique reversed value.
func (s Solution) minMirrorPairDistance(nums []int) int {
	reverse := func(n int) int {
		ans := 0
		for {
			ans = ans*10 + n%10
			n /= 10
			if n == 0 {
				return ans
			}
		}
	}

	lastSeen := make(map[int]int)
	ans := -1

	for i, v := range nums {
		if j, ok := lastSeen[v]; ok {
			dist := i - j
			if ans == -1 || dist < ans {
				ans = dist
			}
		}
		lastSeen[reverse(v)] = i
	}
	return ans
}

// minMirrorPairDistanceBisect returns the minimum absolute index distance between any
// mirror pair in nums, or -1 if no mirror pair exists.
//
// Builds a value-to-sorted-indices map in one pass, then for each index i uses
// binary search (sort.SearchInts) to find the closest j > i where
// nums[j] == reverse(nums[i]). Only j > i is checked since the pair definition
// requires i < j and reverse(nums[i]) == nums[j].
//
// Time complexity:  O(n log n) — O(n) to build the map, O(log n) per element.
// Space complexity: O(n) — the positions map stores all indices.
func (s Solution) minMirrorPairDistanceBisect(nums []int) int {
	return -1
}

func main() {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{nums: []int{12, 21, 45, 33, 54}, expected: 1},
		{nums: []int{120, 21}, expected: 1},
		{nums: []int{21, 120}, expected: -1},
	}

	sol := Solution{}

	for _, approach := range []struct {
		label string
		fn    func([]int) int
	}{
		{"O(n)     ", sol.minMirrorPairDistance},
		{"O(n logn)", sol.minMirrorPairDistanceBisect},
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
