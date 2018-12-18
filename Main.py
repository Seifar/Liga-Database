from InputWindow import InputWindow
from newTournamentWindow import NewTournamentWindow
import GLOBAL

if __name__ == '__main__':
    inputWin = NewTournamentWindow()
    print(inputWin.run())

    GLOBAL.exit()