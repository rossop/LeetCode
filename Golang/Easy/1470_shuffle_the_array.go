package main

import "fmt"

// shuffle returns nums = [x1..xn, y1..yn] re-laid as [x1, y1, x2, y2, ...].
//
// Pre-size the result to 2n and append (x_i, y_i) pairs in a single pass —
// no allocations beyond the output slice.
//
// Time complexity:  O(n)
// Space complexity: O(n) — for the output slice.
func shuffle(nums []int, n int) []int {
	solution := make([]int, 0, 2*n)
	for i := 0; i < n; i++ {
		solution = append(solution, nums[i], nums[n+i])
	}
	return solution
}

func main() {
	testCases := []struct {
		nums     []int
		n        int
		expected []int
	}{
		{[]int{2, 5, 1, 3, 4, 7}, 3, []int{2, 3, 5, 4, 1, 7}},
		{[]int{1, 2, 3, 4, 4, 3, 2, 1}, 4, []int{1, 4, 2, 3, 3, 2, 4, 1}},
		{[]int{1, 1, 2, 2}, 2, []int{1, 2, 1, 2}},
		{[]int{1, 2, 3, 4}, 2, []int{1, 3, 2, 4}},
		{[]int{10, 20, 30, 40, 50, 60}, 3, []int{10, 40, 20, 50, 30, 60}},
	}

	for i, tc := range testCases {
		result := shuffle(tc.nums, tc.n)
		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: nums=%v n=%d | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.nums, tc.n, tc.expected, result, status)
	}
}
