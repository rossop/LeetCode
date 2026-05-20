package main

import (
	"fmt"
	"math/bits"
)

// findThePrefixCommonArray returns C where C[i] counts the integers present
// in both A[0..i] and B[0..i]. A and B are permutations of 1..n with n <= 50.
//
// Bitmask intersection. maskA / maskB each carry a bit per value seen so
// far on their side; (maskA & maskB) is the running intersection, and
// bits.OnesCount64 reads its size in one instruction. n <= 50 fits in a
// single uint64, so the whole prefix lives in two CPU registers.
//
// Time complexity:  O(n)
// Space complexity: O(1) extra (besides the output slice).
func findThePrefixCommonArray(A []int, B []int) []int {
	n := len(A)
	ans := make([]int, n)

	var maskA, maskB uint64

	for i := 0; i < n; i++ {
		maskA |= (1 << A[i])
		maskB |= (1 << B[i])

		ans[i] = bits.OnesCount64(maskA & maskB)
	}
	return ans
}

// findThePrefixCommonArraySeenTwice is the frequency-array variant: any
// value seen twice (once in A, once in B — permutation guarantees no
// duplicates within a side) is common. A single counter tracks how many
// such crossings have occurred.
//
// Time complexity:  O(n)
// Space complexity: O(n)
func findThePrefixCommonArraySeenTwice(A []int, B []int) []int {
	n := len(A)
	ans := make([]int, n)

	seen := make([]int, n+1)
	commonCount := 0

	for i := 0; i < n; i++ {
		seen[A[i]]++
		if seen[A[i]] == 2 {
			commonCount++
		}

		seen[B[i]]++
		if seen[B[i]] == 2 {
			commonCount++
		}

		ans[i] = commonCount
	}

	return ans
}

// findThePrefixCommonArraySet is the map-set baseline — clearest to read,
// quadratic to run because the per-step intersection scans the smaller set.
//
// Time complexity:  O(n^2)
// Space complexity: O(n)
func findThePrefixCommonArraySet(A []int, B []int) []int {
	n := len(A)
	ans := make([]int, n)
	setA := make(map[int]struct{})
	setB := make(map[int]struct{})

	for i := 0; i < n; i++ {
		setA[A[i]] = struct{}{}
		setB[B[i]] = struct{}{}
		ans[i] = len(intersect(setA, setB))
	}

	return ans
}

func intersect(set1, set2 map[int]struct{}) map[int]struct{} {
	intersection := make(map[int]struct{})

	if len(set1) > len(set2) {
		set1, set2 = set2, set1
	}

	for item := range set1 {
		if _, exists := set2[item]; exists {
			intersection[item] = struct{}{}
		}
	}
	return intersection
}

func main() {
	testCases := []struct {
		A        []int
		B        []int
		expected []int
	}{
		{[]int{1, 3, 2, 4}, []int{3, 1, 2, 4}, []int{0, 2, 3, 4}},
		{[]int{2, 3, 1}, []int{3, 1, 2}, []int{0, 1, 3}},
		{[]int{1}, []int{1}, []int{1}},
		{[]int{1, 2}, []int{2, 1}, []int{0, 2}},
	}

	funcs := []struct {
		label string
		fn    func([]int, []int) []int
	}{
		{"findThePrefixCommonArray           ", findThePrefixCommonArray},
		{"findThePrefixCommonArraySeenTwice  ", findThePrefixCommonArraySeenTwice},
		{"findThePrefixCommonArraySet        ", findThePrefixCommonArraySet},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			result := f.fn(tc.A, tc.B)
			status := "PASS"
			if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | A=%v B=%v | Expected: %v | Result: %v | [%s]\n",
				f.label, i+1, tc.A, tc.B, tc.expected, result, status)
		}
	}
}
