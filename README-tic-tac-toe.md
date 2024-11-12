# Tic Tac Toe Game

## Overview
This is a C++ implementation of the classic Tic Tac Toe game featuring both single-player (vs computer) and two-player modes.

## Global Variables
- `board[3][3]`: 2D char array representing the game board
- `currentPlayer`: Tracks current player ('X' or 'O')

## Functions Breakdown

### `void displayBoard()`
- Displays the current game board state
- Creates a visual grid using ASCII characters
- Shows current positions of 'X' and 'O' markers

### `bool checkWin()`
Checks for winning conditions:
- Horizontal rows (3 matches)
- Vertical columns (3 matches)
- Both diagonals
- Returns true if any winning condition is met

### `bool checkDraw()`
- Checks if game board is full
- Returns true if no empty spaces remain
- Used to determine stalemate condition

### `void computerMove()`
- Implements AI opponent moves
- Uses random number generation for position selection
- Ensures selected position is empty
- Places 'O' marker on valid position

### `void playerMove()`
- Handles human player moves
- Takes row and column input (1-3)
- Validates input coordinates
- Places player marker ('X' or 'O') on board

### `void resetBoard()`
- Clears the game board
- Sets all positions to empty spaces
- Resets current player to 'X'

### `int main()`
Main game controller:
1. Displays menu with options:
   - Play against computer
   - Two player mode
   - Exit game
2. Implements game loop:
   - Alternates between players
   - Checks for win/draw conditions
   - Updates board state
   - Handles game completion

## Key C++ Features Used

### Libraries
- `iostream`: Input/output operations
- `cstdlib`: Random number generation
- `ctime`: Time functions for random seed

### Control Structures
- `do-while` loops: Menu and move validation
- `for` loops: Board traversal
- Conditional statements: Game logic

### Input/Output
- `cout`: Display text and board
- `cin`: Player input handling

### Data Types
- 2D arrays: Game board representation
- Characters: Player markers
- Integers: Menu choices and coordinates

## Game Features
1. Two Game Modes:
   - Single player vs computer
   - Two player mode
2. Input Validation
3. Win Detection
4. Draw Detection
5. Replayability
6. Clear Visual Interface


