package main

import (
	"fmt"
	"strconv"
)

// longestCommonPrefix returns the length of the longest digit-prefix shared
// by any pair (x in arr1, y in arr2).
//
// Prefix-set approach: generate every prefix of every value in the smaller
// array by repeatedly dividing by 10 (each step chops one decimal digit),
// then for each value in the other array, peel digits off until a surviving
// prefix lives in the set. The length of that surviving number is the
// match length.
//
// Swapping so we hash the smaller side keeps the set as small as possible.
//
// Time complexity:  O((n + m) * D), D = max digit count.
// Space complexity: O(n * D)
func longestCommonPrefix(arr1 []int, arr2 []int) int {
	if len(arr1) > len(arr2) {
		arr1, arr2 = arr2, arr1
	}

	prefixSet := make(map[int]struct{})

	for _, n := range arr1 {
		for n > 0 {
			if _, ok := prefixSet[n]; ok {
				break
			}
			prefixSet[n] = struct{}{}
			n /= 10
		}
	}

	res := 0
	for _, n := range arr2 {
		for n > 0 {
			if _, ok := prefixSet[n]; ok {
				break
			}
			n /= 10
		}

		if n > 0 {
			if l := len(strconv.Itoa(n)); l > res {
				res = l
			}
		}
	}

	return res
}

func main() {
	testCases := []struct {
		arr1     []int
		arr2     []int
		expected int
	}{
		{[]int{1, 10, 100}, []int{1000}, 3},
		{[]int{1, 2, 3}, []int{4, 4, 4}, 0},
		{[]int{1}, []int{1}, 1},
		{[]int{12345}, []int{12399}, 3},
		{[]int{100, 200}, []int{3000, 4000}, 0},
		{[]int{987}, []int{123, 9870, 9876}, 3},
	}

	for i, tc := range testCases {
		result := longestCommonPrefix(tc.arr1, tc.arr2)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | arr1=%v arr2=%v | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.arr1, tc.arr2, tc.expected, result, status)
	}
}
