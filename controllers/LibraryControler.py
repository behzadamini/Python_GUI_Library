import sys
from views.LibraryView import MainForm
from models.LibraryModel import Repository, Library
from PyQt6.QtWidgets import QApplication,QTableWidgetItem, QPushButton, QMessageBox
from qt_material import apply_stylesheet


class LibraryControler():
    def __init__(self):
        self.MainForm = MainForm()
        self.MainForm.btnSave.clicked.connect(self.save)
        self.MainForm.txtSearch.textChanged.connect(self.TableSearch)
        self.Repository = Repository()
        self.TableFill()

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
            self.MainForm.Table.setItem(row_position, 0, QTableWidgetItem( item["bk_id"] ))
            self.MainForm.Table.setItem(row_position, 1, QTableWidgetItem( item["bk_title"] ))
            self.MainForm.Table.setItem(row_position, 2, QTableWidgetItem( item["bk_author"] ))
            self.MainForm.Table.setItem(row_position, 3, QTableWidgetItem( item["bk_year"] ))
            self.MainForm.Table.setItem(row_position, 4, QTableWidgetItem( item["bk_isbn"] ))

            self.btnEdit = QPushButton("ویرایش")
            self.btnDelete = QPushButton("حذف")

            self.btnEdit.clicked.connect(self.TabeleRowEditClicked)
            self.btnDelete.clicked.connect(self.TabeleDeleteClicked)

            self.MainForm.Table.setCellWidget(row_position, 5, self.btnEdit)
            self.MainForm.Table.setCellWidget(row_position, 6, self.btnDelete)        

    def TabeleRowEditClicked(self):
        SelectedItemIndex = self.MainForm.Table.currentRow()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("آیا میخواهید سطر انتخاب شده را ویرایش کنید؟")
        msg.setWindowTitle("ویرایش اطلاعات")
        
        cancel_button = msg.addButton("نه اشتباه کردم", QMessageBox.ButtonRole.RejectRole)  # دکمه "Abort"   
        ok_button = msg.addButton("بله ویرایش کن", QMessageBox.ButtonRole.AcceptRole)  # دکمه "Proceed"

        msg.exec()

        if msg.clickedButton() == ok_button:
            print("222222")
        
    def TabeleDeleteClicked(self):
        SelectedItemIndex = self.MainForm.Table.currentRow()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("آیا میخواهید سطر انتخاب شده را حذف کنید؟")
        msg.setWindowTitle("حذف اطلاعات")
        
        cancel_button = msg.addButton("نه اشتباه کردم", QMessageBox.ButtonRole.RejectRole)  # دکمه "Abort"           
        ok_button = msg.addButton("بله حذف کن کن", QMessageBox.ButtonRole.AcceptRole)  # دکمه "Proceed"

        msg.exec()

        if msg.clickedButton() == ok_button:
            self.Repository.delete(SelectedItemIndex)
            self.MainForm.Table.removeRow(SelectedItemIndex)

    def run(self):
        self.MainForm.show()