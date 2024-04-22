from makeshift_board import Board
from welcome_screen import welcome_screen
import pygame
import sys
from screens import game_win_screen, game_over_screen

def main():
    new_game = True
    game_over = False
    while True:
        if new_game:
            # Initialize the game
            BG_COLOR = (164, 206, 224)
            screen1 = pygame.display.set_mode((200, 200))
            pygame.display.set_caption("Sudoku")
            test = Board(597, 550, screen1, welcome_screen())
            new_game = False
            game_over = False  # Reset game over flag

        screen1.fill(BG_COLOR)
        test.draw()
        if test.action_rects():
            new_game = True
            pygame.display.flip()
        test.update_board()

        if game_over:
            game_over_screen()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 270 <= x <= 330 and 250 <= y <= 300:  # Restart button coordinates
                        test = Board(597, 550, screen1, welcome_screen())  # Restart the game
                        new_game = True
                        game_over = False
                        break  # Exit the event loop
        else:
            # Check if the board is successfully completed
            completion_status = test.check_board()
            if completion_status == True:
                game_win_screen()
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if 270 <= x <= 330 and 350 <= y <= 400:  # Exit button coordinates
                            pygame.quit()
                            sys.exit()
                        elif 270 <= x <= 330 and 250 <= y <= 300:  # Restart button coordinates
                            test = Board(597, 550, screen1, welcome_screen())  # Restart the game
                            new_game = True
                            game_over = False
                            break  # Exit the event loop
            elif completion_status == False:  # Unsuccesful completion
                game_over = True

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

