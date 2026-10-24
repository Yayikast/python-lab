# Python Programming Coursework: GTS123

Python programs I wrote for GTS123 at SIIT (Year 1, Term 1). They cover the fundamentals: input validation, conditionals, loops, string processing, lists and dictionaries, functions, and numerical work with NumPy.

Each file starts with a one-line description of the problem it solves.

## Requirements

- Python 3.8+
- NumPy (only for `numpy-lab/`): `pip install -r requirements.txt`

## Running a program

Every program is a standalone script that reads from standard input:

```bash
python homework/hw3_coffee_shop_bill.py
```

## Contents

### `homework/`: graded assignments

| File | Topic |
| --- | --- |
| `hw1_capsule_volume_area.py` | Geometry formulas, formatted output |
| `hw2_primes_in_stepped_range.py` | Input validation, nested loops, primality testing |
| `hw3_coffee_shop_bill.py` | Sorting with `itemgetter`, order aggregation, formatted receipt with VAT |
| `hw4_running_sum_until_limit.py` | `while` loops, exception handling, sorting |
| `hw5_word_frequency_buckets.py` | Dictionaries, word counting, text cleanup |
| `hw6_3d_path_distance.py` | Functions, input validation, 3D Euclidean distance |

### `numpy-lab/`: NumPy and linear algebra

| File | Topic |
| --- | --- |
| `lab10_1_matrix_determinant_inverse.py` | Building matrices, `np.linalg.det` / `inv` |
| `lab10_2_linear_system_solver.py` | Solving a 3x3 linear system with a matrix inverse |
| `lab10_3_gpa_from_tsv.py` | Loading TSV data (`grades.tsv`), weighted averages |
| `lab10_4_branch_sales_ranking.py` | Loading TSV data (`sales.tsv`), row sums, `argsort` ranking |
| `lab10_5_longest_distance.py` | Vector arithmetic, distances between points |

### `midterm-practice/`: exam preparation (conditionals, loops, strings)

- `set1/`, `set2/`, `set3/`: practice sets. Time conversion, pricing rules, triangle checks, DNA strings, and several text-based pattern-drawing problems.
- `exercises/`: unit conversions, an EAN-13 barcode check digit, Scrabble word scoring, and a series sum.
- `lab-quiz/`: binary-to-decimal conversion, primes in a range, and a decision-tree quiz.

### `final-practice/`: exam preparation (dictionaries, functions, data processing)

- `lab/`: interactive programs such as a bank-transaction processor, reward-points tracker, score rankings, and medal assignment.
- `lecture/`: word-frequency analysis, a soil-moisture pump simulation, and string filtering.
- `past-exams/2021`, `past-exams/2022`: solutions to past exam questions (prime sums, grouping, compound interest, bank accounts).
