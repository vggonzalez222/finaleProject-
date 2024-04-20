<<<<<<< HEAD
import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.column = col
        self.screen = screen
        self.sketched_value = None
        self.selected = False

    def set_cell_value(self, value):
        if value is None:
            value = 0
        self.value = value
        self.value = int(self.value)
        return self.value

    def set_sketched_value(self, value):
        self.sketched_value = value
        return self.sketched_value

    def draw(self, width, height):
        pygame.font.init()
        font = pygame.font.Font(None, 40)
        if self.sketched_value is not None:
            sketch = font.render(str(self.sketched_value), True, (128, 128, 128))
            rect0 = sketch.get_rect(center=(self.column * width + width / 4, self.row * height + height / 4))
            self.screen.blit(sketch, rect0)
        if self.selected:
            outline = (255, 0, 0)
            rect1 = pygame.Rect(self.column * width, self.row * height, width, height)
            pygame.draw.rect(self.screen, outline, rect1, 3)
        if self.value != 0:
            put = font.render(str(self.value), True, (0, 0, 0))
            rect2 = put.get_rect(center=(self.column * width + width / 2, self.row * height + height / 2))
            self.screen.blit(put, rect2)
=======
import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.column = col
        self.screen = screen
        self.sketched_value = None
        self.selected = False

    def set_cell_value(self, value):
        if value is None:
            value = 0
        self.value = value
        self.value = int(self.value)
        return self.value

    def set_sketched_value(self, value):
        self.sketched_value = value
        return self.sketched_value

    def draw(self, width, height):
        pygame.font.init()
        font = pygame.font.Font(None, 40)
        if self.sketched_value is not None:
            sketch = font.render(str(self.sketched_value), True, (128, 128, 128))
            rect0 = sketch.get_rect(center=(self.column * width + width / 4, self.row * height + height / 4))
            self.screen.blit(sketch, rect0)
        if self.selected:
            outline = (255, 0, 0)
            rect1 = pygame.Rect(self.column * width, self.row * height, width, height)
            pygame.draw.rect(self.screen, outline, rect1, 3)
        if self.value != 0:
            put = font.render(str(self.value), True, (0, 0, 0))
            rect2 = put.get_rect(center=(self.column * width + width / 2, self.row * height + height / 2))
            self.screen.blit(put, rect2)
>>>>>>> origin/main
