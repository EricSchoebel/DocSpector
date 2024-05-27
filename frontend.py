from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from handle_documents import load_documents, search_documents

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 739)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button_stichwortsuche = QtWidgets.QPushButton(self.centralwidget)
        self.button_stichwortsuche.setGeometry(QtCore.QRect(60, 446, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.button_stichwortsuche.setFont(font)
        self.button_stichwortsuche.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                "color: rgb(255, 255, 255);")
        self.button_stichwortsuche.setObjectName("button_stichwortsuche")

        self.button_beenden = QtWidgets.QPushButton(self.centralwidget)
        self.button_beenden.setGeometry(QtCore.QRect(60, 659, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.button_beenden.setFont(font)
        self.button_beenden.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                "color: rgb(255, 255, 255);")
        self.button_beenden.setObjectName("button_beenden")

        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(70, 20, 641, 69))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setAutoFillBackground(False)
        self.heading.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                "border-color: rgb(255, 255, 255);")
        self.heading.setScaledContents(False)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")

        self.button_verzeichnis = QtWidgets.QPushButton(self.centralwidget)
        self.button_verzeichnis.setGeometry(QtCore.QRect(60, 275, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.button_verzeichnis.setFont(font)
        self.button_verzeichnis.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                "color: rgb(255, 255, 255);")
        self.button_verzeichnis.setObjectName("button_verzeichnis")

        self.infotext = QtWidgets.QTextEdit(self.centralwidget)
        self.infotext.setGeometry(QtCore.QRect(60, 100, 661, 151))
        self.infotext.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                "color: rgb(255, 255, 255);\n"
                "border-color: rgb(0,0,0);")
        self.infotext.setReadOnly(True)
        self.infotext.setObjectName("infotext")

        self.textinput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textinput.setGeometry(QtCore.QRect(60, 386, 661, 51))
        self.textinput.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);")
        self.textinput.setObjectName("textinput")

        self.tabellenausgabe = QtWidgets.QTableView(self.centralwidget)
        self.tabellenausgabe.setGeometry(QtCore.QRect(60, 506, 661, 131))
        self.tabellenausgabe.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                "color: rgb(255, 255, 255);\n"
                "font: 14pt \"MS Shell Dlg 2\";")
        self.tabellenausgabe.setObjectName("tabellenausgabe")

        self.ordnerpfadanzeige = QtWidgets.QLabel(self.centralwidget)
        self.ordnerpfadanzeige.setGeometry(QtCore.QRect(60, 333, 661, 31))
        self.ordnerpfadanzeige.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
                "background-color: rgb(49, 49, 49);\n"
                "color: rgb(255, 255, 255);")
        self.ordnerpfadanzeige.setObjectName("ordnerpfadanzeige")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.directory = None
        self.df = None

        self.button_verzeichnis.clicked.connect(self.set_requested_directory)
        self.button_stichwortsuche.clicked.connect(self.start_keyword_search)
        self.button_beenden.clicked.connect(self.button_end_app)


    def set_requested_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(None, "Verzeichnis auswählen", "", options)
        if directory:
            self.directory = directory
            self.df = load_documents(self.directory)
            elided_text = QtGui.QFontMetrics(self.ordnerpfadanzeige.font()).elidedText(directory, QtCore.Qt.ElideMiddle,
                    self.ordnerpfadanzeige.width() - 10)
            self.ordnerpfadanzeige.setText(f" {elided_text}")
            return directory

    def start_keyword_search(self):
        if self.directory:
            search_words = self.textinput.toPlainText().split('+')
            results = search_documents(self.df, search_words)
            self.show_results(results)

    def show_results(self, results):

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['Dateiname', 'Gefundene Suchwörter'])

        for index, row in results.iterrows():
            filename_item = QtGui.QStandardItem(row['filename'])
            filename_item.setTextAlignment(QtCore.Qt.AlignCenter)
            filename_item.setToolTip(row['filename'])  # Wichtig: "Tooltip" ermöglicht Anzeige für hovern
            keywords_item = QtGui.QStandardItem(row['Gefundene Suchwörter'])
            keywords_item.setTextAlignment(QtCore.Qt.AlignCenter)
            keywords_item.setToolTip(row['Gefundene Suchwörter'])  # Wichtig: "Tooltip" ermöglicht Anzeige für hovern
            model.appendRow([filename_item, keywords_item])

        self.tabellenausgabe.setModel(model)

        #Tabelle formatieren
        self.tabellenausgabe.setStyleSheet("""
                QTableView {
                    background-color: rgb(49, 49, 49);
                    color: rgb(255, 255, 255);
                    gridline-color: rgb(80, 80, 80);
                    font-size: 15px; /* Schriftgröße für die Zellen */
                }
                QTableView::item {
                    background-color: rgb(49, 49, 49);
                    color: rgb(255, 255, 255);
                }
                QHeaderView::section {
                    background-color: rgb(49, 49, 49);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(80, 80, 80);
                    font-size: 18px; /* Schriftgröße für die Spaltenüberschriften */
                }
                QTableCornerButton::section {
                    background-color: rgb(49, 49, 49);
                    border: 1px solid rgb(80, 80, 80);
                }
                QScrollBar:vertical {
                    border: 1px solid rgb(80, 80, 80);
                    background: rgb(49, 49, 49);
                    width: 15px;
                    margin: 15px 0 15px 0;
                }
                QScrollBar::handle:vertical {
                    background: rgb(255, 255, 255);
                    min-height: 20px;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    border: 1px solid rgb(80, 80, 80);
                    background: rgb(49, 49, 49);
                    height: 15px;
                    subcontrol-origin: margin;
                }
                QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover {
                    background: rgb(80, 80, 80);
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
                """)
        self.tabellenausgabe.setColumnWidth(0, 200)
        self.tabellenausgabe.setColumnWidth(1, 300)
        header = self.tabellenausgabe.horizontalHeader()
        for col in range(model.columnCount()):
            self.tabellenausgabe.setColumnWidth(col, 200)
        header.setDefaultAlignment(QtCore.Qt.AlignCenter)
        vertical_header = self.tabellenausgabe.verticalHeader()
        vertical_header.setStyleSheet("QHeaderView::section { padding-left: 12px; }")
        self.tabellenausgabe.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tabellenausgabe.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def button_end_app(self):
        app.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DocSpector - Finden Sie Ihre Dokumente schneller"))
        self.button_stichwortsuche.setText(_translate("MainWindow", "Stichwortsuche starten"))
        self.button_beenden.setText(_translate("MainWindow", "Beenden"))
        self.heading.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:32pt; color:#ffffff;\">DocSpector</span></p></body></html>"))
        self.button_verzeichnis.setText(_translate("MainWindow", "Ordnerpfad festlegen"))
        self.infotext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Finden Sie mit DocSpector Stichwörter in Ihren Text- und Worddokumenten sowie in eingefügten Textfeldern von PDF-Dateien.</span></p>\n"
                "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> </span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Spezifizieren Sie zunächst das zu durchsuchende Verzeichnis. </span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Geben Sie dann das gewünschte Stichwort an (bei mehreren Stichwörtern über &quot;+&quot; verbinden, ohne Leerzeichen).</span></p></body></html>"))
        self.textinput.setPlainText(_translate("MainWindow", "Stichwort1+Stichwort2+Stichwort3"))
        self.ordnerpfadanzeige.setText(_translate("MainWindow", "<div style='text-align: center;'>Ausgewählter Pfad: ...</div>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
