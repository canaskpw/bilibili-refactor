# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1047, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1047, 634))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_ico/bilibili.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{border-image: url(img/background.jpg);}\n"
"QWidget::section{border-image:none}\n"
"QSlider{border-image:none}\n"
"QLabel{color:white}\n"
"QMenu{border-image:none}\n"
"QAction{border-image:none}\n"
"\n"
"QPushButton{border-image:none;\n"
"border:1px solid rgb(255, 255, 255);\n"
"background-color:rgba(100, 100, 100,0.5);\n"
"color:white;\n"
"border-radius:10px;\n"
"font: 17pt \"幼圆\";\n"
"}\n"
"QPushButton::hover{background:rgba(0,0,0,0.5)}\n"
"#before_button{border-radius:40px;font:20pt;}\n"
"#before_button:hover{font-weight:900;}\n"
"#before_page_button{font-size:10pt}\n"
"#next_page_button{font-size:10pt}\n"
"#next_button{border-radius:40px;font:20pt;}\n"
"#next_button:hover{font-weight:900}\n"
"#fanju_button{font:10pt}\n"
"#video_button{font:10pt}\n"
"QFrame{border-image:none}\n"
"QLineEdit{\n"
"border-color: rgb(255, 255, 255);\n"
"border-image:none;\n"
"background-color:rgba(0, 0, 0,0.2);\n"
"border:1px solid rgb(255, 255, 255);\n"
"font: 10pt \"幼圆\";\n"
"color:white;\n"
"selection-background-color: rgba(0, 0, 0,0.5);\n"
"border-radius:10px;\n"
"}\n"
"QCheckBox{border-image:none;color:white}\n"
"QTableWidget{\n"
"border-image: none;\n"
"background-color:rgba(0, 0, 0,0.3);\n"
"font: 10pt \"幼圆\";\n"
"selection-background-color: rgba(0, 0, 0,0.5);\n"
"selection-color: rgb(255, 255, 255);\n"
"gridline-color: white;\n"
"color:white;\n"
"border-radius:10px;}\n"
"QHeaderView{background:rgba(0,0,0,0.1);color:white; padding-left:4px; border:1px solid white; border-image: none;}\n"
"QHeaderView::section{background:rgba(0,0,0,0.1); padding-left:4px; border:1px solid white; border-image: none;}\n"
"QProgressBar{\n"
"border-image: none;\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QProgressBar::chunk{\n"
"color:white;\n"
"border-image: none;\n"
"background:rgba(0,255,0,0.3);\n"
"border-radius:10px;\n"
"}\n"
"QScrollBar{\n"
"background:grey;\n"
"border-image:none; \n"
"padding-top:20px;\n"
"padding-bottom:20px;\n"
"padding-left:3px;\n"
"padding-right:3px;\n"
"}\n"
"QScrollBar::handle{\n"
"background:rgba(0,0,0,0.3);\n"
"border-radius:6px;\n"
"min-height:60px;}\n"
"QScrollBar::handle:vertical:hover{ \n"
"background:rgba(0,0,0,0.3);}\n"
"QScrollBar::add-line:vertical{\n"
"background:rgba(0,0,0,0.3);}\n"
"QScrollBar::sub-line:vertical{\n"
"background:rgba(0,0,0,0.3);;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(1000, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("background-color:rgba(255, 0, 0,0.5);")
        self.close_button.setObjectName("close_button")
        self.min_button = QtWidgets.QPushButton(self.centralwidget)
        self.min_button.setGeometry(QtCore.QRect(960, 10, 31, 31))
        self.min_button.setStyleSheet("background-color:rgba(0, 0, 255,0.5);\n"
"")
        self.min_button.setObjectName("min_button")
        self.download_frame = QtWidgets.QFrame(self.centralwidget)
        self.download_frame.setGeometry(QtCore.QRect(60, 790, 920, 590))
        self.download_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.download_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.download_frame.setObjectName("download_frame")
        self.display_table = QtWidgets.QTableWidget(self.download_frame)
        self.display_table.setEnabled(True)
        self.display_table.setGeometry(QtCore.QRect(20, 130, 881, 431))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.display_table.setFont(font)
        self.display_table.setAutoFillBackground(False)
        self.display_table.setStyleSheet("")
        self.display_table.setAutoScroll(True)
        self.display_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.display_table.setAlternatingRowColors(False)
        self.display_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.display_table.setShowGrid(False)
        self.display_table.setGridStyle(QtCore.Qt.SolidLine)
        self.display_table.setObjectName("display_table")
        self.display_table.setColumnCount(6)
        self.display_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(5, item)
        self.display_table.horizontalHeader().setVisible(True)
        self.display_table.horizontalHeader().setCascadingSectionResizes(False)
        self.display_table.horizontalHeader().setHighlightSections(False)
        self.display_table.horizontalHeader().setSortIndicatorShown(False)
        self.display_table.verticalHeader().setVisible(False)
        self.display_table.verticalHeader().setDefaultSectionSize(37)
        self.display_table.verticalHeader().setHighlightSections(True)
        self.display_table.verticalHeader().setSortIndicatorShown(False)
        self.display_table.verticalHeader().setStretchLastSection(False)
        self.download_button = QtWidgets.QPushButton(self.download_frame)
        self.download_button.setGeometry(QtCore.QRect(770, 20, 93, 41))
        self.download_button.setStyleSheet("")
        self.download_button.setObjectName("download_button")
        self.pushButton = QtWidgets.QPushButton(self.download_frame)
        self.pushButton.setGeometry(QtCore.QRect(640, 20, 93, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.url_edit = QtWidgets.QLineEdit(self.download_frame)
        self.url_edit.setGeometry(QtCore.QRect(100, 20, 511, 41))
        self.url_edit.setStyleSheet("")
        self.url_edit.setObjectName("url_edit")
        self.all_select_check_button = QtWidgets.QCheckBox(self.download_frame)
        self.all_select_check_button.setGeometry(QtCore.QRect(30, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.all_select_check_button.setFont(font)
        self.all_select_check_button.setMouseTracking(True)
        self.all_select_check_button.setToolTip("")
        self.all_select_check_button.setStyleSheet("")
        self.all_select_check_button.setObjectName("all_select_check_button")
        self.before_button = QtWidgets.QPushButton(self.centralwidget)
        self.before_button.setGeometry(QtCore.QRect(-80, 60, 170, 91))
        self.before_button.setObjectName("before_button")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(970, 60, 171, 91))
        self.next_button.setStyleSheet("")
        self.next_button.setObjectName("next_button")
        self.search_frame = QtWidgets.QFrame(self.centralwidget)
        self.search_frame.setGeometry(QtCore.QRect(90, 50, 870, 570))
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.search_input = QtWidgets.QLineEdit(self.search_frame)
        self.search_input.setGeometry(QtCore.QRect(70, 10, 551, 51))
        self.search_input.setObjectName("search_input")
        self.search_button = QtWidgets.QPushButton(self.search_frame)
        self.search_button.setGeometry(QtCore.QRect(690, 10, 121, 51))
        self.search_button.setObjectName("search_button")
        self.page_label = QtWidgets.QLabel(self.search_frame)
        self.page_label.setGeometry(QtCore.QRect(420, 520, 72, 21))
        self.page_label.setObjectName("page_label")
        self.tableWidget = QtWidgets.QTableWidget(self.search_frame)
        self.tableWidget.setGeometry(QtCore.QRect(60, 90, 770, 420))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(70)
        self.fanju_button = QtWidgets.QPushButton(self.search_frame)
        self.fanju_button.setGeometry(QtCore.QRect(-40, 160, 93, 28))
        self.fanju_button.setObjectName("fanju_button")
        self.video_button = QtWidgets.QPushButton(self.search_frame)
        self.video_button.setGeometry(QtCore.QRect(-40, 120, 93, 28))
        self.video_button.setObjectName("video_button")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.search_frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(880, 90, 771, 421))
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(70)
        self.before_page_button = QtWidgets.QPushButton(self.search_frame)
        self.before_page_button.setGeometry(QtCore.QRect(260, 520, 93, 28))
        self.before_page_button.setObjectName("before_page_button")
        self.next_page_button = QtWidgets.QPushButton(self.search_frame)
        self.next_page_button.setGeometry(QtCore.QRect(540, 520, 93, 28))
        self.next_page_button.setObjectName("next_page_button")
        self.total_page_label = QtWidgets.QLabel(self.search_frame)
        self.total_page_label.setGeometry(QtCore.QRect(420, 540, 72, 21))
        self.total_page_label.setText("")
        self.total_page_label.setObjectName("total_page_label")
        self.setting_frame = QtWidgets.QFrame(self.centralwidget)
        self.setting_frame.setGeometry(QtCore.QRect(60, 1520, 920, 590))
        self.setting_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setting_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setting_frame.setObjectName("setting_frame")
        self.pushButton_3 = QtWidgets.QPushButton(self.setting_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 190, 421, 211))
        self.pushButton_3.setObjectName("pushButton_3")
        self.download_frame.raise_()
        self.close_button.raise_()
        self.min_button.raise_()
        self.before_button.raise_()
        self.next_button.raise_()
        self.search_frame.raise_()
        self.setting_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.jiexi)
        self.all_select_check_button.stateChanged['int'].connect(MainWindow.all_select)
        self.download_button.clicked.connect(MainWindow.download)
        self.min_button.clicked.connect(MainWindow.min_click)
        self.close_button.clicked.connect(MainWindow.close_click)
        self.next_button.clicked.connect(MainWindow.next_page)
        self.before_button.clicked.connect(MainWindow.before_page)
        self.search_button.clicked.connect(MainWindow.start_search)
        self.video_button.clicked.connect(MainWindow.view_search_video)
        self.fanju_button.clicked.connect(MainWindow.view_search_fanju)
        self.before_page_button.clicked.connect(MainWindow.search_before_page)
        self.next_page_button.clicked.connect(MainWindow.search_next_page)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bilibili-download"))
        self.close_button.setText(_translate("MainWindow", "×"))
        self.min_button.setText(_translate("MainWindow", "-"))
        self.display_table.setSortingEnabled(False)
        item = self.display_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "选择"))
        item = self.display_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "标题"))
        item = self.display_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时长"))
        item = self.display_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "大小"))
        item = self.display_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "进度"))
        item = self.display_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "段落"))
        self.download_button.setText(_translate("MainWindow", "下载"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.all_select_check_button.setText(_translate("MainWindow", "我全都要！"))
        self.before_button.setText(_translate("MainWindow", "   <"))
        self.next_button.setText(_translate("MainWindow", ">   "))
        self.search_button.setText(_translate("MainWindow", "搜索"))
        self.page_label.setText(_translate("MainWindow", "第1页"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "标题"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "简介"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时长"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "发布日期"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "up主"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "播放量"))
        self.fanju_button.setText(_translate("MainWindow", "    番剧"))
        self.video_button.setText(_translate("MainWindow", "    视频"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "标题"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "简介"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "发布日期"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "当前集数/总集数"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "是否完结"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "播放量"))
        self.before_page_button.setText(_translate("MainWindow", "上一页"))
        self.next_page_button.setText(_translate("MainWindow", "下一页"))
        self.pushButton_3.setText(_translate("MainWindow", "setting"))

