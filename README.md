# Light Bill Calculator

## Project Overview

The Light Bill Calculator is a Python-based application designed to estimate electricity bills based on user input. 
The application features a graphical user interface (GUI) built with Tkinter, allowing users to input relevant details 
and select between normal and tiered billing plans. The calculator supports various utility providers and calculates 
estimated bills based on user-defined parameters.

## Features

- **Utility Provider Selection**: Choose from a list of predefined utility providers, each with its own base rate and energy charge.
- **Normal Billing Plan**: Input base charge, energy charge, and kilowatts used to calculate the bill for a standard plan.
- **Tiered Billing Plan**: Enter details for a tiered billing structure, including multiple tier limits and corresponding rates,
- to compute the bill based on different usage tiers.
- **Dynamic GUI**: Switch between normal and tiered billing plans using an interactive interface.

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Code Overview](#code-overview)
5. [Contributing](#contributing)
6. [License](#license)

## Technologies Used

- **Python**: Programming language used for the application.
- **Tkinter**: Python library for creating the GUI.
- **Custom Modules**: 
  - `functions.py`: Contains functions for calculating bills.
  - `Classes.py`: Defines classes for handling utility provider data.
  - `GUI_functions.py`: Provides utility functions for GUI operations.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/light-bill-calculator.git
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. No additional dependencies are required beyond the Python standard library.

3. **Run the Application:**
   Navigate to the project directory and run the main Python file:
   ```bash
   python light_bill_calculator.py
   ```

## Usage

1. **Select Utility Provider:**
   Click on the buttons to choose a utility provider from the list. The selected provider's name and details will be displayed.

2. **Choose Billing Plan:**
   - **Normal Plan**: Enter the base charge, energy charge in cents, and kilowatts used. Click the "Calculate!" button to get the estimated bill.
   - **Tiered Plan**: Enter base charge, tier limits, tier rates, and total kilowatts used. Click the "Calculate!" button to compute the estimated bill based on the tiered structure.

## Code Overview

- **Main Application (`light_bill_calculator.py`)**:
  - Sets up the Tkinter GUI and frames for different functionalities.
  - Provides interaction handlers for selecting utility providers and calculating bills.

- **Utility Provider Classes (`Classes.py`)**:
  - Defines the `tdu` class to represent different utility providers with base rates and energy charges.
    ```python
    # TDU class declaration
    class tdu:
        def __init__(self, name, b, e):
            self.name = name
            self.b = b
            self.e = e
    ```

- **Billing Calculation Functions (`functions.py`)**:
  - Contains functions `getbill` and `getTbill` to compute the estimated bill based on the input parameters.
    ```python
    def getbill(e, k, tc, bc, tb):
        return((e * k) + (tc * k) + bc + tb)

    def getTbill(b, l1, c1, l2, c2, c3, k, te, tb):
        sum = float(0)
        if k > l2:
            sum += c1 * l1
            sum += c2 * (l2 - l1 + 1)
            sum += c3 * (k - l2)
        elif l2 >= k > l1:
            sum += c1 * l1
            sum += c2 * (k - l1)
        else:
            sum += c1 * k
        return sum + (te * k) + b + tb
    ```

- **GUI Utility Functions (`GUI_functions.py`)**:
  - Provides functions for managing GUI frame visibility and interactions.


## License

This project is licensed under the MIT License.

---
