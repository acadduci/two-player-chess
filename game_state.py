import pygame as pg

class GameState:
    def __init__(self, game, board_state="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.game = game
        self.board_state = board_state
        self._parse_fen()
        self.pieces = self._fen_to_grid()

    def _parse_fen(self):
        parts = self.board_state.split(' ')
        assert len(parts) == 6, "Invalid FEN: Must have 6 fields"

        self.placement = parts[0]
        self.turn = parts[1]
        self.castling = parts[2]
        self.en_passant = parts[2]
        self.halfmove = int(parts[4])
        self.fullmove = int(parts[5])

    def _fen_to_grid(self):
        ranks = self.placement.split('/')

        grid = [['.' for _ in range(8)] for _ in range(8)]
        
        for rank_idx, rank_str in enumerate(ranks):
            row = rank_idx
            col = 0

            for char in rank_str:
                if char.isdigit():
                    col += int(char)
                else:
                    grid[row][col] = char
                    col += 1
            
            assert col == 8, f"Invalid FEN rank {rank_idx + 1}"

        return grid

    def get_turn(self):
        return "white" if self.turn == "w" else "black"

    def get_piece_grid(self):
        return self.pieces

    def update(self, new_state=None):
        if new_state:
            self.board_state = new_state
            self._parse_fen()
            self.pieces = self._fen_to_grid()

            # TODO: Increment halfmove/fullmove on moves, etc.

    def make_move(self, from_square, to_square, promotion=None):
        pass
