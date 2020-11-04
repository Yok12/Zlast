# main.py : 두개의 파이썬 파일을 불러와서 하나로 묶는 코드입니다.

import sys
from PyQt5.QtWidgets import QApplication
from SliderDialog.Slider import Slider_Dialog
from ProgressDialog.Progress import ProgressBar_Dialog

if __name__ == '__main__':
    app = QApplication(sys.argv)

    sd = Slider_Dialog()

    pb = ProgressBar_Dialog()

    pb.make_connection(sd)

    sys.exit(app.exec_())