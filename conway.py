"""
Conways Game of Life
Rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""



class Game:
    def __init__(self, board=None) -> None:
        if board is None:
            self.board = [["0" for _ in range(60)] for _ in range(60)]
            self.create_glider_gun(9,9)
            
        else:
            self.board = board



    def frames(self,number_of_frames):
        while number_of_frames > 0:
            self.next_frame()
            number_of_frames -= 1

    def get_num_neighbors(self, row, col):
        # check if board[self.cellX + 1] == 1 or - ## a better way might be to get number of filled sqaures and check if they are next to it,
        # need to implement corner cases _______ STANDARD

        num_neighbors = 0
        for row_, col_ in [
            (row, col + 1),
            (row, col - 1),
            (row - 1, col),
            (row + 1, col),
            (row + 1,col + 1),
            (row + 1,col - 1),
            (row - 1,col + 1),
            (row - 1,col - 1)

        ]:
            if (
                row_ < 0
                or row_ >= len(self.board)
                or col_ < 0
                or col_ >= len(self.board[0])
            ):
                continue

            num_neighbors += int(self.board[row_][col_])

        return num_neighbors

    def delete_cell(self, row, col):
        self.board[row][col] = "0"

    def size(self):
        return len(self.board)

    def get_board_neighbors(self):
        board_size = self.size()
        neighbor_map = []
        for row in range(board_size):
            currentRow = []
            for col in range(board_size):
                    currentRow.append(self.get_num_neighbors(row,col))
                    if len(currentRow) == 11:
                        neighbor_map.append(currentRow)
                    else:
                        continue
        return neighbor_map

    def next_frame(self):
        boardNeighbors = self.get_board_neighbors()
        for i in range(len(boardNeighbors)):
            for j in range(len(boardNeighbors)):
                number = boardNeighbors[i][j]
                if number < 2 and self.board[i][j] == '1':
                    self.delete_cell(i,j)
                elif number > 3 and self.board[i][j] == '1':
                    self.delete_cell(i,j)
                elif number == 3 and self.board[i][j] == '0':
                    self.board[i][j] = '1'
                else:
                    continue

    def create_glider(self,x,y):
        self.board[x][y] = '1'
        self.board[x][y+1] = '1'
        self.board[x][y+2] = '1'
        self.board[x-1][y+2] = '1'
        self.board[x-2][y+1] = '1'

    def create_glider_gun(self,x,y):
        self.board[x][y] = '1'
        self.board[x][y-1] = '1'
        self.board[x+1][y] = '1'
        self.board[x+1][y-1] = '1'
        self.board[x+10][y-1] ='1'
        self.board[x+10][y] ='1'
        self.board[x+10][y+1] ='1'
        self.board[x+11][y-2] = '1'
        self.board[x+11][y+2] = '1'
        self.board[x+12][y-3] = '1'
        self.board[x+13][y-3] = '1'
        self.board[x+12][y+3] = '1'
        self.board[x+13][y+3] = '1'
        self.board[x+14][y] = '1'
        self.board[x+15][y+2] ='1'
        self.board[x+16][y+1] = '1'
        self.board[x+16][y] = '1'
        self.board[x+16][y-1] ='1'
        self.board[x+15][y-2] ='1'
        self.board[x+17][y] = '1'
        self.board[x+20][y-1] = '1'
        self.board[x+20][y-2] = '1'
        self.board[x+20][y-3] = '1'
        self.board[x+21][y-1] = '1'
        self.board[x+21][y-2] = '1'
        self.board[x+21][y-3] = '1'
        self.board[x+22][y-4] = '1'
        self.board[x+22][y] = '1'
        self.board[x+24][y+1] = '1'
        self.board[x+24][y] = '1'
        self.board[x+24][y-5] = '1'
        self.board[x+24][y-4] = '1'
        self.board[x+34][y-1] = '1'
        self.board[x+35][y-1] = '1'
        self.board[x+34][y-2] = '1'
        self.board[x+35][y-2] = '1'