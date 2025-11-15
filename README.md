# Obstruction
Two-player strategy game where players take turns marking cells on a grid to block their opponent. Developed using Python and the pygame library. Inspired by the classic strategy game "Obstruction".
# Obstruction

Obstruction is a two‑player strategy game where players take turns marking cells on a grid. Marking a cell blocks the surrounding cells, and the player who makes the last valid move wins.

## Rules

* Players alternate turns.
* On your turn, you mark any free cell on the board.
* When a cell is marked, that cell **and all neighboring cells** become blocked for the rest of the game.
* A player who has **no valid moves available** on their turn loses.

## Minimax Strategy (AI)

The game includes an AI opponent powered by a **Minimax search algorithm**:

* It simulates all possible future moves for both players from the current board state.
* The AI chooses the move that maximizes its chances of winning while assuming the opponent will play optimally.
* The search depth is limited to keep the computation practical, but even with limited depth the Minimax agent evaluates positions effectively and plays strategically, unlike random or heuristic opponents.
