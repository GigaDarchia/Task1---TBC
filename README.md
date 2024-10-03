# Currency Converter

Currency Converter is a simple GUI application built with Python's `tkinter` library. The application allows users to convert amounts between various international currencies using current exchange rates.

## Features

- **Real-Time Exchange Rates**: The application fetches the latest exchange rates from the [Fawaz Ahmed's Currency API](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json).
- **User-Friendly Interface**: The application offers a simple and intuitive interface using the `tkinter` library.
- **Reset Functionality**: Easily reset the input fields and dropdown selections to their default values.

## Prerequisites

- **Python** 3.x
- Internet connection (to fetch exchange rates)
- **Pillow** library
- **Requests** library

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/GigaDarchia/Task1---TBC.git
    cd Task1---TBC
    ```

2. **Install Required Packages**:
    Ensure you have the required packages installed. You can use pip to install them:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```sh
    python main.py
    ```

## Usage

1. **Launch the application**: Upon running the script, a window titled **"Currency Converting App"** will appear.

2. **Enter Amount**: Input the amount of money you wish to convert in the provided input field.

3. **Select Currencies**: Use the dropdown menus to select the currencies you wish to convert from and to.

4. **Convert**: Click on the **"Convert"** button to see the converted value displayed.

5. **Reset**: Click on the **"Reset"** button to clear all fields and selections.

## Code Overview

- **Fetching Data**: The application fetches the list of available currencies and their latest exchange rates using the `requests` library.
- **User Interface**: The `tkinter` library is used for building the GUI.
- **Conversion Logic**: The exchange rate is applied to the user input amount to calculate the converted amount.


## Acknowledgements

- [Fawaz Ahmed's Currency API](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json) for providing real-time currency exchange rates.
- [Python](https://python.org) and its community for the tools used in this project.
