import sys
from time import process_time
from tokenize import Double
from PyQt5 import QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainFrom(QMainWindow):
    def __init__(self):
        super(MainFrom,self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(200,200,400,400)
        self.initUI()

    def initUI(self):
       
        self.kutu=QtWidgets.QLineEdit(self)
        self.kutu.setAlignment(Qt.AlignRight)
        self.kutu.resize(400,80)
        self.kutu.setStyleSheet("font:25pt Arial Bold;border:1px solid gray;border-radius:5px;background-color:#e6e6fa;")
        self.kutu.move(0,0)


        btn_number=[]
        for i in range(1,10):
            i=QtWidgets.QPushButton(str(i),self)
            i.setFont(QFont("Arial",20))
            i.resize(80,80)
            i.clicked.connect(self.EnterNumber)
            btn_number.append(i)
        
        btn_text=0
        for i in range(0,3):
            for k in range(0,3):
                btn_number[btn_text].move(k*80,80+i*80)
                btn_text+=1
        
           
        self.sifirla=QtWidgets.QPushButton(self)
        self.sifirla.setFont(QFont("Arial",20))
        self.sifirla.setText("C")
        self.sifirla.resize(80,80)
        self.sifirla.move(0,320)
        self.sifirla.clicked.connect(self.EnterNumber)
        
        self.sifir=QtWidgets.QPushButton(self)
        self.sifir.setFont(QFont("Arial",20))
        self.sifir.setText("0")
        self.sifir.resize(80,80)
        self.sifir.move(80,320)       
        self.sifir.clicked.connect(self.Operator)

        self.nokta=QtWidgets.QPushButton(self)
        self.nokta.setFont(QFont("Arial",20))
        self.nokta.setText(".")
        self.nokta.resize(80,80)
        self.nokta.move(160,320)
        self.nokta.clicked.connect(self.Operator)

        self.yuzde=QtWidgets.QPushButton(self)
        self.yuzde.setFont(QFont("Arial",20))
        self.yuzde.setText("%")
        self.yuzde.resize(80,80)
        self.yuzde.move(320,160)
        self.yuzde.clicked.connect(self.Operator)

        self.hesapla=QtWidgets.QPushButton(self)
        self.hesapla.setFont(QFont("Arial",20))
        self.hesapla.setText("=")
        self.hesapla.resize(80,160)
        self.hesapla.move(320,240)
        self.hesapla.clicked.connect(self.topla)

        self.silme=QtWidgets.QPushButton(self)
        self.silme.setFont(QFont("Arial",20))
        self.silme.setText("<")
        self.silme.resize(80,80)
        self.silme.move(320,80)
        self.silme.clicked.connect(self.EnterNumber)

        self.topla=QtWidgets.QPushButton(self)
        self.topla.setFont(QFont("Arial",20))
        self.topla.setText("+")
        self.topla.resize(80,80)
        self.topla.move(240,80)
        self.topla.clicked.connect(self.Operator)

        self.carpma=QtWidgets.QPushButton(self)
        self.carpma.setFont(QFont("Arial",20))
        self.carpma.setText("*")
        self.carpma.resize(80,80)
        self.carpma.move(240,240)
        self.carpma.clicked.connect(self.Operator)

        self.cıkarma=QtWidgets.QPushButton(self)
        self.cıkarma.setFont(QFont("Arial",20))
        self.cıkarma.setText("-")
        self.cıkarma.resize(80,80)
        self.cıkarma.move(240,160)
        self.cıkarma.clicked.connect(self.Operator)

        self.bolme=QtWidgets.QPushButton(self)
        self.bolme.setFont(QFont("Arial",20))
        self.bolme.setText("/")
        self.bolme.resize(80,80)
        self.bolme.move(240,320)
        self.bolme.clicked.connect(self.Operator)
    
    def EnterNumber(self):
        
        btn_text=self.sender().text()
       
        metin=self.kutu.text()+btn_text
        tut=btn_text
        
        
        if tut.find("<")==-1:
            self.kutu.setText(self.kutu.text()+btn_text)
        if not tut.find("<")==-1:
            self.kutu.setText(metin[0:metin.find("<")-1])
        if not tut.find("C")==-1 :
            self.kutu.setText("")
     
        
        
            
        


    def Operator(self):

        btn_text=self.sender().text()    
        ihtimaler=("++","+.","+%","+-","+*","+/","-.","-%","--","-+","-*","-/","**","*.","*%","*+","*-","*/","//","/+","/-","/*","/.","/%","..",".+",".-",".*","./",".%","%+","%-","%/","%*","%.","%%")
       
        tut=self.kutu.text()+btn_text 
        

        if not self.kutu.text() ==""   :
            
            if ihtimaler.count(tut[len(tut)-2:len(tut)])==False:
                
                self.kutu.setText(self.kutu.text()+btn_text)
                 
                
                
            
    

    def topla(self):
        metin=self.kutu.text()
       
        topla=eval(metin)
        self.kutu.setText(str(topla))

        




def app():
    app=QApplication(sys.argv)
    win=MainFrom()
    win.show()
    sys.exit(app.exec_())

app()