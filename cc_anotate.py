import os
import sys
#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, qApp, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

gt_name_path = 'ground_truth'
img_name_path = 'images'

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gt_list = []
        self.img_list = []
        
        self.setWindowTitle("file select")
        self.setWindowIcon(QIcon('img/icon-32x32.png'))

        self.initMenubar()
        self.initLayout()
        self.setPosition()

        #self.setTable()

        self.show()

    def initMenubar(self):
        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(qApp.quit)

        openAction = QAction("&Select Folder", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.selectDirectory)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

    def initLayout(self):
        # レイアウトの addWidget により、親ウィジェットは設定されます
        panelA = QLabel("FileList")
        panelB = QLabel("Image")
        panelC = QLabel("Table1")
        panelD = QLabel("Table2")
        panelE = QLabel("Buttons")

        # Layout には、親ウィジェットを指定すると
        # win.setLayout(grid) を省略可能。
        grid = QGridLayout()

        # row, column, rowSpan, columnSpan
        grid.addWidget(panelA, 0, 0, 2, 1)
        grid.addWidget(panelB, 0, 1)
        grid.addWidget(panelC, 0, 2)
        grid.addWidget(panelD, 1, 1)
        grid.addWidget(panelE, 1, 2)
        grid.setContentsMargins(10, 10, 10, 10)

        # FileList の横幅を固定
        panelA.setMaximumWidth(200)
        grid.setColumnMinimumWidth(0, 200)

    def setPosition(self):
        desktop = qApp.desktop()
        geometry = desktop.screenGeometry()
        # ウインドウサイズ(枠込)を取得
        framesize = self.frameSize()
        # ウインドウの位置を指定
        self.move(geometry.width() / 2 - framesize.width() / 2, geometry.height() / 2 - framesize.height() / 2)
        self.resize(800, 500)

    def selectDirectory(self):
        #self.dirName = QFileDialog.getExistingDirectory(self, "Open Directory", "")
        
        dialog = QFileDialog(self, "Select Directory")
        dialog.setLabelText(QFileDialog.FileName, "Directory name:")
        dialog.setLabelText(QFileDialog.Accept, "Open")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setOptions(QFileDialog.ShowDirsOnly)

        path = ""

        if dialog.exec_():
            r = dialog.selectedFiles()
            path = r[0]

        self.dirName = path

        if os.path.exists(os.path.join(self.dirName, gt_name_path)):
            self.gt_path = os.path.join(self.dirName, gt_name_path)
            self.gt_list = os.listdir(self.gt_path)
        if os.path.exists(os.path.join(self.dirName, img_name_path)):  
            self.img_path = os.path.join(self.dirName, img_name_path)
            self.img_list = os.listdir(self.img_path)
    
    #def setTable(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    sys.exit(app.exec_())