import pyfirmata as pfm
import time

board = pfm.Arduino('COM7')

while True:
    board.digital[8].write(1)
    time.sleep(3)
    board.digital[8].write(0)
    time.sleep(1.5)