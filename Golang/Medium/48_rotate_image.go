package main

import "fmt"

// rotate rotates an n×n matrix 90° clockwise in-place via transpose + reflect.
//
// Step 1 — Transpose: swap matrix[i][j] with matrix[j][i] for j > i.
// Step 2 — Reflect horizontally: reverse each row by swapping j with n-1-j.
//
// Time complexity:  O(n²)
// Space complexity: O(1)
func rotate(matrix [][]int) {
	n := len(matrix)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n/2; j++ {
			matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
		}
	}
}

// rotateLayerByLayer rotates an n×n matrix 90° clockwise in-place by
// processing each concentric ring. Within each ring, four elements are
// cycled in one pass using a single saved value:
//
//	top-left ← bottom-left ← bottom-right ← top-right ← top-left
//
// Time complexity:  O(n²)
// Space complexity: O(1)
func rotateLayerByLayer(matrix [][]int) {
	l, r := 0, len(matrix)-1

	for l < r {
		for i := 0; i < r-l; i++ {
			top, bottom := l, r

			topLeft := matrix[top][l+i]

			matrix[top][l+i] = matrix[bottom-i][l]
			matrix[bottom-i][l] = matrix[bottom][r-i]
			matrix[bottom][r-i] = matrix[top+i][r]
			matrix[top+i][r] = topLeft
		}

		r--
		l++
	}
}

func deepCopy(matrix [][]int) [][]int {
	cp := make([][]int, len(matrix))
	for i, row := range matrix {
		cp[i] = make([]int, len(row))
		copy(cp[i], row)
	}
	return cp
}

func main() {
	testCases := []struct {
		matrix   [][]int
		expected [][]int
	}{
		{
			[][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
			[][]int{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}},
		},
		{
			[][]int{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}},
			[][]int{{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}},
		},
		{[][]int{{1}}, [][]int{{1}}},
	}

	funcs := []struct {
		label string
		fn    func([][]int)
	}{
		{"rotate          ", rotate},
		{"rotateLayerByLayer", rotateLayerByLayer},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			m := deepCopy(tc.matrix)
			f.fn(m)
			status := "PASS"
			if fmt.Sprintf("%v", m) != fmt.Sprintf("%v", tc.expected) {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | Expected: %v | Result: %v | [%s]\n",
				f.label, i+1, tc.expected, m, status)
		}
	}
}
