from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene, QGraphicsPixmapItem, QGraphicsObject, QGraphicsSceneMouseEvent
from PySide6.QtCore import QThread
from PySide6.QtGui import QAction, QPixmap, QPainter
from PySide6 import QtQuick

import tkinter as tk
import matplotlib.pyplot as plt
import tkinter.filedialog
import qimage2ndarray

import pydicom
import threading
import PySide6
import sys
import os

# loader = QUiLoader()
# from_class = loader.load('mainWindow.ui')


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.mainwindow = loader.load('mainWindow.ui')
        self.mainwindow.show()
        self.initialize()
        # print('mainWindow - __init__ Thread Name : ', QThread.currentThread())

    def initialize(self):
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openDicomFiles)

        exitAction = QAction('Exit',self)
        exitAction.triggered.connect(QApplication.quit)

        menubar = self.mainwindow.menuBar()
        filemenu = menubar.addMenu('File')
        filemenu.addAction(openAction)
        filemenu.addSeparator()
        filemenu.addAction(exitAction)

        # print('mainWindow - initialize Thread Name : ',QThread.currentThread())

    def openDicomFiles(self):
        print('File open clicked')

        filename = tk.filedialog.askopenfilename(initialdir='C:/', title='open File', filetypes=(('DICOM file','*.dcm'),('all files','*.*')))
        openFileList = filename

        # print('mainWindow - openDicomFiles Thread Name : ', QThread.currentThread())

        self.readDicomFile(openFileList)


    def readDicomFile(self, filelist):
        print(filelist)
        self.dcm = pydicom.dcmread(filelist)
        self.img = self.dcm.pixel_array

        self.qimage_var = qimage2ndarray.array2qimage(self.img, normalize=True)

        # self.mainwindow.label.setPixmap(QPixmap(self.qimage_var))

        ## graphics view
        self.scene = SceneManager(self.qimage_var)
        # scene.start()
        # self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap(self.qimage_var))

        self.mainwindow.graphicsView.setScene(self.scene)

    # def mouseMoveEvent(self, event):
    #     print('mouse event')
    #     if self.x is None:
    #         self.x = event.x()
    #         self.y = event.y()
    #         return
    #
    #     # painter = QPainter(self.label.pixmap())
    #     # painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
    #     # painter.drawLine(self.x, self.y, event.x(), event.y())
    #     # painter.end()
    #     # self.update()
    #
    #     self.x = event.x()
    #     self.y = event.y()
    #
    #     print(self.x, self.y)





class SceneManager(QGraphicsScene, QThread):
    def __init__(self, img):
        super().__init__()
        print('canvas size is : ',self.sceneRect())

        #### create layer

        # parent.mainwindow.graphicsView.setScene(img_pixel)
        # print('Start Scenemanager Threading')
        print('sceneManager - __init__ Thread Name : ',QThread.currentThread())

    def mouseMoveEvent(self, event):
        # print('event!')
        print('scenemanager - mouseMove Thread Name : ', QThread.currentThread())
        print('Mouse move : {}, {} / {}'.format(event.scenePos().x(), event.scenePos().y(), event))
        if self.x is None :
            self.x = event.x()
            self.y = event.y()
            return

        painter = QPainter(self.addPixmap())
        painter.drawLine(self.x, self.y, event.x(), event.y())
        painter.end()
        mainWindow.graphicsView.setScene()

        self.x = event.x()
        self.y = event.y()

    def mousePressEvent(self, event):
        # print('mouse Pressed')
        print('scenemanager - mouseMove Thread Name : ', QThread.currentThread())
        print('MOuse pressed : {}, {} / {}'.format(event.scenePos().x(), event.scenePos().y(), event))

    def wheelEvent(self, event):
        print('Mouse Wheel Event : {} / {}'.format(event.delta(), event) )








if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main = mainWindow()

    # threadScene = threading.Thread(target=SceneManager)
    # threadScene.start()

    sys.exit(app.exec())