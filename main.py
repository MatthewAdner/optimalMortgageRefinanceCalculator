import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QGridLayout
from PyQt5.QtGui import QDoubleValidator
from rateCalculation import calculateOptimalRate

class MortgageCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        main_layout = QVBoxLayout()

        # Grid layout for parameters
        grid_layout = QGridLayout()
        
        # Left column (Basic Parameters)
        basic_params_label = QLabel("Basic Parameters")
        grid_layout.addWidget(basic_params_label, 0, 0, 1, 2)

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
        row = 1
        for label, default in self.basic_params.items():
            lbl = QLabel(label)
            input_field = QLineEdit(default)
            input_field.setValidator(QDoubleValidator(0.0, 1000000.0, 2))
            grid_layout.addWidget(lbl, row, 0)
            grid_layout.addWidget(input_field, row, 1)
            self.basic_inputs[label] = input_field
            row += 1

        # Right column (Advanced Parameters)
        advanced_params_label = QLabel("Advanced Parameters")
        grid_layout.addWidget(advanced_params_label, 0, 2, 1, 2)

        self.advanced_params = {
            "Rate at which you discount future costs (%)": "5",
            "Average inflation rate over life of new mortgage (%)": "3",
            "Annualized standard deviation of mortgage interest rate (%)": "1.09"
        }

        self.advanced_inputs = {}
        row = 1
        for label, default in self.advanced_params.items():
            lbl = QLabel(label)
            input_field = QLineEdit(default)
            input_field.setValidator(QDoubleValidator(0.0, 100.0, 2))
            grid_layout.addWidget(lbl, row, 2)
            grid_layout.addWidget(input_field, row, 3)
            self.advanced_inputs[label] = input_field
            row += 1

        # Add grid layout to main layout
        main_layout.addLayout(grid_layout)

        # Spacer between parameters and button
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

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

    def update_params(self):
        for key in self.basic_inputs:
            self.basic_params[key] = self.basic_inputs[key].text()
        for key in self.advanced_inputs:
            self.advanced_params[key] = self.advanced_inputs[key].text()

    def calculateRate(self):
        # Update the parameter dictionaries with current input values
        self.update_params()
        # For now, it just returns 0
        result = calculateOptimalRate(
            float(self.basic_params["Remaining mortgage principal ($)"]),
            float(self.basic_params["Years remaining on mortgage"]),
            float(self.basic_params["Interest rate on current mortgage (%)"]),
            float(self.basic_params["Income tax rate (%)"]),
            float(self.basic_params["Years you expect to remain in house"]),
            float(self.basic_params["Points on new mortgage (%)"]),
            float(self.basic_params["Other closing costs on new mortgage ($)"]),
            float(self.advanced_params["Rate at which you discount future costs (%)"]),
            float(self.advanced_params["Average inflation rate over life of new mortgage (%)"]),
            float(self.advanced_params["Annualized standard deviation of mortgage interest rate (%)"])
        )
        self.output_label.setText(f"Optimal Refinance Rate: {result}")
        
        # Debugging
        print()
        print(self.basic_params)
        print(self.advanced_params)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MortgageCalculator()
    sys.exit(app.exec_())
