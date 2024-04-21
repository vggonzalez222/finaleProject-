from makeshift_board import Board
from welcome_screen import welcome_screen
import pygame
import sys


def main():
    new_game = True
    while True:
        if new_game:
            BG_COLOR = (164, 206, 224)
            screen1 = pygame.display.set_mode((200, 200))
            pygame.display.set_caption("Sudoku")
            test = Board(597, 550, screen1, welcome_screen()) # I change the width: 800 and height: 720
            new_game = False
        screen1.fill(BG_COLOR)
        test.draw()
        if test.action_rects():
            new_game = True
            pygame.display.flip()
        test.update_board()
        if type(test.check_board()) != tuple:
            print("test")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x2, y2 = event.pos
                loc1, loc2 = test.click(x2, y2)
                test.select(loc2, loc1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x0, y0 = test.get_cell_pos()
                    test.select(x0 - 1, y0)
                elif event.key == pygame.K_DOWN:
                    x0, y0 = test.get_cell_pos()
                    test.select(x0 + 1, y0)
                elif event.key == pygame.K_LEFT:
                    x0, y0 = test.get_cell_pos()
                    test.select(x0, y0 - 1)
                elif event.key == pygame.K_RIGHT:
                    x0, y0 = test.get_cell_pos()
                    test.select(x0, y0 + 1)
                elif event.key == pygame.K_BACKSPACE:
                    test.sketch(None)
                    test.clear()
                elif event.key == pygame.K_DELETE:
                    test.sketch(None)
                elif event.key == event.key == pygame.K_RETURN:
                    test.place_number()
                elif chr(event.key) in [str(i) for i in range(1, 10)]:
                    test.sketch(chr(event.key))
                else:
                    continue
        pygame.display.update()


if __name__ == "__main__":
    main()
