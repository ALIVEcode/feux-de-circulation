from alimata.actuators.led import Led
from alimata.sensors.sonar import Sonar
from alimata.core.board import Board
from time import sleep

from feuxCirculation import FeuxCirculation
# Creating a new board
board = Board()


feux_west = FeuxCirculation(board, 2, 3, 4)
feux_south = FeuxCirculation(board, 5, 6, 7)




# Main function
def setup():
  pass


def loop():
  feux_west.green()
  feux_south.red()
  sleep(8)
  feux_west.orange()
  sleep(2)
  feux_west.red()
  feux_south.green()
  sleep(8)
  feux_south.orange()
  sleep(2)


board.start(setup, loop)