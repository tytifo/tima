import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import string
import sqlite3


class TextBrowserSample(QMainWindow):
    def __init__(self):
        super(TextBrowserSample, self).__init__()
        uic.loadUi('02.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        name = self.textEdit.toPlainText()  # <---   - text()   +++ toPlainText
        f = open(name, 'r')
        s = f.read()
        for p in string.punctuation:
            if p in s:
                s = s.replace(p, ' ')
        s = s.split()
        a = (sum([len(word) for word in s]) / len(s))
        print(a)
        con = sqlite3.connect("1.db")

        # Создание курсора
        cur = con.cursor()
        result = cur.execute("""SELECT Author FROM author
                    WHERE Avarage_number_of_word = 2.75""").fetchall()
        for elem in result:
            print(elem)
        f.close()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TextBrowserSample()
    form.show()
    sys.exit(app.exec())