package main

import "fmt"

// smallerNumbersThanCurrent returns, for each i, the count of j != i with
// nums[j] < nums[i].
//
// Counting sort + prefix sum over the value range [0, 100]: the prefix at
// v - 1 is exactly the number of values strictly less than v. Independent
// of n once the histogram is built.
//
// Time complexity:  O(n + k), k = 101 (the value range).
// Space complexity: O(k)
func smallerNumbersThanCurrent(nums []int) []int {
	maxPossibleNum := 101
	allNums := make([]int, maxPossibleNum)
	res := make([]int, len(nums))

	for _, v := range nums {
		allNums[v]++
	}

	for i := 1; i < maxPossibleNum; i++ {
		allNums[i] += allNums[i-1]
	}

	for i := 0; i < len(nums); i++ {
		v := nums[i]
		if v == 0 {
			res[i] = 0
		} else {
			res[i] = allNums[v-1]
		}
	}
	return res
}

func main() {
	testCases := []struct {
		nums     []int
		expected []int
	}{
		{[]int{8, 1, 2, 2, 3}, []int{4, 0, 1, 1, 3}},
		{[]int{6, 5, 4, 8}, []int{2, 1, 0, 3}},
		{[]int{7, 7, 7, 7}, []int{0, 0, 0, 0}},
		{[]int{0, 0, 1}, []int{0, 0, 2}},
	}

	for i, tc := range testCases {
		result := smallerNumbersThanCurrent(append([]int(nil), tc.nums...))
		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %v | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.nums, tc.expected, result, status)
	}
}
