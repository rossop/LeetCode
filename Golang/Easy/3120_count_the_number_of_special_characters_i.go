package main

import (
	"fmt"
	"math/bits"
)

// numberOfSpecialChars counts letters that appear both lower- and upper-cased.
//
// Map approach: record every rune seen, then for each lowercase letter check
// whether its uppercase counterpart (c-'a'+'A') is also present.
//
// Time complexity:  O(n)
// Space complexity: O(1) — at most 52 keys.
func numberOfSpecialChars(word string) int {
	s := make(map[rune]bool)
	for _, c := range word {
		s[c] = true
	}

	ans := 0
	for c := 'a'; c <= 'z'; c++ {
		if s[c] && s[c-'a'+'A'] {
			ans++
		}
	}
	return ans
}

// numberOfSpecialCharsBitmask packs presence into two 26-bit masks, one for
// lowercase and one for uppercase. A letter is special iff its bit is set in
// both, so the answer is the popcount of their AND.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func numberOfSpecialCharsBitmask(word string) int {
	var lowerMask, upperMask int32

	for i := 0; i < len(word); i++ {
		ch := word[i]
		if ch >= 'a' && ch <= 'z' {
			lowerMask |= 1 << (ch - 'a')
		} else if ch >= 'A' && ch <= 'Z' {
			upperMask |= 1 << (ch - 'A')
		}
	}

	bothPresent := lowerMask & upperMask
	return bits.OnesCount32(uint32(bothPresent))
}

// numberOfSpecialCharsArrays mirrors the bitmask version with two boolean
// presence arrays, then counts indices flagged in both.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func numberOfSpecialCharsArrays(word string) int {
	const numOfLetters = 26
	var hasLower, hasUpper [numOfLetters]bool
	for i := 0; i < len(word); i++ {
		ch := word[i]
		if ch >= 'a' && ch <= 'z' {
			hasLower[ch-'a'] = true
		} else if ch >= 'A' && ch <= 'Z' {
			hasUpper[ch-'A'] = true
		}
	}

	count := 0
	for i := 0; i < numOfLetters; i++ {
		if hasLower[i] && hasUpper[i] {
			count++
		}
	}
	return count
}

func main() {
	testCases := []struct {
		word     string
		expected int
	}{
		{"aaAbcBC", 3},
		{"abc", 0},
		{"abBCab", 1},
		{"a", 0},
		{"aA", 1},
		{"AaBbCc", 3},
	}

	for _, approach := range []struct {
		label string
		fn    func(string) int
	}{
		{"numberOfSpecialChars       ", numberOfSpecialChars},
		{"numberOfSpecialCharsBitmask", numberOfSpecialCharsBitmask},
		{"numberOfSpecialCharsArrays ", numberOfSpecialCharsArrays},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.word)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | Input: %q | Expected: %d | Result: %d | [%s]\n",
				i+1, tc.word, tc.expected, result, status)
		}
	}
}
