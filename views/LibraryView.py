
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QWidget, QMainWindow, QFormLayout, QAbstractItemView
                            , QLineEdit, QPushButton, QSpinBox, QTableWidget, QBoxLayout, QHeaderView, QMenuBar, QMenu)
from qt_material import apply_stylesheet
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from AppLication import app

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("مدیریت کتابخانه")
        self.resize(1000, 500)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        #self.Set_Menu_bar()

        self.MainWindow_Layout = QHBoxLayout()
        self.MainWindow_Layout.setStretch(0,1)
        self.MainWindow_Layout.setStretch(1,0)
        self.Right_Layout = QFormLayout()
        
        self.Left_Layout = QVBoxLayout()

        self.MainWidget = QWidget()
        self.MainWidget.setLayout(self.MainWindow_Layout)
        self.setCentralWidget(self.MainWidget)

        self.MainWindow_Layout.addLayout(self.Right_Layout, 0)
        self.MainWindow_Layout.addLayout(self.Left_Layout, 1)
        
        self.txtBookName = QLineEdit()
        self.txtBookAuthor = QLineEdit()
        self.txtBookYear = QSpinBox()
        self.txtBookYear.setRange(1300, 1500)
        self.txtBookIsbn = QLineEdit()
        self.btnSave = QPushButton("ثبت")
        self.btnExcel = QPushButton("EXCEL")

        self.Right_Layout.addRow("نام کتاب", self.txtBookName)
        self.Right_Layout.addRow("نویسنده", self.txtBookAuthor)
        self.Right_Layout.addRow("سال چاپ", self.txtBookYear)
        self.Right_Layout.addRow("کد کتاب(isbn)", self.txtBookIsbn)
        self.Right_Layout.addRow("", self.btnSave)
        self.Right_Layout.addRow("", self.btnExcel)

        self.txtSearch = QLineEdit()
        self.txtSearch.setMinimumWidth = 600
        self.txtSearch.setPlaceholderText("جستجو")

        self.Table = QTableWidget()
        self.Table.setColumnCount(8)

        self.Table.setHorizontalHeaderLabels(["کد","نام کتاب","نویسنده","سال چاپ","کد کتاب","ویرایش","حذف","چاپ"])
        self.Table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        header = self.Table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        


        self.Left_Layout.addWidget(self.txtSearch)
        self.Left_Layout.addWidget(self.Table)

    # def Set_Menu_bar(self):

    #     self.menu = self.menuBar()
    #     self.menu_parent = self.menu.addMenu("قالب")
    
    #     for item in app.Theme_List:
    #         action = QAction(item, self)
    #         action.triggered.connect(lambda checked, param=item: self.menu12(param))

    #         self.menu_parent.addAction(action)

    #     #self.menu_parent.addMenu(self.Template_Menu)

    # def menu12(self, item):
    #     print(item)
