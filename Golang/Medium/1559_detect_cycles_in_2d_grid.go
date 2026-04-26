package main

import "fmt"

// containsCycle reports whether the grid contains a cycle of length >= 4
// formed by adjacent cells with the same character value.
//
// TODO: implement
func containsCycle(grid [][]byte) bool {
	return false
}

func main() {
	testCases := []struct {
		grid     [][]byte
		expected bool
	}{
		{
			grid: [][]byte{
				{'a', 'a', 'a', 'a'},
				{'a', 'b', 'b', 'a'},
				{'a', 'b', 'b', 'a'},
				{'a', 'a', 'a', 'a'},
			},
			expected: true,
		},
		{
			grid: [][]byte{
				{'c', 'c', 'c', 'a'},
				{'c', 'd', 'c', 'c'},
				{'c', 'c', 'e', 'c'},
				{'f', 'c', 'c', 'c'},
			},
			expected: true,
		},
		{
			grid: [][]byte{
				{'a', 'b', 'b'},
				{'b', 'z', 'b'},
				{'b', 'b', 'a'},
			},
			expected: false,
		},
	}

	for i, tc := range testCases {
		result := containsCycle(tc.grid)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.expected, result, status)
	}
}
