package main

import (
	"fmt"
	"slices"
)

// isAnagramSort sorts the rune slices of both strings and compares them.
// Cheapest to write; pays a log factor you don't strictly need.
//
// Time complexity:  O(n log n)
// Space complexity: O(n) — rune slices.
func isAnagramSort(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	sRunes := []rune(s)
	tRunes := []rune(t)

	slices.Sort(sRunes)
	slices.Sort(tRunes)

	return slices.Equal(sRunes, tRunes)
}

// isAnagram uses a single rune-frequency map. Increment on s, decrement on
// t; bail the moment a count goes negative — that proves t has a character
// s doesn't (or has too many of one). The length pre-check rules out the
// "all positive at the end" case.
//
// Time complexity:  O(n)
// Space complexity: O(k), k = alphabet size.
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	counts := make(map[rune]int)

	for _, char := range s {
		counts[char]++
	}

	for _, char := range t {
		counts[char]--
		if counts[char] < 0 {
			return false
		}
	}
	return true
}

func main() {
	testCases := []struct {
		s        string
		t        string
		expected bool
	}{
		{"anagram", "nagaram", true},
		{"rat", "car", false},
		{"listen", "silent", true},
		{"a", "a", true},
		{"ab", "ba", true},
		{"abc", "cba", true},
		{"abc", "abcd", false},
		{"racecar", "carrace", true},
		{"jar", "jam", false},
	}

	funcs := []struct {
		label string
		fn    func(string, string) bool
	}{
		{"isAnagram    ", isAnagram},
		{"isAnagramSort", isAnagramSort},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			result := f.fn(tc.s, tc.t)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | s=%q t=%q | Expected: %t | Result: %t | [%s]\n",
				f.label, i+1, tc.s, tc.t, tc.expected, result, status)
		}
	}
}
