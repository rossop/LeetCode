package main

import "fmt"

// Solution groups all approaches for 1646. Get Maximum in Generated Array.
//
// The generated array of length n+1 is defined by:
//
//	nums[0] = 0
//	nums[1] = 1
//	nums[2*i]   = nums[i]              when 2 <= 2*i <= n
//	nums[2*i+1] = nums[i] + nums[i+1]  when 2 <= 2*i+1 <= n
type Solution struct{}

// getMaximumGeneratedNaive returns the maximum of the generated array using
// naive recursion.
//
// Each index is computed by recursively applying the even/odd rules with no
// caching. Overlapping subproblems are recomputed on every call, producing
// exponential work for large n.
//
// Time complexity:  O(2^n) — each call branches into two recursive calls.
// Space complexity: O(n)   — call stack depth.
func (s Solution) getMaximumGeneratedNaive(n int) int {
	var generate func(i int) int
	generate = func(i int) int {
		if i == 0 {
			return 0
		}
		if i == 1 {
			return 1
		}
		if i%2 == 0 {
			return generate(i / 2)
		}
		return generate(i/2) + generate(i/2+1)
	}
	max := 0
	for i:=0; i <= n; i++ {
		if v := generate(i); v > max {
			max = v
		}
	}
	return max
}

// getMaximumGeneratedMemo returns the maximum of the generated array using
// memoized recursion (top-down dynamic programming).
//
// Same recursive structure as the naive approach, but each computed value is
// stored in a map on the way down. Cache hits short-circuit further recursion,
// so each index is computed exactly once.
//
// Time complexity:  O(n) — each index computed once.
// Space complexity: O(n) — memo map and call stack.
func (s Solution) getMaximumGeneratedMemo(n int) int {
	memo := map[int]int{}

	var generate func(i int) int
	generate = func(i int) int {
		if i == 0 {
			return 0
		}
		if i == 1 {
			return 1
		}
		if v, ok := memo[i]; ok {
			return v
		}
		var result int
		if i%2 == 0 {
			result = generate(i/2)
		} else {
			result = generate(i/2) + generate(i/2 + 1)
		}
		memo[i] = result
		return result
	}
	max := 0
	for i:=0; i <= n; i ++ {
		if v := generate(i); v > max {
			max = v
		}
	}
	return max
}

// getMaximumGenerated returns the maximum of the generated array using
// tabulation (bottom-up dynamic programming).
//
// Allocates a slice of length n+1, sets the base cases, then fills each index
// iteratively using the even/odd rules. No recursion or call stack overhead.
//
// Time complexity:  O(n) — single pass to fill the slice.
// Space complexity: O(n) — the slice of length n+1.
func (s Solution) getMaximumGenerated(n int) int {
	if n == 0 {
		return 0
	}
	nums := make([]int, n+1)
	nums[1] = 1
	for i:=2; i <= n; i++ {
		if i%2 == 0 {
			nums[i] = nums[i/2]
		} else {
			nums[i] = nums[i/2] + nums[i/2+1]
		}
	}
	max := 0
	for _, v := range nums {
		if v > max {
			max = v
		}
	}
	return max
}

func main() {
	testCases := []struct {
		n        int
		expected int
	}{
		{n: 7, expected: 3},
		{n: 2, expected: 1},
		{n: 3, expected: 2},
	}

	s := Solution{}

	for _, approach := range []struct {
		label string
		fn    func(int) int
	}{
		{"Naive", s.getMaximumGeneratedNaive},
		{"Memo", s.getMaximumGeneratedMemo},
		{"Tabulation", s.getMaximumGenerated},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.n)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | Input: n=%d | Expected: %d | Result: %d | [%s]\n",
				i+1, tc.n, tc.expected, result, status)
		}
	}
}
