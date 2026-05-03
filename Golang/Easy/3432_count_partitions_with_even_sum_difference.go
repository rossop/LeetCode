package main

import "fmt"

// countPartitions returns the number of partitions with an even sum difference.
//
// For any partition, diff = 2L - S where L is the left sum and S the total.
// Since 2L is always even, the parity of diff depends only on S:
//   - S even → all n-1 partitions are valid
//   - S odd  → no partition is valid
//
// Time complexity:  O(n)
// Space complexity: O(1)
func countPartitions(nums []int) int {
	sum := 0
	for _, val := range nums {
		sum += val
	}
	if sum%2 == 0 {
		return len(nums) - 1
	}
	return 0
}

// countPartitionsLoop returns the count by maintaining a running left sum,
// computing the difference at each partition index without re-summing.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func countPartitionsLoop(nums []int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	counter := 0
	sumLeft := 0
	for i, x := range nums {
		if i == len(nums)-1 {
			continue
		}
		sumLeft += x
		diff := (total - sumLeft) - sumLeft
		if diff%2 == 0 {
			counter++
		}
	}
	return counter
}

func main() {
	testCases := []struct {
		nums     []int
		expected int
	}{
		{[]int{10, 10, 3, 7, 6}, 4},
		{[]int{1, 2, 2}, 0},
		{[]int{2, 4, 6, 8}, 3},
		{[]int{1, 1}, 1},
		{[]int{1, 2}, 0},
	}

	for i, tc := range testCases {
		r1, r2 := countPartitions(tc.nums), countPartitionsLoop(tc.nums)
		s1, s2 := "PASS", "PASS"
		if r1 != tc.expected {
			s1 = "FAIL"
		}
		if r2 != tc.expected {
			s2 = "FAIL"
		}
		fmt.Printf("Example %d | Expected: %d | parity: %d [%s] | loop: %d [%s]\n",
			i+1, tc.expected, r1, s1, r2, s2)
	}
}
