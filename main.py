from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene, QGraphicsPixmapItem, QGraphicsObject, QGraphicsSceneMouseEvent
from PySide6.QtCore import QThread
from PySide6.QtGui import QAction, QPixmap
from PySide6 import QtQuick

import tkinter as tk
import matplotlib.pyplot as plt
import tkinter.filedialog
import qimage2ndarray

import pydicom
import threading
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
        dcm = pydicom.dcmread(filelist)
        img = dcm.pixel_array

        qimage_var = qimage2ndarray.array2qimage(img, normalize=True)

        # self.mainWindow.label.setPixmap(QPixmap(qimage_var))

        ### graphics view
        # scene = SceneManager(qimage_var)
        # scene.start()
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(qimage_var))

        self.mainwindow.graphicsView.setScene(scene)
        

    def mouseMoveEvent(self, event):
        # print('event!')
        # print('scenemanager - mouseMove Thread Name : ', QThread.currentThread())
        print('Mouse move : {}, {} / {}'.format(event.scenePos().x(), event.scenePos().y(), event))

    def mousePressEvent(self, event):
        # print('mouse Pressed')
        # print('scenemanager - mouseMove Thread Name : ', QThread.currentThread())
        print('MOuse pressed : {}, {} / {}'.format(event.scenePos().x(), event.scenePos().y(), event))

    def wheelEvent(self, event):
        print('Mouse Wheel Event : {} / {}', event.delta(), event)

#
#
# class SceneManager(QGraphicsScene):
#     def __init__(self, img):
#         super().__init__()
#
#         # parent.mainwindow.graphicsView.setScene(img_pixel)
#         # print('Start Scenemanager Threading')
#         # print('sceneManager - __init__ Thread Name : ',QThread.currentThread())
#
#     def mouseMoveEvent(self, event):
#         # print('event!')
#         # print('scenemanager - mouseMove Thread Name : ', QThread.currentThread())
#         print('Mouse move : {}, {} / {}'.format(event.scenePos().x(), event.scenePos().y(), event))
#
#     def mousePressEvent(self, event):
#         # print('mouse Pressed')
#         # print('scenemanager - mouseMove Thread Name : ', QThread.currentThread())
#         print('MOuse pressed : {}, {} / {}'.format(event.scenePos().x(), event.scenePos().y(), event))
#
#     def wheelEvent(self, event):
#         print('Mouse Wheel Event : {} / {}', event.delta(), event)








if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main = mainWindow()

    # threadScene = threading.Thread(target=SceneManager)
    # threadScene.start()

    sys.exit(app.exec())