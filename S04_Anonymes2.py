"""
Le but de l'exercice est d'afficher le resultat
de l'addition de la case 'a' avec la case 'b' dans
la case 'c'.

Pour afficher du texte a l'interieur de la case 'c'
vous aurez besoin d'utiliser: c.setText('texte a afficher')
"""

from PySide2 import QtGui, QtCore, QtWidgets
import sys


class MainUi(QtWidgets.QWidget):
    def __init__(self):
        super(MainUi, self).__init__()

        self.setWindowTitle('Calculatrice')

        main_layout = QtGui.QHBoxLayout(self)
        button = QtGui.QPushButton('Calcul')
        a = QtGui.QLineEdit('1')
        b = QtGui.QLineEdit('5')
        label_plus = QtGui.QLabel('+')
        c = QtGui.QLineEdit()
        label_egal = QtGui.QLabel('=')
        main_layout.addWidget(a)
        main_layout.addWidget(label_plus)
        main_layout.addWidget(b)
        main_layout.addWidget(label_egal)
        main_layout.addWidget(c)
        main_layout.addWidget(button)

        c.setText(lambda a, b: a + b)

        button.clicked.connect('INSERER CODE ICI')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainUi()
    win.show()
    app.exec_()
