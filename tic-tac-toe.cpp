
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

char board[3][3] = {{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
char currentPlayer = 'X';

void displayBoard() {
    cout << "     |     |     " << endl;
    cout << "  " << board[0][0] << "  |  " << board[0][1] << "  |  " << board[0][2] << endl;
    cout << "_____|_____|_____" << endl;
    cout << "     |     |     " << endl;
    cout << "  " << board[1][0] << "  |  " << board[1][1] << "  |  " << board[1][2] << endl;
    cout << "_____|_____|_____" << endl;
    cout << "     |     |     " << endl;
    cout << "  " << board[2][0] << "  |  " << board[2][1] << "  |  " << board[2][2] << endl;
    cout << "     |     |     " << endl;
}

bool checkWin() {
    // Check rows
    for(int i = 0; i < 3; i++)
        if(board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ')
            return true;
    
    // Check columns
    for(int i = 0; i < 3; i++)
        if(board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ')
            return true;
    
    // Check diagonals
    if(board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ')
        return true;
    if(board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ')
        return true;
    
    return false;
}

bool checkDraw() {
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            if(board[i][j] == ' ')
                return false;
    return true;
}

void computerMove() {
    srand(time(0));
    int row, col;
    do {
        row = rand() % 3;
        col = rand() % 3;
    } while(board[row][col] != ' ');
    
    board[row][col] = 'O';
}

void playerMove() {
    int row, col;
    do {
        cout << "Player " << currentPlayer << ", enter row (1-3) and column (1-3): ";
        cin >> row >> col;
        row--; col--;
    } while(row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] != ' ');
    
    board[row][col] = currentPlayer;
}

void resetBoard() {
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            board[i][j] = ' ';
    currentPlayer = 'X';
}

int main() {
    int choice;
    
    do {
        cout << "\nTIC TAC TOE MENU" << endl;
        cout << "1. Play against computer" << endl;
        cout << "2. Two player mode" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice (1-3): ";
        cin >> choice;
        
        if(choice == 1 || choice == 2) {
            resetBoard();
            bool gameOver = false;
            
            while(!gameOver) {
                displayBoard();
                
                if(currentPlayer == 'X' || choice == 2)
                    playerMove();
                else
                    computerMove();
                
                if(checkWin()) {
                    displayBoard();
                    if(currentPlayer == 'X' || choice == 2)
                        cout << "Player " << currentPlayer << " wins!" << endl;
                    else
                        cout << "Computer wins!" << endl;
                    gameOver = true;
                }
                else if(checkDraw()) {
                    displayBoard();
                    cout << "Game is a draw!" << endl;
                    gameOver = true;
                }
                
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
            }
        }
    } while(choice != 3);
    
    cout << "Thanks for playing!" << endl;
    return 0;
}
