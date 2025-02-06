from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox
import FinalWin

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Измерение')
        self.setFixedSize(800, 600)


        self.fioedit = QLineEdit()
        self.yearsedit = QLineEdit()

        self.test1edit = QLineEdit()
        self.test2edit = QLineEdit()
        self.test3edit1 = QLineEdit()
        self.test3edit2 = QLineEdit()

        self.timer1_label = QLabel('Осталось: 15 сек')
        self.timer1_label.hide()
        self.timer1_button = QPushButton('Запустить таймер')
        self.timer1_button.clicked.connect(self.start_timer1)

        self.timer2_label = QLabel('Осталось: 30 сек')
        self.timer2_label.hide()
        self.timer2_button = QPushButton('Запустить таймер')
        self.timer2_button.clicked.connect(self.start_timer2)

        self.timer3_label = QLabel('Осталось: 15 сек')
        self.timer3_label.hide()
        self.timer3_button = QPushButton('Запустить таймер')
        self.timer3_button.clicked.connect(self.start_timer3)

        self.submit_button = QPushButton('Отправить результаты')
        self.submit_button.clicked.connect(self.open_last_window)

        line = QVBoxLayout()
        line.addWidget(QLabel('Введите Ф.И.О.:'))
        line.addWidget(self.fioedit)
        line.addWidget(QLabel('Полных лет:'))
        line.addWidget(self.yearsedit)

        line.addWidget(QLabel('Результат 1 (пульс за 15 секунд):'))
        line.addWidget(self.test1edit)
        line.addWidget(self.timer1_button)
        line.addWidget(self.timer1_label)

        line.addWidget(QLabel('Результат 2 (пульс после приседаний за 30 секунд):'))
        line.addWidget(self.test2edit)
        line.addWidget(self.timer2_button)
        line.addWidget(self.timer2_label)

        line.addWidget(QLabel('Результат 3 (пульс за первые 15 секунд и последние 15 секунд):'))
        line.addWidget(QLabel('Первые 15 секунд:'))
        line.addWidget(self.test3edit1)
        line.addWidget(QLabel('Последние 15 секунд:'))
        line.addWidget(self.test3edit2)
        line.addWidget(self.timer3_button)
        line.addWidget(self.timer3_label)

        line.addWidget(self.submit_button)
        self.setLayout(line)

        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.update_timer1)
        self.time1_remaining = 15

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.update_timer2)
        self.time2_remaining = 30

        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.update_timer3)
        self.time3_remaining = 15

    def start_timer1(self):
        self.time1_remaining = 15
        self.timer1_label.setText(f'Осталось: {self.time1_remaining} сек')
        self.timer1_label.show()
        self.timer1.start(1000)

    def update_timer1(self):
        self.time1_remaining -= 1
        self.timer1_label.setText(f'Осталось: {self.time1_remaining} сек')
        if self.time1_remaining == 0:
            self.timer1.stop()
            self.timer1_label.setText('Таймер завершён!')

    def start_timer2(self):
        self.time2_remaining = 30
        self.timer2_label.setText(f'Осталось: {self.time2_remaining} сек')
        self.timer2_label.show()
        self.timer2.start(1000)

    def update_timer2(self):
        self.time2_remaining -= 1
        self.timer2_label.setText(f'Осталось: {self.time2_remaining} сек')
        if self.time2_remaining == 0:
            self.timer2.stop()
            self.timer2_label.setText('Таймер завершён!')

    def start_timer3(self):
        self.time3_remaining = 15
        self.timer3_label.setText(f'Осталось: {self.time3_remaining} сек')
        self.timer3_label.show()
        self.timer3.start(1000)

    def update_timer3(self):
        self.time3_remaining -= 1
        self.timer3_label.setText(f'Осталось: {self.time3_remaining} сек')
        if self.time3_remaining == 0:
            self.timer3.stop()
            self.timer3_label.setText('Таймер завершён!')

    def open_last_window(self):
        try:
            years = int(self.yearsedit.text())  # Теперь years сохраняется и передаётся
            result1 = int(self.test1edit.text())
            result2 = int(self.test2edit.text())
            result3_1 = int(self.test3edit1.text())
            result3_2 = int(self.test3edit2.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка ввода", "Введите корректные числовые данные.")
            return

        final = result3_1 + result3_2
        index = ((4 * (result1 + result2 + final) - 200) / 10) / 10

        self.last_window = FinalWin.LastWindow(index, years)
        self.hide()
        self.last_window.show()



