import pygame
import sys
from makeshift_cell import Cell
from makeshift_sudoku_project import generate_sudoku


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        removal = {"easy": 30, "medium": 40, "hard": 50}
        self.original_board, self.solution_board = generate_sudoku(9, removal[difficulty])
        self.player_board = [row[:] for row in self.original_board]
        self.cells = [[Cell(self.original_board[i][j], i, j, screen) for j in range(9)] for i in range(9)]

    def draw(self):
        for i in range(10):
            if i % 3 == 0:
                line_thickness = 5
            else:
                line_thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * (self.height / 9)),
                             (self.width, i * (self.height / 9)), line_thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * (self.width / 9), 0),
                             (i * (self.width / 9), self.height), line_thickness)
        for row in self.cells:
            for cell in row:
                cell_width = self.width / 9
                cell_height = self.height / 9
                cell.draw(cell_width, cell_height)

    def action_rects(self):  # ngl I was too tired to properly format those boxes, they're functional tho
        pygame.font.init()
        font = pygame.font.SysFont("roboto", 35)
        reset_font = font.render("RESET", True, (255, 255, 255))
        reset_rect = pygame.Rect(self.width / 8, self.height + self.height / 100, self.width / 6, self.height / 11)
        coords0 = reset_font.get_rect()
        coords0.center = reset_rect.center
        pygame.draw.rect(self.screen, (194, 131, 21), reset_rect)
        self.screen.blit(reset_font, coords0)
        restart_font = font.render("RESTART", True, (255, 255, 255))
        restart_rect = pygame.Rect(self.width / 2.5, self.height + self.height / 100, self.width / 6, self.height / 11)
        coords1 = restart_font.get_rect()
        coords1.center = restart_rect.center
        pygame.draw.rect(self.screen, (194, 131, 21), restart_rect)
        self.screen.blit(restart_font, coords1)
        exit_font = font.render("EXIT", True, (255, 255, 255))
        exit_rect = pygame.Rect(self.width / 1.5, self.height + self.height / 100, self.width / 6, self.height / 11)
        coords2 = exit_font.get_rect()
        coords2.center = exit_rect.center
        pygame.draw.rect(self.screen, (194, 131, 21), exit_rect)
        self.screen.blit(exit_font, coords2)
        if reset_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 196, 84), reset_rect)
            self.screen.blit(reset_font, coords0)
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.reset_to_original()
                    break
        elif restart_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 196, 84), restart_rect)
            self.screen.blit(restart_font, coords1)
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    print("new screen")
                    break
        elif exit_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 196, 84), exit_rect)
            self.screen.blit(exit_font, coords2)
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()










    def select(self, row, col):
        if None is row or None is col:
            return None
        if row < 0:
            row = 8
        elif row > 8:
            row = 0
        elif col < 0:
            col = 8
        elif col > 8:
            col = 0
        for cells in self.cells:
            for cell in cells:
                cell.selected = False
        self.cells[row][col].selected = True

    def click(self, x, y):
        cell_width = self.width / 9
        cell_height = self.height / 9
        location = [int(x // cell_width), int(y // cell_height)]
        for i in location:
            if i > 8:
                return [None, None]
        return tuple(location)

    def clear(self):
        for row in self.cells:
            i = self.cells.index(row)
            for cell in row:
                j = row.index(cell)
                if cell.selected:
                    cell.set_sketched_value(None)
                    if self.original_board[i][j] == 0:
                        cell.set_cell_value(0)
        pass

    def sketch(self, value):
        for row in self.cells:
            i = self.cells.index(row)
            for cell in row:
                j = row.index(cell)
                if cell.selected:
                    if self.player_board[i][j] == 0:
                        cell.set_sketched_value(value)
        pass

    def place_number(self):
        for row in self.cells:
            i = self.cells.index(row)
            for cell in row:
                j = row.index(cell)
                if cell.selected:
                    if self.original_board[i][j] == 0:
                        cell.set_cell_value(cell.sketched_value)
                        cell.sketched_value = None
                else:
                    pass

    def get_cell_pos(self):
        for row in self.cells:
            for cell in row:
                if cell.selected:
                    position = [cell.row, cell.column]
                    return tuple(position)

    def reset_to_original(self):
        self.cells = [[Cell(self.original_board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]
        pass

    def is_full(self):
        for row in self.player_board:
            for value in row:
                if value == 0:
                    return False
        return True

    def update_board(self):
        objects = self.cells[:]
        self.player_board = [[cell.value for cell in row] for row in objects]
        return self.player_board

    def find_empty(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    coord = [cell.row, cell.column]
                    return tuple(coord)

    def check_board(self):
        if not self.is_full():
            return self.find_empty()
        elif self.is_full():
            if self.player_board == self.solution_board:
                return True
            else:
                return False


BG_COLOR = (164, 206, 224)
welcome_screen = pygame.display.set_mode((800, 800))
welcome_screen.fill(BG_COLOR)
screen1 = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sudoku")
test = Board(800, 720, screen1, "easy")


while True:
    screen1.fill(BG_COLOR)
    test.draw()
    test.action_rects()
    test.update_board()
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
