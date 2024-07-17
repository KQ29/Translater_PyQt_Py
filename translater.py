import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QMessageBox, QComboBox, QLabel
from PyQt6.QtGui import QIcon
from googletrans import Translator, LANGUAGES

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Translator')
        self.setGeometry(100, 100, 800, 600)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        layout = QVBoxLayout()


        self.input_language_label = QLabel('Input Language:')
        self.input_language_label.setStyleSheet("QLabel { color: #81A1C1; font-size: 14px; }")
        layout.addWidget(self.input_language_label)
        self.input_language_combo = QComboBox()
        self.input_language_combo.addItem("Choose the language")
        self.input_language_combo.addItems([lang.capitalize() for lang in LANGUAGES.values()])
        layout.addWidget(self.input_language_combo)


        self.output_language_label = QLabel('Output Language:')
        self.output_language_label.setStyleSheet("QLabel { color: #81A1C1; font-size: 14px; }")
        layout.addWidget(self.output_language_label)
        self.output_language_combo = QComboBox()
        self.output_language_combo.addItem("Choose the language")
        self.output_language_combo.addItems([lang.capitalize() for lang in LANGUAGES.values()])
        layout.addWidget(self.output_language_combo)


        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)


        self.translate_button = QPushButton('Translate')
        layout.addWidget(self.translate_button)


        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)


        central_widget.setLayout(layout)


        self.translate_button.clicked.connect(self.translate_text)


        self.translator = Translator()

 
        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E3440;
            }
            QLabel {
                font-size: 14px;
            }
            QComboBox {
                background-color: #4C566A;
                color: #D8DEE9;
            }
            QComboBox QAbstractItemView {
                background-color: #4C566A;
                color: #D8DEE9;
                selection-background-color: #81A1C1;
                selection-color: #2E3440;
            }
            QTextEdit {
                background-color: #3B4252;
                color: #D8DEE9;
            }
            QPushButton {
                background-color: #5E81AC;
                color: #ECEFF4;
                border: none;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
            QMessageBox {
                background-color: #4C566A;
                color: #ECEFF4;
                border-radius: 5px;
            }
        """)

    def translate_text(self):
        input_text = self.input_text.toPlainText()


        if not input_text.strip():
            QMessageBox.warning(self, 'Warning', 'Please enter text to translate.')
            return

        try:
 
            input_lang = None
            if self.input_language_combo.currentIndex() > 0:
                input_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.input_language_combo.currentText().lower())]

            output_lang = None
            if self.output_language_combo.currentIndex() > 0:
                output_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.output_language_combo.currentText().lower())]

            if input_lang and output_lang:

                result = self.translator.translate(input_text, src=input_lang, dest=output_lang)
                translated_text = result.text
                self.output_text.setPlainText(translated_text)
            else:
                QMessageBox.warning(self, 'Warning', 'Please choose both input and output languages.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to translate text: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = TranslatorApp()
    translator.show()
    sys.exit(app.exec())
