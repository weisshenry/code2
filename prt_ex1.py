#  print form example
import sys    
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                               QVBoxLayout, QWidget, QTextEdit)
from PySide6.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PySide6.QtGui import QTextDocument, QPainter
import pdb

class PrintFormExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Print Form Example")
        self.setGeometry(100, 100, 600, 400)

        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Text edit area (simulates a form/document content)
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText("This is the content text (HTML) here.")
        layout.addWidget(self.text_edit)

        # Print button
        self.print_button = QPushButton("Print Form")
        self.print_button.clicked.connect(self.print_form)
        layout.addWidget(self.print_button)

    def print_form(self):
        # Create a QPrinter object
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        
        # Create a QPrintPreviewDialog object and pass the printer
        preview_dialog = QPrintPreviewDialog(printer, self)
        
        # Connect the paintRequested signal to our custom paint function
        preview_dialog.paintRequested.connect(self.handle_paint_requested)
        
        # Execute the dialog (shows the print preview window)
        preview_dialog.exec()

    def handle_paint_requested(self, printer):
        # This function is called QPrintPreviewDialog when a page needs to be drawn
        
        # Get the document content from the QTextEdit widget
        document = self.text_edit.document()
        pdb.set_trace()
        # The QTextDocument has a built-in print_ method that can render its content 
        # directly to the QPrinter object
        document.print_(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrintFormExample()
    window.show()
    sys.exit(app.exec())

