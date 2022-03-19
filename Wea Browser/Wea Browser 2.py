import os
from sys import argv
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView

# from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import (
    QMainWindow,
    QToolBar,
    QAction,
    QLineEdit,
    QTabWidget,
    QStatusBar,
    QApplication,
)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # BG Color
        THE_COLOR = [QColor(69, 71, 73), QColor(250, 250, 250)]
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), THE_COLOR[0])
        self.setPalette(pal)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.setCentralWidget(self.tabs)

        # Status Bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # Navegation Bar
        navbar = QToolBar("Navigation")
        navbar.setIconSize(QSize(35, 35))
        self.addToolBar(navbar)

        # Icon Color = White or Black
        Icon_Color = ["_w", "_b"]

        # Back Button
        back_btn = QAction(QIcon(f"assets/left{Icon_Color[0]}.png"), "← Go Back", self)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navbar.addAction(back_btn)

        # Forward Button
        forward_btn = QAction(
            QIcon(f"assets/right{Icon_Color[0]}.png"), "Go Forward →", self
        )
        forward_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navbar.addAction(forward_btn)

        # Reload Button
        reload_btn = QAction(
            QIcon(f"assets/reload{Icon_Color[0]}.png"), "Reload 🔃", self
        )
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navbar.addAction(reload_btn)

        # Stop Button
        stop_btn = QAction(QIcon(f"assets/stop{Icon_Color[0]}.png"), "Stop ❌", self)
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navbar.addAction(stop_btn)

        # Separator
        navbar.addSeparator()

        # Search Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_to_url)
        navbar.addWidget(self.url_bar)

        # Home Button
        home_btn = QAction(
            QIcon(f"assets/home{Icon_Color[0]}.png"), "To Homepage🏠", self
        )
        home_btn.triggered.connect(self.nav_home)
        navbar.addAction(home_btn)

        # New Tab
        self.add_new_tab(QUrl("https://duckduckgo.com/"), "Homepage🏠")
        self.showMaximized()
        self.setWindowTitle("Wea Browser 2")

    # Add New Tabs
    def add_new_tab(self, qurl=None, label="Blank"):
        if qurl is None:
            qurl = QUrl("https://duckduckgo.com/")
        browser = QWebEngineView()
        browser.setUrl(qurl)

        # Index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # Update Url
        browser.urlChanged.connect(
            lambda qurl, browser=browser: self.update_url_bar(qurl, browser)
        )
        browser.loadFinished.connect(
            lambda _, i=i, browser=browser: self.tabs.setTabText(
                i, browser.page().title()
            )
        )

    # Double Click To Open New Tab
    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_url_bar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    # To Close a Tab
    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - Browser" % title)

    # Nav To Homepage
    def nav_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://duckduckgo.com/"))

    # Nav To The Link You Wrote
    def nav_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("https")
        self.tabs.currentWidget().setUrl(q)

    def update_url_bar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)


app = QApplication(argv)
app.setApplicationName("Wea Browser 2")
window = MainWindow()
app.exec_()
