package main

import "fmt"

// maxDistance returns the maximum possible minimum Manhattan distance between
// k selected points on the boundary of a square with the given side length.
//
// TODO: implement
func maxDistance(side int, points [][]int, k int) int {
	return 0
}

func main() {
	testCases := []struct {
		side     int
		points   [][]int
		k        int
		expected int
	}{
		{2, [][]int{{0, 2}, {2, 0}, {2, 2}, {0, 0}}, 4, 2},
		{2, [][]int{{0, 0}, {1, 2}, {2, 0}, {2, 2}, {2, 1}}, 4, 1},
		{2, [][]int{{0, 0}, {0, 1}, {0, 2}, {1, 2}, {2, 0}, {2, 2}, {2, 1}}, 5, 1},
	}

	for i, tc := range testCases {
		result := maxDistance(tc.side, tc.points, tc.k)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | side=%d, k=%d | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.side, tc.k, tc.expected, result, status)
	}
}
