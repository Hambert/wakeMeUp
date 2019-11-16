# import for QT
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# Import for WAKE on lan
from wakeonlan import send_magic_packet

# Import for config file
import json

try:
	with open("pc_config.json", "r") as read_file:
	    data = json.load(read_file)
except:
	data = None
	print("No config file found!")



def on_button_clicked(name):

	# get mac from config file
	for device in data["computer"]:
		if device["name"] == name:
			mac = device["mac"]

	send_magic_packet( mac )

	alert = QMessageBox()
	alert.setText(name + ' [' + mac   + '] will start now')
	alert.exec_()


def createConnect(name):
	return lambda : on_button_clicked( name )


if data != None:
	# create a all buttons
	for device in data["computer"]:
		btn = QPushButton( device["name"] )
		btn.clicked.connect( createConnect( name = device["name"] ) ) 
		layout.addWidget(btn)
else:
	label = QLabel("No config file found! Edit and rename example_config.json to pc_config.json")
	layout.addWidget(label)

def myGUI():
	window.setLayout(layout)
	window.show()
	app.exec_()


if __name__=='__main__':
	myGUI();
