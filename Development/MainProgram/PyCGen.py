import sys
from ImportSource import *
#import character.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtCore import *
class main_window(QMainWindow):
	def __init__(self, *args):
		super(main_window, self).__init__(*args)
		loadUi("/home/mrtreev/Documents/Computer/ProjectWyrmwraith/Development/Qt/PyCGen.ui", self)
		# self.actLoadAllSources.triggered.connect(ImportEverything)
		# triggers
		#self.actSaveAs.triggered.connect(self.saveFileDialog)
		#self.actOpen.triggered.connect(self.openFileNameDialog)
		# self.pushButton.clicked.connect(self.on_pushbutton_clicked)
		# self.actionNew.triggered.connect(self.open_main_dialog)
	# Methods for buttons/triggers
	# Save Character
	def saveFileDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
		if fileName:
			print(fileName)
	# Open Character
	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			Character.loadChar(fileName)
	# Importing sources of a single type
	def ImportAllSources(thing):
		allSources={}
		for root, dirs, files in os.walk('/home/mrtreev/Documents/Computer/ProjectWyrmwraith/Development/Source'):
			for name in files:
				if thing in name:
					allSources.update(importSource(root+'/'+name))
		return allSources
	# Importing all sources
	def importEverything(self):
		myList = ['deities']
		for name in myList:
			ImportAllSources(name)
			setattr(self, name, tempList)
# Running the application
app = QApplication(sys.argv)
widget = main_window()
widget.show()
sys.exit(app.exec_())
