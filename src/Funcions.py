from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings

from PySide6.QtCore import QSettings
from PySide6.QtGui import QFont, QFontDatabase

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow
        self.ui = MainWindow.ui

        # apply font
        self.loadProductSansFont()
        # init app theme
        self.initializeAppTheme()

        self.connectMenuButtons()

    # initialize app theme
    def initializeAppTheme(self):
        """Initialize the application theme from settings"""
        settings = QSettings()
        current_theme = settings.value("THEME")
    
        self.populateThemeList(current_theme)
        
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)

    # CONNECT MENU BUTTONS

    def connectMenuButtons(self):
        self.ui.pengaturanTombol.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.informasiTombol.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.bantuanTombol.clicked.connect(lambda: self.ui.centerMenu.expandMenu())

        self.ui.keluarMenuTombol.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())

    def populateThemeList(self, current_theme):
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)

            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count)

    def changeAppTheme(self):
        
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:

            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    def loadProductSansFont(self):
        font_id = QFontDatabase.addApplicationFont("./fonts/google-sans-cufonfonts/GoogleSans-Regular.ttf")

        if font_id == -1:
            print("failed to load Product Sans Font")

        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            product_sans = QFont(font_family[0])
        else:
            product_sans = QFont("Sans Serif")

        self.main.setFont(product_sans)



