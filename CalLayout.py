

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)

class MyCal(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		grid = QGridLayout()
		self.setLayout(grid)

		names = ['Del', 'CE', 'C', '±', '√',
				 '7'  , '8' , '9', '/', '%',
				 '4'  , '5' , '6', '*', '1/x',
				 '1'  , '2' , '3', '-', '=',
				 '0'        , '.', '+'     ]

		positions = [(i,j) for i in range(4) for j in range(5)]
		print(positions)

		for position, name in zip(positions, names):

			if name == '=':
				continue
			button = QPushButton(name)
			grid.addWidget(button, *position)

		button = QPushButton(names[19])
		grid.addWidget(button, *[3, 4, 2, 1])

		button = QPushButton(names[20])
		grid.addWidget(button, *[4, 0, 1, 2])

		button = QPushButton(names[21])
		grid.addWidget(button, *[4, 2])

		button = QPushButton(names[22])
		grid.addWidget(button, *[4, 3])

		self.move(300, 150)
		self.setWindowTitle('Calculator')
		self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyCal()
    sys.exit(app.exec_())