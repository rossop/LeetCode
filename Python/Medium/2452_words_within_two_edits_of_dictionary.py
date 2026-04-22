"""
2452. Words Within Two Edits of Dictionary

Problem Statement:
You are given two string arrays queries and dictionary. All words in each array
have the same length. In one edit you can change any letter in a query word to
any other letter. Find all words from queries that, after at most two edits,
equal some word from dictionary.

Return the matching words in the same order they appear in queries.

Constraints:
- 1 <= queries.length, dictionary.length <= 100
- n == queries[i].length == dictionary[j].length
- 1 <= n <= 100
- All words consist of lowercase English letters.

Examples:

Example 1:
    Input: queries = ["word","note","ants","wood"],
           dictionary = ["wood","joke","moat"]
    Output: ["word","note","wood"]

Example 2:
    Input: queries = ["yes"], dictionary = ["not"]
    Output: []
"""


class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        """
        Returns all query words that are within two edits of any dictionary word.

        For each (query, dict_word) pair, counts mismatched character positions
        using zip and a generator expression. If the difference count is <= 2,
        the query is a match — append it and move to the next query via break.

        zip naturally handles equal-length strings and the generator is concise,
        but note it does not short-circuit: all n characters are compared even
        after the difference count exceeds 2. For the given constraints
        (n <= 100) this is negligible.

        Time complexity:  O(q * d * n) where q = len(queries), d = len(dictionary),
                          n = word length.
        Space complexity: O(q) for the output list.
        """
        result: list[str] = []
        for q in queries:
            for d in dictionary:
                differences: int = sum(
                    char_q != char_d for char_q, char_d in zip(q, d)
                )
                if differences <= 2:
                    result.append(q)
                    break
        return result

    def twoEditWordsEarlyExit(self, queries: list[str], dictionary: list[str]) -> list[str]:
        """
        Returns all query words within two edits of any dictionary word,
        with early exit once the difference count exceeds 2.

        Identical logic to twoEditWords but breaks the inner character loop
        as soon as differences > 2. For large n this avoids unnecessary
        comparisons, though within the given constraints (n <= 100) the
        difference is small.

        Time complexity:  O(q * d * n) worst case; faster in practice due to
                          early exit.
        Space complexity: O(q)
        """
        result: list[str] = []
        for q in queries:
            for d in dictionary:
                differences: int = 0
                for char_q, char_d in zip(q, d):
                    if char_q != char_d:
                        differences += 1
                    if differences > 2:
                        break
                if differences <= 2:
                    result.append(q)
                    break
        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["word", "note", "ants", "wood"], ["wood", "joke", "moat"], ["word", "note", "wood"]),
        (["yes"], ["not"], []),
        (["abc"], ["abc"], ["abc"]),
        (["abc"], ["xyz"], []),
        (["ab", "cd"], ["ac", "ef"], ["ab", "cd"]),
    ]

    for label, method in [
        ("twoEditWords          ", solution.twoEditWords),
        ("twoEditWordsEarlyExit ", solution.twoEditWordsEarlyExit),
    ]:
        for queries, dictionary, expected in test_cases:
            result = method(queries, dictionary)
            assert result == expected, \
                f"{label} failed: queries={queries}, dict={dictionary} → expected {expected}, got {result}"
        print(f"  {label} passed")

    print("All test cases passed!")
