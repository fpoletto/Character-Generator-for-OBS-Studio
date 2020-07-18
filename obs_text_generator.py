from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import io
import os
import time
import shutil
from PIL import Image, ImageDraw


class MainWindow(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI
        uic.loadUi('gui.ui', self)
        self.pushButton.clicked.connect(self.update_image_file)
        self.pushButton_2.clicked.connect(self.set_single_lines)
        self.pushButton_8.clicked.connect(self.set_merged_line)
        #self.pushButton_9.clicked.connect(lambda: self.update_timer_run())
        self.pushButton_9.clicked.connect(self.set_countdown)
        self.pushButton_10.clicked.connect(self.set_clock)
        self.pushButton_11.clicked.connect(self.select_image_file)
        self.pushButton_12.clicked.connect(self.set_progress_meter)
        self.pushButton_13.clicked.connect(self.set_rotator)
        self.separator = '    '
        self.run_clock = TheClock()
        self.update_rotation = TheRotator()
        self.countdown_start = 10 #self.lineEdit_8.text()


    def set_rotator(self):
        if self.update_rotation.isRunning():
            self.update_rotation.quit()

        try:
            if self.lineEdit_32.text():
                MainWindow.rotation_sleep = int(self.lineEdit_32.text())
            else:
                if self.update_rotation.isRunning():
                    self.update_rotation.quit()
                MainWindow.rotation_sleep = 0
        except Exception as E:
            print(E)

        try:
            MainWindow.text1 = self.lineEdit_26.text()
            MainWindow.text2 = self.lineEdit_27.text()
            MainWindow.text3 = self.lineEdit_28.text()
            MainWindow.text4 = self.lineEdit_29.text()
            MainWindow.text5 = self.lineEdit_30.text()
            MainWindow.text6 = self.lineEdit_31.text()

        except Exception as E:
            print(E)

        if MainWindow.rotation_sleep != 0:
            self.update_rotation.start()


    def select_image_file(self):
        try:
            self.new_file = str(QtWidgets.QFileDialog.getOpenFileName()[0])
            self.lineEdit_17.setText(self.new_file)
            print(self.new_file)
        except Exception as E:
            print(E)

    def update_image_file(self):
        try:
            self.old_file = 'C:\\Users\\Megalos\\PycharmProjects\\obs_text_generator\\image.jpg'
            shutil.copy(self.new_file, self.old_file)
        except Exception as E:
            print(E)

    def set_clock(self):
        if self.checkBox_13.isChecked():
            self.run_clock.start()
        elif self.checkBox_14.isChecked():
            if self.run_clock.isRunning():
                self.run_clock.quit()
            f = open('clock.txt', mode='w', encoding='utf-8')
            f.write('')
            f.close()


    def set_countdown(self):
        #if self.runTimer():
         #   print(self.runTimer.isRunning())
            #self.runTimer().quit()

        if self.lineEdit_8.text():
            MainWindow.countdown_start = int(self.lineEdit_8.text())
            print(MainWindow.countdown_start)
            self.run_timer = TheCountdown()
            self.run_timer.start()

        else:
            MainWindow.countdown_start = 10
            self.run_timer = TheCountdown()
            self.run_timer.start()


    def set_single_lines(self):
        try:
            if self.lineEdit_7.text():
                self.lineEdit.setMaxLength(int(self.lineEdit_7.text()))
            f = open('line1.txt', mode='w', encoding='utf-8')
            print(self.lineEdit.text())
            f.write(self.lineEdit.text())
            f.close()
        except Exception as E:
            print(E)

        try:
            if self.lineEdit_18.text():
                self.lineEdit_2.setMaxLength(int(self.lineEdit_18.text()))
            f = open('line2.txt', mode='w', encoding='utf-8')
            print(self.lineEdit_2.text())
            f.write(self.lineEdit_2.text())
            f.close()
        except Exception as E:
            print(E)

        try:
            if self.lineEdit_19.text():
                self.lineEdit_3.setMaxLength(int(self.lineEdit_19.text()))
            f = open('line3.txt', mode='w', encoding='utf-8')
            print(self.lineEdit_3.text())
            f.write(self.lineEdit_3.text())
            f.close()
        except Exception as E:
            print(E)

        try:
            if self.lineEdit_20.text():
                self.lineEdit_4.setMaxLength(int(self.lineEdit_20.text()))
            f = open('line4.txt', mode='w', encoding='utf-8')
            print(self.lineEdit_4.text())
            f.write(self.lineEdit_4.text())
            f.close()
        except Exception as E:
            print(E)

        try:
            if self.lineEdit_21.text():
                self.lineEdit_5.setMaxLength(int(self.lineEdit_21.text()))
            f = open('line5.txt', mode='w', encoding='utf-8')
            print(self.lineEdit_5.text())
            f.write(self.lineEdit_5.text())
            f.close()
        except Exception as E:
            print(E)

        try:
            if self.lineEdit_22.text():
                self.lineEdit_6.setMaxLength(int(self.lineEdit_22.text()))
            f = open('line6.txt', mode='w', encoding='utf-8')
            print(self.lineEdit_6.text())
            f.write(self.lineEdit_6.text())
            f.close()
        except Exception as E:
            print(E)

    def set_merged_line(self):

        if self.checkBox.isChecked():
            self.separator = '■'

        if self.checkBox_2.isChecked():
            self.separator = '●'

        if self.checkBox_3.isChecked():
            self.separator = '♥'

        if self.checkBox_4.isChecked():
            self.separator = '♠'

        if self.checkBox_5.isChecked():
            self.separator = '♣'

        if self.checkBox_6.isChecked():
            self.separator = '♦'

        if self.checkBox_7.isChecked():
            self.separator = '┼'

        if self.checkBox_8.isChecked():
            self.separator = '□'

        if self.checkBox_9.isChecked():
            self.separator = '☺'

        if self.checkBox_10.isChecked():
            self.separator = '♫'

        if self.checkBox_11.isChecked():
            self.separator = '☼'

        if self.checkBox_12.isChecked():
            self.separator = '♯'

        if self.lineEdit_23.text():
            self.maxChars = int(self.lineEdit_23.text())

        else:
            self.maxChars = 256

        self.lineEdit_9.setMaxLength(int(self.maxChars))
        self.lineEdit_10.setMaxLength(int(self.maxChars))
        self.lineEdit_11.setMaxLength(int(self.maxChars))
        self.lineEdit_12.setMaxLength(int(self.maxChars))
        self.lineEdit_13.setMaxLength(int(self.maxChars))
        self.lineEdit_14.setMaxLength(int(self.maxChars))
        self.lineEdit_15.setMaxLength(int(self.maxChars))
        self.lineEdit_16.setMaxLength(int(self.maxChars))

        try:
            self.group_line = str()
            if self.lineEdit_9.text():
                self.group_line = f'{self.lineEdit_9.text()}'

            if self.lineEdit_10.text():
                self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()}'

            if self.lineEdit_11.text():
                self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()} {self.separator} {self.lineEdit_11.text()}'

            if self.lineEdit_12.text():
                self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()} {self.separator} {self.lineEdit_11.text()} {self.separator} {self.lineEdit_12.text()}'

            if self.lineEdit_13.text():
                self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()} {self.separator} {self.lineEdit_11.text()} {self.separator} {self.lineEdit_12.text()} {self.separator} ' \
                                  f'{self.lineEdit_13.text()}'

            if self.lineEdit_14.text():
                self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()} {self.separator} {self.lineEdit_11.text()} {self.separator} {self.lineEdit_12.text()} {self.separator} ' \
                                  f'{self.lineEdit_13.text()} {self.separator} {self.lineEdit_14.text()}'

            if self.lineEdit_15.text():
                self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()} {self.separator} {self.lineEdit_11.text()} {self.separator} {self.lineEdit_12.text()} {self.separator} ' \
                                  f'{self.lineEdit_13.text()} {self.separator} {self.lineEdit_14.text()} {self.separator} {self.lineEdit_15.text()}'

            if self.lineEdit_16.text():
                self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()} {self.separator} {self.lineEdit_11.text()} {self.separator} {self.lineEdit_12.text()} {self.separator} ' \
                                  f'{self.lineEdit_13.text()} {self.separator} {self.lineEdit_14.text()} {self.separator} {self.lineEdit_15.text()} {self.separator} {self.lineEdit_16.text()}'

            '''
            self.group_line = f'{self.lineEdit_9.text()} {self.separator} {self.lineEdit_10.text()} {self.separator} {self.lineEdit_11.text()} {self.separator} {self.lineEdit_12.text()} {self.separator} ' \
                              f'{self.lineEdit_13.text()} {self.separator} {self.lineEdit_14.text()} {self.separator} {self.lineEdit_15.text()} {self.separator} {self.lineEdit_16.text()} {self.separator} '
            '''
            f = open('group.txt', mode='w', encoding='utf-8')
            print(self.group_line)
            f.write(self.group_line)
            f.close()
        except Exception as E:
            print(E)


    def set_progress_meter(self):
        img = Image.new('RGBA', (200, 80), (255, 0, 0, 0))

        draw = ImageDraw.Draw(img)
        outline = 10  # line thickness
        max = 10
        #atual = int(input('Qual o total até agora? '))
        atual = int(self.lineEdit_24.text())
        x1 = 25
        y1 = 25
        x2 = 40
        y2 = 75
        cheio = 0
        vazio = 0

        # draw.rectangle((x1, y1, x2, y2), fill=(255, 0, 0), outline=(255, 255, 37, 128))
        # draw.rectangle((x1+1, y1+1, x2-1, y2-1), fill=(255, 0, 0), outline=(255, 255, 37, 128))
        # x1 += 10
        # x2 += 10
        r = 0
        while r < max:

            if r < atual:
                #draw.rectangle((x1, y1, x2, y2), fill=(0, 44, 62, 0), outline=(120, 188, 196, 0))
                #draw.rectangle((x1 + 1, y1 + 1, x2 - 1, y2 - 1), fill=(0, 44, 62, 0), outline=(120, 188, 196, 0))
                draw.rectangle((x1, y1, x2, y2), outline=(247, 248, 243, 0))
                #draw.rectangle((x1 + 1, y1 + 1, x2 - 1, y2 - 1), fill=(0, 44, 62, 0), outline=(247, 248, 243, 0))
                draw.rectangle((x1 + 1, y1 + 1, x2 - 1, y2 - 1), fill=(120, 188, 196, 0), outline=(247, 248, 243, 0))
                x1 += 16
                x2 += 16
                print(atual)
            else:
                #draw.rectangle((x1, y1, x2, y2), fill=(0, 0, 0, 0), outline=(247, 248, 243, 0))
                draw.rectangle((x1, y1, x2, y2), outline=(247, 248, 243, 0))
                draw.rectangle((x1 + 1, y1 + 1, x2 - 1, y2 - 1), outline=(247, 248, 243, 0))
                x1 += 16
                x2 += 16
                print(max)
            r += 1

        img.save('test.gif', 'GIF', transparency=0)



class TheRotator(QtCore.QThread):

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        while True:
            if MainWindow.text1:
                f = open('rotation.txt', mode='w', encoding='utf-8')
                print(MainWindow.text1)
                f.write(MainWindow.text1)
                f.close()
                time.sleep(MainWindow.rotation_sleep)
                if MainWindow.text2:
                    f = open('rotation.txt', mode='w', encoding='utf-8')
                    print(MainWindow.text2)
                    f.write(MainWindow.text2)
                    f.close()
                    time.sleep(MainWindow.rotation_sleep)
                    if MainWindow.text3:
                        f = open('rotation.txt', mode='w', encoding='utf-8')
                        print(MainWindow.text3)
                        f.write(MainWindow.text3)
                        f.close()
                        time.sleep(MainWindow.rotation_sleep)
                        if MainWindow.text4:
                            f = open('rotation.txt', mode='w', encoding='utf-8')
                            print(MainWindow.text4)
                            f.write(MainWindow.text4)
                            f.close()
                            time.sleep(MainWindow.rotation_sleep)
                            if MainWindow.text5:
                                f = open('rotation.txt', mode='w', encoding='utf-8')
                                print(MainWindow.text5)
                                f.write(MainWindow.text5)
                                f.close()
                                time.sleep(MainWindow.rotation_sleep)
                                if MainWindow.text6:
                                    f = open('rotation.txt', mode='w', encoding='utf-8')
                                    print(MainWindow.text6)
                                    f.write(MainWindow.text6)
                                    f.close()
                                    time.sleep(MainWindow.rotation_sleep)

class TheClock(QtCore.QThread):

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        while True:
            self.theTime = f'{time.localtime().tm_hour}:{str(time.localtime().tm_min).zfill(2)}'
            f = open('clock.txt', mode='w', encoding='utf-8')
            print(self.theTime)
            f.write(self.theTime)
            f.close()
            time.sleep(5)


class TheCountdown(QtCore.QThread):

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.t = MainWindow.countdown_start

        try:
            print('thread')
            while self.t:
                print('while')
                mins, secs = divmod(self.t, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                print(timeformat, end='\r')
                time.sleep(.5)
                self.t -= 1
                if timeformat == '00:01':
                    timeformat = '00:00'
                    pass
                f = io.open('timer.txt', mode='w', encoding=None)
                print(timeformat)
                f.write(str(timeformat))
                f.close()
                time.sleep(1)
        except Exception as E:
            print(E)
        #MainWindow.runTimer.quit()



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()