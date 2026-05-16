package main

import (
	"fmt"
	"strings"
)

// findWordsContaining returns every index i such that words[i] contains the
// character x.
//
// strings.Contains handles the substring search. Order matches input order.
//
// Time complexity:  O(n * m), n = len(words), m = avg word length.
// Space complexity: O(k), k = number of matching words.
func findWordsContaining(words []string, x byte) []int {
	indexes := []int{}
	for i, word := range words {
		if strings.Contains(word, string(x)) {
			indexes = append(indexes, i)
		}
	}

	return indexes
}

// findWordsContainingBare is the manual byte-scan variant — no stdlib search,
// breaks on first match per word.
//
// Time complexity:  O(n * m)
// Space complexity: O(k)
func findWordsContainingBare(words []string, x byte) []int {
	res := []int{}

	for i, word := range words {
		for j := 0; j < len(word); j++ {
			if word[j] == x {
				res = append(res, i)
				break
			}
		}
	}
	return res
}

func main() {
	testCases := []struct {
		words    []string
		x        byte
		expected []int
	}{
		{[]string{"leet", "code"}, 'e', []int{0, 1}},
		{[]string{"abc", "bcd", "aaaa", "cbc"}, 'a', []int{0, 2}},
		{[]string{"abc", "bcd", "aaaa", "cbc"}, 'z', []int{}},
	}

	funcs := []struct {
		label string
		fn    func([]string, byte) []int
	}{
		{"findWordsContaining    ", findWordsContaining},
		{"findWordsContainingBare", findWordsContainingBare},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			result := f.fn(tc.words, tc.x)
			status := "PASS"
			if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | Input: words=%v x=%q | Expected: %v | Result: %v | [%s]\n",
				f.label, i+1, tc.words, tc.x, tc.expected, result, status)
		}
	}
}
