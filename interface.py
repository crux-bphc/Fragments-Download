import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import asyncio
import aiohttp
from ytvid import *
from downloaderOOP import *
from ytlist import *


class AppInterface(QWidget):

    def __init__(self, parent=None):
        super(AppInterface, self).__init__(parent)
        self.setGeometry(600, 600, 300, 300)
        self.setWindowTitle('Downloader')
        self.box = QVBoxLayout()
        self.startUI()
        self.frags = 8
        self.url = None
        self.downloader = None

    def startUI(self):
        try:
            self.l1.close()
            self.b1.close()
        except:
            pass
        self.l1 = QLabel("Enter the download URL here")
        self.l2 = QLabel("Select the number of fragments")
        self.t1 = QLineEdit()
        self.b1 = QPushButton("Select download folder")
        self.l3 = QLabel()
        self.b1.clicked.connect(self.select_path)
        self.b2 = QPushButton("Download")
        self.b2.clicked.connect(self.preDownload)
        self.combo = QComboBox()
        for i in range(2, 33):
            self.combo.addItem(str(i))
        self.combo.currentIndexChanged.connect(self.Changed_Selection)
        self.combo.setCurrentIndex(6)
        self.box.addWidget(self.l1)
        self.box.addWidget(self.t1)
        self.box.addWidget(self.l2)
        self.box.addWidget(self.combo)
        self.box.addWidget(self.b1)
        self.box.addWidget(self.l3)
        self.box.addWidget(self.b2)
        self.setLayout(self.box)

    def select_path(self):
        path_select = QFileDialog()
        path_select.setFileMode(QFileDialog.Directory)
        file_path = None
        self.path = ""
        if path_select.exec_():
            file_path = path_select.selectedFiles()
        if file_path:
            self.path = file_path[0]
            self.path = self.path + "/"
            self.l3.setText(self.path)

    def Changed_Selection(self, i):
        self.frags = int(i)+2

    def preDownload(self):
        if len(self.t1.text()) > 1:
            self.url = self.t1.text()
            if "youtube" in self.url or "youtu.be" in self.url:
                self.l1.close()
                self.l2.close()
                self.l3.close()
                self.b1.close()
                self.b2.close()
                self.t1.close()
                self.combo.close()
                if 'list' in self.url:
                    try:
                        ylist = ytlist(self.url)
                        videolist = ylist.populateVideoList()
                        print(videolist)
                        for i in videolist:
                            self.url = i
                            self.startDownload()
                    except:
                        self.l1 = QLabel("There was an error.")
                        self.b1 = QPushButton("Back")
                        self.b1.clicked.connect(self.startUI)
                        self.box.addWidget(self.l1)
                        self.box.addWidget(self.b1)
                else:
                    self.YoutubeUI()
            else:
                self.l1.close()
                self.l2.close()
                self.l3.close()
                self.b1.close()
                self.b2.close()
                self.t1.close()
                self.combo.close()
                self.downloader = downloadUrl(self.url, self.path)
                self.startDownload()

    def YoutubeStream(self, i):
        self.downloader.setStream(i)

    def YoutubeUI(self):
        self.label = QLabel("Select your preferred file type")
        self.cbox = QComboBox()
        self.downloader = ytvideo(self.url, self.path)
        streams = self.downloader.sendStreams()
        for i in streams:
            self.cbox.addItem(str(i))
        self.cbox.currentIndexChanged.connect(self.YoutubeStream)
        self.b = QPushButton("Download!")
        self.b.clicked.connect(self.startDownload)
        self.box.addWidget(self.label)
        self.box.addWidget(self.cbox)
        self.box.addWidget(self.b)

    def startDownload(self):
        try:
            self.label.close()
            self.cbox.close()
            self.b.close()
        except:
            pass
        self.label = QLabel("Your download has started..")
        self.box.addWidget(self.label)
        try:
            event = asyncio.get_event_loop()
            event.run_until_complete(self.downloader.download())
        except:
            self.label.setText(
                "There was a network error. Please try again later")


def main():
    app = QApplication(sys.argv)
    App_UI = AppInterface()
    App_UI.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
