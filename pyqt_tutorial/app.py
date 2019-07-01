import sys
from PyQt5.QtWidgets import QDialog, QApplication
from MyFirstUI import Ui_Form

class AppWindow(QDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # click event function will be shown under ui
        self.ui.pushButton.clicked.connect(self.pushButtonClick)
        self.show()

    def pushButtonClick(self):
        self.ui.label.setText("Hello World")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())