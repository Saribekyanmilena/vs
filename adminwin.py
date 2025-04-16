import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QWidget, QListWidgetItem
from admin_win import Ui_AdminWin
from adduser import Ui_Form
from regwin import Ui_Form1
import MySQLdb

#Подключение к БД
conn = MySQLdb.connect('localhost', 'root', '', 'kvalik_Kalashnikova')
cur = conn.cursor()

class AdminWin(QDialog, Ui_AdminWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.info_doc()
        self.pushButton.clicked.connect(self.open_add)
        self.pushButton_2.clicked.connect(self.open_red)

    def info_doc(self):
        cur.execute("select document_id, title, description, end_time, status from document")
        doc = cur.fetchall()
        for docs in doc:
            document_id, title, description, end_time, status = docs
            self.listWidget.addItem(f'{document_id}, {title}, {description}, {end_time}, {status}\n')

    def open_add(self):
        self.add_main = AddUser()
        self.add_main.show()

    def open_red(self):
        self.red_main = RedDoc()
        self.red_main.show()


class AddUser(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.add_user)

    def add_user(self):
        try:
            name = self.lineEdit.text()
            surname = self.lineEdit_2.text()
            password = self.lineEdit_3.text()
            role = self.comboBox.currentText()

            if name and surname and password:
                cur.execute('insert into users(name, surname, password, role) values (%s, %s, %s, %s)',
                            (name, surname, password, role))
                conn.commit()
                QMessageBox.information(self, 'Успех', 'ПОльзователь добавлен')
            else:
                QMessageBox.warning(self, 'ошибка', 'введите поля корректно')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'{e}')

class RedDoc(QDialog, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.load_info_doc)
        self.pushButton.clicked.connect(self.save_doc)

    def load_info_doc(self):
        try:
            doc_id = self.lineEdit_5.text()
            if not doc_id:
                QMessageBox.warning(self, 'Ошибка', 'Введите ID')
                return

            cur.execute('select title, description, start_time, end_time, status from document where document_id = %s', doc_id)
            docs = cur.fetchone()
            if not docs:
                QMessageBox.warning(self, 'Ошибка', 'Данные не найдены')
                return
            title, description, start_time, end_time, status = docs
            self.lineEdit.setText(title)
            self.lineEdit_2.setText(description)
            self.lineEdit_3.setText(str(start_time))
            self.lineEdit_4.setText(str(end_time))
            self.comboBox.setCurrentIndex(self.comboBox.findData(status))
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f"{e}")

    def save_doc(self):
        try:
            doc_id = self.lineEdit_5.text()
            if not doc_id:
                QMessageBox.warning(self, 'Ошибка', 'Введите ID')
                return

            title = self.lineEdit.text()
            description = self.lineEdit_2.text()
            start_time = self.lineEdit_3.text()
            end_time = self.lineEdit_4.text()
            status = self.comboBox.currentText()

            cur.execute('update document set title = %s, description = %s,start_time = %s, end_time = %s, status = %s where document_id = %s',
                            (title, description, start_time, end_time, status, doc_id))
            conn.commit()
            QMessageBox.information(self, 'успех', 'Документы отредактированы')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'{e}')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWin()
    window.show()
    sys.exit(app.exec())
