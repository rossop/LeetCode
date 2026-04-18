package main

import "fmt"

// romanToInt converts a Roman numeral string to its integer value.
//
// Uses a map[byte]int for O(1) symbol lookup. Single left-to-right pass:
// if the current symbol is smaller than the next one it is a subtraction
// case (e.g. IV, IX, XL) so it is subtracted; otherwise it is added.
//
// Symbol values: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
//
// Time complexity:  O(n) — single pass over the string.
// Space complexity: O(1) — fixed-size lookup map.
func romanToInt(s string) int {
	romanMap := map[byte]int{
		'I': 1, 'V': 5, 'X': 10, 'L': 50,
		'C': 100, 'D': 500, 'M': 1000,
	}

	ans := 0
	n := len(s)

	for i := 0; i < n; i++ {
		if i < n-1 && romanMap[s[i]] < romanMap[s[i+1]] {
			ans -= romanMap[s[i]]
		} else {
			ans += romanMap[s[i]]
		}
	}
	return ans
}

func main() {
	testCases := []struct {
		s        string
		expected int
	}{
		{s: "III", expected: 3},
		{s: "IV", expected: 4},
		{s: "IX", expected: 9},
		{s: "LVIII", expected: 58},
		{s: "MCMXCIV", expected: 1994},
		{s: "MMMCMXCIX", expected: 3999},
	}

	for i, tc := range testCases {
		result := romanToInt(tc.s)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: s=%q | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.s, tc.expected, result, status)
	}
}
