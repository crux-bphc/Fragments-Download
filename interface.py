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
        self.frags = 8
        self.url = None
        self.downloader = None
        self.path = ""
        self.isTube = False
        self.start_ui()

    def start_ui(self):
        try:
            self.l1.close()
            self.b1.close()
        except:
            pass
        # Creates initial UI screen
        self.l1 = QLabel("Enter the download URL here")
        self.l2 = QLabel("Select the number of fragments")
        self.t1 = QLineEdit()
        self.b1 = QPushButton("Select download folder")
        self.l3 = QLabel()
        self.b1.clicked.connect(self.select_path)
        self.b2 = QPushButton("Download")
        self.b2.clicked.connect(self.predownload)
        self.combo = QComboBox()
        for i in range(2, 33):
            self.combo.addItem(str(i))
        # Bind ComboBox to detect changes in current value
        self.combo.currentIndexChanged.connect(self.changed_selection)
        # Default number of fragments is 8
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
        # Select destination folder for download
        path_select = QFileDialog()
        path_select.setFileMode(QFileDialog.Directory)
        file_path = None
        if path_select.exec_():
            file_path = path_select.selectedFiles()
        if file_path:
            self.path = file_path[0]
            self.path = self.path + "/"
            self.l3.setText(self.path)

    def changed_selection(self, i):
        self.frags = int(i)+2

    def predownload(self):
        if len(self.t1.text()) > 1:
            self.url = self.t1.text()
            """Check if the URL leads to a Youtube video

            A Youtube video requires an intermediate step before it can
            be downloaded, and therefore we must check if the URL leads
            to a video, playlist, or if it is any other file.
            """
            if "youtube" in self.url or "youtu.be" in self.url:
                self.isTube = True
                self.l1.close()
                self.l2.close()
                self.l3.close()
                self.b1.close()
                self.b2.close()
                self.t1.close()
                self.combo.close()
                if 'list' in self.url:
                    try:
                        ylist = YtList(self.url)
                        videolist = ylist.populatevideolist()
                        print(videolist)
                        for i in videolist:
                            self.url = i
                            self.startdownload()
                    except:
                        self.l1 = QLabel("There was an error.")
                        self.b1 = QPushButton("Back")
                        self.b1.clicked.connect(self.start_ui)
                        self.box.addWidget(self.l1)
                        self.box.addWidget(self.b1)
                else:
                    self.youtube_ui()
            else:
                self.l1.close()
                self.l2.close()
                self.l3.close()
                self.b1.close()
                self.b2.close()
                self.t1.close()
                self.combo.close()
                self.downloader = DownloadUrl(self.url, self.path)
                self.startdownload()

    def youtubestream(self, i):
        self.downloader.setstream(i)

    def youtube_ui(self):
        # Select the preferred file type for downloading
        self.label = QLabel("Select your preferred file type")
        self.cbox = QComboBox()
        self.downloader = YtVideo(self.url, self.path)
        streams = self.downloader.sendstreams()
        for i in streams:
            self.cbox.addItem(str(i))
        self.cbox.currentIndexChanged.connect(self.youtubestream)
        self.b = QPushButton("Download!")
        self.b.clicked.connect(self.startdownload)
        self.box.addWidget(self.label)
        self.box.addWidget(self.cbox)
        self.box.addWidget(self.b)

    def startdownload(self):
        try:
            self.label.close()
            self.cbox.close()
            self.b.close()
        except:
            pass
        self.l1 = QLabel("Your download is complete")
        self.box.addWidget(self.l1)
        self.b1 = QPushButton("Back")
        self.b1.clicked.connect(self.start_ui)
        self.box.addWidget(self.b1)
        self.downloader.setfrags(self.frags)
        try:
            if self.isTube is True:
                event = asyncio.get_event_loop()
                event.run_until_complete(self.downloader.download())
            else:
                event = asyncio.get_event_loop()
                event.run_until_complete(self.downloader.downloadallfrags())
        except:
            self.l1.setText(
                "There was a network error. Please try again later")


def main():
    app = QApplication(sys.argv)
    App_UI = AppInterface()
    App_UI.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
