# AI-Enhanced Calculator

## Overview

The **AI-Enhanced Calculator** is a web-based application that not only performs standard calculations but also integrates AI capabilities to predict the next calculation a user might want to perform. This project showcases the use of Natural Language Processing (NLP) in a calculator, enabling it to understand and process user input more intelligently.

## Features

- **Standard Calculations:** Perform basic arithmetic operations.
- **AI Predictions:** Predicts the next calculation based on the current input using NLP.
- **Web Interface:** User-friendly web interface for inputting calculations.

## Project Structure

- **main.py:**  
  The main script that handles the core logic of the calculator, including processing user inputs and interacting with the AI model.

- **nlp_main.py:**  
  This script manages the Natural Language Processing aspect of the project. It includes the functions and models used to predict the next possible calculation based on user input.

- **index.html:**  
  The front-end HTML file that serves as the user interface. It includes a form for inputting calculations and displays the results and predictions.

- **templates/** (if exists):  
  Folder containing HTML templates for rendering the web pages.

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ai-enhanced-calculator.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd ai-enhanced-calculator
   ```

3. **Create a Virtual Environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. **Install the Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application:**
   ```bash
   python main.py
   ```

6. **Access the Application:**
   - Open a web browser and navigate to `http://localhost:5000`.

## Usage

- Enter your calculation in the text box and click "Calculate."
- The AI will also predict the next possible calculation and display it below the result.

## Future Improvements

- **Enhanced NLP Models:** Improve the accuracy of the prediction model.
- **Additional Operations:** Expand the calculator to support more complex mathematical functions.
- **User Authentication:** Add user authentication for personalized experience and history tracking.

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for suggestions and bug reports.
