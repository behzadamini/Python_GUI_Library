from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys


class App():
    def __init__(self):
        self.App = QApplication(sys.argv)
        self.Theme_List =  [
            'dark_amber.xml',
            'dark_blue.xml',
            'dark_cyan.xml',
            'dark_lightgreen.xml',
            'dark_pink.xml',
            'dark_purple.xml',
            'dark_red.xml',
            'dark_teal.xml',
            'dark_yellow.xml',
            'light_amber.xml',
            'light_blue.xml',
            'light_cyan.xml',
            'light_cyan_500.xml',
            'light_lightgreen.xml',
            'light_pink.xml',
            'light_purple.xml',
            'light_red.xml',
            'light_teal.xml',
            'light_yellow.xml']

        self.Theme_List_Index = 0
        self.Theme_Current = ""
        #self.App_Theme_Change()
    

    def App_Theme_Change(self, item=""):                

        if item == "":
            apply_stylesheet(self.App, theme= self.Theme_List[self.Theme_List_Index])
            extra = {'font_family': 'Shabnam', 'font_size':'14px'}
            apply_stylesheet(self.App, self.Theme_List[self.Theme_List_Index], invert_secondary=True, extra=extra)  
        
        else:
            apply_stylesheet(self.App, theme= item)
            extra = {'font_family': 'Shabnam', 'font_size':'14px'}
            apply_stylesheet(self.App, item, invert_secondary=True, extra=extra)  

app = App()