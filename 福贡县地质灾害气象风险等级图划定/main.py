from PyQt5.Qt import *
from PyQt5 import QtWidgets

import image_save
from mainwindow import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5 import QtGui
from drawing import picture_drawing as pid
from image_save import *
import time

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    """加载图片"""
    """
    def picture_load(self):
        filename = 'R-C.jpg'
        picture = QtGui.QPixmap(filename)
        self.graphicsView.setPixmap(picture)
    """

    @pyqtSlot()
    def on_pushButton1_clicked(self):
        print('你按下了确定键')
        self.levels = []
        self.colors = []
        a = self.MA.currentText()
        self.levels.append(a)
        b = self.SHI.currentText()
        self.levels.append(b)
        c = self.LU.currentText()
        self.levels.append(c)
        d = self.SHANG.currentText()
        self.levels.append(d)
        e = self.JIA.currentText()
        self.levels.append(e)
        f = self.ZI.currentText()
        self.levels.append(f)
        g = self.PI.currentText()
        self.levels.append(g)
        for level in self.levels:
            if level == '4级':
                self.colors.append('red')
            if level == '3级':
                self.colors.append('orange')
            if level == '2级':
                self.colors.append('yellow')
            if level == '1级':
                self.colors.append('none')
        print(self.levels)
        print(self.colors)
        pid(colors=self.colors)
    #按下预览键后将图片载入graphicView控件中并显示
    @pyqtSlot()
    def on_pushButton2_clicked(self):
        print('你按下了预览键')

        frame = QImage("my_plot.png")
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)                   #载入图片
        self.graphicsView.fitInView(item,Qt.KeepAspectRatio)#图片填充方式

    @pyqtSlot()
    def on_pushButton3_clicked(self):
        print('你按下了保存图片键')
        formatted_date = time.strftime("%Y-%m-%d")
        picture_savename = f'福贡县地质灾害气象风险图{formatted_date}.png'
        image_save.save_image_to_directory('my_plot.png','保存图片',picture_savename)

"""主程序：启动窗口程序"""
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())