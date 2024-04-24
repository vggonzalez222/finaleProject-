from board import Board
from welcome_screen import welcome_screen
import pygame
import sys


def main():
    new_game = True
    while True:
        if new_game:
            # Initialize the game
            screen1 = pygame.display.set_mode((200, 200))
            pygame.display.set_caption("Sudoku")
            game_board = Board(600, 540, screen1, welcome_screen())
            new_game = False
        screen1.fill((164, 206, 224))
        game_board.draw()
        if game_board.action_rects():
            new_game = True
            pygame.display.flip()
        game_board.update_board()  # both update and check board need to be here
        if not game_board.check_board():
            new_game = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x2, y2 = event.pos
                loc1, loc2 = game_board.click(x2, y2)
                game_board.select(loc2, loc1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    x0, y0 = game_board.get_cell_pos()
                    game_board.select(x0 - 1, y0)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x0, y0 = game_board.get_cell_pos()
                    game_board.select(x0 + 1, y0)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x0, y0 = game_board.get_cell_pos()
                    game_board.select(x0, y0 - 1)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x0, y0 = game_board.get_cell_pos()
                    game_board.select(x0, y0 + 1)
                elif event.key == pygame.K_BACKSPACE:
                    game_board.sketch(None)
                    game_board.clear()
                elif event.key == pygame.K_DELETE:
                    game_board.sketch(None)
                elif event.key == event.key == pygame.K_RETURN:
                    game_board.place_number()
                elif event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                    game_board.sketch(1)
                elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                    game_board.sketch(2)
                elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                    game_board.sketch(3)
                elif event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                    game_board.sketch(4)
                elif event.key == pygame.K_5 or event.key == pygame.K_KP_5:
                    game_board.sketch(5)
                elif event.key == pygame.K_6 or event.key == pygame.K_KP_6:
                    game_board.sketch(6)
                elif event.key == pygame.K_7 or event.key == pygame.K_KP_7:
                    game_board.sketch(7)
                elif event.key == pygame.K_8 or event.key == pygame.K_KP_8:
                    game_board.sketch(8)
                elif event.key == pygame.K_9 or event.key == pygame.K_KP_9:
                    game_board.sketch(9)
                else:
                    continue
        pygame.display.update()


if __name__ == "__main__":
    main()
