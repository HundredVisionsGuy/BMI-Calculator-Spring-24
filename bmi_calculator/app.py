import sys
import controller
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        self.resize(640, 480)
        self.setContentsMargins(12, 12, 12, 12)
        self.bmi = 0.0

        # Create our widgets
        title_label = QLabel("BMI Calculator",
                             alignment=Qt.AlignmentFlag.AlignTop)
        title_label.setFont(QFont("Calibri", 22, 800, True))

        # weight input
        weight_label = QLabel("Weight: ")
        self.weight_input = QSpinBox(alignment=Qt.AlignmentFlag.AlignLeft)
        self.weight_input.setMaximum(1400)
        self.weight_input.setMinimum(10)
        self.weight_input.setSuffix(" lbs.")
        self.weight_input.setValue(140)
        weight_layout = QHBoxLayout()
        weight_layout.setContentsMargins(0, 6, 0, 14)
        weight_layout.addWidget(weight_label)
        weight_layout.addWidget(self.weight_input)
        weight_layout.addStretch()

        # money input
        height_label = QLabel("Height: ")
        self.height_input = QSpinBox(alignment=Qt.AlignmentFlag.AlignLeft)
        self.height_input.setValue(60)
        self.height_input.setMaximum(120)
        self.height_input.setMinimum(24)
        self.height_input.setSuffix(" in.")

        height_layout = QHBoxLayout()
        height_layout.addWidget(height_label)
        height_layout.addWidget(self.height_input)
        height_layout.addStretch()

        calculate_button = QPushButton("Calculate")
        calculate_button.setCheckable(True)
        calculate_button.clicked.connect(self.calculate_bmi)

        clear_button = QPushButton("Clear")
        clear_button.setCheckable(True)
        clear_button.clicked.connect(self.clear_screen)

        action_layout = QHBoxLayout()
        action_layout.addWidget(calculate_button)
        action_layout.addWidget(clear_button)

        self.display_label = QTextEdit("")

        layout = QVBoxLayout()

        # Add widgets to the layout
        layout.addWidget(title_label)
        layout.addLayout(weight_layout)
        layout.addLayout(height_layout)
        layout.addLayout(action_layout)
        layout.addWidget(self.display_label)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def calculate_bmi(self):
        # Get data from inputs
        weight = self.weight_input.value()
        height = self.height_input.value()

        self.bmi = controller.calculate_bmi(weight, height)
        output = controller.format_output(self.bmi)
        self.display_label.setText(output)

    def clear_screen(self):
        pass


app = QApplication(sys.argv)
# app.setStyle("Fusion")
app.setFont(QFont("Calibri", 14))
window = MainWindow()
window.show()

app.exec()
