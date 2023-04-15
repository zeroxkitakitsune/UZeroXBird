import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem, QTableView, QMessageBox, QHeaderView
from PySide6.QtCore import QFile, QDir, QPersistentModelIndex

from twitter import Twitter

from ui.mainwindowui import Ui_MainWindow
from ui.linkaccountui import Ui_linkAnAccountDialog
from ui.followui import Ui_followDialog
from ui.tweetui import Ui_tweetDialog
from ui.retweetui import Ui_retweetDialog
from ui.likeui import Ui_likeDialog
from ui.proxyui import Ui_proxyDialog

twitter = Twitter()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.linkedAccountsTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.linkedAccountsTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.ui.linkedAccountsTableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.linkedAccountsTableWidget.setSelectionBehavior(QTableView.SelectRows)
        self.ui.linkedAccountsTableWidget.selectionModel().selectionChanged.connect(enableBtns)

class linkAnAccountDialog(QDialog):
    def __init__(self):
        super(linkAnAccountDialog, self).__init__()
        self.ui = Ui_linkAnAccountDialog()
        self.ui.setupUi(self)

class proxyDialog(QDialog):
    def __init__(self):
        super(proxyDialog, self).__init__()
        self.ui = Ui_proxyDialog()
        self.ui.setupUi(self)

class followDialog(QDialog):
    def __init__(self):
        super(followDialog, self).__init__()
        self.ui = Ui_followDialog()
        self.ui.setupUi(self)

class tweetDialog(QDialog):
    def __init__(self):
        super(tweetDialog, self).__init__()
        self.ui = Ui_tweetDialog()
        self.ui.setupUi(self)

class retweetDialog(QDialog):
    def __init__(self):
        super(retweetDialog, self).__init__()
        self.ui = Ui_retweetDialog()
        self.ui.setupUi(self)

class likeDialog(QDialog):
    def __init__(self):
        super(likeDialog, self).__init__()
        self.ui = Ui_likeDialog()
        self.ui.setupUi(self)

def enableBtns(selected, deselected):
    window.ui.followBtn.setEnabled(True)
    window.ui.tweetBtn.setEnabled(True)
    window.ui.retweetBtn.setEnabled(True)
    window.ui.likeBtn.setEnabled(True)
    window.ui.deleteBtn.setEnabled(True)

def linkAccount():
    
    global twitter
    
    link_an_account_dialog = linkAnAccountDialog()
    proxy_dialog = proxyDialog()
    proxyBtn = proxy_dialog.exec()
    if proxyBtn == 1:
        proxy = proxy_dialog.ui.proxyText.toPlainText()
        
        button = link_an_account_dialog.exec()
        if button == 1:

            curl = link_an_account_dialog.ui.curlText.toPlainText()
            name = link_an_account_dialog.ui.nameText.toPlainText()
            twitter.link_account(name, curl, proxy)
            window.ui.linkedAccountsTableWidget.setRowCount(len(twitter.listAccounts))
            row = 0
            for account in twitter.listAccounts:
                window.ui.linkedAccountsTableWidget.setItem(row,0,QTableWidgetItem(account['name']))
                window.ui.linkedAccountsTableWidget.setItem(row,1,QTableWidgetItem(account['guest_id']))
                window.ui.linkedAccountsTableWidget.setItem(row,2,QTableWidgetItem(account['proxies']['https']))
                row += 1

def importSessions():
    
    global twitter

    fileName, _ = QFileDialog.getOpenFileName(window, 'Single File', QDir.rootPath() , '*.json')
    
    twitter.import_sessions(fileName)
    
    window.ui.linkedAccountsTableWidget.setRowCount(len(twitter.listAccounts))
    
    row = 0
    for account in twitter.listAccounts:
        window.ui.linkedAccountsTableWidget.setItem(row,0,QTableWidgetItem(account['name']))
        window.ui.linkedAccountsTableWidget.setItem(row,1,QTableWidgetItem(account['guest_id']))
        window.ui.linkedAccountsTableWidget.setItem(row,2,QTableWidgetItem(account['proxies']['https']))
        row += 1

def exportSessions():
    
    global twitter
    twitter.export_sessions()

def follow():
    global twitter

    follow_dialog = followDialog()
    
    rows = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    
    button = follow_dialog.exec()
    if button == 1:
        names = []
        for row in rows:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(row.row(), 0)))
        twitter.follow(names, follow_dialog.ui.followText.toPlainText())

def tweet():
    global twitter

    tweet_dialog = tweetDialog()
    
    rows = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    
    button = tweet_dialog.exec()
    if button == 1:
        names = []
        for row in rows:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(row.row(), 0)))
        twitter.tweet(names, tweet_dialog.ui.tweetText.toPlainText())

def retweet():
    global twitter

    retweet_dialog = retweetDialog()
    
    rows = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    
    button = retweet_dialog.exec()
    if button == 1:
        names = []
        for row in rows:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(row.row(), 0)))
        if retweet_dialog.ui.pauseCheckBox.isChecked():
            twitter.retweet(names, retweet_dialog.ui.rtText.toPlainText(), True)
        else:
            twitter.retweet(names, retweet_dialog.ui.rtText.toPlainText(), False)


def like():
    
    global twitter

    like_dialog = likeDialog()
    
    rows = window.ui.linkedAccountsTableWidget.selectionModel().selectedRows()
    button = like_dialog.exec()
    if button == 1:
        names = []
        for row in rows:
            names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(row.row(), 0)))
        twitter.like(names, like_dialog.ui.likeText.toPlainText())

def delete():
    
    global twitter
    rows = []
    names = []
    for model_index in window.ui.linkedAccountsTableWidget.selectionModel().selectedRows():
        i = QPersistentModelIndex(model_index)
        rows.append(i)

    for row in rows:
        names.append(window.ui.linkedAccountsTableWidget.model().data(window.ui.linkedAccountsTableWidget.model().index(row.row(), 0)))
        window.ui.linkedAccountsTableWidget.removeRow(row.row())
    twitter.delete(names)    


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.ui.linkAccountBtn.clicked.connect(linkAccount)
    window.ui.importSessionsBtn.clicked.connect(importSessions)
    window.ui.exportSessionsBtn.clicked.connect(exportSessions)
    window.ui.followBtn.clicked.connect(follow)
    window.ui.tweetBtn.clicked.connect(tweet)
    window.ui.retweetBtn.clicked.connect(retweet)
    window.ui.likeBtn.clicked.connect(like)
    window.ui.deleteBtn.clicked.connect(delete)
    window.show()

    sys.exit(app.exec())


