import pygame

# constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
ORIGINAL_X = 150
ORIGINAL_Y = 500
SQUARE_SIZE = 100

square_1 = pygame.rect.Rect(ORIGINAL_X, ORIGINAL_Y, SQUARE_SIZE, SQUARE_SIZE)
square_2 = pygame.rect.Rect(ORIGINAL_X, SCREEN_HEIGHT-ORIGINAL_Y-SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
square_3 = pygame.rect.Rect(SCREEN_WIDTH-ORIGINAL_X-SQUARE_SIZE, ORIGINAL_Y, SQUARE_SIZE, SQUARE_SIZE)
square_4 = pygame.rect.Rect(SCREEN_WIDTH-ORIGINAL_X-SQUARE_SIZE, SCREEN_HEIGHT-ORIGINAL_Y-SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

KEY_REPEAT_SETTING = (200,70)