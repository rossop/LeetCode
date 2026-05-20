package main

import "fmt"

// replaceElements replaces every arr[i] with the max of arr[i+1..n-1]; the
// last element becomes -1.
//
// Walk right-to-left holding maxSoFar — the max of everything strictly to
// the right of i. Swap arr[i] with maxSoFar in one move, then fold the
// original value into maxSoFar for the next step. Initial -1 satisfies the
// "last element becomes -1" rule for free.
//
// Time complexity:  O(n)
// Space complexity: O(1) — in place.
func replaceElements(arr []int) []int {
	n := len(arr)
	if n == 0 {
		return arr
	}

	maxSoFar := -1
	for i := n - 1; i >= 0; i-- {
		currentVal := arr[i]
		arr[i] = maxSoFar

		if currentVal > maxSoFar {
			maxSoFar = currentVal
		}
	}
	return arr
}

// replaceElementsLeftToRight is the brute-force variant: for each i, scan
// the suffix arr[i+1..] for its max via an inner loop.
//
// Time complexity:  O(n^2)
// Space complexity: O(1) — in place.
func replaceElementsLeftToRight(arr []int) []int {
	n := len(arr)
	if n == 0 {
		return arr
	}

	for i := 0; i < n-1; i++ {
		maxIdx := i + 1
		for j := i + 1; j < n; j++ {
			if arr[j] > arr[maxIdx] {
				maxIdx = j
			}
		}

		arr[i] = arr[maxIdx]
	}

	if n > 0 {
		arr[n-1] = -1
	}
	return arr
}

func main() {
	testCases := []struct {
		arr      []int
		expected []int
	}{
		{[]int{2, 4, 5, 3, 1, 2}, []int{5, 5, 3, 2, 2, -1}},
		{[]int{3, 3}, []int{3, -1}},
		{[]int{400}, []int{-1}},
		{[]int{1, 2, 3, 4, 5}, []int{5, 5, 5, 5, -1}},
		{[]int{5, 4, 3, 2, 1}, []int{4, 3, 2, 1, -1}},
	}

	funcs := []struct {
		label string
		fn    func([]int) []int
	}{
		{"replaceElements           ", replaceElements},
		{"replaceElementsLeftToRight", replaceElementsLeftToRight},
	}

	for _, f := range funcs {
		for i, tc := range testCases {
			input := append([]int(nil), tc.arr...)
			result := f.fn(input)
			status := "PASS"
			if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
				status = "FAIL"
			}
			fmt.Printf("%s | Example %d | Input: %v | Expected: %v | Result: %v | [%s]\n",
				f.label, i+1, tc.arr, tc.expected, result, status)
		}
	}
}
