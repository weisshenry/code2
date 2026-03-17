# dsp1 display posSet (from grades.txt) Pyside6 grid
import sys              
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout, 
                             QLineEdit, QVBoxLayout, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PySide6.QtGui import QIntValidator, QFont
import csv
import pdb

class SudokuGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Sudoku")
        self.init_ui()
        self.setFixedSize(390,500)

    def init_ui(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Make cells closer together

        # Create 9x9 Input Fields
        self.cells = []
        for row in range(9):
            row_cells = []
            for col in range(9):
                line_edit = QLineEdit()
                line_edit.setFixedSize(40, 40)
                line_edit.setAlignment(Qt.AlignCenter)
                line_edit.setFont(QFont("Arial", 8))
                # Set styling based on subgrids
                self.set_cell_style(line_edit, row, col)                
                grid_layout.addWidget(line_edit, row, col)
                row_cells.append(line_edit)
            self.cells.append(row_cells)
        main_layout.addLayout(grid_layout)        
        # Action Buttons
        self.check_btn = QPushButton("Check Solution")
        self.check_btn.clicked.connect(self.check_solution)
        main_layout.addWidget(self.check_btn)        
        # Print button
        self.print_button = QPushButton("Print Form")
        self.print_button.clicked.connect(self.print_form)
        main_layout.addWidget(self.print_button) 
        self.setLayout(main_layout)   
        
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

        # The QTextDocument has a built-in print_ method that can render its content 
        # directly to the QPrinter object
        document.print_(printer)   

    def set_cell_style(self, line_edit, row, col):
        """Adds borders to create 3x3 subgrids."""
        border_style = "QLineEdit {"
        border_style += "border: 1px solid gray;"        
        # Thicker border for subgrid edges
        if (row + 1) % 3 == 0 and row < 8:
            border_style += "border-bottom: 5px solid black;"
        if (col + 1) % 3 == 0 and col < 8:
            border_style += "border-right: 5px solid black;"
        if col == 0: border_style += " border-left: 5px solid black;"
        if row == 0: border_style += " border-top: 5px solid black;" 
        if col == 8: border_style += " border-right: 5px solid black;"
        if row == 8: border_style += " border-bottom: 5px solid black;"     
        border_style += "}"
        line_edit.setStyleSheet(border_style)

    def get_grid_data(self):
        """Retrieves values from the GUI into a 2D list."""
        data = []
        for row in range(9):
            row_data = []
            for col in range(9):
                text = self.cells[row][col].text()
                row_data.append(int(text) if text.isdigit() else 0)
            data.append(row_data)
        return data
       
    def set_grid_data(self):
        """Retrieves values from the GUI into a 2D list."""
        npx = self.read_csv_line_by_line('grades.txt')    
        for row in range(9):
            row_data = []
            for col in range(9):                
                self.cells[row][col].setText(npx[row][col])      
        return      
       
    def read_csv_line_by_line(self,filename):
       npx =[] 
       npx= [[0 for j in range(9)] for i in range(9)]    
       with open(filename, newline='') as csvfile:       
          csv_reader = csv.reader(csvfile, delimiter=',')           
          lx =0
          for row in csv_reader:              
             for gx in range(9):  
                datx= row[gx]
                datx = datx.replace(' ','')
                npx[lx][gx] = datx               
             lx = lx  +1         
       return npx      

    def check_solution(self):
        """Placeholder for validation logic."""
        #data = self.get_grid_data()
        self.set_grid_data()
        #print(data) # Replace with validation logic
        QMessageBox.information(self, "Result", "Checking logic needed!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SudokuGrid()
    window.show()
    sys.exit(app.exec())




