import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Example')
        
        # create widgets
        top_widget = QWidget(self)
        bottom_left_widget = QWidget(self)
        bottom_right_widget = QWidget(self)
        
        # set background colors for demonstration purposes
        top_widget.setStyleSheet('background-color: yellow')
        bottom_left_widget.setStyleSheet('background-color: blue')
        bottom_right_widget.setStyleSheet('background-color: green')
        
        # create layouts
        main_layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()
        
        # add widgets to layouts
        main_layout.addWidget(top_widget)
        bottom_layout.addWidget(bottom_left_widget)
        bottom_layout.addWidget(bottom_right_widget)
        main_layout.addLayout(bottom_layout)
        
        self.setLayout(main_layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
