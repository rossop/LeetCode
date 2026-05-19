package main

import "fmt"

// getCommon returns the smallest integer present in both sorted (non-decreasing)
// arrays, or -1 if no element is shared.
//
// Two pointers walk in tandem; advance whichever side is smaller. On equality
// the value is the smallest common element (arrays are sorted), so return
// immediately. Disjoint-range checks short-circuit when the arrays don't
// overlap at all.
//
// Time complexity:  O(n + m)
// Space complexity: O(1)
func getCommon(nums1 []int, nums2 []int) int {
	p1, p2 := 0, 0
	n1, n2 := len(nums1), len(nums2)

	if nums1[0] > nums2[n2-1] {
		return -1
	}
	if nums2[0] > nums1[n1-1] {
		return -1
	}

	for p1 < n1 && p2 < n2 {
		if nums1[p1] < nums2[p2] {
			p1++
		} else if nums1[p1] > nums2[p2] {
			p2++
		} else {
			return nums1[p1]
		}
	}
	return -1
}

func main() {
	testCases := []struct {
		nums1    []int
		nums2    []int
		expected int
	}{
		{[]int{1, 2, 3}, []int{2, 4}, 2},
		{[]int{1, 2, 3, 6}, []int{2, 3, 4, 5}, 2},
		{[]int{1, 2, 3}, []int{4, 5, 6}, -1},
		{[]int{5}, []int{5}, 5},
		{[]int{1, 1, 2}, []int{2, 2, 3}, 2},
	}

	for i, tc := range testCases {
		result := getCommon(tc.nums1, tc.nums2)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: nums1=%v nums2=%v | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.nums1, tc.nums2, tc.expected, result, status)
	}
}
