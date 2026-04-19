package main

import "fmt"

// maxDistance returns the maximum distance j - i over all valid pairs (i, j)
// where i <= j and nums1[i] <= nums2[j].
//
// Two-pointer strategy exploiting the non-increasing property of both arrays:
//   - If nums1[i] <= nums2[j]: valid pair found; record the distance and advance
//     j to search for a larger distance.
//   - If nums1[i] > nums2[j]: no valid j exists at this position for this i;
//     advance i to try a smaller nums1 value.
//
// When i temporarily exceeds j the distance j-i is negative; max() with the
// running best ensures those iterations don't affect the result.
//
// Time complexity:  O(n + m) — each pointer moves at most len(nums1)+len(nums2) steps.
// Space complexity: O(1)
func maxDistance(nums1 []int, nums2 []int) int {
	i, j := 0, 0
	maxDist := 0
	len1, len2 := len(nums1), len(nums2)

	for i < len1 && j < len2 {
		if nums1[i] <= nums2[j] {
			if d := j - i; d > maxDist {
				maxDist = d
			}
			j++
		} else {
			i++
		}
	}
	return maxDist
}

// maxDistanceNaive returns the maximum distance using nested loops.
//
// For each i, scans j from i onwards and breaks early when nums2[j] drops
// below nums1[i] (valid because nums2 is non-increasing). Worst case O(n × m).
//
// Time complexity:  O(n × m)
// Space complexity: O(1)
func maxDistanceNaive(nums1 []int, nums2 []int) int {
	maxDist := 0
	len1, len2 := len(nums1), len(nums2)

	for i := 0; i < len1; i++ {
		for j := i; j < len2; j++ {
			if nums1[i] <= nums2[j] {
				if d := j - i; d > maxDist {
					maxDist = d
				}
			} else {
				break
			}
		}
	}
	return maxDist
}

func main() {
	testCases := []struct {
		nums1    []int
		nums2    []int
		expected int
	}{
		{nums1: []int{55, 30, 5, 4, 2}, nums2: []int{100, 20, 10, 10, 5}, expected: 2},
		{nums1: []int{2, 2, 2}, nums2: []int{10, 10, 1}, expected: 1},
		{nums1: []int{30, 29, 19, 5}, nums2: []int{25, 25, 25, 25, 25}, expected: 2},
		{nums1: []int{5}, nums2: []int{5}, expected: 0},
		{nums1: []int{1}, nums2: []int{1}, expected: 0},
	}

	for _, approach := range []struct {
		label string
		fn    func([]int, []int) int
	}{
		{"maxDistance     ", maxDistance},
		{"maxDistanceNaive", maxDistanceNaive},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.nums1, tc.nums2)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | nums1=%v nums2=%v | Expected: %d | Result: %d | [%s]\n",
				i+1, tc.nums1, tc.nums2, tc.expected, result, status)
		}
	}
}
