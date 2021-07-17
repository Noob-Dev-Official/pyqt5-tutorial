from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

## "self" is like "this" in Java
## we are extending QMainWindow
class MyWindow(QMainWindow):
	def __init__(self):
		## calling the constructor of QMainWindow
		super(MyWindow, self).__init__()
		self.initUI()
		
	def initUI(self):
		# label
		label = QtWidgets.QLabel(self) # initialing label variable
		label.setText("First label") # setting label text
		label.move(50, 50) # move the label (x, y)
		
		# button
		b1 = QtWidgets.QPushButton(self) # creating a button
		b1.setText("Click me") # setting the text
		b1.clicked.connect(clicked) # event listener for the button

	# event listener for the button
	def clicked(self):
		self.label.setText("button pressed")

def window():
	app = QApplication(sys.argv) # starter of the GUI
	win = QMainWindow() # making a window
	win.setGeometry(200, 200, 1000, 500) # xpos, ypos, width, height # xpos and ypos says where to show up the window on your screen
	win.setWindowTitle("Dashboard")
	
	
	
	
	win.show() # to show window
	sys.exit(app.exec_()) # this is waiting for QApplication to exit, when it does, this closes the application
	
window()
