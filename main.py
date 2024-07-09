import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout

class MortgageCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        main_layout = QHBoxLayout()
        
        # Left column (Basic Parameters)
        basic_params_layout = QVBoxLayout()
        basic_params_layout.addWidget(QLabel("Basic Parameters"))
        
        self.basic_params = {
            "Remaining mortgage principal ($)": "250000",
            "Years remaining on mortgage": "25",
            "Interest rate on current mortgage (%)": "6.00",
            "Income tax rate (%)": "28",
            "Years you expect to remain in house": "10",
            "Points on new mortgage (%)": "1.00",
            "Other closing costs on new mortgage ($)": "2000"
        }
        
        self.basic_inputs = {}
        for label, default in self.basic_params.items():
            row = QHBoxLayout()
            lbl = QLabel(label)
            input_field = QLineEdit(default)
            row.addWidget(lbl)
            row.addWidget(input_field)
            self.basic_inputs[label] = input_field
            basic_params_layout.addLayout(row)
        
        # Right column (Advanced Parameters)
        advanced_params_layout = QVBoxLayout()
        advanced_params_layout.addWidget(QLabel("Advanced Parameters"))
        
        self.advanced_params = {
            "Rate at which you discount future costs (%)": "5",
            "Average inflation rate over life of new mortgage (%)": "3",
            "Annualized standard deviation of mortgage interest rate (%)": "1.09"
        }
        
        self.advanced_inputs = {}
        for label, default in self.advanced_params.items():
            row = QHBoxLayout()
            lbl = QLabel(label)
            input_field = QLineEdit(default)
            row.addWidget(lbl)
            row.addWidget(input_field)
            self.advanced_inputs[label] = input_field
            advanced_params_layout.addLayout(row)
        
        # Add columns to main layout
        main_layout.addLayout(basic_params_layout)
        main_layout.addLayout(advanced_params_layout)
        
        # Calculate button
        self.calculate_button = QPushButton("Calculate Optimal Refinance Rate")
        self.calculate_button.clicked.connect(self.calculateRate)
        main_layout.addWidget(self.calculate_button)
        
        # Output
        self.output_label = QLabel("")
        main_layout.addWidget(self.output_label)
        
        # Set the layout
        self.setLayout(main_layout)
        self.setWindowTitle('Mortgage Calculator')
        self.show()

    def calculateRate(self):
        # This function will use the inputs to calculate the optimal refinance rate
        # For now, it just returns 0
        # You can implement your calculation logic here
        result = 0
        self.output_label.setText(f"Optimal Refinance Rate: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MortgageCalculator()
    sys.exit(app.exec_())
