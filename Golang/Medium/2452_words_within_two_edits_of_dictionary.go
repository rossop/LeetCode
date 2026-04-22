package main

import "fmt"

// twoEditWords returns all query words that are within two edits of any
// dictionary word.
//
// For each (query, dict_word) pair, counts mismatched character positions with
// an early-exit inner loop: as soon as differences > 2, the pair is abandoned.
// When a match is found the query is appended to the result and the dictionary
// loop breaks.
//
// Time complexity:  O(q * d * n) worst case; early exit reduces work in practice.
// Space complexity: O(q) for the output slice.
func twoEditWords(queries []string, dictionary []string) []string {
	var result []string
	for _, q := range queries {
		for _, d := range dictionary {
			differences := 0
			for i := 0; i < len(q); i++ {
				if q[i] != d[i] {
					differences++
					if differences > 2 {
						break
					}
				}
			}
			if differences <= 2 {
				result = append(result, q)
				break
			}
		}
	}
	return result
}

func main() {
	testCases := []struct {
		queries    []string
		dictionary []string
		expected   []string
	}{
		{
			queries:    []string{"word", "note", "ants", "wood"},
			dictionary: []string{"wood", "joke", "moat"},
			expected:   []string{"word", "note", "wood"},
		},
		{
			queries:    []string{"yes"},
			dictionary: []string{"not"},
			expected:   nil,
		},
		{
			queries:    []string{"abc"},
			dictionary: []string{"abc"},
			expected:   []string{"abc"},
		},
		{
			queries:    []string{"abc"},
			dictionary: []string{"xyz"},
			expected:   nil,
		},
	}

	for i, tc := range testCases {
		result := twoEditWords(tc.queries, tc.dictionary)
		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | queries=%v | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.queries, tc.expected, result, status)
	}
}
