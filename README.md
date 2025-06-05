# Snake and Ladder - Minimum Dice Throws Problem 🎲🐍🪜

This project solves the classic **Snake and Ladder problem** using **Breadth-First Search (BFS)**. The goal is to find the **minimum number of dice throws** required to reach the last cell of the board from the first cell, considering the positions of snakes and ladders.

---

## 🧠 Problem Statement

Given a board with `N` cells (numbered from `0` to `N-1`), and an array `move[]` such that:
- `move[i] = -1` indicates no snake or ladder at cell `i`.
- `move[i] = x` indicates a snake or ladder from `i` to `x`.

You can throw a dice (1 to 6), and **must climb up** if it's a ladder or **go down** if it's a snake.

### 🎯 Objective:
Find the **minimum number of dice throws** to reach cell `N-1` from cell `0`.

---

## 🚀 Approach

- Model the board as a **graph**.
- Each cell has edges to the next 6 possible positions based on dice roll.
- If a cell has a ladder/snake, move directly to its destination.
- Perform a **BFS** traversal to find the **shortest path** to the destination.

---

## 🧪 Example

With the following board setup:

```python
N = 30
moves = [-1] * N

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
```

✅ Output:

    Min Dice throws required is 3

📁 Files

    main.py – Python implementation of the algorithm.

    README.md – Project description and instructions.

🧑‍💻 How to Run

    Make sure you have Python 3 installed.

    Run the script:

python main.py

🕒 Time Complexity

    Time: O(N)

    Space: O(N)
    Each cell is visited only once, and queue operations are constant time.

📚 References

    BFS algorithm for shortest path in unweighted graphs
