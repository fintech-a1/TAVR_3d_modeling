from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene, QGraphicsPixmapItem, QGraphicsObject, QGraphicsSceneMouseEvent
from PySide6.QtCore import QThread
from PySide6.QtGui import QAction, QPixmap

import tkinter as tk
import matplotlib.pyplot as plt
import tkinter.filedialog
import qimage2ndarray

import pydicom
# import PySide6
import sys
import os


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.mainwindow = loader.load('mainWindow.ui')
        self.mainwindow.show()
        self.initialize()

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

    def openDicomFiles(self):
        print('File open clicked')

        filename = tk.filedialog.askopenfilename(initialdir='C:/', title='open File', filetypes=(('DICOM file','*.dcm'),('all files','*.*')))
        openFileList = filename

        self.readDicomFile(openFileList)

    def readDicomFile(self, filelist):
        print(filelist)
        dcm = pydicom.dcmread(filelist)
        img = dcm.pixel_array

        qimage_var = qimage2ndarray.array2qimage(img, normalize=True)

        # self.mainWindow.label.setPixmap(QPixmap(qimage_var))

        ### graphics view
        # scene = QGraphicsScene()
        scene = SceneManager()
        scene.addPixmap(QPixmap(qimage_var))

        self.mainwindow.graphicsView.setScene(scene)
        # scene.signalMousePos.connect(prnt)


class SceneManager(QGraphicsScene):
    def __init__(self):
        super().__init__()

    def mouseMoveEvent(self, event):
        print('event!')
        print('Mouse move : {}, {}'.format(event.scenePos().x(), event.scenePos().y()))

    def mousePressEvent(self, event):
        print('mouse Pressed')
        print('MOuse pressed : {}, {}'.format(event.scenePos().x(), event.scenePos().y()))








app = QApplication(sys.argv)
main = mainWindow()
sys.exit(app.exec())