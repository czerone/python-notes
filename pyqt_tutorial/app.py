import sys
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
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

    def resizeEvent(self, event):
        print('Filename Encryption Window Resize!')
        width, height = event.size().width(), event.size().height()
        print(event.size())
        print(width, height)

    def closeEvent(self, event):
        print('Filename Encryption Window Close!')
        self.l = LoginWindow()
        print('Login Window Open!')
        self.l.show()

class LoginWindow(QDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_LoginProfile()
        self.ui.setupUi(self)

        # click event function will be shown under ui
        self.ui.login_button.clicked.connect(self.loginCheck)
        self.show()

    def loginCheck(self):
        print('check account and password...')
        input_account = self.ui.input_account.text()
        input_password = self.ui.input_password.text()
        if input_password == 'chen' and input_account == 'poting':
            print('Success')
            self.ui.result.setText("Success")
            self.slot_btn_function()
        else:
            print('Failed')
            self.ui.result.setText("Failed")

    def slot_btn_function(self):
        print('Login Window Close!')
        self.hide()
        print('Filename Encryption Window Open!')
        self.a = AppWindow()
        self.a.show()

    def resizeEvent(self, event):
        print('Login Window Resize!')
        width, height = event.size().width(), event.size().height()
        print(event.size())
        print(width, height)

    def closeEvent(self, event):
        print('Login Window Close!')


def main():
    app = QApplication(sys.argv)
    w = LoginWindow()
    print('Login Window Open!')
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()