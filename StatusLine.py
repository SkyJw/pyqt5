import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

	def __init__(self):
		super().__init__()#引用父类的构造函数

		self.initUI()

	def initUI(self):
		self.statusBar().showMessage('Ready')

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('StatusBar')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())