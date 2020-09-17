from controller import Controller
from renderer import Renderer

def main():
    snake = Controller()
    window = Renderer(snake)
    window.start_the_game()


if __name__ == '__main__':
    main()




