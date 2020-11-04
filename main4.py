import time
import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector


class timer_Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python Stop watch")

        # setting geometry
        self.setGeometry(700, 0, 100, 480)

        # calling method
        self.timer_Components()

        # showing all the widgets
        self.show()

    def timer_Components(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.count = 0
        self.flag = False
        self.timer_label = QLabel(self)
        self.timer_label.setGeometry(0, 0, 300, 100)

        self.timer_label.setText(str(self.count))
        self.timer_label.setFont(QFont('Arial', 25))

        start = QPushButton("Start", self)
        start.setGeometry(0, 100, 50, 40)
        start.pressed.connect(self.Start)

        pause = QPushButton("Pause", self)
        pause.setGeometry(0, 150, 50, 40)
        pause.pressed.connect(self.Pause)

        re_set = QPushButton("Re-set", self)
        re_set.setGeometry(0, 200, 50, 70)
        re_set.pressed.connect(self.Re_set)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showTime(self):
        if self.flag:
            self.count += 1
        text = str(self.count / 10)
        self.timer_label.setText(text)

    def Start(self):
        self.flag = True

    def Pause(self):
        self.flag = False

    def Re_set(self):
        self.flag = False
        self.count = 0
        self.timer_label.setText(str(self.count))


config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",  # local
    "database": "edge",  # Database name
    "port": "3306"  # port는 최초 설치 시 입력한 값
}
try:
    conn = mysql.connector.connect(**config)
    print(conn)
    # db select, insert, update, delete 작업 객체
    cursor = conn.cursor()
    sql1 = "SELECT * FROM non_accident"
    sql2 = "SELECT * FROM accident"
    # cursor 객체를 이용해서 수행한다.
    cursor.execute(sql1)
    edgeDB = cursor.fetchall()
    cursor.execute(sql2)
    edgeDB2 = cursor.fetchall()

    print(edgeDB)
    print(edgeDB2)

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


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def setTableWidgetData(self):
        # 기둥 헤더 이름 정하기
        line_headers = ['T1_G', 'T2_G', 'T3_G', 'T4_G', 'O']
        column_headers = ['Time']
        self.tableWidget1.setVerticalHeaderLabels(line_headers)
        self.tableWidget1.setHorizontalHeaderLabels(column_headers)

        # for k, v in edge.items():
        #     col = column_idx_lookup[k]
        #     for row, val in enumerate(v):
        #         item = QTableWidgetItem(val)
        #         if col == 4:
        #             item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        #
        #         self.tableWidget1.setItem(row, col, item)

        # 디비에서 값을 가져와서 테이블에 넣는 로직.

        self.num = 0
        for a in edgeDB[0]:
            self.tableWidget1.setItem(self.num, 0, QTableWidgetItem(str(a)))
            self.num = self.num + 1

        self.tableWidget1.resizeColumnsToContents()
        self.tableWidget1.resizeRowsToContents()

    def setTableWidgetData2(self):
        # 기둥 헤더 이름 정하기
        line_headers = ['T1_G', 'T2_G', 'T3_G', 'T4_G', 'O']
        column_headers = ['Time']
        self.tableWidget2.setVerticalHeaderLabels(line_headers)
        self.tableWidget2.setHorizontalHeaderLabels(column_headers)

        # 디비에서 값을 가져와서 테이블에 넣는 로직.
        self.num2 = 0
        for a in edgeDB2[0]:
            self.tableWidget2.setItem(self.num2, 0, QTableWidgetItem(str(a)))
            self.num2 = self.num2 + 1

        self.tableWidget2.resizeColumnsToContents()
        self.tableWidget2.resizeRowsToContents()

    def initUI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle('Rasp_GUI')
        pixmap = QPixmap('crossroad.jpg')
        pixmap2 = QPixmap('K-Shield_BI_12.png')
        self.lbl_img = QLabel(self)
        self.lbl_img.setPixmap(pixmap)
        self.lbl_img.setGeometry(16, 40, 380, 400)
        self.lbl_img.setStyleSheet("border : 4px solid black;")
        self.lbl_img2 = QLabel(self)
        self.lbl_img2.setPixmap(pixmap2)
        self.lbl_img2.setGeometry(720, 400, 75, 75)
        self.layout_traffic()  # 초기 신호등 UI 세팅

        self.Accident = QPushButton('Accident', self)  # Accident 버튼 정의
        self.Accident.move(500, 250)
        self.Accident.clicked.connect(self.testb)
        # self.Accident.clicked.connect(lambda: self.t2())

        self.Non_Accident = QPushButton('Non_Accid', self)  # Non_Accident 버튼 정의
        self.Non_Accident.move(400, 250)
        self.Non_Accident.clicked.connect(self.testa)

        # 요기서부터 테이블 모양 보여주기
        self.tableWidget1 = QTableWidget(self)
        self.tableWidget1.setGeometry(400, 40, 100, 200)

        self.tableWidget1.setRowCount(5)
        self.tableWidget1.setColumnCount(1)

        self.tableWidget1.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget2 = QTableWidget(self)
        self.tableWidget2.setGeometry(500, 40, 100, 200)

        self.tableWidget2.setRowCount(5)
        self.tableWidget2.setColumnCount(1)

        self.tableWidget2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setTableWidgetData()
        self.setTableWidgetData2()
        self.setGeometry(0, 0, 800, 480)

        self.show()

    def layout_traffic(self):
        layout = QPixmap('layout.png')
        layout2 = QPixmap('layout2.png')

        # 껍데기
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

        # 불
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

        return

    def testa(self):

        self.test_1(edgeDB[0][0])
        self.test_o(edgeDB[0][4])
        self.test_2(edgeDB[0][1])
        self.test_o(edgeDB[0][4])
        self.test_3(edgeDB[0][2])
        self.test_o(edgeDB[0][4])
        self.test_4(edgeDB[0][3])
        self.test_o(edgeDB[0][4])

    def testb(self):

        self.test_1(edgeDB2[0][0])
        self.test_o(edgeDB2[0][4])
        self.test_2(edgeDB2[0][1])
        self.test_o(edgeDB2[0][4])
        self.test_3(edgeDB2[0][2])
        self.test_o(edgeDB2[0][4])
        self.test_4(edgeDB2[0][3])
        self.test_o(edgeDB2[0][4])

    def test_1(self, t):

        self.red2_img.setStyleSheet("background-color: red")
        self.red3_img.setStyleSheet("background-color: red")
        self.red4_img.setStyleSheet("background-color: red")
        self.green1_img.setStyleSheet("background-color: green")
        self.leftg1_img.setStyleSheet("background-color: green")

        self.update()
        self.repaint()  # 새로고침
        time.sleep(t)

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
        self.repaint()  # 새로고침
        time.sleep(t)

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
        time.sleep(t)

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
        time.sleep(t)

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
        time.sleep(t)
        self.orange1_img.setStyleSheet("background-color: black")
        self.orange2_img.setStyleSheet("background-color: black")
        self.orange3_img.setStyleSheet("background-color: black")
        self.orange4_img.setStyleSheet("background-color: black")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = QApplication(sys.argv)

    ex = MyApp()
    #window = timer_Window()

    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    ex.setStyleSheet(dark_stylesheet)
    #window.setStyleSheet(dark_stylesheet)

    ex.show()

    sys.exit(app.exec_())
    #sys.exit(timer.exec())