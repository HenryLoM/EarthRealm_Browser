import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QKeySequence

# - - - - - - - functions - - - - - - -

def navigate(url):
    if not url.startswith("http"):
        url = "http://" + url
    if url.count(".") != 0:
        browser.setUrl(QUrl(url))
    else:
        url = url + ".com"
        browser.setUrl(QUrl(url))

def navigate_home():
    browser.setUrl(QUrl.fromLocalFile(os.path.join(current_dir, "index.html")))

def show_website_info():
    current_title = browser.page().title()
    current_url = browser.url().toString()
    QMessageBox.information(window, "Details", f"Website info:\n\n"
                                               f"Name • {current_title}\n\n"
                                               f"URL • {current_url}")

# - - - - - - - primary - - - - - - -

# base
app = QApplication(sys.argv)
QApplication.setApplicationName("EarthRealm")

# browser's settings
browser = QWebEngineView()
browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)  # full-screen available
browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)  # js assisting

# window's settings
window = QMainWindow()
window.setCentralWidget(browser)
window.showMaximized()
window.setWindowTitle("EarthRealm")

# home page
current_dir = os.path.dirname(os.path.abspath(__file__))
browser.setUrl(QUrl.fromLocalFile(os.path.join(current_dir, "index.html")))

# - - - - - - - gui - - - - - - -

# navigation bar
navbar = QToolBar()
window.addToolBar(navbar)

# back button
back_btn = QAction("Back", window)
back_btn.triggered.connect(browser.back)
back_btn.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_B))  # Shortcut for Cmd+B or Ctrl+B
navbar.addAction(back_btn)

# forward button
forward_btn = QAction("Forward", window)
forward_btn.triggered.connect(browser.forward)
forward_btn.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))  # Shortcut for Cmd+F or Ctrl+F
navbar.addAction(forward_btn)

# reload button
reload_btn = QAction("Reload", window)
reload_btn.triggered.connect(browser.reload)
reload_btn.setShortcut(QKeySequence.Refresh)  # Shortcut for Cmd+R or Ctrl+R
navbar.addAction(reload_btn)

# url bar
url_bar = QLineEdit()
url_bar.returnPressed.connect(lambda: navigate(url_bar.text()))
navbar.addWidget(url_bar)

# go button
go_btn = QAction("Go", window)
go_btn.triggered.connect(lambda: navigate(url_bar.text()))
go_btn.setShortcut(QKeySequence(Qt.Key_Return))  # Shortcut for Return or Enter key
navbar.addAction(go_btn)

# home button
home_btn = QAction("Home", window)
home_btn.triggered.connect(navigate_home)
home_btn.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_H))  # Shortcut for Cmd+H or Ctrl+H
navbar.addAction(home_btn)

# url-showing button
show_url_btn = QAction("Website details", window)
show_url_btn.triggered.connect(show_website_info)
navbar.addAction(show_url_btn)

# add separator
navbar.addSeparator()

# for end
sys.exit(app.exec_())
