"""This is the file that executes the actual game loop."""
from control import *
from model import *
from view import *


new_game = Game()
app = QApplication(sys.argv)
new_game.set_up_start_screen()
app.exec_()
