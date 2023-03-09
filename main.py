import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from ui_imagedialog import Ui_ImageDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ImageDialog()
ui.setupUi(window)

window.show()

'''Окно ошибки'''
msg = QMessageBox().critical(window,
                             'VahVahTitle',
                             'Some Info',
                             QMessageBox.StandardButton.Ok
                             | QMessageBox.StandardButton.Cancel,
                             )
print(msg)

'''Всплывающее окно'''
msgBox = QMessageBox()
msgBox.setWindowTitle('My Super Title')
msgBox.setText("The document has been modified.")
msgBox.setInformativeText("Do you want to save your changes?")
msgBox.setStandardButtons(
    QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
msgBox.setDefaultButton(QMessageBox.StandardButton.Save)
ret = msgBox.exec()
print(ret)

txt = 'Hello World!'
print(txt)

sys.exit(app.exec())


