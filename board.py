import pygame as pg

board = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
]


class Board:
    def __init__(self, game):
        self.game = game
        self.board = board
        self.screen_width, self.screen_height = self.game.screen.get_size()
        self.square_size = min(self.screen_width, self.screen_height) // 8
        self.offset_y = (self.screen_height - 8 * self.square_size) // 2
        self.offset_x = (self.screen_width - 8 * self.square_size) // 2
        self.light_color = pg.Color("white")
        self.dark_color = pg.Color("darkgrey")
        self.piece_images = {}

    def draw(self, piece_grid):
        self._draw_squares()
        self._draw_pieces(piece_grid)

    def screen_to_board(self, mouse_x, mouse_y):
        if (
            mouse_x < self.offset_x
            or mouse_x >= self.offset_x + 8 * self.square_size
            or mouse_y < self.offset_y
            or mouse_y >= self.offset_y + 8 * self.square_size
        ):
            return None
        col = (mouse_x - self.offset_x) // self.square_size
        row = (mouse_y - self.offset_y) // self.square_size
        return row, col

    def _draw_squares(self):
        for row in range(8):
            for col in range(8):
                x = self.offset_x + col * self.square_size
                y = self.offset_y + row * self.square_size
                color = (
                    self.light_color if self.board[row][col] == 0 else self.dark_color
                )
                pg.draw.rect(
                    self.game.screen, color, (x, y, self.square_size, self.square_size)
                )
                pg.draw.rect(
                    self.game.screen,
                    pg.Color("black"),
                    (x, y, self.square_size, self.square_size),
                    1,
                )

    def _draw_pieces(self, piece_grid):
        for row in range(8):
            for col in range(8):
                piece = piece_grid[row][col]
                if piece != ".":
                    x = self.offset_x + col * self.square_size + (self.square_size // 2)
                    y = self.offset_y + row * self.square_size + (self.square_size // 2)
                    if piece in self.piece_images:
                        img = self.piece_images[piece]
                        img_rect = img.get_rect(center=(x, y))
                        self.game.screen.blit(img, img_rect)
                    else:
                        font = pg.font.SysFont(None, self.square_size // 2)
                        text_color = pg.Color("black" if piece.isupper() else "white")
                        text = font.render(piece, True, text_color)
                        text_rect = text.get_rect(center=(x, y))
                        self.game.screen.blit(text, text_rect)
