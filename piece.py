class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, game_state, from_row, from_col, to_row, to_col):
        # Override in subclasses. game_state provides grid for path checks
        raise NotImplementedError


class Pawn(Piece):
    def is_valid_move(self, game_state, fr, fc, tr, tc):
        direction = -1 if self.color == "white" else 1
        delta_row = tr - fr
        if delta_row != direction and delta_row != 2 * direction:
            return False
        if abs(tc - fc) > 0:
            return delta_row == direction and abs(tc - fc) == 1
        # TODO: Starting double-step, en passant, promotion
        return tc == fc and (
            delta_row == direction
            or (
                delta_row == 2 * direction and fr == (1 if self.color == "white" else 6)
            )
        )


class Rook(Piece):
    def is_valid_move(self, game_state, fr, fc, tr, tc):
        if not (fr == tr or fc == tc):
            return False
        # Check if the path is clear (ray tracing)
        step_row = 0 if fr == tr else (1 if tr > fr else -1)
        step_col = 0 if fc == tc else (1 if tc > fc else -1)
        r, c = fr + step_row, fc + step_col
        while r != tr or c != tc:
            if game_state.pieces[r][c] != ".":  # Blocked
                return False
            r += step_row
            c += step_col
        return True
