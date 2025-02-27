from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resources
import mysql.connector as mc
from mysql.connector import *

class Ui_BurialForm(object):

    def setupUi(self, BurialForm):
        BurialForm.setObjectName("BurialForm")
        BurialForm.resize(1080, 650)
        BurialForm.setMaximumSize(QtCore.QSize(1080, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/resources/CCRO Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BurialForm.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(BurialForm)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 47, 26))
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(680, 50, 131, 26))
        self.label_2.setStyleSheet("font: 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 47, 26))
        self.label_3.setStyleSheet("font: 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 361, 21))
        self.label_4.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(690, 260, 131, 26))
        self.label_5.setStyleSheet("font: 12pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 47, 26))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 300, 41, 26))
        self.label_7.setStyleSheet("font: 12pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 300, 151, 26))
        self.label_8.setStyleSheet("font: 12pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 300, 131, 26))
        self.label_9.setStyleSheet("font: 12pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 340, 181, 26))
        self.label_10.setStyleSheet("font: 12pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 90, 71, 26))
        self.label_11.setStyleSheet("font: 12pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 130, 131, 26))
        self.label_12.setStyleSheet("font: 12pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(540, 130, 111, 26))
        self.label_13.setStyleSheet("font: 12pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 170, 991, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 240, 991, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(130, 190, 191, 16))
        self.label_14.setStyleSheet("font: 12pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(180, 210, 81, 16))
        self.label_15.setStyleSheet("font: 12pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(400, 178, 18, 71))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(650, 178, 18, 71))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(790, 205, 141, 16))
        self.label_17.setStyleSheet("font: 12pt \"Arial\";")
        self.label_17.setObjectName("label_17")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(409, 192, 250, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(410, 217, 250, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(510, 180, 51, 16))
        self.label_18.setStyleSheet("font: 12pt \"Arial\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(500, 205, 71, 16))
        self.label_19.setStyleSheet("font: 12pt \"Arial\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(500, 229, 71, 16))
        self.label_20.setStyleSheet("font: 12pt \"Arial\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(100, 385, 241, 16))
        self.label_21.setStyleSheet("font: 12pt \"Arial\";")
        self.label_21.setObjectName("label_21")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 420, 261, 26))
        self.label_16.setStyleSheet("font: 12pt \"Arial\";")
        self.label_16.setObjectName("label_16")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(40, 460, 311, 26))
        self.label_22.setStyleSheet("font: 12pt \"Arial\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(40, 500, 211, 26))
        self.label_23.setStyleSheet("font: 12pt \"Arial\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(40, 540, 371, 26))
        self.label_24.setStyleSheet("font: 12pt \"Arial\";")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(520, 540, 181, 26))
        self.label_25.setStyleSheet("font: 12pt \"Arial\";")
        self.label_25.setObjectName("label_25")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.clicked.connect(self.submission)
        self.submit.setGeometry(QtCore.QRect(860, 590, 171, 41))
        self.submit.setStyleSheet("font: 12pt \"Aria Black\";\n"
"background-color: #1fae51;\n"
"color: rgb(250, 255, 249);\n"
"border-radius:15px;")
        self.submit.setDefault(False)
        self.submit.setFlat(False)
        self.submit.setObjectName("submit")
        self.preview = QtWidgets.QPushButton(self.centralwidget)
        self.preview.setGeometry(QtCore.QRect(680, 590, 171, 41))
        self.preview.setStyleSheet("font: 12pt \"Aria Black\";\n"
"background-color: #eed202;\n"
"color: rgb(250, 255, 249);\n"
"border-radius:15px;")
        self.preview.setDefault(False)
        self.preview.setFlat(False)
        self.preview.setObjectName("preview")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(230, 50, 621, 531))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logos/resources/CCRO Logo78.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(100, 50, 194, 26))
        self.dateTimeEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dateTimeEdit.setStyleSheet("font: 12pt \"Arial\";\n"
"")
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setSpecialValueText("")
        self.dateTimeEdit.setProperty("showGroupSeparator", False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.ref = QtWidgets.QLineEdit(self.centralwidget)
        self.ref.setGeometry(QtCore.QRect(820, 50, 211, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ref.setFont(font)
        self.ref.setStyleSheet("color: rgb(207, 0, 3);")
        self.ref.setAlignment(QtCore.Qt.AlignCenter)
        self.ref.setObjectName("ref")
        self.nameofpayer = QtWidgets.QLineEdit(self.centralwidget)
        self.nameofpayer.setGeometry(QtCore.QRect(100, 90, 931, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nameofpayer.setFont(font)
        self.nameofpayer.setAlignment(QtCore.Qt.AlignCenter)
        self.nameofpayer.setObjectName("nameofpayer")
        self.city = QtWidgets.QLineEdit(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(160, 130, 371, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.city.setFont(font)
        self.city.setAlignment(QtCore.Qt.AlignCenter)
        self.city.setObjectName("city")
        self.province = QtWidgets.QLineEdit(self.centralwidget)
        self.province.setGeometry(QtCore.QRect(660, 130, 371, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.province.setFont(font)
        self.province.setAlignment(QtCore.Qt.AlignCenter)
        self.province.setObjectName("province")
        self.nameofdead = QtWidgets.QLineEdit(self.centralwidget)
        self.nameofdead.setGeometry(QtCore.QRect(90, 260, 591, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nameofdead.setFont(font)
        self.nameofdead.setAlignment(QtCore.Qt.AlignCenter)
        self.nameofdead.setObjectName("nameofdead")
        self.nationality = QtWidgets.QLineEdit(self.centralwidget)
        self.nationality.setGeometry(QtCore.QRect(790, 260, 241, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nationality.setFont(font)
        self.nationality.setAlignment(QtCore.Qt.AlignCenter)
        self.nationality.setObjectName("nationality")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(80, 300, 81, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.age.setFont(font)
        self.age.setAlignment(QtCore.Qt.AlignCenter)
        self.age.setObjectName("age")
        self.sex = QtWidgets.QLineEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(210, 300, 81, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sex.setFont(font)
        self.sex.setAlignment(QtCore.Qt.AlignCenter)
        self.sex.setObjectName("sex")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(440, 300, 131, 26))
        self.dateTimeEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dateTimeEdit_2.setStyleSheet("font: 12pt \"Arial\";\n"
"")
        self.dateTimeEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit_2.setSpecialValueText("")
        self.dateTimeEdit_2.setProperty("showGroupSeparator", False)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.causeofdeath = QtWidgets.QLineEdit(self.centralwidget)
        self.causeofdeath.setGeometry(QtCore.QRect(730, 300, 301, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.causeofdeath.setFont(font)
        self.causeofdeath.setAlignment(QtCore.Qt.AlignCenter)
        self.causeofdeath.setObjectName("causeofdeath")
        self.nameofcemetery = QtWidgets.QLineEdit(self.centralwidget)
        self.nameofcemetery.setGeometry(QtCore.QRect(210, 340, 821, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nameofcemetery.setFont(font)
        self.nameofcemetery.setAlignment(QtCore.Qt.AlignCenter)
        self.nameofcemetery.setObjectName("nameofcemetery")
        self.infection = QtWidgets.QLineEdit(self.centralwidget)
        self.infection.setGeometry(QtCore.QRect(300, 420, 731, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.infection.setFont(font)
        self.infection.setAlignment(QtCore.Qt.AlignCenter)
        self.infection.setObjectName("infection")
        self.embalming = QtWidgets.QLineEdit(self.centralwidget)
        self.embalming.setGeometry(QtCore.QRect(340, 460, 691, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.embalming.setFont(font)
        self.embalming.setAlignment(QtCore.Qt.AlignCenter)
        self.embalming.setObjectName("embalming")
        self.disposition = QtWidgets.QLineEdit(self.centralwidget)
        self.disposition.setGeometry(QtCore.QRect(250, 500, 781, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.disposition.setFont(font)
        self.disposition.setAlignment(QtCore.Qt.AlignCenter)
        self.disposition.setObjectName("disposition")
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(410, 540, 101, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.amount.setFont(font)
        self.amount.setText("")
        self.amount.setAlignment(QtCore.Qt.AlignCenter)
        self.amount.setReadOnly(True)
        self.amount.setObjectName("amount")
        self.collectingOfficer = QtWidgets.QLineEdit(self.centralwidget)
        self.collectingOfficer.setGeometry(QtCore.QRect(700, 540, 331, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.collectingOfficer.setFont(font)
        self.collectingOfficer.setAlignment(QtCore.Qt.AlignCenter)
        self.collectingOfficer.setObjectName("collectingOfficer")
        self.logo.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.label_17.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_16.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.submit.raise_()
        self.preview.raise_()
        self.dateTimeEdit.raise_()
        self.ref.raise_()
        self.nameofpayer.raise_()
        self.city.raise_()
        self.province.raise_()
        self.nameofdead.raise_()
        self.nationality.raise_()
        self.age.raise_()
        self.sex.raise_()
        self.dateTimeEdit_2.raise_()
        self.causeofdeath.raise_()
        self.nameofcemetery.raise_()
        self.infection.raise_()
        self.embalming.raise_()
        self.disposition.raise_()
        self.amount.raise_()
        self.collectingOfficer.raise_()
        BurialForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(BurialForm)
        QtCore.QMetaObject.connectSlotsByName(BurialForm)

    def retranslateUi(self, BurialForm):
        _translate = QtCore.QCoreApplication.translate
        BurialForm.setWindowTitle(_translate("BurialForm", "Burial Form"))
        self.label.setText(_translate("BurialForm", "DATE:"))
        self.label_2.setText(_translate("BurialForm", "REFERENCE NO."))
        self.label_3.setText(_translate("BurialForm", "NAME:"))
        self.label_4.setText(_translate("BurialForm", "BURIAL PERMIT AND FEE RECEIPT FORM"))
        self.label_5.setText(_translate("BurialForm", "NATIONALITY:"))
        self.label_6.setText(_translate("BurialForm", "AGE:"))
        self.label_7.setText(_translate("BurialForm", "SEX:"))
        self.label_8.setText(_translate("BurialForm", "CAUSE OF DEATH:"))
        self.label_9.setText(_translate("BurialForm", "DATE OF DEATH:"))
        self.label_10.setText(_translate("BurialForm", "NAME OF CEMETERY:"))
        self.label_11.setText(_translate("BurialForm", "MR./MS."))
        self.label_12.setText(_translate("BurialForm", "TO THE CITY OF:"))
        self.label_13.setText(_translate("BurialForm", "PROVINCE OF:"))
        self.label_14.setText(_translate("BurialForm", "PERMISSION IS HEREBY"))
        self.label_15.setText(_translate("BurialForm", "GRANTED"))
        self.label_17.setText(_translate("BurialForm", "THE REMAINS OF"))
        self.label_18.setText(_translate("BurialForm", "INTER"))
        self.label_19.setText(_translate("BurialForm", "DISINTER"))
        self.label_20.setText(_translate("BurialForm", "REMOVE"))
        self.label_21.setText(_translate("BurialForm", "IN CASE OF DISINTERNMENT -"))
        self.label_16.setText(_translate("BurialForm", "INFECTIOUS OR NON-INFECTIOUS:"))
        self.label_22.setText(_translate("BurialForm", "BODY EMBALMED OR NOT EMBALMED:"))
        self.label_23.setText(_translate("BurialForm", "DISPOSITION OF REMAINS:"))
        self.label_24.setText(_translate("BurialForm", "AMOUNT OF THE FEE PER CITY ORDINANCE:  ₱"))
        self.label_25.setText(_translate("BurialForm", "COLLECTING OFFICER:"))
        self.submit.setText(_translate("BurialForm", "SUBMIT"))
        self.preview.setText(_translate("BurialForm", "PREVIEW"))
        self.dateTimeEdit.setDisplayFormat(_translate("BurialForm", "dd-MM-yyyy"))
        self.ref.setInputMask(_translate("BurialForm", "0000009"))
        self.age.setInputMask(_translate("BurialForm", "00"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("BurialForm", "dd-MM-yyyy"))

            #auto display payment
        global amount
        amount = int (10)
        self.amount.setText(str(amount))
        
        #warning message
    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()

    def pop_window_success(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("{}".format(text))
        msg.setWindowTitle("{}".format(text))
        msg.exec_()
        

    def user_input(self):
        if self.ref.text()=="":
                self.pop_window("Reference Number is required.")
        else:
        
                refNum =self.ref.text()
                nameOfpayer = self.nameofpayer.text().upper()
                city = self.city.text().upper()
                province = self.province.text().upper()
                NameofDead =self.nameofdead.text().upper()
                nationality = self. nationality.text().upper()
                age = self.age.text().upper()
                sex = self.sex.text().upper()
                causeOfDeath = self.causeofdeath.text().upper()
                NameofCemetery = self.nameofcemetery.text().upper()
                infect = self.infection.text().upper()
                embalm = self.embalming.text().upper()
                dispo = self.disposition.text().upper()
                officer =self.collectingOfficer.text().upper()

                dateOfDeath = self.dateTimeEdit_2.date().toString("dd-MM-yyyy")
                dateToday = self.dateTimeEdit.date().toString("dd-MM-yyyy")

                #print (refNum+" "+dateToday+" "+nameOfpayer.+" "+city+" "+province+" "+NameofDead+" "+nationality+" "+age+" "+sex+" "+dateOfDeath+" "+causeOfDeath+" "+NameofCemetery+" "+infect+" "+embalm+" "+dispo+" "+str(amount)+" "+officer)

        con = mc.connect(
                host="localhost",
                user="root",
                passwd="",
                database="ccro_cdo"
            )
        with con:
                cur = con.cursor()
                add_data ="INSERT INTO burial_permit_data (refNum,date,payer,city,prov,nameOfdead,nat,age,sex,dateofdeath,causeofdeath,nameofcemetery,infect,embalm,dispo,amt,colOfficer) VALUES(%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (refNum,dateToday,nameOfpayer,city,province,NameofDead,nationality,age,sex,dateOfDeath,causeOfDeath,NameofCemetery,infect,embalm,dispo,amount,officer)
                
                cur.execute(add_data)

                
                con.commit()
                cur.close()
                con.close()
                #BurialForm.close()
                self.pop_window_success("Data Saved.")
                

    def submission(self):
                self.user_input()

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BurialForm = QtWidgets.QMainWindow()
    ui = Ui_BurialForm()
    ui.setupUi(BurialForm)
    BurialForm.show()
    sys.exit(app.exec_())
