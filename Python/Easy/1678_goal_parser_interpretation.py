"""
1678. Goal Parser Interpretation

Problem Statement: You own a Goal Parser that can interpret a string `command`.
The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
The Goal Parser will interpret "G" as the string "G", "()" as the string "o",
and "(al)" as the string "al". The interpreted strings are then concatenated in
the original order.

Given the string `command`, return the Goal Parser's interpretation of the
command.

Constraints: - 1 <= command.length <= 100 - `command` consists of "G", "()",
and/or "(al)" in some order.

Example 1:
    Input: command = "G()(al)" Output: "Goal" Explanation:
        G -> G () -> o (al) -> al The final concatenated result is "Goal".

Example 2:
    Input: command = "G()()()()(al)" Output: "Gooooal"

Example 3:
    Input: command = "(al)G(al)()()G" Output: "alGalooG"

"""

from typing import List


class Solution:
    """
    A class that provides solutions for interpreting Goal Parser commands.

    The class contains two methods: 1. `interpret`: A method that processes the
    input command in a step-by-step manner. 2. `interpretOptimized`: An
    optimized version that uses in-built string replacement for better
    efficiency.
    """

    def interpret(self, command: str) -> str:
        """
        Interprets the command string by parsing it character by character and
        identifying sequences of 'G', '()', and '(al)'.

        Time Complexity: O(n), where n is the length of the command string.
        Space Complexity: O(n), for storing the output list and intermediate
        strings.

        Args:
            command: A string containing the Goal Parser commands.

        Returns:
            str: The interpreted string based on the command.
        """
        p1: int = 0
        p2: int = 0
        n: int = len(command)

        ans: List[str] = []

        while p1 < n:
            if command[p1] == 'G':
                ans.append('G')
            elif command[p1] == '(':
                p2 = p1 + 1
                subAns: List[str] = []
                while command[p2] != ')':
                    subAns.append(command[p2])
                    p2 += 1
                p1 = p2
                if len(subAns) == 0:
                    ans.append('o')
                else:
                    ans.append(''.join(subAns))
            p1 += 1
        return "".join(ans)

    def interpretOptimized(self, command: str) -> str:
        """
        Optimized approach to interpret the command using string replacements.
        We directly replace '()' with 'o' and '(al)' with 'al' using Python's
        built-in string replacement method.

        Time Complexity: O(n), where n is the length of the command string.
        Space Complexity: O(n), since string replacement creates new strings.

        Args:
            command: A string containing the Goal Parser commands.

        Returns:
            str: The interpreted string based on the command.
        """
        # Replacing "()" with "o" and "(al)" with "al"
        return command.replace("()", "o").replace("(al)", "al")


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("G()(al)", "Goal"),             # Example 1
        ("G()()()()(al)", "Gooooal"),    # Example 2
        ("(al)G(al)()()G", "alGalooG"),  # Example 3
        ("G", "G"),                      # Custom Test Case 1 (only 'G')
        ("()()", "oo"),                 # Custom Test Case 2 (only '()')
    ]

    # Instantiate the solution class
    solution = Solution()

    # Loop through each test case
    for i, (comm, expected) in enumerate(test_cases):
        result = solution.interpret(comm)
        assert result == expected, \
            f"Test case {i+1} failed: Expected {expected}, got {result}"

        result_optimized = solution.interpretOptimized(comm)
        assert result_optimized == expected, \
            (f"Optimized Test case {i+1} failed:"
             f"Expected {expected}, got {result_optimized}")

    print("All test cases passed!")
