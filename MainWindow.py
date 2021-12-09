# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import Resources_rc

class Ui_C42_Toollist(object):
    def setupUi(self, C42_Toollist):
        if not C42_Toollist.objectName():
            C42_Toollist.setObjectName(u"C42_Toollist")
        C42_Toollist.resize(560, 145)
        C42_Toollist.setMinimumSize(QSize(560, 110))
        C42_Toollist.setMaximumSize(QSize(560, 145))
        C42_Toollist.setContextMenuPolicy(Qt.ActionsContextMenu)
        icon = QIcon()
        icon.addFile(u":/newPrefix/data/Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        C42_Toollist.setWindowIcon(icon)
        C42_Toollist.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #232430;\n"
"	color: #000000;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: #232430;\n"
"	color: #c1c1c1;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #ff9c2b;\n"
"	color: #000000;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-color: #000000;\n"
"	padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #ff9c2b;\n"
"	color: #000000;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-color: #000000;\n"
"	padd"
                        "ing: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #38394e;\n"
"	color: #c1c1c1;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #4a4c68;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView-----*/\n"
"QTableView, \n"
"QHeaderView, \n"
"QTableView::item \n"
"{\n"
"	background-color: #232430;\n"
"	color: #c1c1c1;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #41424e;\n"
"    color: #c1c1c1;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #232430;\n"
"	border: 1px solid #37384d;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator{\n"
"	background-color: #1d1d28;\n"
"	border: 1px solid #37384d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator:checked{\n"
"	image:url(\"./ressource"
                        "s/check.png\"); /*To replace*/\n"
"	background-color: #1d1d28;\n"
"\n"
"}\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabWidget::pane \n"
"{ \n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"    left: 5px; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab \n"
"{\n"
"    color: #c1c1c1;\n"
"    min-width: 1px;\n"
"	padding-left: 25px;\n"
"	margin-left:-22px;\n"
"    height: 28px;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"    color: #c1c1c1;\n"
"	font-weight: bold;\n"
"    height: 28px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!first \n"
"{\n"
"    margin-left: -20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover \n"
"{\n"
"    color: #DDD;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"	min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"	min-height: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"")
        C42_Toollist.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(C42_Toollist)
        self.centralwidget.setObjectName(u"centralwidget")
        self.OriginalPath = QLineEdit(self.centralwidget)
        self.OriginalPath.setObjectName(u"OriginalPath")
        self.OriginalPath.setEnabled(True)
        self.OriginalPath.setGeometry(QRect(10, 10, 441, 31))
        self.OriginalPath.setCursor(QCursor(Qt.ArrowCursor))
        self.OriginalPath.setDragEnabled(True)
        self.OriginalPath.setReadOnly(True)
        self.BTN_Laden = QPushButton(self.centralwidget)
        self.BTN_Laden.setObjectName(u"BTN_Laden")
        self.BTN_Laden.setGeometry(QRect(460, 10, 91, 71))
        self.BTN_Laden.setCursor(QCursor(Qt.PointingHandCursor))
        self.FinalPath = QLineEdit(self.centralwidget)
        self.FinalPath.setObjectName(u"FinalPath")
        self.FinalPath.setGeometry(QRect(10, 50, 441, 31))
        self.FinalPath.setCursor(QCursor(Qt.ArrowCursor))
        self.FinalPath.setDragEnabled(True)
        self.FinalPath.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(255, 125, 50, 15))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.BTN_umwandeln = QPushButton(self.centralwidget)
        self.BTN_umwandeln.setObjectName(u"BTN_umwandeln")
        self.BTN_umwandeln.setGeometry(QRect(230, 90, 100, 30))
        self.BTN_umwandeln.setCursor(QCursor(Qt.PointingHandCursor))
        C42_Toollist.setCentralWidget(self.centralwidget)

        self.retranslateUi(C42_Toollist)

        QMetaObject.connectSlotsByName(C42_Toollist)
    # setupUi

    def retranslateUi(self, C42_Toollist):
        C42_Toollist.setWindowTitle(QCoreApplication.translate("C42_Toollist", u"C42_Toollist", None))
#if QT_CONFIG(tooltip)
        C42_Toollist.setToolTip(QCoreApplication.translate("C42_Toollist", u"C42_Toollist", None))
#endif // QT_CONFIG(tooltip)
        self.OriginalPath.setText("")
        self.OriginalPath.setPlaceholderText(QCoreApplication.translate("C42_Toollist", u"C:\\", None))
        self.BTN_Laden.setText(QCoreApplication.translate("C42_Toollist", u"Datei Laden", None))
        self.FinalPath.setText("")
        self.FinalPath.setPlaceholderText(QCoreApplication.translate("C42_Toollist", u"C:\\", None))
        self.label.setText(QCoreApplication.translate("C42_Toollist", u"V0.1", None))
        self.BTN_umwandeln.setText(QCoreApplication.translate("C42_Toollist", u"Umwandeln", None))
    # retranslateUi

