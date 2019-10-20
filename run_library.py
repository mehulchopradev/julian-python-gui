from PyQt5 import QtWidgets
from library import Ui_MainWindow

class LibraryMainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    self.lib_window = Ui_MainWindow()
    self.lib_window.setupUi(self)

    self.show()

  # slots
  def onregister(self):
    self.lib_window.stackedWidget.setCurrentIndex(1)

  def onlogin(self):
    self.lib_window.stackedWidget.setCurrentIndex(0)


app = QtWidgets.QApplication([])
lib_main_window = LibraryMainWindow()
app.exec_()

