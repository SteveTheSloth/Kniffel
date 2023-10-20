from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 454)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionView_Lists = QAction(MainWindow)
        self.actionView_Lists.setObjectName(u"actionView_Lists")
        self.actionCreate_New_List = QAction(MainWindow)
        self.actionCreate_New_List.setObjectName(u"actionCreate_New_List")
        self.actionAppend_Existing_List = QAction(MainWindow)
        self.actionAppend_Existing_List.setObjectName(u"actionAppend_Existing_List")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(260, 40, 101, 41))
        self.Die = QGraphicsView(self.centralwidget)
        self.Die.setObjectName(u"Die")
        self.Die.setGeometry(QRect(60, 220, 61, 61))
        self.Die_2 = QGraphicsView(self.centralwidget)
        self.Die_2.setObjectName(u"Die_2")
        self.Die_2.setGeometry(QRect(160, 220, 61, 61))
        self.Die_3 = QGraphicsView(self.centralwidget)
        self.Die_3.setObjectName(u"Die_3")
        self.Die_3.setGeometry(QRect(260, 220, 61, 61))
        self.Die_4 = QGraphicsView(self.centralwidget)
        self.Die_4.setObjectName(u"Die_4")
        self.Die_4.setGeometry(QRect(360, 220, 61, 61))
        self.Die_5 = QGraphicsView(self.centralwidget)
        self.Die_5.setObjectName(u"Die_5")
        self.Die_5.setGeometry(QRect(460, 220, 61, 61))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 330, 101, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 330, 101, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(380, 330, 101, 41))
        self.pushButton_3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 578, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuLists = QMenu(self.menubar)
        self.menuLists.setObjectName(u"menuLists")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLists.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuLists.addAction(self.actionView_Lists)
        self.menuLists.addAction(self.actionCreate_New_List)
        self.menuLists.addAction(self.actionAppend_Existing_List)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionView_Lists.setText(QCoreApplication.translate("MainWindow", u"View Lists", None))
        self.actionCreate_New_List.setText(QCoreApplication.translate("MainWindow", u"Create New List", None))
        self.actionAppend_Existing_List.setText(QCoreApplication.translate("MainWindow", u"Append Existing List", None))
#if QT_CONFIG(tooltip)
        self.Name.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Scores</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Take", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Cross", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuLists.setTitle(QCoreApplication.translate("MainWindow", u"Lists", None))
    # retranslateUi
    
    

    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    go = Ui_MainWindow()
    f = QMainWindow()
    go.setupUi(f)
    f.show()
    sys.exit(app.exec_())