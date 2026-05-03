package main

import "fmt"

// distance returns arr where arr[i] = sum of |i - j| for all j with nums[j] == nums[i].
//
// TODO: implement
func distance(nums []int) []int {
	return make([]int, len(nums))
}

func main() {
	testCases := []struct {
		nums     []int
		expected []int
	}{
		{[]int{1, 3, 1, 1, 2}, []int{5, 0, 3, 4, 0}},
		{[]int{0, 5, 3}, []int{0, 0, 0}},
		{[]int{1, 1}, []int{1, 1}},
		{[]int{1, 1, 1}, []int{3, 2, 3}},
	}

	for i, tc := range testCases {
		result := distance(tc.nums)
		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.expected, result, status)
	}
}
