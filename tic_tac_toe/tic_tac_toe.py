
EMPTY_BOARD = [" " for i in range(9)]
CPU_PLAYER = 2

WINNING_STATES = [ (0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6) ] 

class Tic_tac_toe:
    def __init__(self):
        self.current_player = 0
        self.game_state = EMPTY_BOARD.copy()
        self._total_moves = 0
    # ToDo, add CPU logic. 
    # 1. add constructor for deciding if cpu is playing
    # 2. add function for CPU taking a turn
    # 3. update make_move to account for CPU's turn before prompting players
    
    def _reset_board(self):
        self.__init__(self)
    
    def __repr__(self):
        return "{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}".format(*self.game_state)
        
        
    def __place(self, position, player):
        self.game_state[position] = player
    
    def _is_valid_move(self, position):
        if self.game_state[position] == " ":
            return True
        return False
                    
    def _is_game_over(self):
        if self._total_moves == len(self.game_state):
            print(repr(self))
            print("It's a tie")
            return True
        for x1, x2, x3 in WINNING_STATES:
            if self.game_state[x1] != " " and self.game_state[x1] == self.game_state[x2] and self.game_state[x1] == self.game_state[x3]:
                print(repr(self))
                print("player {} has won the game".format(self.game_state[x1]))
                return True
        return False

        
    def make_move(self, position):
        if not self._is_valid_move(position):
            print(repr(self))
            print("Not a valid move")
            print("Still Player {}'s turn".format(self.current_player + 1))
            return
        self.__place(position, self.current_player + 1)
        self.current_player = (self.current_player + 1) % 2
        if self._is_game_over():
            print("board reset")
            self._reset_board()
        else:
            print(repr(self))
            print("Player {}'s turn".format(self.current_player + 1))
            
            
            
        