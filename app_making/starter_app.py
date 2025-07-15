from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from random import choice

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(500, 500)

title = QLabel("Random Keywords")
text_1 = QLabel("?")
text_2 = QLabel("?")
text_3 = QLabel("?")

button_1 = QPushButton("Click Me")
button_2 = QPushButton("Click Me")
button_3 = QPushButton("Click Me")

my_words = ["monsoon", "summer", "winter", "autumn", "spring", "fall"]

master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment = Qt.AlignCenter)

row2.addWidget(text_1, alignment=Qt.AlignCenter)
row2.addWidget(text_2, alignment=Qt.AlignCenter)
row2.addWidget(text_3, alignment=Qt.AlignCenter)

row3.addWidget(button_1)
row3.addWidget(button_2)
row3.addWidget(button_3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

def random_word_1():
    word = choice(my_words)
    text_1.setText(word)

def random_word_2():
    word = choice(my_words)
    text_2.setText(word)

def random_word_3():
    word = choice(my_words)
    text_3.setText(word)

button_1.clicked.connect(random_word_1)
button_2.clicked.connect(random_word_2)
button_3.clicked.connect(random_word_3)

main_window.show()
app.exec_()
