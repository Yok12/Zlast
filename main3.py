import time
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
from PyQt5.uic.properties import QtGui, QtCore

config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",    #local
    "database": "edge", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값
}

try:
    conn = mysql.connector.connect(**config)
    print(conn)
    # db select, insert, update, delete 작업 객체
    cursor = conn.cursor()
    # 실행할 select 문 구성
    sql = "SELECT * FROM non_accident"
    # cursor 객체를 이용해서 수행한다.
    cursor.execute(sql)
    # select 된 결과 셋 얻어오기
    edgeDB = cursor.fetchall()  # tuple 이 들어있는 list
    print(edgeDB)

    # DB 에 저장된 rows 출력해보기
except mysql.connector.Error as err:
   print(err)

edge = {
    't_1': [],
    't_2': [],
    't_3': [],
    't_4': [],
    't_5': [],
}

column_idx_lookup = {'t_1': 0, 't_2': 1, 't_3': 2, 't_4': 3, 't_5': 4}


# class TestThread(QThread):
#
#     def __init__(self, parent=None):
#         super().__init__()
#         self.main = parent
#         self.isRun = False
#
#     def run(self):
#         if self.isRun:
#             print("qasdasda")


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def setTableWidgetData(self):
        #기둥 헤더 이름 정하기
        line_headers = ['T1_G', 'T1_G', 'T1_G', 'T1_G', 'O']
        self.tableWidget.setVerticalHeaderLabels(line_headers)
        for k, v in edge.items():
            col = column_idx_lookup[k]
            for row, val in enumerate(v):
                item = QTableWidgetItem(val)
                if col == 4:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)

                self.tableWidget.setItem(row, col, item)

        #디비에서 값을 가져와서 테이블에 넣는 로직.
        self.num = 0
        for a in edgeDB[0]:
            self.tableWidget.setItem(self.num, 0, QTableWidgetItem(str(a)))
            self.num = self.num + 1


        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def initUI(self):
        # self.setWindow(Qt.FramelessWindowHint)
        self.setWindowTitle('Rasp_GUI')
        pixmap = QPixmap('crossroad.jpg')
        self.lbl_img = QLabel(self)
        self.lbl_img.setPixmap(pixmap)
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_img)
        self.setLayout(vbox)
        self.layout_traffic() #초기 신호등 UI 세팅
        self.Accident = QPushButton('Accident', self)  #Accident 버튼 정의
        self.Accident.move(680, 350)
        self.Accident.clicked.connect(self.test)
        # self.th = TestThread(self)
        #self.Accident.clicked.connect(lambda: self.t2())


        self.Non_Accident = QPushButton('Non_Accid', self)    #Non_Accident 버튼 정의
        self.Non_Accident.move(680, 390)
        self.Non_Accident.clicked.connect(self.test)

        #요기서부터 테이블 모양 보여주기
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(400, 40, 100, 200)

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(1)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setTableWidgetData()

        self.resize(800, 480)
        self.show()

    # @pyqtSlot()
    # def threadStart(self):
    #     if not self.th.isRun:
    #         print('메인 : 쓰레드 시작')
    #         self.th.isRun = True
    #         self.th.start()
    #
    # @pyqtSlot()
    # def threadStop(self):
    #     if self.th.isRun:
    #         print('메인 : 쓰레드 정지')
    #         self.th.isRun = False

    def reset(self):
        loop = QEventLoop()
        QTimer.singleShot(10000, loop.quit)
        loop.exec_()

    def layout_traffic(self):
            layout = QPixmap('layout.png')
            layout2 = QPixmap('layout2.png')

            #껍데기
            self.layout1_img = QLabel(self)
            self.layout1_img.setPixmap(layout)
            self.layout1_img.setGeometry(190, 300, 80, 20)

            self.layout2_img = QLabel(self)
            self.layout2_img.setPixmap(layout2)
            self.layout2_img.setGeometry(240, 160, 20, 80)

            self.layout3_img = QLabel(self)
            self.layout3_img.setPixmap(layout)
            self.layout3_img.setGeometry(140, 160, 80, 20)

            self.layout4_img = QLabel(self)
            self.layout4_img.setPixmap(layout2)
            self.layout4_img.setGeometry(140, 240, 20, 80)

            #불
            self.red1_img = QLabel(self)
            self.red1_img.setGeometry(250, 300, 20, 20)
            self.red2_img = QLabel(self)
            self.red2_img.setGeometry(240, 160, 20, 20)
            self.red3_img = QLabel(self)
            self.red3_img.setGeometry(140, 160, 20, 20)
            self.red4_img = QLabel(self)
            self.red4_img.setGeometry(140, 300, 20, 20)

            self.orange1_img = QLabel(self)
            self.orange1_img.setGeometry(230, 300, 20, 20)
            self.orange2_img = QLabel(self)
            self.orange2_img.setGeometry(240, 180, 20, 20)
            self.orange3_img = QLabel(self)
            self.orange3_img.setGeometry(160, 160, 20, 20)
            self.orange4_img = QLabel(self)
            self.orange4_img.setGeometry(140, 280, 20, 20)

            self.green1_img = QLabel(self)
            self.green1_img.setGeometry(210, 300, 20, 20)
            self.green2_img = QLabel(self)
            self.green2_img.setGeometry(240, 200, 20, 20)
            self.green3_img = QLabel(self)
            self.green3_img.setGeometry(180, 160, 20, 20)
            self.green4_img = QLabel(self)
            self.green4_img.setGeometry(140, 260, 20, 20)

            self.leftg1_img = QLabel(self)
            self.leftg1_img.setGeometry(190, 300, 20, 20)
            self.leftg2_img = QLabel(self)
            self.leftg2_img.setGeometry(240, 220, 20, 20)
            self.leftg3_img = QLabel(self)
            self.leftg3_img.setGeometry(200, 160, 20, 20)
            self.leftg4_img = QLabel(self)
            self.leftg4_img.setGeometry(140, 240, 20, 20)

            self.red2_img.setStyleSheet("background-color: red")
            self.red3_img.setStyleSheet("background-color: red")
            self.red4_img.setStyleSheet("background-color: red")
            self.green1_img.setStyleSheet("background-color: green")
            self.leftg1_img.setStyleSheet("background-color: green")

            return

    def test(self):

        self.test_1(edgeDB[0][0])
        self.test_o(edgeDB[0][4])
        self.test_2(edgeDB[0][1])
        self.test_o(edgeDB[0][4])
        self.test_3(edgeDB[0][2])
        self.test_o(edgeDB[0][4])
        self.test_4(edgeDB[0][3])
        self.test_o(edgeDB[0][4])


    def test_1(self, t):

        self.red2_img.setStyleSheet("background-color: red")
        self.red3_img.setStyleSheet("background-color: red")
        self.red4_img.setStyleSheet("background-color: red")
        self.green1_img.setStyleSheet("background-color: green")
        self.leftg1_img.setStyleSheet("background-color: green")
        self.update()
        self.repaint() #새로고침
        reset(5)

        self.red2_img.setStyleSheet("background-color: black")
        self.red3_img.setStyleSheet("background-color: black")
        self.red4_img.setStyleSheet("background-color: black")
        self.green1_img.setStyleSheet("background-color: black")
        self.leftg1_img.setStyleSheet("background-color: black")

    def test_2(self, t):
        self.red1_img.setStyleSheet("background-color: red")
        self.red3_img.setStyleSheet("background-color: red")
        self.red4_img.setStyleSheet("background-color: red")
        self.green2_img.setStyleSheet("background-color: green")
        self.leftg2_img.setStyleSheet("background-color: green")
        self.update()
        self.repaint() #새로고침
        self.reset()

        self.red1_img.setStyleSheet("background-color: black")
        self.red3_img.setStyleSheet("background-color: black")
        self.red4_img.setStyleSheet("background-color: black")
        self.green2_img.setStyleSheet("background-color: black")
        self.leftg2_img.setStyleSheet("background-color: black")

    def test_3(self, t):
        self.red1_img.setStyleSheet("background-color: red")
        self.red2_img.setStyleSheet("background-color: red")
        self.red4_img.setStyleSheet("background-color: red")
        self.green3_img.setStyleSheet("background-color: green")
        self.leftg3_img.setStyleSheet("background-color: green")
        self.update()
        self.repaint()  # 새로고침
        self.reset()

        self.red1_img.setStyleSheet("background-color: black")
        self.red2_img.setStyleSheet("background-color: black")
        self.red4_img.setStyleSheet("background-color: black")
        self.green3_img.setStyleSheet("background-color: black")
        self.leftg3_img.setStyleSheet("background-color: black")

    def test_4(self, t):
        self.red1_img.setStyleSheet("background-color: red")
        self.red2_img.setStyleSheet("background-color: red")
        self.red3_img.setStyleSheet("background-color: red")
        self.green4_img.setStyleSheet("background-color: green")
        self.leftg4_img.setStyleSheet("background-color: green")
        self.update()
        self.repaint()  # 새로고침
        self.reset()
        self.red1_img.setStyleSheet("background-color: black")
        self.red2_img.setStyleSheet("background-color: black")
        self.red3_img.setStyleSheet("background-color: black")
        self.green4_img.setStyleSheet("background-color: black")
        self.leftg4_img.setStyleSheet("background-color: black")

    def test_o(self, t):
        self.orange1_img.setStyleSheet("background-color: orange")
        self.orange2_img.setStyleSheet("background-color: orange")
        self.orange3_img.setStyleSheet("background-color: orange")
        self.orange4_img.setStyleSheet("background-color: orange")
        self.update()
        self.repaint()  # 새로고침
        self.reset()
        self.orange1_img.setStyleSheet("background-color: black")
        self.orange2_img.setStyleSheet("background-color: black")
        self.orange3_img.setStyleSheet("background-color: black")
        self.orange4_img.setStyleSheet("background-color: black")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion')) # 헤더색 변경
    # timer = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





