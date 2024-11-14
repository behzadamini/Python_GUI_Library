import sys
import pandas as pd
from views.LibraryView import MainForm
from models.LibraryModel import Repository, Library
from PyQt6.QtWidgets import QApplication,QTableWidgetItem, QPushButton, QMessageBox
from PyQt6.QtGui import QAction
from qt_material import apply_stylesheet
from AppLication import app
from controllers.PrintBookControler_1 import PrintControler1
from controllers.PrintBookControler_2 import PrintControler2




class LibraryControler():
    def __init__(self):
        self.MainForm = MainForm()
        self.MainForm.btnSave.clicked.connect(self.save)
        self.MainForm.txtSearch.textChanged.connect(self.TableSearch)
        self.MainForm.btnExcel.clicked.connect(self.export_to_excel)
        self.Repository = Repository()
        self.TableFill()
        self.Load_Menu()
        

    def Load_Menu(self):
        self.main_menu = self.MainForm.menuBar()
        self.menu1 = self.main_menu.addMenu("قالب")

        for item in app.Theme_List:
            action = QAction(item, self.main_menu)
            action.triggered.connect(lambda checked, param = item: self.Theme(param))
            self.menu1.addAction(action)

        self.Theme("")
        
    def Theme(self, item):
        app.App_Theme_Change(item)

    def TableFill(self):

        AllRecord = self.Repository.SelectAll(Library)
        for item in AllRecord:
            self.TableAddItem([{
                "bk_id": item.bk_id,
                "bk_title":item.bk_title,
                "bk_author":item.bk_author,
                "bk_year": item.bk_year,
                "bk_isbn": item.bk_isbn}])

    def TableClear(self):
        self.MainForm.Table.setRowCount(0)
            
        
    def TableSearch(self):
        TableRowCount = self.MainForm.Table.rowCount()

        if TableRowCount == 0:
            return
        
        if self.MainForm.txtSearch.text() == "":
            if TableRowCount != self.MainForm.Table.rowCount():
                self.TableFill()
                return
        
        result = self.Repository.Search(self.MainForm.txtSearch.text())
        if len(result) > 0:
            self.TableClear()
            
            for item in result:
                self.TableAddItem([{
                    "bk_id": item.bk_id,
                    "bk_title" : item.bk_title,
                    "bk_author" : item.bk_author,
                    "bk_year" : item.bk_year,
                    "bk_isbn" : item.bk_isbn
                }])      
        else:
            pass
    
    
    def save(self):
        book = [{
            "bk_title" : self.MainForm.txtBookName.text(),
            "bk_author" : self.MainForm.txtBookAuthor.text(),
            "bk_year" : self.MainForm.txtBookYear.text(),
            "bk_isbn" : self.MainForm.txtBookIsbn.text()
        }]
        Insert = self.Repository.add(Library(book[0]["bk_title"],book[0]["bk_author"],book[0]["bk_year"],book[0]["bk_isbn"]))        
        book[0]["bk_id"] = Insert
        self.TableAddItem(book)

    def TableAddItem(self, book):

        for item in book:
            row_position = 0  # self.MainForm.Table.rowCount()
            self.MainForm.Table.insertRow(row_position)
            self.MainForm.Table.setItem(row_position, 0, QTableWidgetItem( str(item["bk_id"]) ))
            self.MainForm.Table.setItem(row_position, 1, QTableWidgetItem( item["bk_title"] ))
            self.MainForm.Table.setItem(row_position, 2, QTableWidgetItem( item["bk_author"] ))
            self.MainForm.Table.setItem(row_position, 3, QTableWidgetItem( item["bk_year"] ))
            self.MainForm.Table.setItem(row_position, 4, QTableWidgetItem( item["bk_isbn"] ))

            self.btnEdit = QPushButton("ویرایش")
            self.btnDelete = QPushButton("حذف")
            self.btnPrint = QPushButton("چاپ")

            self.btnEdit.clicked.connect(self.TabeleRowEditClicked)
            self.btnDelete.clicked.connect(self.TabeleDeleteClicked)
            self.btnPrint.clicked.connect(self.print_A6)

            self.MainForm.Table.setCellWidget(row_position, 5, self.btnEdit)
            self.MainForm.Table.setCellWidget(row_position, 6, self.btnDelete)        
            self.MainForm.Table.setCellWidget(row_position, 7, self.btnPrint)        

    def TabeleRowEditClicked(self):
        button = self.MainForm.sender()
        if button:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("آیا میخواهید سطر انتخاب شده را ویرایش کنید؟")
            msg.setWindowTitle("ویرایش اطلاعات")
            
            cancel_button = msg.addButton("نه اشتباه کردم", QMessageBox.ButtonRole.RejectRole)  # دکمه "Abort"   
            ok_button = msg.addButton("بله ویرایش کن", QMessageBox.ButtonRole.AcceptRole)  # دکمه "Proceed"

            msg.exec()

            if msg.clickedButton() == ok_button:
                row = self.MainForm.Table.indexAt(button.pos()).row()
                id = self.MainForm.Table.item(row, 0).text()
                title = self.MainForm.Table.item(row, 1).text()
                author = self.MainForm.Table.item(row, 2).text()
                year = self.MainForm.Table.item(row, 3).text()
                isbn = self.MainForm.Table.item(row, 4).text()

                self.Repository.update(id, Library(Title=title, Author=author, Year=year, Isbn=isbn))
        
    def TabeleDeleteClicked(self):
        button = self.MainForm.sender()
        if button:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("آیا میخواهید سطر انتخاب شده را حذف کنید؟")
            msg.setWindowTitle("حذف اطلاعات")

            cancel_button = msg.addButton("نه اشتباه کردم", QMessageBox.ButtonRole.RejectRole)  # دکمه "Abort"           
            ok_button = msg.addButton("بله حذف کن کن", QMessageBox.ButtonRole.AcceptRole)  # دکمه "Proceed"

            msg.exec()

            if msg.clickedButton() == ok_button:
                row = self.MainForm.Table.indexAt(button.pos()).row()
                id = self.MainForm.Table.item(row, 0).text()

                self.Repository.delete(int(id))

                self.MainForm.Table.removeRow(row)

    def export_to_excel(self):
        path, _ = QFileDialog.getSaveFileName(self.MainForm.Table, "Save File", "", "Excel Files (*.xlsx)")
        if path:
        # استخراج داده‌ها از QTableWidget
            data = []
            for row in range(self.MainForm.Table.rowCount()):
                row_data = []
                for column in range(self.MainForm.Table.columnCount()):
                    if column < 5:
                        item = self.MainForm.Table.item(row, column)
                        row_data.append(item.text() if item else "")
                data.append(row_data)

            # ساخت DataFrame و ذخیره به اکسل
            df = pd.DataFrame(data, columns=['کد', 'نام کتاب', 'نویسنده', 'سال چاپ', ' کد isbn'])
            df.to_excel(path, index=False)

    def print_A6(self):
        row = self.MainForm.Table.indexAt(self.MainForm.sender().pos()).row()
        data = {
        "کد کتاب": self.MainForm.Table.item(row, 0).text(),
        "نام کتاب": self.MainForm.Table.item(row, 1).text(),
        "نویسنده": self.MainForm.Table.item(row, 2).text(),
        "سال چاپ": self.MainForm.Table.item(row, 3).text(),
        "کد ISBN": self.MainForm.Table.item(row, 4).text()
        }

        PrintControler1.print(self.MainForm.Table ,data)
        PrintControler2.print(data)

    def run(self):
        self.MainForm.show()