import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import TR_mainframe

from tkinter import messagebox, Text, Tk, WORD, DISABLED

import os
import parse_data
import Save_html


root = Tk()
root.withdraw()


class App(QtWidgets.QMainWindow, TR_mainframe.Ui_TrainingResults):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_find_fit.clicked.connect(self.browse_fit)
        self.btn_save.clicked.connect(self.browse_path)
        self.btn_go.clicked.connect(self.go)

    def browse_fit(self):
        filename = QFileDialog.getOpenFileName(filter='*.FIT')
        path = filename[0]
        self.text_path_to_fit.setText(path)

    def browse_path(self):
        path = QFileDialog.getExistingDirectory(directory=r'C:\\')
        self.text_path_to_save.setText(path+'/')

    @staticmethod
    def ShowRes(data):
        show_res = Tk()
        text = Text(master=show_res, height=50, width=80, bg="white",
                    fg='black', wrap=WORD)
        text.pack()
        text.insert(1.0, data)
        text.config(state=DISABLED)
        show_res.mainloop(1)

    def go(self):
        fitfile = self.text_path_to_fit.toPlainText()
        if fitfile == '':
            messagebox.showerror("Error", 'Пустая строка!')

        elif not os.path.exists(fitfile):
            messagebox.showerror("Error", 'Файла не существует!')

        elif fitfile[-4:].lower() != '.fit':
            messagebox.showerror("Error", 'Неверный формат!')

        else:
            if self.btn_txt.isChecked():
                if self.text_path_to_save.toPlainText() == '':
                    messagebox.showerror("Error", 'Не указан путь сохранения!')
                else:
                    parse_data.save_res(self.text_path_to_fit.toPlainText(), self.text_path_to_save.toPlainText())
                    messagebox.showinfo('Успешно!', "Результаты сохранены")
            if self.btn_map.isChecked():
                if self.text_path_to_save.toPlainText() == '':
                    messagebox.showerror("Error", 'Не указан путь сохранения!')
                else:
                    Save_html.save_map(self.text_path_to_fit.toPlainText(), self.text_path_to_save.toPlainText())
                    messagebox.showinfo('Успешно!', "Карта сохранена")
            self.ShowRes(parse_data.data_res(self.text_path_to_fit.toPlainText()))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
