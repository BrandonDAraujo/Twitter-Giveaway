from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import json
import GiveAway
import time

class winnerWindow():
    def winnerFunc(self, thirdWindow, winners):
        if len(winners) > 1:
            print(winners)
            thirdWindow.setObjectName('WinnerWindow')
            thirdWindow.resize(300, 500)
            thirdWindow.setMinimumSize(QtCore.QSize(300, 500))
            thirdWindow.setMaximumSize(QtCore.QSize(300, 500))
            self.thirdWindowCenter = QtWidgets.QWidget(thirdWindow)
            #self.list = QtWidgets.QTextBrowser(thirdWindow)
            #self.list.setGeometry(10, 10, 280, 480)
            self.groupbox = QtWidgets.QGroupBox(self.thirdWindowCenter)
            self.groupbox.setGeometry(0,0, 280, 500)
            self.formLayout = QtWidgets.QFormLayout(self.thirdWindowCenter)
            self.formLayout.setContentsMargins(0,0,0,0)
            thirdWindow.setCentralWidget(self.thirdWindowCenter)
            self.cycle = 0
            for sepWinners in winners:
                self.cycle +=1
                labeling = QtWidgets.QLabel()
                labeling.setText(f'{self.cycle}.<a href="https://www.twitter.com/{sepWinners}">{sepWinners}')
                labeling.setOpenExternalLinks(True)
                self.labelingFont = QtGui.QFont()
                self.labelingFont.setPointSize(15)
                labeling.setFont(self.labelingFont)

                self.formLayout.addRow(labeling)
            self.groupbox.setLayout(self.formLayout)
            self.scroll = QtWidgets.QScrollArea(self.thirdWindowCenter)
            self.scroll.setGeometry(0,0, 300, 500)
            self.scroll.setWidget(self.groupbox)
            self.scroll.setWidgetResizable(True)

            #for sepWinners in winners:
            #    sortedWinners = F'1. {sepWinners}'
            #    self.list.insertItem(1, sortedWinners)
        elif len(winners) == 1:
            winners = winners[0]
            thirdWindow.setObjectName('WinnerWindow')
            thirdWindow.resize(900, 300)
            thirdWindow.setMinimumSize(QtCore.QSize(900, 300))
            thirdWindow.setMaximumSize(QtCore.QSize(900, 300))
            self.thirdWindowCenter = QtWidgets.QWidget(thirdWindow)
            self.thirdWindowCenter.setObjectName('ThirdWindowCenter')
            self.gif = QtGui.QMovie('fireworks.gif')
            self.gifLabel = QtWidgets.QLabel(self.thirdWindowCenter)
            self.gifLabel.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.gifLabel.setGeometry(QtCore.QRect(0, 0, 900, 300))
            self.gifLabel.setMovie(self.gif)
            self.fSound = QtMultimedia.QSound('fireworksSound.wav')
            self.gif.start()
            self.fSound.play()
            self.labelWin = QtWidgets.QLabel(self.thirdWindowCenter)
            self.labelWin.setGeometry(QtCore.QRect(0, 0, 900, 180))
            self.labelWin.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
            self.hypeLink = QtWidgets.QLabel(self.thirdWindowCenter)
            self.hypeLink.setGeometry(QtCore.QRect(0, 155, 900, 70))


            thirdWindow.setCentralWidget(self.thirdWindowCenter)
            translate = QtCore.QCoreApplication.translate
            self.labelWin.setText(translate('thirdWindow', '{}'.format(winners)))
            self.winnerFont = QtGui.QFont()
            self.winnerFont.setBold(True)
            self.winnerFont.setPointSize(55)
            self.labelWin.setFont(self.winnerFont)
            self.hypeLink.setOpenExternalLinks(True)
            self.hypeLink.setText(f'<a href="https://www.twitter.com/{winners}">@{winners}')
            self.hypeLink.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
            self.hypeFont = QtGui.QFont()
            self.hypeFont.setPointSize(16)
            self.hypeLink.setFont(self.hypeFont)
        else:
            thirdWindow.setObjectName('WinnerWindow')
            thirdWindow.resize(462, 192)
            thirdWindow.setMinimumSize(QtCore.QSize(462, 192))
            thirdWindow.setMaximumSize(QtCore.QSize(462, 192))
            self.thirdWindowCenter = QtWidgets.QWidget(thirdWindow)
            thirdWindow.setCentralWidget(self.thirdWindowCenter)
            translate = QtCore.QCoreApplication.translate
            self.textLabel = QtWidgets.QLabel(self.thirdWindowCenter)
            self.textLabel.setGeometry(QtCore.QRect(0, 0, 462, 192))
            self.textLabelFont = QtGui.QFont()
            self.textLabelFont.setBold(True)
            self.textLabel.setFont(self.textLabelFont)
            self.textLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.textLabel.setText(translate('thirdWindow', 'No Winners Selected'))
            self.textLabel2 = QtWidgets.QLabel(self.thirdWindowCenter)
            self.textLabel2.setGeometry(QtCore.QRect(0, 22, 450, 250))
            self.textLabel2Font = QtGui.QFont()
            self.textLabel2.setFont(self.textLabel2Font)
            self.textLabel2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.textLabel2.setText(translate('thirdWindow', 'No twitter users met the filter requirements.'))

class Worker(QtCore.QThread):
    all_done = QtCore.pyqtSignal(object)
    def __init__(self, tweetLink, followers, winCount, tAgeDays, timeFilter):
        super(Worker, self).__init__()
        self.tweetLink = tweetLink
        self.followers = followers
        self.winCount = winCount
        self.tAgeDays = tAgeDays
        self.timeFilter = timeFilter

    def next_step(self):
        winners = GiveAway.GStart(self.tweetLink, self.followers, self.winCount, self.tAgeDays, self.timeFilter)
        self.all_done.emit(winners)
    def run(self):
        self.next_step()

class Worker1(QtCore.QThread):
    all_done1 = QtCore.pyqtSignal(object)
    def __init__(self):
        super(Worker1, self).__init__()

    def next_step(self):
        for x in range(1,8):
            self.all_done1.emit(1)
            time.sleep(1.5)
    def run(self):
        self.next_step()

class keyWindow():
    def keyWinFunc(self, secondWindow):
        secondWindow.setObjectName("MainWindow")
        secondWindow.resize(500, 150)
        secondWindow.setMinimumSize(QtCore.QSize(500, 150))
        secondWindow.setMaximumSize(QtCore.QSize(500, 150))
        self.centralwidgetKey = QtWidgets.QWidget(secondWindow)
        self.centralwidgetKey.setObjectName('CentralWidgetKey')
        self.labelKey = QtWidgets.QLabel(self.centralwidgetKey)
        self.labelKey.setGeometry(QtCore.QRect(5, 5, 101, 16))
        self.labelKey.setObjectName("label_key")
        self.labelKeySecret = QtWidgets.QLabel(self.centralwidgetKey)
        self.labelKeySecret.setGeometry(QtCore.QRect(5, 31, 101, 16))
        self.labelKeySecret.setObjectName('Label_Key_Secret')
        self.labelToken = QtWidgets.QLabel(self.centralwidgetKey)
        self.labelToken.setGeometry(QtCore.QRect(5, 57, 101, 16))
        self.labelToken.setObjectName('Label_Token')
        self.labelTokenSecret = QtWidgets.QLabel(self.centralwidgetKey)
        self.labelTokenSecret.setGeometry(QtCore.QRect(5, 83, 101, 16))
        self.labelTokenSecret.setObjectName('Label_Token_Secret')
        self.saveButton = QtWidgets.QPushButton(self.centralwidgetKey)
        self.saveButton.setGeometry(QtCore.QRect(220, 130, 60, 20))
        self.saveButton.setObjectName('Button_Save')
        self.saveButton.clicked.connect(self.saveBtn)
        self.saveButton.clicked.connect(secondWindow.close)
        #Key
        self.key = QtWidgets.QLineEdit(self.centralwidgetKey)
        self.key.setGeometry(QtCore.QRect(75, 5, 415, 20))
        self.key.setObjectName('Key_Edit')
        #Key Secret
        self.keySecret = QtWidgets.QLineEdit(self.centralwidgetKey)
        self.keySecret.setGeometry(QtCore.QRect(75, 31, 415, 20))
        self.keySecret.setObjectName('KeySecret_Edit')
        #Token
        self.Token = QtWidgets.QLineEdit(self.centralwidgetKey)
        self.Token.setGeometry(QtCore.QRect(75, 57, 415, 20))
        self.Token.setObjectName('Token_Edit')
        #Token Secret
        self.tokenSecret = QtWidgets.QLineEdit(self.centralwidgetKey)
        self.tokenSecret.setGeometry(QtCore.QRect(75, 83, 415, 20))
        self.tokenSecret.setObjectName('TokenSecret_Edit')

        secondWindow.setCentralWidget(self.centralwidgetKey)
        translate = QtCore.QCoreApplication.translate
        self.labelKey.setText(translate("secondWindow", 'Key:'))
        self.labelKeySecret.setText(translate("secondWindow", 'Key Secret:'))
        self.labelToken.setText(translate("secondWindow", 'Token:'))
        self.labelTokenSecret.setText(translate("secondWindow", 'Token Secret:'))
        self.saveButton.setText(translate("secondWindow", 'Save'))
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

        try:
            with open('twitter_credential.json', 'r') as reInput1:
                reInput = json.load(reInput1)
                self.key.setText(reInput['CONSUMER_KEY'])
                self.keySecret.setText(reInput['CONSUMER_SECRET'])
                self.Token.setText(reInput['ACCESS_TOKEN'])
                self.tokenSecret.setText(reInput['ACCESS_SECRET'])
        except FileNotFoundError:
            pass

    def saveBtn(self):
        newCred = {"CONSUMER_KEY": self.key.text().replace(' ',''),
                "CONSUMER_SECRET": self.keySecret.text().replace(' ',''),
                "ACCESS_TOKEN": self.Token.text().replace(' ',''),
                "ACCESS_SECRET": self.tokenSecret.text().replace(' ','')}
        with open('twitter_credential.json','w') as creds:
            json.dump(newCred, creds)


class countDown():
    def countDownFunction(self, countDownWindow, winners):
        self.cycle = 6
        self.winners = winners
        self.countDownWindow = countDownWindow
        countDownWindow.setObjectName("CountWindow")
        countDownWindow.resize(300, 300)
        countDownWindow.setMinimumSize(QtCore.QSize(300, 300))
        countDownWindow.setMaximumSize(QtCore.QSize(300, 300))
        self.countDownWindowCenter = QtWidgets.QWidget(countDownWindow)
        countDownWindow.setCentralWidget(self.countDownWindowCenter)
        self.counter = QtWidgets.QLabel(self.countDownWindowCenter)
        self.counter.setGeometry(QtCore.QRect(0, -10, 300, 300))
        self.translate = QtCore.QCoreApplication.translate
        self.worker1 = Worker1() 
        self.worker1.start()
        self.worker1.all_done1.connect(self.countDown)
    def countDown(self):
        if self.cycle > 0:
            self.cycle -=1
            self.counter.setText(self.translate('countDownWindow', str(self.cycle)))
            self.counterFont = QtGui.QFont()
            self.counterFont.setPointSize(160)
            self.counterFont.setBold(True)
            self.counter.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.counter.setFont(self.counterFont)
        else:
            self.countDownWindow.close()
            self.thirdWindow = QtWidgets.QMainWindow()
            self.win = winnerWindow()
            self.win.winnerFunc(self.thirdWindow, self.winners)
            self.thirdWindow.show()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498*2, 300*2)
        MainWindow.setMinimumSize(QtCore.QSize(498*2, 300*2))
        MainWindow.setMaximumSize(QtCore.QSize(498*2, 300*2))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(350*2, 0, 141*2, 280*2))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.clicked)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 179*2, 351*2, 181*2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1*2, 1*2)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1*2, 1*2, 1*2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 5*2, 404, 16*2))
        self.label.setObjectName("label")
        self.tAge = QtWidgets.QLabel(self.centralwidget)
        self.tAge.setGeometry(QtCore.QRect(80*2, 95*2, 110*2, 16*2))
        self.tAge_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tAge_edit.setGeometry(QtCore.QRect(80*2, 115*2, 100*2, 20*2))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(2*2, 25*2, 341*2, 20*2))
        self.lineEdit.setObjectName("lineEdit")
        self.tweetInput = QtWidgets.QLabel(self.centralwidget)
        self.tweetInput.setGeometry(QtCore.QRect(0, 50*2, 404, 16*2))
        self.tweetInput.setObjectName("tweetInput")
        self.followerEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.followerEdit.setGeometry(QtCore.QRect(2*2, 70*2, 341*2, 20*2))
        self.followerEdit.setObjectName("followerEdit")
        self.followerEdit.returnPressed.connect(self.pressed)
        self.winnerCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.winnerCountLabel.setGeometry(QtCore.QRect(0, 95*2, 404, 16*2))
        self.winnerCountLabel.setObjectName("WinnerCountLabel")
        self.winnerCountEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.winnerCountEdit.setGeometry(QtCore.QRect(2*2, 115*2, 50*2, 20*2))
        self.winnerCountEdit.setObjectName('WinnerCountEdit')
        self.timeFilter = QtWidgets.QLabel(self.centralwidget)
        self.timeFilter.setGeometry(QtCore.QRect(208*2, 95*2, 110*2, 16*2))
        self.timeFilterEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.timeFilterEdit.setGeometry(QtCore.QRect(208*2, 115*2, 105*2, 20*2))

        self.kError = QtWidgets.QLabel(self.centralwidget)
        self.kError.setGeometry(QtCore.QRect(2*2, 135*2, 341*2, 16*2))
        self.kError.setObjectName("kError")
        self.tError = QtWidgets.QLabel(self.centralwidget)
        self.tError.setGeometry(QtCore.QRect(2*2, 135*2, 341*2, 16*2))
        self.tError.setObjectName("tError")
        self.lError = QtWidgets.QLabel(self.centralwidget)
        self.lError.setGeometry(QtCore.QRect(2*2, 135*2, 341*2, 16*2))
        self.lError.setObjectName("lError")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(2*2, 135*2, 341*2, 16*2))
        self.error.setObjectName("error")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498*2, 21*2))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def pressed(self):
        copiedText = self.followerEdit.text()
        self.listWidget.insertItem(1, copiedText)
        self.followerEdit.clear()
    def clicked(self):
        self.listWidget.takeItem(self.listWidget.currentRow())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.defaultFont = QtGui.QFont()
        self.defaultFont.setPointSize(16)
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.setText(_translate("MainWindow", "Change Keys"))
        self.pushButton_2.clicked.connect(self.keyChecker)
        self.label.setText(_translate("MainWindow", "Target Tweet Link:"))
        self.tweetInput.setText(_translate("MainWindow", "Required To Follow:"))
        self.winnerCountLabel.setText(_translate("MainWindow", "# Winners"))
        self.winnerCountEdit.setText(_translate("MainWindow", '1'))
        self.tAge.setText(_translate("MainWindow", 'Account Age'))
        self.timeFilter.setText(_translate("MainWindow", 'Time Filter'))
        self.timeFilterEdit.setText(_translate("MainWindow", '0'))
        self.tAge_edit.setText(_translate('MainWindow', ''))
        self.followerEdit.setText(_translate('MainWindow',''))
        self.lineEdit.setText(_translate('MainWindow',''))
        self.lineEdit.setFont(self.defaultFont)
        self.followerEdit.setFont(self.defaultFont)
        self.label.setFont(self.defaultFont)
        self.tweetInput.setFont(self.defaultFont)
        self.winnerCountLabel.setFont(self.defaultFont)
        self.winnerCountEdit.setFont(self.defaultFont)
        self.tAge.setFont(self.defaultFont)
        self.timeFilter.setFont(self.defaultFont)
        self.timeFilterEdit.setFont(self.defaultFont)
        self.tAge_edit.setFont(self.defaultFont)

        self.kError.setStyleSheet('color: red')
        self.kError.hide()
        self.kError.setText(_translate("MainWindow", "Key Error! Please re-check your keys."))
        self.tError.setStyleSheet('color: red')
        self.tError.setText(_translate("MainWindow", "An error has occured with that tweet. Double check tweet link."))
        self.tError.hide()
        self.lError.setStyleSheet('color: red')
        self.lError.setText(_translate("MainWindow", "Rate limit exceeded! Please wait 15 minutes before trying again."))
        self.lError.hide()
        self.error.setStyleSheet('color: red')
        self.error.setText(_translate("MainWindow", "An error has occured."))
        self.error.hide()

    def winFunc(self, winners):
        _translate = QtCore.QCoreApplication.translate
        if winners in ['|keys|', '|tweet|', '|limit|', '|Error|']:
            self.pushButton.setDisabled(False)
            self.pushButton_2.setDisabled(False)
            if winners == '|keys|':
                self.kError.show()
            elif winners == '|tweet|':
                self.tError.show()
            elif winners == '|limit|':
                self.lError.show()
            elif winners == '|Error|':
                self.error.show()
        else:
            self.pushButton.setDisabled(False)
            self.pushButton_2.setDisabled(False)
            self.countDownWindow = QtWidgets.QMainWindow()
            self.count = countDown()
            self.count.countDownFunction(self.countDownWindow, winners)
            self.countDownWindow.show()

    def start(self):
        self.kError.hide()
        self.tError.hide()
        self.lError.hide()
        self.error.hide()
        self.lineEdit.setFocus(False)
        self.tweetInput.setFocus(False)
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        tweetLink = self.lineEdit.text()
        winCount = self.winnerCountEdit.text()
        tAgeDays = self.tAge_edit.text()
        timeFilter = self.timeFilterEdit.text()
        followers = []
        for followerItem in range(0, self.listWidget.count()):
            followers.append(self.listWidget.item(followerItem).text())
        self.worker = Worker(tweetLink, followers, winCount, tAgeDays, timeFilter)
        self.worker.start()
        self.worker.all_done.connect(self.winFunc)

        

    def keyChecker(self):
        alertButton = QtWidgets.QMessageBox()
        alertButton.setWindowTitle('Alert!')
        alertButton.setText("Do you want to edit keys?")
        alertButton.setIcon(QtWidgets.QMessageBox.Question)
        alertButton.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        alertButton.setDefaultButton(QtWidgets.QMessageBox.No)
        alertButton.buttonClicked.connect(self.alertwind)
        a = alertButton.exec_()

    def alertwind(self, i):
        if i.text() == "&Yes":
            self.secondWindow = QtWidgets.QMainWindow()
            self.keyWin = keyWindow()
            self.keyWin.keyWinFunc(self.secondWindow)
            self.secondWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
