from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class LastWindow(QWidget):
    def __init__(self, index, years):
        super().__init__()
        self.setWindowTitle('Результат теста')
        self.setFixedSize(800, 600)


        status = self.get_status(index, years)


        result_text = f"Индекс Руфье: {index:.2f}\nСостояние здоровья: {status}"

        result_label = QLabel(result_text)
        result_label.setWordWrap(True)
        result_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(result_label, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def get_status(self, index, years):

        levels = {
            "Низкий": [(15, 16.5, 18, 19.5, 21)],
            "Удовлетворительный": [(11, 12.5, 14, 15.5, 17), (14.9, 16.4, 17.9, 19.4, 20.9)],
            "Средний": [(6, 7.5, 9, 10.5, 12), (10.9, 12.4, 13.9, 15.4, 16.9)],
            "Выше среднего": [(0.5, 2, 3.5, 5, 6.5), (5.9, 7.4, 8.9, 10.4, 11.9)],
            "Высокий": [(0.4, 1.9, 3.4, 4.9, 6.4)]
        }


        if years >= 15:
            age_index = 0
        elif years >= 13:
            age_index = 1
        elif years >= 11:
            age_index = 2
        elif years >= 9:
            age_index = 3
        else:
            age_index = 4


        for category, ranges in levels.items():
            if len(ranges) == 1:
                if index >= ranges[0][age_index]:
                    return category
            else:
                if ranges[0][age_index] <= index <= ranges[1][age_index]:
                    return category

        return "Ошибка в расчете"