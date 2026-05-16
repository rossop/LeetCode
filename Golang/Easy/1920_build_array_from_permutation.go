package main

import "fmt"

// buildArray returns ans where ans[i] = nums[nums[i]] using an O(n) auxiliary
// array.
//
// Time complexity:  O(n)
// Space complexity: O(n) — for the output array.
func buildArray(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = nums[nums[i]]
	}
	return ans
}

// buildArrayInPlace solves the follow-up: produce nums[nums[i]] in-place with
// O(1) extra space.
//
// Trick: pack new and old values into each slot. Since nums[i] < 1000 by the
// problem constraint, encode as old + 1000 * (new % 1000) — the high digits
// hold the answer, the low digits preserve the original so later indices can
// still recover it. A second pass divides out the encoding.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func buildArrayInPlace(nums []int) []int {
	n := len(nums)
	for i := 0; i < n; i++ {
		nums[i] += 1000 * (nums[nums[i]] % 1000)
	}

	for i := 0; i < n; i++ {
		nums[i] /= 1000
	}
	return nums
}

func main() {
	testCases := []struct {
		nums     []int
		expected []int
	}{
		{[]int{0, 2, 1, 5, 3, 4}, []int{0, 1, 2, 4, 5, 3}},
		{[]int{5, 0, 1, 2, 3, 4}, []int{4, 5, 0, 1, 2, 3}},
		{[]int{0}, []int{0}},
		{[]int{4, 3, 2, 1, 0}, []int{0, 1, 2, 3, 4}},
	}

	funcs := []struct {
		label string
		fn    func([]int) []int
	}{
		{"buildArray       ", buildArray},
		{"buildArrayInPlace", buildArrayInPlace},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			input := append([]int(nil), tc.nums...)
			result := f.fn(input)
			status := "PASS"
			if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | Input: %v | Expected: %v | Result: %v | [%s]\n",
				f.label, i+1, tc.nums, tc.expected, result, status)
		}
	}
}
