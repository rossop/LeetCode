package main

import "fmt"

func minLength(s string) int {
    // We use a byte slice as a stack
    stack := []byte{}

    for i := 0; i < len(s); i++ {
        char := s[i]

        // If stack is not empty, check the last added element
        if len(stack) > 0 {
            last := stack[len(stack)-1]

            // Check for "AB" or "CD" pairs
            if (last == 'A' && char == 'B') || (last == 'C' && char == 'D') {
                // "Pop" the last element and don't add the current char
                stack = stack[:len(stack)-1]
                continue
            }
        }

        // Otherwise, "Push" the current character
        stack = append(stack, char)
    }

    // The remaining elements in the stack form the final string
    return len(stack)
}


func main() {
	// Define your examples in a slice of structs
	testCases := []struct {
		input    string
		expected int
	}{
		{input: "ABFCACDB", expected: 2}, // Example 1
		{input: "ACBBD", expected: 5},    // Example 2
	}

	// Iterate through examples and print results
	for i, tc := range testCases {
		result := minLength(tc.input)
		status := "PASS"
		if result != tc.expected {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %s | Expected: %d | Result: %d | [%s]\n",
			i+1, tc.input, tc.expected, result, status)
	}
}
