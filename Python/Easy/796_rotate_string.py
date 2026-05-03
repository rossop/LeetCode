"""
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal
after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost
position. For example, if s = "abcde", then it will be "bcdea" after one
shift.

Constraints:
- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters.

Examples:

Example 1:
    Input: s = "abcde", goal = "cdeab"
    Output: true

Example 2:
    Input: s = "abcde", goal = "abced"
    Output: false
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Returns True if goal is a rotation of s.

        Key insight: every rotation of s is a contiguous substring of s + s.
        Checking goal in s + s (with equal lengths) captures all n rotations
        in a single O(n) substring search.

        Time complexity:  O(n)
        Space complexity: O(n) for the concatenated string
        """
        return len(s) == len(goal) and goal in s + s

    def rotateStringLoop(self, s: str, goal: str) -> bool:
        """
        Returns True if goal is a rotation of s via explicit rotation.

        The set check provides a fast O(n) early exit when the character
        multisets differ (necessary condition for a rotation). The loop then
        applies each of the n shifts and compares directly.

        Note: the set check is an optimisation heuristic, not a correctness
        filter — same character sets don't guarantee a rotation.

        Time complexity:  O(n²) — n rotations each creating an O(n) string
        Space complexity: O(n) per rotation
        """
        if set(s) != set(goal):
            return False
        if len(s) != len(goal):
            return False
        for _ in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ("a", "a", True),
        ("ab", "ba", True),
        ("aa", "aa", True),
        ("abc", "acb", False),
    ]

    for label, method in [
        ("rotateString    ", solution.rotateString),
        ("rotateStringLoop", solution.rotateStringLoop),
    ]:
        for s, goal, expected in test_cases:
            result = method(s, goal)
            assert result == expected, \
                f"{label} failed: s={s!r}, goal={goal!r} → expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
