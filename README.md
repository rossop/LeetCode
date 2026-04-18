# LeetCode
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Go](https://img.shields.io/badge/go-1.21-00ADD8.svg)
[![LeetCode user rossop](https://img.shields.io/badge/dynamic/json?style=flat&labelColor=black&color=%23ffa116&label=Solved&query=solved&url=https%3A%2F%2Fleetcode-badge.vercel.app%2Fapi%2Fusers%2Frossop&logo=leetcode&logoColor=yellow)](https://leetcode.com/rossop/)

This repository contains my solutions to LeetCode problems, organised by programming language and difficulty level. It also includes notes and tips on solving problems and understanding key concepts.

## Table of Contents
- [Folder Structure](#folder-structure)
- [Naming Convention](#naming-convention)
- [How to Use](#how-to-use)
- [Languages](#languages)
- [References](#references)
- [Contributing](#contributing)
- [License](#license)

## Folder Structure

```plaintext
LeetCode/
│
├── Python/
│   ├── Easy/
│   │   ├── 1_two_sum.py
│   │   └── ...
│   ├── Medium/
│   │   └── ...
│   └── Hard/
│       └── ...
│
├── Golang/
│   ├── Easy/
│   │   ├── 1_two_sum.go
│   │   └── ...
│   ├── Medium/
│   │   └── ...
│   └── Hard/
│       └── ...
│
└── README.md
```

## Naming Convention

Files are named using the pattern `{problem_number}_{snake_case_title}.{ext}`.

Within each file, solutions follow this method naming pattern:

| Method name | Description |
|---|---|
| `solve` / `methodName` | Canonical solution — optimal approach, matches LeetCode signature |
| `methodNameAlternative` | Alternative with the same complexity but a different technique |
| `methodNameBisect` | Variant using binary search |
| `methodNameNaive` | Brute-force reference implementation |

Where multiple approaches exist they are all implemented and tested in the same file.

## How to Use

**Python**
```bash
python3 Python/Easy/13_roman_to_integer.py
```

**Go**
```bash
go run Golang/Easy/13_roman_to_integer.go
```

## Languages
- **Python**: Primary language for solutions. Emphasises readability and Pythonic idioms.
- **Go**: Secondary language. Solutions explore idiomatic Go patterns including byte slices, closures, and standard library packages (`slices`, `cmp`).

## References
- Starting out: [AlgoMap.io](https://algomap.io/)
- Structured roadmap and video explanations: [NeetCode.io](https://neetcode.io/)
- Beginner-friendly video content: [Greg Hogg](https://linktr.ee/greghogg) — [YouTube](https://www.youtube.com/@GregHogg)
- LeetCode badge generator: [leetcode-badge.vercel.app](https://leetcode-badge.vercel.app/)

## Contributing
Feel free to leave comments and suggestions by submitting pull requests or opening issues.

## License
This project is licensed under the MIT License — see the [LICENSE](LICENCE) file for details.
