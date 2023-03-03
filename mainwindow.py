from PyQt5.QtWidgets import QMessageBox,\
    QScrollArea, \
    QHBoxLayout, \
    QMainWindow, \
    QVBoxLayout, \
    QPushButton, \
    QFileDialog,\
    QGroupBox,\
    QRadioButton,\
    QLayout,\
    QSlider,\
    QLabel,\
    QWidget
from PyQt5.QtCore import Qt
import numpy as np
from image_widget import ImageWidget

import cv2
import os

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        '''
        Constructor. In this function, we create all the variables we will use
        in the code. If we cannot assign any value yet, we assign None. This way,
        from the beginning of the class, we know all the variables that belongs
        to the class. If not, we have to read all the code in order to know, and
        if we read the variable and it has not been created yet, the program will
        crash.        
        '''
        super(MainWindow, self).__init__(parent)

        self.right_layout = QVBoxLayout()
        self.left_layout = QVBoxLayout()
        self.main_layout = QHBoxLayout()

        self.image_widget_top = None
        self.image_widget_bottom = None

        self.initialize_widget()
        self.setWindowTitle("diqCare: Image filter method python project")
        # setting geometry
        self.setGeometry(100, 100,1000, 600)

    def initialize_widget(self):
        ## Here you start initializing your widgets
        ##add button to initialize
        self.add_button()
        ## add radio button for filter
        self.add_radio_for_filter()
        ##add file dialog
        # self.add_image()
        # add slider
        self.add_slider()
        # Add the widgets that we want to add to the MainWindow must be added
        # before this line
        self.set_main_window_layouts()

    def set_main_window_layouts(self):

        # We create scroll area to allows to slide the window, when the screen
        # size is not enough
        left_scroll = QScrollArea()
        right_scroll = QScrollArea()

        left_scroll.setWidgetResizable(True)
        right_scroll.setWidgetResizable(True)

        # The MainWindow is splitted into two areas, left and right, each of them
        # with the corresponding layouts
        left_widget = QWidget()
        right_widget = QWidget()
        main_widget = QWidget()

        left_widget.setLayout(self.left_layout)
        left_scroll.setWidget(left_widget)
        self.right_layout.addStretch(1)
        right_widget.setLayout(self.right_layout)
        right_scroll.setWidget(right_widget)

        self.main_layout.addWidget(left_scroll)
        self.main_layout.addWidget(right_scroll)
        main_widget.setLayout(self.main_layout)

        self.setCentralWidget(main_widget)

    def add_button(self):
        #create a button for reset image and filter
        button=QPushButton("Select Image ", self)
        self.right_layout.addWidget(button)
        button.clicked.connect(self.add_image)

    def add_image(self):
        image=QFileDialog.getOpenFileName(self,
            'Open file',
            '',
            "PNG files ( *.png *.jpg *.jpeg *.gif *.gif)")
        # self.right_layout.addWidget(image)
        self.add_image_widget(image)
        # print(image)
    # add filter for radio button select 
    def add_radio_for_filter(self):

        self.group_box=QGroupBox("Select Filter method")
        self.radio1=QRadioButton("Average Smoothing")
        self.radio2=QRadioButton("Gaussian Filter")
        self.radio3=QRadioButton("Laplacian Filter")
        self.radio4=QRadioButton("Sober Filter")
        self.radio5=QRadioButton("Roberts Filter")

        layout = QVBoxLayout()
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        layout.addWidget(self.radio5)
        
        self.radio1.toggled.connect(lambda:self.filter_action())
        self.radio2.toggled.connect(lambda:self.filter_action())
        self.radio3.toggled.connect(lambda:self.filter_action())
        self.radio4.toggled.connect(lambda:self.filter_action())
        self.radio5.toggled.connect(lambda:self.filter_action())

        layout.addStretch(1)
        # We set this layout to be the layout of the groupbox
        self.group_box.setLayout(layout)

        layout.setSizeConstraint(QLayout.SetMinimumSize)
        # We place this groupbox in the right layout
        self.right_layout.addWidget(self.group_box)

    def add_slider(self):
        self.slider_initial_value=21
        #add label for filter size
        label=QLabel(self)
        
        label.setText("Set Filter size")
        self.right_layout.addWidget(label)
        
        self.label_slider=QLabel(self)
        self.label_slider.setText(str(self.slider_initial_value))
        self.right_layout.addWidget(self.label_slider)

        #add slider to change filter size
        slider=QSlider(Qt.Horizontal, self)
        slider.setValue(self.slider_initial_value)
        self.right_layout.addWidget(slider)
        slider.valueChanged[int].connect(self.slider_value_change)

    def slider_value_change(self, value):
        self.label_slider.setText(str(value))
        self.slider_initial_value=value
        self.filter_action()

    def add_image_widget(self,import_image):
        # We create two instances of the custom class, to load two images
        
        self.image_widget_top = ImageWidget(self)
        self.image_widget_bottom = ImageWidget(self)
        
        # We load an image to show
        root_dir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(root_dir, 'images/Lenna_GL.png')
        filepath=import_image[0]
        img = cv2.imread(filepath, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
        self.gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if not img is None:
            self.image_widget_top.updateImage(img)
        
        self.left_layout.addWidget(self.image_widget_top)
    
    def filter_action(self):
        filter_size=self.slider_initial_value
        # if self.gray_image is None:
        #     msgBox = QMessageBox()
        #     msgBox.setIcon(QMessageBox.Information)
        #     msgBox.setText("Please select filter image")
        #     msgBox.setWindowTitle("Warning")
        #     msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #     msgBox.exec()
            
        if self.radio1.isChecked():
            kernel = np.ones((filter_size, filter_size), np.float32) / (filter_size**2)
            filtered_image = cv2.filter2D(self.gray_image, -1, kernel)
            self.filtered_image(filtered_image)
        elif self.radio2.isChecked():
            kernel = cv2.getGaussianKernel(filter_size, 0)
            filtered_image = cv2.filter2D(self.gray_image, -1, kernel * kernel.T)
            self.filtered_image(filtered_image)
        elif self.radio3.isChecked():
            if filter_size % 2 == 1 and filter_size <= 31:
                filtered_image = cv2.Laplacian(self.gray_image, -1, ksize=filter_size)
                self.filtered_image(filtered_image)
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Filter size must be odd and less than 31")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msgBox.exec()
        elif self.radio4.isChecked():
            if filter_size % 2 == 1 and filter_size <= 31:
                filtered_image = cv2.Sobel(self.gray_image, -1, 1, 1, ksize=filter_size)
                self.filtered_image(filtered_image)
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Filter size must be odd and less than 31")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msgBox.exec()
        elif self.radio5.isChecked():
            filtered_image = cv2.filter2D(self.gray_image, -1, np.array([[1, 0], [0, -1]], np.float32))
            self.filtered_image(filtered_image)
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Please select filter method")
            msgBox.setWindowTitle("Warning")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.exec()
    def filtered_image(self,img2):
             # We load another filter image to show
        if not img2 is None:
            self.image_widget_bottom.updateImage(img2)

        # We add the widget to the Left layout
        self.left_layout.addWidget(self.image_widget_bottom)