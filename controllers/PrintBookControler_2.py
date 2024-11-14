
from PyQt6.QtPrintSupport import  QPrintDialog
from PyQt6.QtGui import QTextDocument, QTextOption
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtCore import Qt
import datetime



class PrintControler2():

    @staticmethod
    def print(data):
            
        # اطلاعات برای جایگزینی در قالب HTML
        # context = {
        #     "title": "گزارش روزانه",
        #     "main_text": "این یک گزارش نمونه است که در آن متن‌های مختلف قرار داده شده است.",
        #     "date": datetime.datetime.now().strftime("%Y/%m/%d")
        # }

        # خواندن قالب HTML و جایگزینی مکان‌نگه‌دارها با مقادیر
        #with open("C:/Users/pc/Desktop/Library Management/PrintTemplayte/template.html", "r", encoding="utf-8") as file:
        with open(r"controllers\PrintTemplayte\template.html", "r", encoding="utf-8") as file:
            html_content = file.read()
            for key, value in data.items():
                html_content = html_content.replace(f"{{{{ {key} }}}}", value)

        # ایجاد سند و بارگذاری محتوای HTML
        
        text_option = QTextOption()
        text_option.setTextDirection(Qt.LayoutDirection.RightToLeft)
        
        document = QTextDocument()
        document.setDefaultTextOption(text_option)
        document.setHtml(html_content)

        

        # ایجاد پرینتر و باز کردن دیالوگ پرینت
        printer = QPrinter()
        print_dialog = QPrintDialog(printer)
        if print_dialog.exec() == QPrintDialog.DialogCode.Accepted:
            document.print(printer)





