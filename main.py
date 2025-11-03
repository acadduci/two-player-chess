import pygame as pg
import sys
from settings import *
from board import *
from game_state import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.selected_square = None
        self.image_scale_factor = 0.6
        self.board.piece_images["P"] = self.scale_image(
            pg.image.load("piece_images/white-pawn.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["R"] = self.scale_image(
            pg.image.load("piece_images/white-rook.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["Q"] = self.scale_image(
            pg.image.load("piece_images/white-queen.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["N"] = self.scale_image(
            pg.image.load("piece_images/white-knight.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["K"] = self.scale_image(
            pg.image.load("piece_images/white-king.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["B"] = self.scale_image(
            pg.image.load("piece_images/white-bishop.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["p"] = self.scale_image(
            pg.image.load("piece_images/black-pawn.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["r"] = self.scale_image(
            pg.image.load("piece_images/black-rook.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["q"] = self.scale_image(
            pg.image.load("piece_images/black-queen.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["n"] = self.scale_image(
            pg.image.load("piece_images/black-knight.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["k"] = self.scale_image(
            pg.image.load("piece_images/black-king.png").convert_alpha(),
            self.image_scale_factor,
        )
        self.board.piece_images["b"] = self.scale_image(
            pg.image.load("piece_images/black-bishop.png").convert_alpha(),
            self.image_scale_factor,
        )

    def scale_image(self, image, scale_factor):
        original_width = image.get_width()
        original_height = image.get_height()
        new_width = original_width * scale_factor
        new_height = original_height * scale_factor
        return pg.transform.scale(image, (new_width, new_height))

    def new_game(self):
        self.board = Board(self)
        self.game_state = GameState(self)

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        pg.display.flip()
        self.game_state.update()

    def draw(self):
        self.board.draw(self.game_state.get_piece_grid())

    def handle_click(self, mouse_x, mouse_y):
        board_pos = self.board.screen_to_board(mouse_x, mouse_y)
        if board_pos is None:
            self.selected_square = None
            return
        row, col = board_pos
        piece_grid = self.game_state.get_piece_grid()
        piece = piece_grid[row][col]

        if self.selected_square is None:
            if piece != ".":
                self.selected_square = (row, col)
                print(f"Selected {piece} at {row},{col}")
            else:
                print("Empty square-no selection")
        else:
            from_row, from_col = self.selected_square
            print(f"Attempting move: ({from_row}, {from_col}) -> ({row},{col})")
            new_state = self.game_state.make_move(from_row, from_col, row, col)
            self.game_state.update(new_state)
            self.selected_square = None

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    self.handle_click(mouse_x, mouse_y)

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    # print(game.game_state.pieces)
    game.run()
