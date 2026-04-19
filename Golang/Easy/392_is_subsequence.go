package main

import "fmt"

// Solution groups all approaches for 392. Is Subsequence.
//
// Given two strings s and t, return true if s is a subsequence of t, or false
// otherwise. A subsequence preserves relative order but need not be contiguous.
type Solution struct{}

// isSubsequence returns true if s is a subsequence of t.
//
// Two-pointer approach: ps tracks progress through s, pt through t.
// On every iteration pt advances; ps advances only on a character match.
// s is a subsequence of t iff ps reaches len(s) before pt is exhausted.
//
// Time complexity:  O(len(t))
// Space complexity: O(1)
func (sol Solution) isSubsequence(s, t string) bool {
	ps, pt := 0, 0
	lenS, lenT := len(s), len(t)

	for ps < lenS && pt < lenT {
		if s[ps] == t[pt] {
			ps++
		}
		pt++
	}
	return ps == lenS
}

// isSubsequenceAlternative returns true if s is a subsequence of t using an
// explicit for loop over t with early return on full match.
//
// Time complexity:  O(len(t))
// Space complexity: O(1)
func (sol Solution) isSubsequenceAlternative(s, t string) bool {
	return false // TODO
}

func main() {
	testCases := []struct {
		s        string
		t        string
		expected bool
	}{
		{s: "abc", t: "ahbgdc", expected: true},
		{s: "axc", t: "ahbgdc", expected: false},
		{s: "", t: "ahbgdc", expected: true},
		{s: "abc", t: "", expected: false},
		{s: "ahbgdc", t: "ahbgdc", expected: true},
	}

	sol := Solution{}

	for _, approach := range []struct {
		label string
		fn    func(string, string) bool
	}{
		{"isSubsequence           ", sol.isSubsequence},
		{"isSubsequenceAlternative", sol.isSubsequenceAlternative},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.s, tc.t)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | Input: s=%q t=%q | Expected: %v | Result: %v | [%s]\n",
				i+1, tc.s, tc.t, tc.expected, result, status)
		}
	}
}
