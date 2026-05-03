package main

import (
	"fmt"
	"strings"
)

// rotateString reports whether goal is a rotation of s.
//
// Every rotation of s appears as a contiguous substring of s+s. A single
// strings.Contains call over the doubled string captures all n rotations.
//
// Time complexity:  O(n)
// Space complexity: O(n) for the concatenated string
func rotateString(s string, goal string) bool {
	return len(s) == len(goal) && strings.Contains(s+s, goal)
}

// rotateStringLoop reports whether goal is a rotation of s via explicit
// rotation, returning true as soon as a match is found.
//
// Time complexity:  O(n²) — n shifts each allocating an O(n) string
// Space complexity: O(n) per shift
func rotateStringLoop(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	if len(s) == 0 {
		return true
	}
	for i := 0; i < len(s); i++ {
		s = s[1:] + string(s[0])
		if s == goal {
			return true
		}
	}
	return false
}

func main() {
	testCases := []struct {
		s, goal  string
		expected bool
	}{
		{"abcde", "cdeab", true},
		{"abcde", "abced", false},
		{"a", "a", true},
		{"ab", "ba", true},
		{"aa", "aa", true},
		{"abc", "acb", false},
	}

	for i, tc := range testCases {
		r1, r2 := rotateString(tc.s, tc.goal), rotateStringLoop(tc.s, tc.goal)
		s1, s2 := "PASS", "PASS"
		if r1 != tc.expected {
			s1 = "FAIL"
		}
		if r2 != tc.expected {
			s2 = "FAIL"
		}
		fmt.Printf("Example %d | Expected: %v | contains: %v [%s] | loop: %v [%s]\n",
			i+1, tc.expected, r1, s1, r2, s2)
	}
}
