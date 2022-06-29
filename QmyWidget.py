import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap

from ui_Widget import Ui_Widget


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构构造函数
        self.ui = Ui_Widget()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

    # self.ui.label_Picture.load(":/QtApp/Image/Picture1.svg")

    ##=====由connectSlotByName()自动与组件的信号关联的槽函数=====
    def on_btnClose_clicked(self):  # 关闭退出
        form.close()

    def on_btnCalculate_clicked(self):  # 计算各成份体积
        num_Primer = self.ui.spinBox_Primer.value()
        num_cDNA = self.ui.spinBox_cDNA.value()
        num_Loss = self.ui.spinBox_Loss.value()
        num_Eight_Tubes = str((num_Primer * num_cDNA * 3) // 8) + " 条"
        num_Tubes = str((num_Primer * num_cDNA * 3) % 8) + " 孔"
        system_state = self.ui.checkBox_10uL.isChecked()  # 判断体系
        if system_state == True:
            T_num_Primer = str(1.0 * 3 * num_cDNA + 1.0 * num_Loss) + " µL"
            T_num_Water = str(1.5 * 3 * num_cDNA + 1.5 * num_Loss) + " µL"
            T_num_cDNA = str(2.5 * 3 * num_Primer + 2.5 * num_Loss) + " µL"
            T_num_Mix = str(5.0 * 3 * num_Primer + 5.0 * num_Loss) + " µL"
        else:
            T_num_Primer = str(2.0 * 3 * num_cDNA + 2.0 * num_Loss) + " µL"
            T_num_Water = str(3.0 * 3 * num_cDNA + 3.0 * num_Loss) + " µL"
            T_num_cDNA = str(5.0 * 3 * num_Primer + 5.0 * num_Loss) + " µL"
            T_num_Mix = str(10.0 * 3 * num_Primer + 10.0 * num_Loss) + " µL"
        self.ui.lineEdit_Primer.setText(T_num_Primer)
        self.ui.lineEdit_Water.setText(T_num_Water)
        self.ui.lineEdit_cDNA.setText(T_num_cDNA)
        self.ui.lineEdit_Mix.setText(T_num_Mix)
        self.ui.lineEdit_Eight_Tubes.setText(num_Eight_Tubes)
        self.ui.lineEdit_Tubes.setText(num_Tubes)

        self.ui.label_Picture.setPixmap(QPixmap(":/icons/Picture2.svg"))

    def on_btnReset_clicked(self):  # 重置
        self.ui.lineEdit_Primer.clear()
        self.ui.lineEdit_Water.clear()
        self.ui.lineEdit_cDNA.clear()
        self.ui.lineEdit_Mix.clear()
        self.ui.lineEdit_Eight_Tubes.clear()
        self.ui.lineEdit_Tubes.clear()
        self.ui.spinBox_Primer.setValue(0)
        self.ui.spinBox_cDNA.setValue(0)
        self.ui.spinBox_Loss.setValue(1)
        self.ui.checkBox_10uL.click()
        self.ui.label_Picture.setPixmap(QPixmap(":/icons/Picture1.svg"))


if __name__ == "__main__":  ##用于当前窗口测试
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
