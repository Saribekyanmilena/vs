import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QWidget
from autorisation import Ui_Autorisation
from adminwin import AdminWin
import MySQLdb


#Подключение к БД
conn = MySQLdb.connect('localhost', 'root', '', 'kvalik_Kalashnikova')
cur = conn.cursor()

class RegWindow(QDialog, Ui_Autorisation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.login)

    def login(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if not name or not password:
            QMessageBox.warning(self, 'Ошибка', 'Заполните поля')
            return

        try:
            cur.execute("select user_id, role from users where name = %s and password = %s", (name, password))
            user = cur.fetchone()
            if user:
                user_id, role = user
                if role == 'admin':
                    self.main_window = AdminWin()
                else:
                    QMessageBox.warning(self, 'Ошибка', 'Не удалось открыть')
                self.main_window.show()
                self.hide()
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f"{e}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegWindow()
    window.show()
    sys.exit(app.exec())