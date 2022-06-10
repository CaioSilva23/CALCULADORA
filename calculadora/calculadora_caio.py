import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):  # A QMainWindow classe fornece uma janela principal do aplicativo
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora CAIO')  # TITULO DO APP
        self.setFixedSize(300, 400)  # DEFINE O TAMANHO PADRÃO DO APP
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # CRIANDO O DISPLAY
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)  # DESABILITANDO O INPUT DO DISPLAY
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px;} '
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # CRIANDO OS BOTÕES E ESTILOS
        self.add_btn(QPushButton('7'), 1, 0, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('8'), 1, 1, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('9'), 1, 2, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('+'), 1, 3, 1, 1,None,'background: #5d8b8c; color: #fff; font-weight:700')
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),  # LIMPANDO O DISPLAY
            'background: #e6760b; color: #fff; font-weight:700'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('5'), 2, 1, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('6'), 2, 2, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('-'), 2, 3, 1, 1,None,'background: #5d8b8c; color: #fff; font-weight:700')
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]  # LIMPANDO O DISPLAY DE UM EM UM ELEMENTO
            ),
            'background: #5d8b8c; color: #fff; font-weight:700'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('2'), 3, 1, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('3'), 3, 2, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('/'), 3, 3, 1, 1,None,'background: #5d8b8c; color: #fff; font-weight:700')
        self.add_btn(QPushButton(''), 3, 4, 1, 1,None,'background: #5d8b8c; color: #fff; font-weight:700')

        self.add_btn(QPushButton('.'), 4, 0, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('0'), 4, 1, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton(''), 4, 2, 1, 1,None,'background: #A9A9A9; color: #fff; font-weight:700')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1,None,'background: #5d8b8c; color: #fff; font-weight:700')
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.resultado,
            'background: #5d8b8c; color: #fff; font-weight:700'
        )


        self.setCentralWidget(self.cw)  # SETANDO O WIDGET CENTRAL COMO CW

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):  # MÉTODO CRIADO PARA ADICIONAR BOTÕES
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)
        if style: # ESTILO DOS BOTÕES
            btn.setStyleSheet(style)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def resultado(self):
        try:
            self.display.setText(
                str(eval(self.display.text())) # AVALIANDO A CONTA DO DISPLAY
            )
        except Exception as e:
            self.display.setText('Conta Inválida!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec()
