
from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QWindow)
from PyQt5.QtWidgets import *
import sys




class Ui_MainWindow(object):
    def setupUi(self, MainWindow, newgame):
        self.game = newgame
        self.mainwindow = MainWindow
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(609, 453)
        self.names = list()
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionChange_Scores = QAction(MainWindow)
        self.actionChange_Scores.setObjectName(u"actionChange_Scores")
        self.actionView_Lists = QAction(MainWindow)
        self.actionView_Lists.setObjectName(u"actionView_Lists")
        self.actionCreate_New_List = QAction(MainWindow)
        self.actionCreate_New_List.setObjectName(u"actionCreate_New_List")
        self.actionContinue_Existing_List = QAction(MainWindow)
        self.actionContinue_Existing_List.setObjectName(u"actionContinue_Existing_List")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.namelist = list()
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 130, 151, 51))
        self.namelist.append(self.lineEdit)
        font = QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(360, 130, 151, 51))
        self.lineEdit_4.setFont(font)
        self.namelist.append(self.lineEdit_4)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 200, 151, 51))
        self.lineEdit_2.setFont(font)
        self.namelist.append(self.lineEdit_2)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(360, 200, 151, 51))
        self.lineEdit_5.setFont(font)
        self.namelist.append(self.lineEdit_5)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(110, 270, 151, 51))
        self.lineEdit_3.setFont(font)
        self.namelist.append(self.lineEdit_3)
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(360, 270, 151, 51))
        self.lineEdit_6.setFont(font)
        self.namelist.append(self.lineEdit_6)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 340, 151, 61))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 40, 201, 51))
        font2 = QFont()
        font2.setPointSize(17)
        self.label.setFont(font2)
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 130, 21, 51))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 200, 21, 51))
        self.label_3.setFont(font3)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 270, 21, 51))
        self.label_4.setFont(font3)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 130, 21, 51))
        self.label_5.setFont(font3)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 200, 21, 51))
        self.label_6.setFont(font3)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 270, 21, 51))
        self.label_7.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 609, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuLists = QMenu(self.menubar)
        self.menuLists.setObjectName(u"menuLists")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.pushButton)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuLists.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.actionNew.triggered.connect(self.new_game)
        self.menuFile.addAction(self.actionLoad)
        self.actionLoad.triggered.connect(self.load)
        self.menuFile.addAction(self.actionSave)
        self.actionSave.triggered.connect(self.save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.quit)
        self.menuSettings.addAction(self.actionChange_Scores)
        self.actionChange_Scores.triggered.connect(self.change_scores)
        self.menuLists.addAction(self.actionView_Lists)
        self.actionView_Lists.triggered.connect(self.viewlist)
        self.menuLists.addAction(self.actionCreate_New_List)
        self.actionCreate_New_List.triggered.connect(self.createlist)
        self.menuLists.addAction(self.actionContinue_Existing_List)
        self.actionContinue_Existing_List.triggered.connect(self.continuelist)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionChange_Scores.setText(QCoreApplication.translate("MainWindow", u"Change Scores", None))
        self.actionView_Lists.setText(QCoreApplication.translate("MainWindow", u"View Lists", None))
        self.actionCreate_New_List.setText(QCoreApplication.translate("MainWindow", u"Create New List", None))
        self.actionContinue_Existing_List.setText(QCoreApplication.translate("MainWindow", u"Continue Existing List", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.pushButton.clicked.connect(self.cont_clicked)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Player Names", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"3.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"5.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"2.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"4.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"6.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuLists.setTitle(QCoreApplication.translate("MainWindow", u"Lists", None))
    # retranslateUi
    

    

    def cont_clicked(self):
        if self.namelist != []: 
            self.game.got_names([x.text() for x in self.namelist if x.text() != ""])
            
            
    def continuelist(self):
        self.game.from_list()
        

    def setupgameUi(self, MainWindow, newgame):
        self.game = newgame
        self.mainwindow = MainWindow
        self.layout = QGridLayout()
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 454)
        self.pics = [one := QPixmap("one.gif"), two := QPixmap("two.gif"), three := QPixmap("three.gif"), four := QPixmap("four.gif"), five := QPixmap("five.gif"), six := QPixmap("six.gif")]

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
        
        self.make_labels()
        self.activate_player(0)
        self.dice = list()
        for i in range(5):
            x = QGraphicsView(self.centralwidget)
            x.setObjectName(str(i+1))
            x.setGeometry(QRect(60 + 100*i, 220, 61, 61))   
            self.dice.append(x)
            x.hide()
            
            
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 330, 101, 41))
        self.pushButton.clicked.connect(self.roll)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 330, 101, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.take)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(310, 330, 101, 41))
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(self.cross)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(450, 330, 101, 41))
        self.pushButton_4.setFont(font)
        self.pushButton_4.clicked.connect(self.keep)
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
        self.actionNew.triggered.connect(self.new_game)
        self.menuFile.addAction(self.actionLoad)
        self.actionLoad.triggered.connect(self.load)
        self.menuFile.addAction(self.actionSave)
        self.actionSave.triggered.connect(self.save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.quit)
        self.menuLists.addAction(self.actionView_Lists)
        self.actionView_Lists.triggered.connect(self.viewlist)
        self.menuLists.addAction(self.actionCreate_New_List)
        self.actionCreate_New_List.triggered.connect(self.createlist)
        self.menuLists.addAction(self.actionAppend_Existing_List)
        self.actionAppend_Existing_List.triggered.connect(self.appendlist)

        self.retranslategameUi(MainWindow)
        
        

        QMetaObject.connectSlotsByName(MainWindow)
        self.game.start_round()
    # setupUi
    
    
        
    def retranslategameUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionView_Lists.setText(QCoreApplication.translate("MainWindow", u"View Lists", None))
        self.actionCreate_New_List.setText(QCoreApplication.translate("MainWindow", u"Create New List", None))
        self.actionAppend_Existing_List.setText(QCoreApplication.translate("MainWindow", u"Append Existing List", None))

        for i in self.Name:
            i.setText(QCoreApplication.translate("MainWindow", i.objectName(), None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Take", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Cross", None))
        self.pushButton_4.setText(QCoreApplication.translate("Mainwindow", u"Keep", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuLists.setTitle(QCoreApplication.translate("MainWindow", u"Lists", None))
    # retranslateUi
    
    def change_dice_pictures(self, values):
        for index, i in enumerate(values):
            scene = QGraphicsScene()
            item = QGraphicsPixmapItem(self.pics[i-1])
            scene.addItem(item)
            self.dice[index].setScene(scene)
            
    def make_labels(self):
        xpos = 260 - len(self.game.playerlist)*20
        self.Name = list()
        for index, i in enumerate(self.game.playerlist):
            x = QLabel(self.centralwidget)
            x.setObjectName(i.name)
            x.setText(QCoreApplication.translate("MainWindow", i.name, None))
            x.setGeometry(QRect(xpos + index*80, 40, 61, 41))
            self.Name.append(x)
            x.show()
            
    def new_labels(self):
        try:
            for i in self.Name:
                i.destroy()
                i.hide()
        except AttributeError:
            self.make_labels()
            
            
    def roll(self):
        for i in self.dice:
            i.show()
        values = self.game.roll()
        self.change_dice_pictures(values)

    def take(self):
        self.show_options(self.game.activeplayer.options_take())
        

    def cross(self):
        self.show_options(self.game.activeplayer.options_cross(), 1)
    
    def keep(self):
        if 1 <= self.game.activeplayer.rollcount < 3:
            self.show_keep_options(self.game.activeplayer.mydice)
        else: return
        
    def show_keep_options(self, dice):
        try: self.optionswidget.destroy()
        except: pass
        self.optionswidget = QWidget()
        self.optionswidget.layout = QGridLayout()
        self.optionswidget.setLayout(self.optionswidget.layout)
        for index, i in enumerate(dice):
            cbutton = QCheckBox(str(i.value))
            cbutton.die = i
            if i.kept:
                cbutton.setChecked(True)
            cbutton.toggled.connect(self.kept)
            self.optionswidget.layout.addWidget(cbutton, index, 0)
        self.optionswidget.show()
        
    def update_tooltip(self, index, toolst):
        self.Name[index].setToolTip(toolst)
        
    def show_options(self, options, state=0):
        try: self.optionswidget.destroy()
        except: pass
        self.optionswidget = QWidget()
        self.optionswidget.layout = QGridLayout()
        if state == 0:
            text = "take"
            buttonclick = self.taken
        elif state == 1:
            text = "cross"
            buttonclick = self.crossed
        take = QPushButton()
        take.setText(text)
        take.clicked.connect(buttonclick)
        dismiss = QPushButton()
        dismiss.setText("dismiss")
        dismiss.clicked.connect(self.optionswidget.close)
        self.optionswidget.setLayout(self.optionswidget.layout)
        self.radiobuttons = list()
        
        for key, value in options.items():
            x = QRadioButton(str(value[0]) + "\t" + value[1])
            x.value = (key, value[0], value[1])
            self.optionswidget.layout.addWidget(x, key, 0)
            self.radiobuttons.append(x)            
        self.optionswidget.layout.addWidget(take, 16, 0)
        self.optionswidget.layout.addWidget(dismiss, 16, 1)
        take.setFixedWidth(50)
        dismiss.setFixedWidth(50)
        self.optionswidget.show()

    def taken(self):
        for i in self.radiobuttons:
            if i.isChecked():
                self.game.take_option(i.value)
                for i in self.dice:
                    i.hide()
                self.game.end_turn()
                self.optionswidget.destroy()
    
    def crossed(self):
        for i in self.radiobuttons:
            if i.isChecked():
                self.game.take_option(i.value)
                for i in self.dice:
                    i.hide()
                self.game.end_turn()
                self.optionswidget.destroy()
    
    def kept(self):
        cbutton = self.optionswidget.sender()
        self.game.keep(cbutton.die)
        
    def activate_player(self, index):
        for i in self.Name:
            i.setStyleSheet("")
        self.Name[index].setStyleSheet("background-color: lightgreen")
        
    def show_winners(self, winners):
        for i in self.Name:
            i.setStyleSheet("")
        for i in winners:
            for j in self.Name:
                if i.name == j.text():
                    j.setStyleSheet("background-color: red")
        
    def new_game(self):
        self.game.new_game()
    
    def load(self):
        self.game.load_game()
        
    def show_load_files(self, files, save):
        self.loadradio = list()
        self.loadable = QWidget()
        layout = QGridLayout()
        label = QLabel()
        layout.addWidget(label)
        self.loadable.setLayout(layout)
        if save:
            self.savelabels = list()
            for i in files:
                x = QLabel()
                x.setText(i)
                self.savelabels.append(x)
                layout.addWidget(x)
            label.setText("Please enter a name for you save game.")
            namein = QLineEdit()
            savebutton = QPushButton()
            savebutton.setText("Save")
            savebutton.clicked.connect(lambda: self.savebutton(namein))
            layout.addWidget(namein)
            layout.addWidget(savebutton)
        else:
            for i in files:
                x = QRadioButton()
                x.setText(i)
                self.loadradio.append(x)
                layout.addWidget(x)
            label.setText("Please pick the game you want to laod.")
            loadbutton = QPushButton()
            loadbutton.setText("Load")
            loadbutton.clicked.connect(self.loadbutton_clicked)
            layout.addWidget(loadbutton)
        self.loadable.show()
        
    def loadbutton_clicked(self):
        for i in self.loadradio:
            if i.isChecked():
                self.loadable.destroy()
                self.game.load_game_picked(i.text())
                break
                
    
    def save(self):
        self.game.save_game()
        
    """def get_file_name(self):
        self.nameinput = QWidget()
        namein = QLineEdit()
        label = QLabel()
        label.setText("Please enter a name for you save game.")
        layout = QGridLayout()
        self.nameinput.setLayout(layout)
        savebutton = QPushButton()
        savebutton.clicked.connect(lambda: self.savebutton(namein))
        savebutton.setText("Save")
        layout.addWidget(label)
        layout.addWidget(namein)
        layout.addWidget(savebutton)
        self.nameinput.show()"""
    
    def savebutton(self, namein):
        self.loadable.destroy()
        x = namein.text()
        self.game.save_game_named(x)
        
    def success(self, name):
        self.success = QMessageBox()
        self.success.setText(f"File {name} was successfully saved.")
        self.success.setStandardButtons(QMessageBox.Ok)
        self.success.show()

    def fileexist_popup(self, name):
        self.fileexists = QMessageBox()
        self.fileexists.setText(f"File {name} already exists. Please chose a different name.")
        self.fileexists.setStandardButtons(QMessageBox.Ok)
        returnValue = QMessageBox.Ok
        if returnValue == QMessageBox.Ok:
            self.fileexists.destroy()
            self.get_file_name()
        self.fileexists.show()
        
    
        
    
    def quit(self):
        self.quitpopup()
        
    def change_scores(self):
        pass
    
    def endend(self):
        print("quit pressed")
        
    def quitpopup(self):
        quitpop = QMessageBox()
        quitpop.setText("Do you want to save the game before quitting?")
        quitpop.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)        
        returnValue = quitpop.exec()
        if returnValue == QMessageBox.Yes:
            self.game.save_game()
        elif returnValue == QMessageBox.No:
            self.game.quit_game()
        elif returnValue == QMessageBox.Cancel:
            quitpop.destroy()
    
    def viewlist(self):
        self.game.view_list()
    
    def get_list_name(self, sheets, newgame):
        self.listsview = QWidget()
        self.listsview.layout = QGridLayout()
        self.listsview.setLayout(self.listsview.layout)
        self.listbuttons = list()
        for i in sheets:
            x = QRadioButton()
            x.setText(i)
            self.listsview.layout.addWidget(x)
            self.listbuttons.append(x)
        okbutton = QPushButton()
        okbutton.setText("Ok")
        okbutton.clicked.connect(lambda: self.get_list_info(newgame))
        
        cancbutton = QPushButton()
        cancbutton.setText("Cancel")
        cancbutton.clicked.connect(self.listsview_destroy)
        self.listsview.layout.addWidget(okbutton, len(sheets)+1, 0)
        self.listsview.layout.addWidget(cancbutton, len(sheets)+1, 1)
        self.listsview.show()
    
    def listsview_destroy(self):
        self.listsview.destroy()
        
    def get_list_info(self, newgame):
        for index, i in enumerate(self.listbuttons):
            if i.isChecked():
                print(i.text())
                self.listsview.destroy()
                self.game.get_list(index, newgame)
                break
    
    def show_list(self, columns):
        self.showlist = QWidget()
        self.showlist.layout = QGridLayout()
        self.showlist.setLayout(self.showlist.layout)
        for i in range(len(columns[0])):
            for index, j in enumerate(columns):
                x = QLabel()
                x.setText(str(j[i]))
                self.showlist.layout.addWidget(x,i,index)
        okbutton = QPushButton()
        okbutton.setText("Ok")
        okbutton.clicked.connect(self.showlist_destroy)
        self.showlist.layout.addWidget(okbutton)
        self.showlist.show()
    
    def showlist_destroy(self):
        self.showlist.destroy()
            
    def createlist(self):
        self.game.create_list()
        print("createlist")
    
    def name_popup(self, names=None):
        self.namepop = QWidget()
        self.namepop.layout = QGridLayout()
        self.namepop.setLayout(self.namepop.layout)
        label = QLabel()
        label.setText("Please enter player names.")
        self.namepop.layout.addWidget(label)
        self.createlist_names = list()
        for i in range(3):
            for j in range(2):
                x = QLineEdit()
                self.namepop.layout.addWidget(x, i+1 , j)
                self.createlist_names.append(x)
        if names != None:
            for index, k in enumerate(names):
                self.createlist_names[index].setText(k)
        label_2 = QLabel()
        label_2.setText("Please enter your scoring system")
        label_3 = QLabel()
        label_3.setText("(points from first to last place ->)")
        self.namepop.layout.addWidget(label_2)
        self.namepop.layout.addWidget(label_3)
        self.createlist_scores = list()
        for i in range(6):
            x = QLineEdit()
            x.setFixedSize(QSize(16, 24))
            self.namepop.layout.addWidget(x, 4, i+2)
            self.createlist_scores.append(x)
        contbutton = QPushButton()
        contbutton.setText("Continue")
        contbutton.clicked.connect(self.cont_name_pop)
        
        
        label_4 = QLabel()
        label_4.setText("Bonus for no crossed-off scores:")
        self.namepop.layout.addWidget(label_4)
        self.bonus_box = QCheckBox()
        self.namepop.layout.addWidget(self.bonus_box)
        self.namepop.layout.addWidget(contbutton, 6, 0)
        self.namepop.show()
        
    def cont_name_pop(self):
        if self.createlist_names != [] and self.createlist_scores != []:
            self.namepop.destroy()
            self.namelist = QWidget()
            self.namelist.layout = QGridLayout()
            self.namelist.setLayout(self.namelist.layout)
            label = QLabel()
            label.setText("Enter list name")
            self.namein = QLineEdit()
            okbutton = QPushButton()
            okbutton.setText("Save")
            okbutton.clicked.connect(self.re_name_score)
            self.namelist.layout.addWidget(label)
            self.namelist.layout.addWidget(self.namein)
            self.namelist.layout.addWidget(okbutton)
            self.namelist.show()
        else: pass
        
    def re_name_score(self):
        if self.namein.text() != "":
            sheetname = self.namein.text()
            names = [x.text() for x in self.createlist_names if x.text() != ""]
            scores = [int(x.text()) for x in self.createlist_scores if x.text() != ""]
            if self.bonus_box.isChecked(): scores.append("A")
            self.game.make_list(sheetname, names, scores)
            self.namelist.destroy()
            self.namein.destroy()
    
    def appendlist(self):
        self.game.view_list()
        
