package main

import "fmt"

// getDistances returns intervals where intervals[i] = sum of |i - j| for all j
// with arr[j] == arr[i].
//
// TODO: implement
func getDistances(arr []int) []int {
	return make([]int, len(arr))
}

func main() {
	testCases := []struct {
		arr      []int
		expected []int
	}{
		{[]int{2, 1, 3, 1, 2, 3, 3}, []int{4, 2, 7, 2, 4, 4, 5}},
		{[]int{10, 5, 10, 10}, []int{5, 0, 3, 4}},
		{[]int{1, 1}, []int{1, 1}},
		{[]int{1, 2, 3}, []int{0, 0, 0}},
	}

	for i, tc := range testCases {
		result := getDistances(tc.arr)
		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.expected, result, status)
	}
}
