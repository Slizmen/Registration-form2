import sys

from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QDateEdit, QPushButton, QHBoxLayout, QVBoxLayout

class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Регистрация')
        nameField = QLineEdit()
        passwordField = QLineEdit()
        dateField = QDateEdit()
        buttonReg = QPushButton('Зарегистрироваться')
        nameField.setMaxLength(10)
        passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        layout = QVBoxLayout()
        layout1 = QFormLayout()
        layout1.addRow('Имя', nameField)
        layout1.addRow('Пароль', passwordField)
        layout1.addRow('Дата рождения', dateField)
        layout.addLayout(layout1)
        layout.addWidget(buttonReg)
        self.setLayout(layout)

class Authorisation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')
        nameField = QLineEdit()
        passwordField = QLineEdit()
        nameField.setMaxLength(10)
        passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        enterBut = QPushButton('Войти')
        regBut = QPushButton('Регистрация')
        layout = QVBoxLayout()
        layout1 = QFormLayout()
        layout1.addRow('Имя', nameField)
        layout1.addRow('Пароль', passwordField)
        layout2 = QHBoxLayout()
        layout2.addWidget(enterBut)
        layout2.addWidget(regBut)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        self.setLayout(layout)
        regBut.clicked.connect(self.reg_form) 

    def reg_form(self):
        self.reg = Registration()
        self.reg.show()


app = QApplication(sys.argv)
window = Authorisation()
window.show()
sys.exit(app.exec())