from sys import argv
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QMainWindow,
    QToolBar,
    QAction,
    QLineEdit,
    QApplication,
    QTabWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Tabs
        self.tabs = QTabWidget()
        # BG Color
        THE_COLOR = [QColor(69, 71, 73), QColor(250, 250, 250)]
        self.setAutoFillBackground(True)
        pl = self.palette()
        pl.setColor(self.backgroundRole(), THE_COLOR[0])
        self.setPalette(pl)

        # Main Page
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navegation Bar
        navbar = QToolBar()
        navbar.setIconSize(QSize(35, 35))
        self.addToolBar(navbar)

        Icon_Color = ["_w", "_b"]

        # Back Button
        back_btn = QAction(QIcon(f"assets/left{Icon_Color[0]}.png"), "← Go Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward Button
        forward_btn = QAction(
            QIcon(f"assets/right{Icon_Color[0]}.png"), "Go Forward →", self
        )
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload Button
        reload_btn = QAction(
            QIcon(f"assets/reload{Icon_Color[0]}.png"), "Reload 🔃", self
        )
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Search Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        # Home Button
        home_btn = QAction(QIcon(f"assets/home{Icon_Color[0]}.png"), "Home🏠", self)
        home_btn.triggered.connect(self.nav_home)
        navbar.addAction(home_btn)

    def nav_home(self):
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))

    def nav_to_url(self):
        url = self.url_bar.text()
        if "https://" not in url and "http://" not in url:
            self.browser.setUrl(QUrl("https://" + url))
        else:
            self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(argv)
QApplication.setApplicationName("Wea Browser 1")
window = MainWindow()
app.exec_()
