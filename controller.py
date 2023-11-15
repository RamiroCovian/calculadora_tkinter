import view
from tkinter import Tk


class Controller:
    def __init__(self, main):
        self.main_controller = main
        self.view = view.Calculator(self.main_controller)


if __name__ == "__main__":
    main = Tk()
    application = Controller(main)
    main.mainloop()
