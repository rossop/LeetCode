package main

import (
	"fmt"
	"strings"
)

// isPalindrome reports whether s is a palindrome after lowercasing letters
// and ignoring non-alphanumeric characters.
//
// Two pointers walk inward from both ends, skipping any non-alphanumeric
// byte before comparing case-insensitively. No extra string is allocated
// for the filtered form — the skip is done in place on the index.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		for l < r && !isAlphaNum(s[l]) {
			l++
		}

		for r > l && !isAlphaNum(s[r]) {
			r--
		}

		if strings.ToLower(string(s[l])) != strings.ToLower(string(s[r])) {
			return false
		}
		l++
		r--
	}
	return true
}

func isAlphaNum(c byte) bool {
	return ('A' <= c && c <= 'Z') ||
		('a' <= c && c <= 'z') ||
		('0' <= c && c <= '9')
}

func main() {
	testCases := []struct {
		input    string
		expected bool
	}{
		{"A man, a plan, a canal: Panama", true},
		{"race a car", false},
		{" ", true},
		{"No lemon, no melon", true},
		{"Was it a car or a cat I saw?", true},
	}

	for i, tc := range testCases {
		result := isPalindrome(tc.input)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %q | Expected: %t | Result: %t | [%s]\n",
			i+1, tc.input, tc.expected, result, status)
	}
}
