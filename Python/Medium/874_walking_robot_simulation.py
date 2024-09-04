"""
Solution class for LeetCode problem 874: 'Walking Robot Simulation'.

The robot is placed on an infinite XY-plane starting at the origin (0, 0), and
it follows a sequence of commands that allow it to move forward and rotate left
or right. The robot is also subject to obstacles on the grid, and it cannot
move through obstacles.

The objective is to simulate the robot's movements based on the commands and
obstacles and return the maximum Euclidean distance (squared) that the robot
reaches from the origin during its movement.

Constraints: - The commands are either turns or forward movements. - Obstacles
are located at certain grid points, and the robot cannot move
    through these points.
- The robot must calculate the furthest distance from the origin based on its
    movement path.

This file contains two solutions: one using a `set` for obstacles and another
efficient alternative.
"""
from typing import List


class Solution:
    """
    Solution class for LeetCode problem 874: 'Walking Robot Simulation'.
    """
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Simulates the robot's movement based on a list of commands and
        obstacles. The robot moves in the four cardinal directions (North,
        East, South, and West). The method returns the maximum Euclidean
        distance squared that the robot reaches from the origin.

        Time Complexity:
            O(c + o), where c is the number of commands, and o is the number of
            obstacles.
        Space Complexity:
            O(o), where o is the number of obstacles (set size).

        Args:
            commands (List[int]): A list of integers representing the movement
            commands. obstacles (List[List[int]]): A list of obstacles
            represented by their grid positions.

        Returns:
            int: The maximum squared Euclidean distance from the origin reached
            by the robot.
        """
        pos = [0, 0]
        d = 0  # Initial direction (facing North)
        direction = [
            [0, 1],   # North
            [1, 0],   # East
            [0, -1],  # South
            [-1, 0],  # West
        ]
        furthest_point = 0
        obstacles_set = set(map(tuple, obstacles))  # Convert obstacles to set of tuples

        def move(steps: int, pos: List[int]) -> List[int]:
            """Moves the robot and updates position while avoiding obstacles."""
            for _ in range(steps):
                new_pos = pos.copy()
                new_pos[0] += direction[d][0]
                new_pos[1] += direction[d][1]

                if tuple(new_pos) in obstacles_set:
                    return pos.copy()
                pos = new_pos.copy()
            return pos.copy()

        for comm in commands:
            if comm == -1:  # Turn right
                d = (d + 1) % 4
            elif comm == -2:  # Turn left
                d = (d - 1) % 4
            elif comm > 0:  # Move forward
                pos = move(comm, pos)
                furthest_point = max(furthest_point, pos[0]**2 + pos[1]**2)

        return furthest_point

    def robotSimOptimized(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Optimized version of the robot simulation using a direct approach without 
        separate function calls. It processes commands and obstacles in a single loop.

        Time Complexity:
            O(c + o), where c is the number of commands and o is the number of obstacles.
        Space Complexity:
            O(o), where o is the number of obstacles stored in a set for O(1) lookups.

        Args:
            commands (List[int]): A list of movement commands.
            obstacles (List[List[int]]): A list of obstacles on the grid.

        Returns:
            int: The maximum Euclidean distance squared from the origin reached by the robot.
        """
        x, y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # North, East, South, West
        d = 0
        res = 0
        obstacles = {tuple(o) for o in obstacles}  # Convert obstacles to set for fast lookup

        for command in commands:
            if command == -1:
                d = (d + 1) % 4  # Turn right
            elif command == -2:
                d = (d - 1) % 4  # Turn left
            else:
                dx, dy = directions[d]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles:  # If next step is an obstacle
                        break
                    x += dx
                    y += dy
                res = max(res, x**2 + y**2)  # Update the furthest distance
        return res

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([4, -1, 3], [], 25),
        ([4, -1, 4, -2, 4], [[2, 4]], 65),
        ([6, -1, -1, 6], [], 36),
        ([1, -1, 1, -1], [], 2),
        ([5, 5, 5, 5], [[0, 4], [1, 2]], 9),
    ]

    # Instantiate the solution class
    solution = Solution()

    # Run test cases for the default solution
    for i, (commands, obstacles, expected) in enumerate(test_cases):
        result = solution.robotSim(commands, obstacles)
        assert result == expected, \
            f"Test case {i+1} failed: Expected {expected}, but got {result}"

    # Run test cases for the optimized solution
    for i, (commands, obstacles, expected) in enumerate(test_cases):
        result = solution.robotSimOptimized(commands, obstacles)
        assert result == expected, (
            f"Optimized test case {i+1} failed: " +
            f"Expected {expected}, but got {result}")

    print("All test cases passed!")
