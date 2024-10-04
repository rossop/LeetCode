"""
2491. Divide Players Into Teams of Equal Skill

Problem Statement: You are given a positive integer array `skill` of even
length `n`, where `skill[i]` denotes the skill of the ith player. Divide the
players into `n / 2` teams of size 2 such that the total skill of each team
is equal.

The chemistry of a team is equal to the product of the skills of the players on
that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no
way to divide the players into teams such that the total skill of each team is
equal.

Constraints:
- 2 <= skill.length <= 10^5
- skill.length is even
- 1 <= skill[i] <= 1000

Examples:

Example 1:
    Input: skill = [3,2,5,1,3,4]
    Output: 22 Explanation:
    Divide the players into the following teams: (1, 5), (2, 4), (3, 3),
    where each team has a total skill of 6.
    The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3
    * 3 = 5 + 8 + 9 = 22.

Example 2:
    Input: skill = [3,4] Output: 12 Explanation: The two players form a team
    with a total skill of 7. The chemistry of the team is 3 * 4 = 12.

Example 3:
    Input: skill = [1,1,2,3] Output: -1 Explanation: There is no way to divide
    the players into teams such that the total skill of each team is equal.
"""

from typing import List, Tuple


class Solution:
    """
    This class provides two methods to divide players into teams such that all
    teams have equal skill, and computes the sum of the chemistry of all the
    teams.

    Methods:
    1. dividePlayers: Uses frequency counting to form teams.
    2. dividePlayersSorting: Uses sorting to find pairs of players with equal
    skill sum.
    """
    def dividePlayers(self, skill: List[int]) -> int:
        """
        Uses frequency counting to determine if teams can be formed where all
        teams have equal total skill. If possible, returns the total chemistry
        of all the teams. Otherwise, returns -1.

        Time Complexity: O(n), where n is the length of the `skill` array.
        Space Complexity: O(1000), as we use a fixed-size list for skill
            frequency.

        Args:
            skill: List[int] - The array of players' skills.

        Returns:
            int - The total chemistry of all the teams, or -1 if it is not
            possible.
        """
        assert min(skill) > 0, "Input out of range"
        assert max(skill) < 1001, "Input out of range"

        n: int = len(skill)
        total_skill: int = sum(skill)
        # Skill frequency array for skills between 1 and 1000.
        skill_frequency: List[int] = [0] * 1000

        # Count the frequency of each skill
        for player_skill in skill:
            skill_frequency[player_skill - 1] += 1

        # Check if total_skill is divisible by the number of teams
        if total_skill % (n // 2) != 0:
            return -1

        target_team_skill: int = total_skill // (n // 2)
        total_chemistry: int = 0

        for player_skill in skill:
            partner_skill: int = target_team_skill - player_skill

            if skill_frequency[partner_skill - 1] == 0:
                return -1

            total_chemistry += player_skill * partner_skill
            skill_frequency[partner_skill - 1] -= 1

        return total_chemistry // 2  # Chemistry was calculated twice

    def dividePlayersSorting(self, skill: List[int]) -> int:
        """
        Sorts the skills and forms pairs by selecting the smallest and largest
        elements. Checks if all pairs have equal total skill. If possible,
        returns the total chemistry of all the teams. Otherwise, returns -1.

        Time Complexity: O(n log n), where n is the length of the `skill` array
        due to sorting. Space Complexity: O(n), due to the space needed to
        store pairs and the sorted array.

        Args:
            skill: List[int] - The array of players' skills.

        Returns:
            int - The total chemistry of all the teams, or -1 if it is not
            possible.
        """
        skill.sort()
        right: int = len(skill) - 1
        left: int = 0

        # Initialize the first pair
        pairs: List[Tuple[int, int]] = [(skill[left], skill[right])]
        summ: int = skill[left] + skill[right]
        total_chemistry: int = skill[left] * skill[right]
        right -= 1
        left += 1

        # Form teams and check if they all have the same skill sum
        while left < right:
            if summ != skill[left] + skill[right]:
                return -1

            pairs.append((skill[left], skill[right]))
            total_chemistry += skill[left] * skill[right]
            right -= 1
            left += 1

        return total_chemistry


# Test cases to validate the solution
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 5, 1, 3, 4], 22),
        ([3, 4], 12),
        ([1, 1, 2, 3], -1),
        ([10, 10, 20, 20], 400),
        ([5, 1, 1, 5], 10),
    ]

    solution = Solution()

    # Test the frequency-based method
    print("Testing dividePlayers method:")
    for i, (skill_list, expected) in enumerate(test_cases):
        result = solution.dividePlayers(skill_list)
        assert result == expected, \
            f"Test case {i+1} failed (Frequency): Expected {expected}, but got {result}"
    print("All test cases passed for dividePlayers method!")

    # Test the sorting-based method
    print("\nTesting dividePlayersSorting method:")
    for i, (skill_list, expected) in enumerate(test_cases):
        result = solution.dividePlayersSorting(skill_list)
        assert result == expected, \
            f"Test case {i+1} failed (Sorting): Expected {expected}, but got {result}"
    print("All test cases passed for dividePlayersSorting method!")
