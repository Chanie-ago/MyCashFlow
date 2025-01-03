# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 518)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(821, 471))
        self.hboxLayout = QHBoxLayout(self.centralwidget)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.hboxLayout.setContentsMargins(10, 10, 10, 10)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 0, 5)
        self.menuTombol = QPushButton(self.widget)
        self.menuTombol.setObjectName(u"menuTombol")
        self.menuTombol.setMinimumSize(QSize(35, 30))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuTombol.setIcon(icon)

        self.verticalLayout_3.addWidget(self.menuTombol, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.halamanTombol = QPushButton(self.widget_2)
        self.halamanTombol.setObjectName(u"halamanTombol")
        font1 = QFont()
        font1.setBold(False)
        self.halamanTombol.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.halamanTombol.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.halamanTombol)

        self.pemasukanTombol = QPushButton(self.widget_2)
        self.pemasukanTombol.setObjectName(u"pemasukanTombol")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/plus-square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pemasukanTombol.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pemasukanTombol)

        self.pengeluaranTombol = QPushButton(self.widget_2)
        self.pengeluaranTombol.setObjectName(u"pengeluaranTombol")
        font2 = QFont()
        font2.setPointSize(9)
        self.pengeluaranTombol.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/minus-square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pengeluaranTombol.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pengeluaranTombol)

        self.laporanTombol = QPushButton(self.widget_2)
        self.laporanTombol.setObjectName(u"laporanTombol")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/print.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.laporanTombol.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.laporanTombol)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.pengaturanTombol = QPushButton(self.widget_3)
        self.pengaturanTombol.setObjectName(u"pengaturanTombol")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pengaturanTombol.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.pengaturanTombol)

        self.informasiTombol = QPushButton(self.widget_3)
        self.informasiTombol.setObjectName(u"informasiTombol")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.informasiTombol.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.informasiTombol)

        self.bantuanTombol = QPushButton(self.widget_3)
        self.bantuanTombol.setObjectName(u"bantuanTombol")
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_solid/icons/font_awesome/solid/circle-question.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bantuanTombol.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.bantuanTombol)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.hboxLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.keluarMenuTombol = QPushButton(self.widget_4)
        self.keluarMenuTombol.setObjectName(u"keluarMenuTombol")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.keluarMenuTombol.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.keluarMenuTombol)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_6 = QVBoxLayout(self.settingPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.widget_5 = QWidget(self.settingPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame = QFrame(self.widget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.themeList = QComboBox(self.frame)
        self.themeList.setObjectName(u"themeList")

        self.horizontalLayout_3.addWidget(self.themeList)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.widget_5, 0, Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.centerMenuPages.addWidget(self.settingPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textBrowser = QTextBrowser(self.helpPage)
        self.textBrowser.setObjectName(u"textBrowser")
        font3 = QFont()
        font3.setKerning(True)
        self.textBrowser.setFont(font3)

        self.verticalLayout_9.addWidget(self.textBrowser, 0, Qt.AlignHCenter)

        self.centerMenuPages.addWidget(self.helpPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_8 = QVBoxLayout(self.informationPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.textBrowser_2 = QTextBrowser(self.informationPage)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_8.addWidget(self.textBrowser_2)

        self.centerMenuPages.addWidget(self.informationPage)

        self.verticalLayout_5.addWidget(self.centerMenuPages)


        self.hboxLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.mainBody)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_6 = QHBoxLayout(self.header)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, -1)
        self.tittleTxt = QLabel(self.header)
        self.tittleTxt.setObjectName(u"tittleTxt")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.tittleTxt.setFont(font4)

        self.horizontalLayout_6.addWidget(self.tittleTxt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 5)
        self.minimizeBtn = QPushButton(self.frame_4)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon9)

        self.horizontalLayout_7.addWidget(self.minimizeBtn, 0, Qt.AlignRight)

        self.restoreBtn = QPushButton(self.frame_4)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon10)

        self.horizontalLayout_7.addWidget(self.restoreBtn, 0, Qt.AlignRight)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(28, 24))
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon11)

        self.horizontalLayout_7.addWidget(self.closeBtn, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.frame_4, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.header, 0, Qt.AlignTop)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        self.horizontalLayout_8 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.verticalLayout_11 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.mainPages = QCustomQStackedWidget(self.mainPagesCont)
        self.mainPages.setObjectName(u"mainPages")
        self.menuHalaman = QWidget()
        self.menuHalaman.setObjectName(u"menuHalaman")
        self.horizontalLayout_9 = QHBoxLayout(self.menuHalaman)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.totalPemasukan = QWidget(self.menuHalaman)
        self.totalPemasukan.setObjectName(u"totalPemasukan")
        self.verticalLayout_12 = QVBoxLayout(self.totalPemasukan)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.totalPemasukan)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setBold(True)
        self.label_5.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_10 = QWidget(self.totalPemasukan)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_22 = QVBoxLayout(self.widget_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.incomeDateEditFilter = QDateEdit(self.widget_10)
        self.incomeDateEditFilter.setObjectName(u"incomeDateEditFilter")

        self.verticalLayout_22.addWidget(self.incomeDateEditFilter)

        self.incomeRefreshButton = QPushButton(self.widget_10)
        self.incomeRefreshButton.setObjectName(u"incomeRefreshButton")
        self.incomeRefreshButton.setFont(font5)

        self.verticalLayout_22.addWidget(self.incomeRefreshButton)

        self.tableWidget = QTableWidget(self.widget_10)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_22.addWidget(self.tableWidget)

        self.labelTotalIncome = QLabel(self.widget_10)
        self.labelTotalIncome.setObjectName(u"labelTotalIncome")
        self.labelTotalIncome.setFont(font5)

        self.verticalLayout_22.addWidget(self.labelTotalIncome)

        self.labelSaldo = QLabel(self.widget_10)
        self.labelSaldo.setObjectName(u"labelSaldo")
        self.labelSaldo.setFont(font5)

        self.verticalLayout_22.addWidget(self.labelSaldo)


        self.verticalLayout_12.addWidget(self.widget_10)


        self.horizontalLayout_9.addWidget(self.totalPemasukan)

        self.widget_15 = QWidget(self.menuHalaman)
        self.widget_15.setObjectName(u"widget_15")

        self.horizontalLayout_9.addWidget(self.widget_15)

        self.totalPengeluaran = QWidget(self.menuHalaman)
        self.totalPengeluaran.setObjectName(u"totalPengeluaran")
        self.verticalLayout_21 = QVBoxLayout(self.totalPengeluaran)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_9 = QLabel(self.totalPengeluaran)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.verticalLayout_21.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_11 = QWidget(self.totalPengeluaran)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_23 = QVBoxLayout(self.widget_11)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.expenseDateEditFilter = QDateEdit(self.widget_11)
        self.expenseDateEditFilter.setObjectName(u"expenseDateEditFilter")

        self.verticalLayout_23.addWidget(self.expenseDateEditFilter)

        self.expenseRefreshButton = QPushButton(self.widget_11)
        self.expenseRefreshButton.setObjectName(u"expenseRefreshButton")
        self.expenseRefreshButton.setFont(font5)

        self.verticalLayout_23.addWidget(self.expenseRefreshButton)

        self.expenseTableWidget_2 = QTableWidget(self.widget_11)
        if (self.expenseTableWidget_2.columnCount() < 2):
            self.expenseTableWidget_2.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.expenseTableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.expenseTableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.expenseTableWidget_2.setObjectName(u"expenseTableWidget_2")

        self.verticalLayout_23.addWidget(self.expenseTableWidget_2)

        self.labelTotalExpense = QLabel(self.widget_11)
        self.labelTotalExpense.setObjectName(u"labelTotalExpense")
        self.labelTotalExpense.setFont(font5)

        self.verticalLayout_23.addWidget(self.labelTotalExpense)


        self.verticalLayout_21.addWidget(self.widget_11)


        self.horizontalLayout_9.addWidget(self.totalPengeluaran)

        self.mainPages.addWidget(self.menuHalaman)
        self.pengeluaranHalaman = QWidget()
        self.pengeluaranHalaman.setObjectName(u"pengeluaranHalaman")
        self.horizontalLayout_5 = QHBoxLayout(self.pengeluaranHalaman)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabelPengeluaran = QWidget(self.pengeluaranHalaman)
        self.tabelPengeluaran.setObjectName(u"tabelPengeluaran")
        self.verticalLayout_18 = QVBoxLayout(self.tabelPengeluaran)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_7 = QWidget(self.tabelPengeluaran)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_20 = QVBoxLayout(self.widget_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_8)

        self.refreshButton_2 = QPushButton(self.widget_7)
        self.refreshButton_2.setObjectName(u"refreshButton_2")

        self.verticalLayout_20.addWidget(self.refreshButton_2)

        self.expenseTableWidget = QTableWidget(self.widget_7)
        if (self.expenseTableWidget.columnCount() < 5):
            self.expenseTableWidget.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.expenseTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.expenseTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.expenseTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.expenseTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.expenseTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.expenseTableWidget.setObjectName(u"expenseTableWidget")
        self.expenseTableWidget.setTabletTracking(False)
        self.expenseTableWidget.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_20.addWidget(self.expenseTableWidget)

        self.deleteExpenseButton = QPushButton(self.widget_7)
        self.deleteExpenseButton.setObjectName(u"deleteExpenseButton")
        self.deleteExpenseButton.setFont(font5)

        self.verticalLayout_20.addWidget(self.deleteExpenseButton)


        self.verticalLayout_18.addWidget(self.widget_7)


        self.horizontalLayout_5.addWidget(self.tabelPengeluaran)

        self.inputKeluar = QWidget(self.pengeluaranHalaman)
        self.inputKeluar.setObjectName(u"inputKeluar")
        self.inputKeluar.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.inputKeluar)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.inputKeluar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 70))
        self.label_4.setMaximumSize(QSize(90, 70))
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.inputKeluar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.expenseDateEdit = QDateEdit(self.frame_5)
        self.expenseDateEdit.setObjectName(u"expenseDateEdit")

        self.verticalLayout_19.addWidget(self.expenseDateEdit)

        self.expenseAmountEdit = QLineEdit(self.frame_5)
        self.expenseAmountEdit.setObjectName(u"expenseAmountEdit")

        self.verticalLayout_19.addWidget(self.expenseAmountEdit)

        self.expenseDescriptionEdit = QLineEdit(self.frame_5)
        self.expenseDescriptionEdit.setObjectName(u"expenseDescriptionEdit")

        self.verticalLayout_19.addWidget(self.expenseDescriptionEdit)

        self.expenseCategoryEdit = QLineEdit(self.frame_5)
        self.expenseCategoryEdit.setObjectName(u"expenseCategoryEdit")

        self.verticalLayout_19.addWidget(self.expenseCategoryEdit)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.addExpenseButton = QPushButton(self.inputKeluar)
        self.addExpenseButton.setObjectName(u"addExpenseButton")
        self.addExpenseButton.setMinimumSize(QSize(50, 50))
        self.addExpenseButton.setMaximumSize(QSize(50, 50))
        self.addExpenseButton.setIcon(icon3)
        self.addExpenseButton.setIconSize(QSize(30, 30))

        self.verticalLayout_13.addWidget(self.addExpenseButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.inputKeluar)

        self.mainPages.addWidget(self.pengeluaranHalaman)
        self.pemasukanHalaman = QWidget()
        self.pemasukanHalaman.setObjectName(u"pemasukanHalaman")
        self.horizontalLayout = QHBoxLayout(self.pemasukanHalaman)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabelPemasukan = QWidget(self.pemasukanHalaman)
        self.tabelPemasukan.setObjectName(u"tabelPemasukan")
        self.verticalLayout_16 = QVBoxLayout(self.tabelPemasukan)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_9 = QWidget(self.tabelPemasukan)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_17 = QVBoxLayout(self.widget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)

        self.refreshButton = QPushButton(self.widget_9)
        self.refreshButton.setObjectName(u"refreshButton")

        self.verticalLayout_17.addWidget(self.refreshButton)

        self.incomeTableWidget = QTableWidget(self.widget_9)
        if (self.incomeTableWidget.columnCount() < 5):
            self.incomeTableWidget.setColumnCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.incomeTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.incomeTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.incomeTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.incomeTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.incomeTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        self.incomeTableWidget.setObjectName(u"incomeTableWidget")

        self.verticalLayout_17.addWidget(self.incomeTableWidget)

        self.deleteIncomeButton = QPushButton(self.widget_9)
        self.deleteIncomeButton.setObjectName(u"deleteIncomeButton")
        self.deleteIncomeButton.setFont(font5)

        self.verticalLayout_17.addWidget(self.deleteIncomeButton)


        self.verticalLayout_16.addWidget(self.widget_9)


        self.horizontalLayout.addWidget(self.tabelPemasukan)

        self.inputMasuk = QWidget(self.pemasukanHalaman)
        self.inputMasuk.setObjectName(u"inputMasuk")
        self.inputMasuk.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.inputMasuk)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.inputMasuk)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 70))
        self.label.setMaximumSize(QSize(80, 70))
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.inputMasuk)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.incomeDataEdit = QDateEdit(self.frame_2)
        self.incomeDataEdit.setObjectName(u"incomeDataEdit")

        self.verticalLayout_15.addWidget(self.incomeDataEdit)

        self.incomeAmountEdit = QLineEdit(self.frame_2)
        self.incomeAmountEdit.setObjectName(u"incomeAmountEdit")

        self.verticalLayout_15.addWidget(self.incomeAmountEdit)

        self.incomeCategoryEdit = QLineEdit(self.frame_2)
        self.incomeCategoryEdit.setObjectName(u"incomeCategoryEdit")

        self.verticalLayout_15.addWidget(self.incomeCategoryEdit)

        self.incomeDescriptionEdit = QLineEdit(self.frame_2)
        self.incomeDescriptionEdit.setObjectName(u"incomeDescriptionEdit")

        self.verticalLayout_15.addWidget(self.incomeDescriptionEdit)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.addIncomeButton = QPushButton(self.inputMasuk)
        self.addIncomeButton.setObjectName(u"addIncomeButton")
        self.addIncomeButton.setMinimumSize(QSize(50, 50))
        self.addIncomeButton.setMaximumSize(QSize(50, 50))
        icon12 = QIcon()
        icon12.addFile(u":/font_awesome_regular/icons/font_awesome/regular/square-plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addIncomeButton.setIcon(icon12)
        self.addIncomeButton.setIconSize(QSize(30, 30))

        self.verticalLayout_14.addWidget(self.addIncomeButton, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.inputMasuk)

        self.mainPages.addWidget(self.pemasukanHalaman)
        self.laporanHalaman = QWidget()
        self.laporanHalaman.setObjectName(u"laporanHalaman")
        self.verticalLayout_24 = QVBoxLayout(self.laporanHalaman)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_12 = QWidget(self.laporanHalaman)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_25 = QVBoxLayout(self.widget_12)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_26 = QVBoxLayout(self.widget_13)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_10 = QLabel(self.widget_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.reportDateEdit = QDateEdit(self.widget_13)
        self.reportDateEdit.setObjectName(u"reportDateEdit")
        self.reportDateEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.reportDateEdit)


        self.verticalLayout_25.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.downloadButton = QPushButton(self.widget_14)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setMaximumSize(QSize(200, 200))
        self.downloadButton.setSizeIncrement(QSize(0, 0))
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.downloadButton.setIcon(icon13)
        self.downloadButton.setIconSize(QSize(200, 200))

        self.horizontalLayout_10.addWidget(self.downloadButton)


        self.verticalLayout_25.addWidget(self.widget_14)


        self.verticalLayout_24.addWidget(self.widget_12)

        self.mainPages.addWidget(self.laporanHalaman)

        self.verticalLayout_11.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainPagesCont)


        self.verticalLayout_10.addWidget(self.mainContents)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setPointSize(8)
        self.label_6.setFont(font6)

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.footer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_3, 0, Qt.AlignVCenter)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.footer, 0, Qt.AlignBottom)


        self.hboxLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(1)
        self.mainPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuTombol.setText("")
        self.halamanTombol.setText(QCoreApplication.translate("MainWindow", u"Halaman", None))
        self.pemasukanTombol.setText(QCoreApplication.translate("MainWindow", u"Pemasukan", None))
        self.pengeluaranTombol.setText(QCoreApplication.translate("MainWindow", u"Pengeluaran", None))
        self.laporanTombol.setText(QCoreApplication.translate("MainWindow", u"Laporan", None))
        self.pengaturanTombol.setText(QCoreApplication.translate("MainWindow", u"Pengaturan", None))
        self.informasiTombol.setText(QCoreApplication.translate("MainWindow", u"Informasi", None))
        self.bantuanTombol.setText(QCoreApplication.translate("MainWindow", u"Bantuan", None))
        self.keluarMenuTombol.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pengaturan", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tema", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kelompok 3 :</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /"
                        "></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Muhammad Putra Abriel Chaniago (23051204181)</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gadang Jatu Mahiswara (23051204189)</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sarah Nabila (23051204195)</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rahma Nur Aiza (23051204197)</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\">contact us:</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">github.com/Chanie-ago</p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">MyCashFlow</span> adalah aplikasi pengaturan keuangan yang dirancang untuk membantu pengguna dalam mengelola pemasukan, pengeluaran, dan tabungan.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program ini adalah solusi yang menarik untuk personal finance managemen.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Projek Akhir Semester 3</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mata Kuliah diampu oleh Dosen:</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I Made Suartana, S.Kom., M.Kom</p></body></html>", None))
        self.tittleTxt.setText(QCoreApplication.translate("MainWindow", u"MyCashFlow", None))
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TOTAL PEMASUKAN", None))
        self.incomeRefreshButton.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"amount", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"category", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"description", None));
        self.labelTotalIncome.setText("")
        self.labelSaldo.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TOTAL PENGELUARAN", None))
        self.expenseRefreshButton.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        ___qtablewidgetitem5 = self.expenseTableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None));
        ___qtablewidgetitem6 = self.expenseTableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Jumlah", None));
        self.labelTotalExpense.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"HALAMAN PENGELUARAN", None))
        self.refreshButton_2.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        ___qtablewidgetitem7 = self.expenseTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem8 = self.expenseTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None));
        ___qtablewidgetitem9 = self.expenseTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Biaya", None));
        ___qtablewidgetitem10 = self.expenseTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem11 = self.expenseTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Keterangan", None));
        self.deleteExpenseButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PENGELUARAN", None))
        self.expenseAmountEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Biaya", None))
        self.expenseDescriptionEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.expenseCategoryEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Keterangan", None))
        self.addExpenseButton.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"HALAMAN PEMASUKAN", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        ___qtablewidgetitem12 = self.incomeTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem13 = self.incomeTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tanggal", None));
        ___qtablewidgetitem14 = self.incomeTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Biaya", None));
        ___qtablewidgetitem15 = self.incomeTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem16 = self.incomeTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Keterangan", None));
        self.deleteIncomeButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PEMASUKAN", None))
        self.incomeAmountEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Biaya", None))
        self.incomeCategoryEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.incomeDescriptionEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Keterangan", None))
        self.addIncomeButton.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD LAPORAN KEUANGAN", None))
        self.downloadButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tugas Akhir Semester 3 (Kelompok 3)", None))
    # retranslateUi

