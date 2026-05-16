package main

import "fmt"

// finalValueAfterOperations returns the final value of X (initially 0) after
// applying each operation in order.
//
// Every operation is a 3-byte string with the operator sitting at index 0 or 2
// — the other position holds 'X'. Checking either slot for '+' decides the
// sign without parsing the full token.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func finalValueAfterOperations(operations []string) int {
	ans := 0
	for _, op := range operations {
		if op[0] == '+' || op[2] == '+' {
			ans++
		} else {
			ans--
		}
	}
	return ans
}

func main() {
	testCases := []struct {
		operations []string
		expected   int
	}{
		{[]string{"--X", "X++", "X++"}, 1},
		{[]string{"++X", "++X", "X++"}, 3},
		{[]string{"X++", "++X", "--X", "X--"}, 0},
		{[]string{"++X"}, 1},
		{[]string{"--X", "--X", "--X"}, -3},
	}

	for i, tc := range testCases {
		result := finalValueAfterOperations(tc.operations)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %v | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.operations, tc.expected, result, status)
	}
}
