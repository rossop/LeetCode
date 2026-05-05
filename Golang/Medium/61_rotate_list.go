package main

import "fmt"

// ListNode is the singly-linked list node used by LeetCode.
type ListNode struct {
	Val  int
	Next *ListNode
}

// rotateRight rotates the list to the right by k places.
//
// One pass measures the length and captures the tail. After reducing k
// modulo the length, a second pass walks to the node just before the new
// head; splitting there and joining the original tail to the original
// head completes the rotation.
//
// Time complexity:  O(n)
// Space complexity: O(1)
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}

	length, tail := 1, head
	for tail.Next != nil {
		tail = tail.Next
		length++
	}

	k = k % length
	if k == 0 {
		return head
	}

	cur := head
	for i := 0; i < length-1-k; i++ {
		cur = cur.Next
	}

	newHead := cur.Next
	cur.Next = nil
	tail.Next = head

	return newHead
}

func createLinkedList(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := &ListNode{Val: vals[0]}
	current := head
	for _, v := range vals[1:] {
		current.Next = &ListNode{Val: v}
		current = current.Next
	}
	return head
}

func linkedListToSlice(head *ListNode) []int {
	res := []int{}
	for n := head; n != nil; n = n.Next {
		res = append(res, n.Val)
	}
	return res
}

func main() {
	testCases := []struct {
		vals     []int
		k        int
		expected []int
	}{
		{[]int{1, 2, 3, 4, 5}, 2, []int{4, 5, 1, 2, 3}},
		{[]int{0, 1, 2}, 4, []int{2, 0, 1}},
		{[]int{}, 0, []int{}},
		{[]int{1}, 99, []int{1}},
		{[]int{1, 2}, 3, []int{2, 1}},
	}

	for i, tc := range testCases {
		head := createLinkedList(tc.vals)
		rotated := rotateRight(head, tc.k)
		result := linkedListToSlice(rotated)

		status := "PASS"
		if fmt.Sprintf("%v", result) != fmt.Sprintf("%v", tc.expected) {
			status = "FAIL"
		}
		fmt.Printf("Example %d | Input: %v k=%d | Expected: %v | Result: %v | [%s]\n",
			i+1, tc.vals, tc.k, tc.expected, result, status)
	}
}
