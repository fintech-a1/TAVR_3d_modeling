# from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
# from PySide6.QtCore import QSize
# import sys
#
# class Qt_Ex(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('Qt Example')
#         self.setFixedSize(QSize(250, 100))
#         self.label = QLabel("마우스이벤트")
#         self.setCentralWidget(self.label)
#
#     def mouseMoveEvent(self, event):
#         self.label.setText('mouseMoveEvent')
#         print('mouseMoveEvent')
#
#     def mousePressEvent(self, event):
#         self.label.setText("mousePressEvent")
#         print('mousePressEvent')
#
#     def mouseReleaseEvent(self, event):
#         self.label.setText("mouseReleaseEvent")
#         print('mouseReleaseEvent')
#
#     def mouseDoubleClickEvent(self, event):
#         self.label.setText("mouseDoubleClickEvent")
#         print("mouseDoubleClickEvent")
#
#
# app = QApplication(sys.argv)
# window = Qt_Ex()
# window.show()
#
# app.exec()


a = {'한국','중국','일본'}

a.add('베트남')
a.add('중국')
a.remove('일본')
a.update({'홍콩','한국','태국'})

print(a)
