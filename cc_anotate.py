import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, qApp, QFileDialog
from PyQt5.QtGui import QIcon

gt_name_path = 'ground-truth'
img_name_path = 'images'

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(qApp.quit)

        openAction = QAction("&Open", self)
        openAction.triggered.connect(self.open)

        saveAction = QAction("&Save", self)
        saveAction.triggered.connect(self.save)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)

        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        self.setWindowTitle("file select")
        self.setWindowIcon(QIcon('img/icon-32x32.png'))
        self.setGeometry(50, 50, 800, 500)
        self.show()

    def open(self):
        dialog = QFileDialog(self, "Select Directory")
        dialog.setLabelText(QFileDialog.FileName, "Directory name:")
        dialog.setLabelText(QFileDialog.Accept, "Open")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setOptions(QFileDialog.ShowDirsOnly)

        path = QFileDialog.getExistingDirectory(self, "Open Directory", "")

        if dialog.exec_():
            r = dialog.selectedFiles()
            path = r[0]
    
        self.gt_path = os.path.join(path, gt_name_path)
        self.img_path = os.path.join(path, img_name_path)

        gt_list = os.listdir(self.gt_path)
        img_list = os.listdir(self.img_path)

        print(gt_list)

    def save(self):
        dialog = QFileDialog(self, "Select Directory")
        dialog.setLabelText(QFileDialog.FileName, "Directory name:")
        dialog.setLabelText(QFileDialog.Accept, "Open")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setOptions(QFileDialog.ShowDirsOnly)

        path = QFileDialog.getExistingDirectory(self, "Open Directory", "")

        if dialog.exec_():
            r = dialog.selectedFiles()
            path = r[0]

        print(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    sys.exit(app.exec_())