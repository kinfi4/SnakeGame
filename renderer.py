import pygame
from constants import SIZE_OF_WINDOW, SIZE_OF_BLOCK, DIRECTIONS, FPS
from controller import Controller


def create_the_window():
    pygame.init()


class Renderer:
    def __init__(self, snake: Controller):
        self.snake = snake
        self.clock = pygame.time.Clock()
        self.sc = pygame.display.set_mode([SIZE_OF_WINDOW, SIZE_OF_WINDOW])

        create_the_window()

    def start_the_game(self):
        self.sc.fill(pygame.Color('black'))
        reward = 0

        while self.snake.alive:
            print('iteration')

            self.check_the_player()
            reward = self.snake.step()

            # drawing the head of the snake
            pygame.draw.rect(self.sc, pygame.Color('green'), (*self.snake.head_position, SIZE_OF_BLOCK, SIZE_OF_BLOCK))

            # drawing the apple
            pygame.draw.rect(self.sc, pygame.Color('red'), (*self.snake.apple_position, SIZE_OF_BLOCK, SIZE_OF_BLOCK))

            # deleting the tail
            pygame.draw.rect(self.sc, pygame.Color('black'), (*self.snake.last_tail_position, SIZE_OF_BLOCK, SIZE_OF_BLOCK))

            pygame.display.flip()
            self.clock.tick(20)

            self.check_the_player()

        print('The end', reward)

    def check_the_player(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.snake.current_direction = 4
                if event.key == pygame.K_a:
                    self.snake.current_direction = 1
                if event.key == pygame.K_s:
                    self.snake.current_direction = 2
                if event.key == pygame.K_d:
                    self.snake.current_direction = 3






