import os
import io
import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import webbrowser

# تابع برای اصلاح و راست‌چین کردن متن فارسی
def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

def generate_and_show_library_report(books, filename="library_report.pdf"):
    # ثبت فونت فارسی
    font_path = os.path.join(os.path.dirname(__file__), 'Shabnam-FD.ttf')
    pdfmetrics.registerFont(TTFont('Shabnam FD', font_path))
    
    # ایجاد فایل PDF
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # تنظیمات ابتدایی صفحه
    c.setFont("Shabnam FD", 16)
    c.drawRightString(500, height - 50, reshape_text("گزارش کتابخانه"))

    # تنظیم فونت و داده‌های جدول
    c.setFont("Shabnam FD", 12)
    table_data = [
        [reshape_text("عنوان"), reshape_text("نویسنده"), reshape_text("سال انتشار"), reshape_text("شماره کتاب")]
    ] + [[reshape_text(cell) for cell in row] for row in books]

    # ایجاد جدول با داده‌ها
    table = Table(table_data, colWidths=[150, 150, 80, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Shabnam FD'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # اضافه کردن جدول به صفحه
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, height - 200)

    # ذخیره فایل PDF
    c.save()
    print(f"گزارش با نام '{filename}' ساخته و ذخیره شد.")

    # نمایش فایل PDF
    webbrowser.open(filename)

# داده‌های آزمایشی کتاب‌ها به زبان فارسی
books = [
    ["بوف کور", "AصادقA هدایتA", "۱۹۳۷", "۱۲۳"],
    ["کلیدر", "محمود دولت‌آبادی", "۱۹۸۴", "۴۵۶"],
    ["سمفونی مردگان", "عباس معروفی", "۱۹۸۹", "۷۸۹"],
]

# ایجاد و نمایش گزارش
generate_and_show_library_report(books)
