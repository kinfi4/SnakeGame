from random import randrange
from constants import SIZE_OF_WINDOW, SIZE_OF_BLOCK, REWARD, DIRECTIONS

from time import sleep


class Controller:
    def __init__(self):
        self.start_position = (randrange(0, SIZE_OF_WINDOW, SIZE_OF_BLOCK),
                               randrange(0, SIZE_OF_WINDOW, SIZE_OF_BLOCK))

        self.snake_blocks = [self.start_position]
        self.apple_position = self.init_food()
        self.alive = True
        self.current_direction = randrange(1, 5, 1)
        self.last_tail_position = None
        self.head_position = self.snake_blocks[0]

        print(self.current_direction)

    def init_food(self):
        food_position = (randrange(0, SIZE_OF_WINDOW, SIZE_OF_BLOCK),
                         randrange(0, SIZE_OF_WINDOW, SIZE_OF_BLOCK))

        while food_position in self.snake_blocks:
            food_position = (randrange(0, SIZE_OF_WINDOW, SIZE_OF_BLOCK),
                             randrange(0, SIZE_OF_WINDOW, SIZE_OF_BLOCK))

        self.apple_position = food_position
        return food_position

    def step(self):
        print(self.snake_blocks[0])

        self.snake_blocks = [((self.snake_blocks[0][0] + (DIRECTIONS[self.current_direction][0] * SIZE_OF_BLOCK),
                               self.snake_blocks[0][1] + (DIRECTIONS[self.current_direction][1] * SIZE_OF_BLOCK)))] \
                            + self.snake_blocks

        self.last_tail_position = self.snake_blocks.pop()
        self.head_position = self.snake_blocks[0]

        # Write the end game checking
        if self.snake_blocks[0][0] < 0 or self.snake_blocks[0][0] > SIZE_OF_WINDOW - SIZE_OF_BLOCK or \
                self.snake_blocks[0][1] < 0 or self.snake_blocks[0][1] > SIZE_OF_WINDOW - SIZE_OF_BLOCK:
            self.alive = False

        if self.snake_blocks[0] in self.snake_blocks[1:]:
            self.alive = False

        reward = self.check_if_got_an_apple()
        return reward

    def check_if_got_an_apple(self):
        reward = 0
        if self.snake_blocks[0] == self.apple_position:
            reward = REWARD
            self.init_food()
            self.add_tail()

        return reward

    def add_tail(self):
        self.snake_blocks.append((self.snake_blocks[len(self.snake_blocks) - 1][0]
                                  - DIRECTIONS[self.current_direction][0],
                                  self.snake_blocks[len(self.snake_blocks) - 1][1]
                                  - DIRECTIONS[self.current_direction][1]))
