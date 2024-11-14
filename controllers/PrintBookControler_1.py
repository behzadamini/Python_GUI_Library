
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QAction, QPainter, QPageSize, QFont, QPageLayout, QTextOption
from PyQt6.QtCore import QPoint, QMarginsF, QRect, Qt


class PrintControler1():

    @staticmethod
    def print(parent_widget, data):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        printer.setPageSize(QPageSize(QPageSize.PageSizeId.A6))
        printer.setPageOrientation(QPageLayout.Orientation.Landscape)
        printer.setPageMargins(QMarginsF(20, 30, 20, 20))  # حاشیه‌ها برای فضای بهتر

        # نمایش گفتگوی چاپ
        dialog = QPrintDialog(printer, parent_widget)
        if dialog.exec() != QPrintDialog.DialogCode.Accepted:
            return

        painter = QPainter(printer)

        # تنظیمات فونت
        font = QFont("B Mitra", 14)  # اندازه فونت کوچکتر
        painter.setFont(font)

        # رسم عنوان فارسی
        painter.drawText(0, 0, 2000, 300, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, "مدیریت کتابخانه")

        # تنظیم فاصله بین خطوط و مکان شروع
        y_offset = 200  # شروع مختصات y
        line_height = 200  # ارتفاع مناسب برای هر خط
        for key, value in data.items():
            painter.drawText(100, y_offset, 1500, line_height, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, f"{key}: {value}")
            y_offset += line_height  # افزایش y برای هر خط جدید

        painter.end()