package main

import "fmt"

// closetTarget returns the shortest distance from startIndex to any occurrence
// of target in the circular array words, or -1 if target is not present.
//
// For a circular array of length n, the distance between indices a and b is:
//
//	min(|a - b|, n - |a - b|)
//
// Parameters:
//   - words:      the circular string array
//   - target:     the string to search for
//   - startIndex: the index to start from
//
// Returns the minimum distance to any occurrence of target, or -1 if absent.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func closetTarget(words []string, target string, startIndex int) int {
	n := len(words)
	// Sentinel options:
	//   n+1  — safe but loose; valid distances are in [0, n-1]
	//   n/2+1 — tightest safe value; going both ways, the worst-case shortest
	//            distance is n/2 (opposite side of the array), so n/2+1 can
	//            never be a real result
	res := n/2 + 1

	for i, v := range words {
		if v == target {
			// direct distance between startIndex and i (ignoring wrap)
			diff := i - startIndex
			if diff < 0 {
				diff = -diff
			}
			// clockwise: diff steps right
			// counter-clockwise: n - diff steps left
			// take the shorter of the two
			if diff < n-diff {
				res = min(res, diff)
			} else {
				res = min(res, n-diff)
			}
		}
	}

	if res == n/2+1 {
		return -1 // target was never found
	}
	return res
}

func main() {
	testCases := []struct {
		words       []string
		target      string
		startIndex  int
		expected    int
	}{
		{words: []string{"hello", "i", "am", "leetcode", "hello"}, target: "hello", startIndex: 1, expected: 1},
		{words: []string{"a", "b", "leetcode"}, target: "leetcode", startIndex: 0, expected: 1},
		{words: []string{"i", "eat", "leetcode"}, target: "ate", startIndex: 0, expected: -1},
	}

	for i, tc := range testCases {
		result := closetTarget(tc.words, tc.target, tc.startIndex)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: words=%v target=%q startIndex=%d | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.words, tc.target, tc.startIndex, tc.expected, result, status)
	}
}
