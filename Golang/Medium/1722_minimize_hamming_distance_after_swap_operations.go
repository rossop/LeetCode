package main

import "fmt"

// Solution groups all approaches for 1722. Minimize Hamming Distance After
// Swap Operations.
//
// Indices connected through allowedSwaps form components within which source
// elements can be freely rearranged. The minimum Hamming distance equals the
// number of target positions that cannot be matched by any available source
// value within the same component.
type Solution struct{}

// minimumHammingDistance returns the minimum Hamming distance using Union-Find.
//
// Unions all swap pairs into components, groups source values by component root
// into a frequency map, then greedily matches target values against the map.
//
// Time complexity:  O(n + m·α(n)) where m = len(allowedSwaps).
// Space complexity: O(n)
func (sol Solution) minimumHammingDistance(source, target []int, allowedSwaps [][]int) int {
	return 0 // TODO
}

// minimumHammingDistanceDFS returns the minimum Hamming distance using DFS to
// find connected components on the swap graph.
//
// Builds an adjacency list from allowedSwaps, finds each connected component
// via DFS, then counts how many target values in the component are unmatched
// by source values using frequency maps and min(src_freq, tgt_freq).
//
// Time complexity:  O(n + m) where m = len(allowedSwaps).
// Space complexity: O(n + m)
func (sol Solution) minimumHammingDistanceDFS(source, target []int, allowedSwaps [][]int) int {
	return 0 // TODO
}

func main() {
	testCases := []struct {
		source       []int
		target       []int
		allowedSwaps [][]int
		expected     int
	}{
		{
			source: []int{1, 2, 3, 4}, target: []int{2, 1, 4, 5},
			allowedSwaps: [][]int{{0, 1}, {2, 3}}, expected: 1,
		},
		{
			source: []int{1, 2, 3, 4}, target: []int{1, 3, 2, 4},
			allowedSwaps: [][]int{}, expected: 2,
		},
		{
			source: []int{5, 1, 2, 4, 3}, target: []int{1, 5, 4, 2, 3},
			allowedSwaps: [][]int{{0, 4}, {4, 2}, {1, 3}, {1, 4}}, expected: 0,
		},
		{source: []int{1}, target: []int{1}, allowedSwaps: [][]int{}, expected: 0},
		{source: []int{1}, target: []int{2}, allowedSwaps: [][]int{}, expected: 1},
	}

	sol := Solution{}

	for _, approach := range []struct {
		label string
		fn    func([]int, []int, [][]int) int
	}{
		{"minimumHammingDistance   ", sol.minimumHammingDistance},
		{"minimumHammingDistanceDFS", sol.minimumHammingDistanceDFS},
	} {
		fmt.Printf("--- %s ---\n", approach.label)
		for i, tc := range testCases {
			result := approach.fn(tc.source, tc.target, tc.allowedSwaps)
			status := "PASS"
			if result != tc.expected {
				status = "FAIL"
			}
			fmt.Printf("  Example %d | source=%v target=%v | Expected: %d | Result: %d | [%s]\n",
				i+1, tc.source, tc.target, tc.expected, result, status)
		}
	}
}
