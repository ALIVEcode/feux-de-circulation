from alimata.core.board import Board
from alimata.actuators.led import Led

class FeuxCirculation:
    def __init__(self, board: Board, red_pin: int, orange_pin: int, green_pin: int):
        self.board = board
        self.red_light = Led(board, red_pin)
        self.orange_light = Led(board, orange_pin)
        self.green_light = Led(board, green_pin)

    def green(self):
        self.red_light.off()
        self.orange_light.off()
        self.green_light.on()

    def orange(self):
        self.red_light.off()
        self.orange_light.on()
        self.green_light.off()

    def red(self):
        self.red_light.on()
        self.orange_light.off()
        self.green_light.off()