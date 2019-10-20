from PyQt5 import QtWidgets
from calculator import Ui_MainWindow

class CalcMainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    self.calc_window = Ui_MainWindow()
    self.calc_window.setupUi(self)

    self.calc_window.operations.addItems(['+','-','*'])

    self.show()

  # slots
  def oncalculate(self):
    n1 = float(self.calc_window.first.text())
    n2 = float(self.calc_window.second.text())

    op = self.calc_window.operations.currentText()

    if op == '+':
      ans = n1 + n2
    elif op == '-':
      ans = n1 - n2
    else:
      ans = n1 * n2

    self.calc_window.answer.setText(str(ans))


app = QtWidgets.QApplication([])
calc_main_window = CalcMainWindow()
app.exec_()

