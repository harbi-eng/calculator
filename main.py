from PyQt5 import QtWidgets as qtw , QtCore as qtc,QtGui as qtg
from calc import  Ui_Form
from math import e, sqrt, pi,sin,cos,tan,sinh,cosh,tanh,log10,log
import  re

class window(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.newtext=False
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connections()


    def clear(self):
        self.ui.line.setText("")

    def delet(self):
        text=self.ui.line.text()
        if len(text):
            self.ui.line.setText(text[:-1])
#1+2*5^ (7)
#5*2+1
    def power(self,data):
        data=data.split('^')
        reversed_data=data[0][::-1]
        for index,char in enumerate(reversed_data):
            if not char.isdigit():
                data=data[0][:-index]+'pow('+data[0][-index:]+','+data[1][1:]
                break

        print(data)
        return data

    def calc(self):
        text = self.ui.line.text()
        text=text.replace('x','*').replace('π','pi').replace('√','sqrt').replace('ln(','log(e,').replace('−','-').replace('÷','/')
        if text.find('^')>0:
            text=self.power(text)
        try:
            while text[0]=='0':
                text=text.replace('0','',1)

            ans = eval(text)
            self.ui.line.setText(str(ans))
        except TypeError as e:
            print(e.args)

    def print_sign(self):
        button = self.sender()
        self.ui.line.setText(self.ui.line.text()+button.text())

    def sign_with_pracket(self):
        button = self.sender()
        self.ui.line.setText(self.ui.line.text()+button.text()+'(')




    def connections(self):
        self.ui.zero.clicked.connect(self.print_sign)
        self.ui.one.clicked.connect(self.print_sign)
        self.ui.two.clicked.connect(self.print_sign)
        self.ui.three.clicked.connect(self.print_sign)
        self.ui.four.clicked.connect(self.print_sign)
        self.ui.five.clicked.connect(self.print_sign)
        self.ui.six.clicked.connect(self.print_sign)
        self.ui.seven.clicked.connect(self.print_sign)
        self.ui.eghit.clicked.connect(self.print_sign)
        self.ui.nine.clicked.connect(self.print_sign)
        self.ui.pi.clicked.connect(self.print_sign)
        self.ui.add.clicked.connect(self.print_sign)
        self.ui.sub.clicked.connect(self.print_sign)
        self.ui.div.clicked.connect(self.print_sign)
        self.ui.mult.clicked.connect(self.print_sign)
        self.ui.dot.clicked.connect(self.print_sign)
        self.ui.mod.clicked.connect(self.print_sign)
        self.ui.exp.clicked.connect(self.print_sign)

        self.ui.open.clicked.connect(self.print_sign)
        self.ui.close.clicked.connect(self.print_sign)

        self.ui.delete_2.clicked.connect(self.delet)
        self.ui.clear.clicked.connect(self.clear)

        self.ui.eq.clicked.connect(self.calc)

        self.ui.sin.clicked.connect(self.sign_with_pracket)
        self.ui.sinh.clicked.connect(self.sign_with_pracket)
        self.ui.cos.clicked.connect(self.sign_with_pracket)
        self.ui.cosh.clicked.connect(self.sign_with_pracket)
        self.ui.tan.clicked.connect(self.sign_with_pracket)
        self.ui.tanh.clicked.connect(self.sign_with_pracket)

        self.ui.log.clicked.connect(self.sign_with_pracket)
        self.ui.ln.clicked.connect(self.sign_with_pracket)
        self.ui.sqrt.clicked.connect(self.sign_with_pracket)
        self.ui.pow.clicked.connect(self.sign_with_pracket)


if __name__ == '__main__':
    app = qtw.QApplication([])
    calc = window()
    calc.show()

    app.exec_()





