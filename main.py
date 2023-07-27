from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtCore import QThread
from PySide6.QtGui import QAction, QPixmap

import tkinter as tk
import matplotlib.pyplot as plt
import tkinter.filedialog
import qimage2ndarray

import pydicom
import sys
import os


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.mainWindow = loader.load('mainWindow.ui')
        self.initialize()
        self.mainWindow.show()

    def initialize(self):
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openDicomFiles)

        exitAction = QAction('Exit',self)
        exitAction.triggered.connect(QApplication.quit)

        menubar = self.mainWindow.menuBar()
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
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(qimage_var))

        self.mainWindow.graphicsView.setScene(scene)





app = QApplication(sys.argv)
main = mainWindow()
sys.exit(app.exec())