import sys
import cv2
import ipaddress 
import datetime
from PyQt5 import  QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QMainWindow,QDialog,QApplication

class Recorder(QMainWindow):
    def __init__(self):
        super(Recorder,self).__init__()
        loadUi('reco.ui',self)
        self.setWindowIcon(QtGui.QIcon('Video_Recorder_red-Icon_16px.png'))
        self.setWindowTitle("Video Rescorder")
        self.logic=0
        self.START.clicked.connect(self.STARTclicked)
        self.TEXT.setText('Please Press "Enter" to record video')
        self.STOP.clicked.connect(self.STOPclicked)
        self.EXIT.clicked.connect(self.Exitclicked)
    
    @pyqtSlot()
    def STARTclicked(self):
        self.logic=1
        cap = cv2.VideoCapture(self.QLineEdit.text())
        cap.set(3, 1280)
        cap.set(4, 720)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        date = datetime.datetime.now()
        out=cv2.VideoWriter('Capture/video_%s-%s-%sT%sH%sm%ss.avi'%(date.year,date.month,date.day,date.hour,date.minute,date.second),fourcc,20.0,(1280,720))
        while(cap.isOpened()):
            ret,frame = cap.read()
            if ret ==True:
                self.displayImage(frame,1)
                cv2.waitKey()
                if(self.logic==1):
                    out.write(frame)
                    self.TEXT.setText('video recording Start')
                if(self.logic==0):
                    self.TEXT.setText('video recording Stop')
                    break
            else:
                print('return not found')

        cap.release()
        cv2.destroyAllWindows()



    def STOPclicked(self):
        ret = QMessageBox.question(self, 'Save', "Are you want to save ", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            self.logic=0

    def Exitclicked(self):
        cv2.destroyAllWindows()

    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if(img.shape[2])==4:
                qformat=QImage.Format_RGBA888
            else:
                qformat=QImage.Format_RGB888
                
        
        img=QImage(img,img.shape[1],img.shape[0],qformat)
        img=img.rgbSwapped()

        self.imgLabel.setPixmap(QPixmap.fromImage(img))

app=QApplication(sys.argv)
window=Recorder()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exit')



 



                
