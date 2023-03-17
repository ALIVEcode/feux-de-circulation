from alimata.core.board import Board
from alimata.actuators.led import Led
from aliot.aliot_obj import AliotObj
import time
class FeuxCirculation:
    def __init__(self, feux_de_circulation : AliotObj, board: Board, position: str, red_pin: int, orange_pin: int, green_pin: int):
        self.feux_de_circulation = feux_de_circulation
        self.board = board
        self.position = position
        self.red_light = Led(board, red_pin)
        self.orange_light = Led(board, orange_pin)
        self.green_light = Led(board, green_pin)

    def green(self):
        self.red_light.off()
        self.orange_light.off()
        self.green_light.on()

        self.feux_de_circulation.update_doc({f"/document/lights/{self.position}/state":"Green"})
        time.sleep(0.1)

    def orange(self):
        self.red_light.off()
        self.orange_light.on()
        self.green_light.off()
        self.feux_de_circulation.update_doc({f"/document/lights/{self.position}/state":"Yellow"})
        time.sleep(0.1)


    def red(self):
        self.red_light.on()
        self.orange_light.off()
        self.green_light.off()
        self.feux_de_circulation.update_doc({f"/document/lights/{self.position}/state":"Red"})
        time.sleep(0.1)
