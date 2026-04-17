package main

import "fmt"

// findFinalValue returns the final value of original after repeatedly doubling
// it while it exists in nums.
//
// Searches nums for the current value on each iteration. When the value is no
// longer present, returns it immediately. The bounded constraint
// (nums[i], original <= 1000) limits doublings to at most log2(1000) ≈ 10
// iterations, so the loop runs a constant number of times.
//
// Parameters:
//   - nums:     the array of integers to search
//   - original: the starting value to search for and double
//
// Returns the first value in the doubling sequence not found in nums.
//
// Time complexity:  O(n) — each membership check is O(n), at most O(log max_val) iterations.
// Space complexity: O(1)
func findFinalValue(nums []int, original int) int {
	// 1. Build the lookup map ONCE (O(N) time, O(N) space)
    lookup := make(map[int]struct{}, len(nums))
    for _, val := range nums {
        lookup[val] = struct{}{}
    }

    num := original

    for {
        // O(1) instant lookup
        if _, exists := lookup[num]; exists {
            num *= 2
        } else {
            return num
        }
    }
}

func main() {
	testCases := []struct {
		nums     []int
		original int
		expected int
	}{
		{nums: []int{5, 3, 6, 1, 12}, original: 3, expected: 24},
		{nums: []int{2, 7, 9}, original: 4, expected: 4},
	}

	for i, tc := range testCases {
		result := findFinalValue(tc.nums, tc.original)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: nums=%v original=%d | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.nums, tc.original, tc.expected, result, status)
	}
}
