package main

import "fmt"

// Solution groups all approaches for 1768. Merge Strings Alternately.
//
// Given two strings word1 and word2, merge them by adding letters in
// alternating order starting with word1. If one string is longer, append the
// remaining letters at the end.
type Solution struct{}

// mergeAlternately merges word1 and word2 alternately using a two-pointer
// while loop over a pre-allocated byte slice.
//
// Uses []byte instead of a string builder or repeated concatenation to avoid
// allocating a new string on every append. The byte slice is pre-allocated
// with capacity n+m so no re-allocations occur during the loop.
// Casting to string(result) once at the end is the only final allocation.
//
// Time complexity:  O(n1 + n2)
// Space complexity: O(n1 + n2)
func (s Solution) mergeAlternately(word1, word2 string) string {
	n, m := len(word1), len(word2)
	result := make([]byte, 0, n+m)
	i, j := 0, 0

	for i < n || j < m {
		if i < n {
			result = append(result, word1[i])
			i++
		}
		if j < m {
			result = append(result, word2[j])
			j++
		}
	}

	return string(result)
}

// mergeAlternatelyMinLoop merges word1 and word2 alternately using a
// two-phase approach: one loop up to min(n, m) appending both characters at
// once, then a single append of the remaining tail.
//
// append(result, word1[i], word2[i]) adds two bytes in one call, avoiding a
// second append per iteration. word1[l:]... spreads the remaining bytes
// directly into the slice — no character-by-character loop for the tail.
// min() is a built-in as of Go 1.21.
//
// Time complexity:  O(n1 + n2)
// Space complexity: O(n1 + n2)
func (s Solution) mergeAlternatelyMinLoop(word1, word2 string) string {
	n, m := len(word1), len(word2)
	l := min(n, m)
	result := make([]byte, 0, n+m)

	for i := 0; i < l; i++ {
		result = append(result, word1[i], word2[i])
	}

	result = append(result, word1[l:]...)
	result = append(result, word2[l:]...)

	return string(result)
}

// mergeAlternatelyMap merges word1 and word2 alternately by iterating up to
// max(len(word1), len(word2)) and appending each character when in range.
//
// Time complexity:  O(n1 + n2)
// Space complexity: O(n1 + n2)
func (s Solution) mergeAlternatelyMap(word1, word2 string) string {
	return "" // TODO
}

func main() {
	testCases := []struct {
		word1    string
		word2    string
		expected string
	}{
		{word1: "abc", word2: "pqr", expected: "apbqcr"},
		{word1: "ab", word2: "pqrs", expected: "apbqrs"},
		{word1: "abcd", word2: "pq", expected: "apbqcd"},
	}

	sol := Solution{}

	for _, approach := range []struct {
		label string
		fn    func(string, string) string
	}{
		{"mergeAlternately      ", sol.mergeAlternately},
		{"mergeAlternatelyMinLoop", sol.mergeAlternatelyMinLoop},
		{"mergeAlternatelyMap   ", sol.mergeAlternatelyMap},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.word1, tc.word2)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | Input: word1=%q word2=%q | Expected: %q | Result: %q | [%s]\n",
				i+1, tc.word1, tc.word2, tc.expected, result, status)
		}
	}
}
