
from controllers.LibraryControler import LibraryControler
from qt_material import apply_stylesheet
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

apply_stylesheet(app, theme='dark_yellow.xml')
extra = {'font_family': 'Shabnam', 'font_size':'14px'}
apply_stylesheet(app, 'dark_yellow.xml', invert_secondary=True, extra=extra)    


lib = LibraryControler()
lib.run()




sys.exit(app.exec())



