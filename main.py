import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QComboBox, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon

class FontAdjusterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font and Color Adjuster")
        self.setWindowIcon(QIcon("asset/slider.png"))
        self.setMinimumSize(900, 600)


        # === LABEL UTAMA (NIM) ===
        self.label = QLabel("F1D022061")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 40))
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.label.setFixedHeight(300)
        self.label.setAutoFillBackground(True)

        # === FOOTER ===
        self.footer = QLabel("Created by\nM Ilham Abdul Shaleh\nF1D022061")
        self.footer.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.footer.setStyleSheet("font-size: 8pt; padding: 5px; color: gray;")

        # === FONT SIZE SLIDER ===
        fontSizeLabel = QLabel("Font Size")
        self.fontSizeSlider = QSlider(Qt.Horizontal)
        self.fontSizeSlider.setMinimum(20)
        self.fontSizeSlider.setMaximum(60)
        self.fontSizeSlider.setValue(40)
        self.fontSizeSlider.setFixedHeight(30)
        self.fontSizeSlider.valueChanged.connect(self.updateFontSize)

        # === FONT COLOR (GRAYSCALE) SLIDER ===
        fontColorLabel = QLabel("Font Color (Grayscale)")
        self.fontColorSlider = QSlider(Qt.Horizontal)
        self.fontColorSlider.setMinimum(0)
        self.fontColorSlider.setMaximum(255)
        self.fontColorSlider.setValue(0)
        self.fontColorSlider.setFixedHeight(30)
        self.fontColorSlider.valueChanged.connect(self.updateFontColor)

        # === BACKGROUND COLOR SLIDER ===
        bgColorLabel = QLabel("Background Color (Grayscale)")
        self.bgColorSlider = QSlider(Qt.Horizontal)
        self.bgColorSlider.setMinimum(0)
        self.bgColorSlider.setMaximum(255)
        self.bgColorSlider.setValue(255)
        self.bgColorSlider.setFixedHeight(30)
        self.bgColorSlider.valueChanged.connect(self.updateBackgroundColor)

        # === FONT FAMILY COMBOBOX ===
        fontFamilyLabel = QLabel("Font Family")
        self.fontFamilyCombo = QComboBox()
        self.fontFamilyCombo.addItems([
            "Arial",
            "Comic Sans MS",
            "Times New Roman",
            "Courier New",
            "Calibri",
            "Verdana",
            "Georgia",
            "Tahoma"
        ])
        self.fontFamilyCombo.setFixedHeight(50)
        self.fontFamilyCombo.currentIndexChanged.connect(self.updateFontFamily)
        self.fontFamilyCombo.setStyleSheet("padding: 15px;")

        # === LAYOUT ===
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        layout.addWidget(fontSizeLabel)
        layout.addWidget(self.fontSizeSlider)

        layout.addWidget(fontColorLabel)
        layout.addWidget(self.fontColorSlider)

        layout.addWidget(bgColorLabel)
        layout.addWidget(self.bgColorSlider)

        layout.addWidget(fontFamilyLabel)
        layout.addWidget(self.fontFamilyCombo)

        layout.addStretch()
        layout.addWidget(self.footer)

        self.setLayout(layout)

        # Inisialisasi tampilan awal
        self.updateFontColor()
        self.updateBackgroundColor()

    def updateFontSize(self):
        currentFont = self.label.font()
        newSize = self.fontSizeSlider.value()
        currentFont.setPointSize(newSize)
        self.label.setFont(currentFont)

    def updateFontColor(self):
        gray = self.fontColorSlider.value()
        self.label.setStyleSheet(f"color: rgb({gray}, {gray}, {gray});")

    def updateBackgroundColor(self):
        value = self.bgColorSlider.value()
        color = QColor(value, value, value)
        palette = self.label.palette()
        palette.setColor(QPalette.Window, color)
        self.label.setPalette(palette)

    def updateFontFamily(self):
        family = self.fontFamilyCombo.currentText()
        size = self.fontSizeSlider.value()
        self.label.setFont(QFont(family, size))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontAdjusterApp()
    window.show()
    sys.exit(app.exec_())
