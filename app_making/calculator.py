from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("CALCULATOR")
main_window.resize(500, 500)

text_box = QLineEdit()
grid = QGridLayout()

button_list = [ "C", "%", "X", "/",
                "7", "8", "9", "*",
                "4", "5", "6", "-", 
                "1", "2", "3", "+", 
                " ", "0", ".", "="]



# clear = QPushButton("C")
# delete = QPushButton("X")

row = 0
col = 0

for text in button_list:
    button = QPushButton(text)

    grid.addWidget(button, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1




master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

# button_row = QHBoxLayout()
# button_row.addWidget(clear)
# button_row.addWidget(delete)

# master_layout.addLayout(button_row)

main_window.setLayout(master_layout)
main_window.show()
app.exec_()