# Sudoku Solver
This project implements various search algorithms to solve Sudoku puzzles. It was developed as part of an Artificial Intelligence class to explore different techniques for solving complex problems.

This is a Python-based project that leverages different search algorithms to find solutions for 
Sudoku puzzles. The implementation includes heuristic algorithms, depth-first search, A*, and more, providing a comprehensive exploration of problem-solving strategies in the context of Sudoku.

## Sudoku format
The Sudoku puzzles are represented in text files using the following format:
301086504046521070500000001400800002080347900009050038004090200008734090007208103

In this format, each '0' denotes an empty square, and each number represents a filled square, organized in rows.

When visualized as a grid, the above file translates to:

    -------------------------
    | 3 0 1 | 0 8 6 | 5 0 4 |
    | 0 4 6 | 5 2 1 | 0 7 0 |
    | 5 0 0 | 0 0 0 | 0 0 1 |
    |-------+-------+-------|
    | 4 0 0 | 8 0 0 | 0 0 2 |
    | 0 8 0 | 3 4 7 | 9 0 0 |
    | 0 0 9 | 0 5 0 | 0 3 8 |
    |-------+-------+-------|
    | 0 0 4 | 0 9 0 | 2 0 0 |
    | 0 0 8 | 7 3 4 | 0 9 0 |
    | 0 0 7 | 2 0 8 | 1 0 3 |
    -------------------------


## Algorithms used

-Breadth First Search (BFS)
-Depth First Search (DFS)
-A*
-Greedy Search, with 3 variations (row/column completion, cell completion)

## Getting started 
1. Clone the repository: ```git clone ```
2. Download the dataset from [this link](https://www.kaggle.com/rohanrao/sudoku), then place it in the /data folder.
3. Install numpy using ```pip install numpy```
4. Run main passing as argument the path to the dataset ```python main.py path\sudoku_solver\data\sudoku.csv```
