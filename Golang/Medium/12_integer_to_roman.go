package main

import (
	"fmt"
	"strings"
)

// Solution groups all approaches for 12. Integer to Roman.
//
// Given an integer in [1, 3999], convert it to a Roman numeral.
// The thirteen value-symbol pairs (including the six subtraction cases)
// are listed in descending order; a greedy pass produces the correct result.
type Solution struct{}

// intToRoman converts num to a Roman numeral using strings.Builder.
//
// Iterates over a slice of anonymous structs holding (value, symbol) pairs
// in descending order. For each pair, repeatedly writes the symbol and
// subtracts the value while num >= value.
//
// strings.Builder is preferred over string concatenation in Go: it writes
// bytes into an internal buffer and allocates exactly once on String(). Each
// += on a string copies the entire string, making concatenation O(n²) in the
// worst case; Builder keeps it O(n).
//
// The slice of anonymous structs (rather than a map) preserves descending
// order without a separate sort step — Go maps have no guaranteed iteration
// order.
//
// Time complexity:  O(1) — iteration count is bounded by the fixed value range.
// Space complexity: O(1)
func (s Solution) intToRoman(num int) string {
	romanValues := []struct {
		value  int
		symbol string
	}{
		{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
		{100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
		{10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"},
		{1, "I"},
	}

	var builder strings.Builder

	for _, rv := range romanValues {
		for num >= rv.value {
			builder.WriteString(rv.symbol)
			num -= rv.value
		}
	}

	return builder.String()
}

// intToRomanConcat converts num to a Roman numeral using string concatenation.
//
// Identical greedy logic to intToRoman but accumulates the result with +=
// instead of strings.Builder. Simpler to read at the cost of extra allocations
// per append — acceptable here because the output length is bounded by a
// small constant (longest Roman numeral is "MMMCMXCIX", 9 characters).
//
// Time complexity:  O(1)
// Space complexity: O(1)
func (s Solution) intToRomanConcat(num int) string {
	romanValues := []struct {
		value  int
		symbol string
	}{
		{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
		{100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
		{10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"},
		{1, "I"},
	}

	result := ""

	for _, rv := range romanValues {
		for num >= rv.value {
			result += rv.symbol
			num -= rv.value
		}
	}
	return result
}

func main() {
	testCases := []struct {
		num      int
		expected string
	}{
		{num: 3749, expected: "MMMDCCXLIX"},
		{num: 58, expected: "LVIII"},
		{num: 1994, expected: "MCMXCIV"},
		{num: 1, expected: "I"},
		{num: 3999, expected: "MMMCMXCIX"},
		{num: 4, expected: "IV"},
		{num: 9, expected: "IX"},
		{num: 40, expected: "XL"},
		{num: 400, expected: "CD"},
		{num: 900, expected: "CM"},
	}

	sol := Solution{}

	for _, approach := range []struct {
		label string
		fn    func(int) string
	}{
		{"intToRoman      ", sol.intToRoman},
		{"intToRomanConcat", sol.intToRomanConcat},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.num)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | Input: num=%-4d | Expected: %-10s | Result: %-10s | [%s]\n",
				i+1, tc.num, tc.expected, result, status)
		}
	}
}
