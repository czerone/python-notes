import sys
from PyQt5.QtWidgets import QDialog, QMainWindow, QWidget, QApplication
from LoginPageUI import Ui_LoginProfile
from FileNameEncryption import Ui_FileEncryption


class AppWindow(QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui =Ui_FileEncryption()
        self.ui.setupUi(self)

        # click event function will be shown under ui
        self.ui.start_button.clicked.connect(self.changeName)
        self.show()

    def changeName(self):
        input_file_name = self.ui.input_file_name.text()
        input_file_address = self.ui.input_file_address.text()
        sequence = self.ui.sequence.text()
        self.ui.result.setText("Change Name Success")



class LoginWindow(QDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_LoginProfile()
        self.ui.setupUi(self)

        # click event function will be shown under ui
        self.ui.login_button.clicked.connect(self.loginCheck)
        self.show()

    def loginCheck(self):
        input_account = self.ui.input_account.text()
        input_password = self.ui.input_password.text()
        if input_password == 'chen' and input_account == 'poting':
            self.ui.result.setText("Success")
            self.slot_btn_function()
        else:
            self.ui.result.setText("Failed")
    def slot_btn_function(self):
        self.hide()
        self.a = AppWindow()
        self.a.show()

def main():
    app = QApplication(sys.argv)
    w = LoginWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()