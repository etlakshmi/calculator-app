# Simple Python Calculator with Streamlit UI

A user-friendly calculator application with a web interface built using Python and Streamlit. Perform basic arithmetic operations through an intuitive graphical interface.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Documentation](#code-documentation)
- [Screenshots](#screenshots)
- [Examples](#examples)
- [Contributing](#contributing)

---

## 🎯 Overview

This calculator project consists of two main components:
- **Backend (`main.py`)**: Core calculation functions
- **Frontend (`app.py`)**: Streamlit web interface

The application provides a clean, interactive web interface for performing basic arithmetic operations without requiring any command-line knowledge.

---

## ✨ Features

- 🌐 **Web-Based Interface** - Easy-to-use Streamlit UI
- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract one number from another
- ✖️ **Multiplication** - Multiply two numbers
- ➗ **Division** - Divide with zero-division error handling
- 🔢 **Decimal Support** - Works with integers and floating-point numbers
- 🎨 **Clean UI** - Modern, responsive design
- ⚡ **Real-time Results** - Instant calculation display
- 🛡️ **Error Handling** - Prevents division by zero

---

## 🚀 Installation

### Prerequisites

Ensure you have Python 3.7+ installed on your system.

### Step 1: Install Required Packages

```bash
pip install streamlit
```

### Step 2: Download the Files

Download both `main.py` and `app.py` to the same directory.

### Step 3: Run the Application

```bash
streamlit run app.py
```

The calculator will open automatically in your default web browser at `http://localhost:8501`

---

## 💻 Usage

### Running the Web App

1. Open your terminal/command prompt
2. Navigate to the project directory
3. Run the command:
   ```bash
   streamlit run app.py
   ```
4. The calculator will open in your web browser
5. Enter numbers and select an operation
6. Click "Calculate" to see the result

### Using Functions Programmatically

You can also import the calculator functions in your own Python scripts:

```python
from main import add, subtract, multiply, divide

result = add(10, 5)        # Returns: 15
result = subtract(10, 5)   # Returns: 5
result = multiply(10, 5)   # Returns: 50
result = divide(10, 5)     # Returns: 2.0
```

---

## 📁 Project Structure

```
calculator-project/
│
├── main.py          # Core calculator functions
├── app.py           # Streamlit web interface
└── README.md        # This documentation file
```

---

## 📚 Code Documentation

### `main.py` - Calculator Functions

This file contains the core arithmetic functions:

```python
def add(Number1, Number2):
    return Number1 + Number2

def subtract(Number1, Number2):
    return Number1 - Number2

def multiply(Number1, Number2):
    return Number1 * Number2

def divide(Number1, Number2):
    if Number2 == 0:
        return "Error! Cannot divide by zero."
    return Number1 / Number2
```

#### Function Details

**`add(Number1, Number2)`**
- **Purpose**: Adds two numbers
- **Parameters**: Two numbers (int/float)
- **Returns**: Sum of the numbers
- **Example**: `add(5, 3)` → `8`

**`subtract(Number1, Number2)`**
- **Purpose**: Subtracts second number from first
- **Parameters**: Two numbers (int/float)
- **Returns**: Difference of the numbers
- **Example**: `subtract(10, 4)` → `6`

**`multiply(Number1, Number2)`**
- **Purpose**: Multiplies two numbers
- **Parameters**: Two numbers (int/float)
- **Returns**: Product of the numbers
- **Example**: `multiply(6, 7)` → `42`

**`divide(Number1, Number2)`**
- **Purpose**: Divides first number by second
- **Parameters**: Two numbers (int/float)
- **Returns**: Quotient or error message
- **Example**: `divide(20, 4)` → `5.0`
- **Error**: `divide(10, 0)` → `"Error! Cannot divide by zero."`

---

### `app.py` - Streamlit Interface

This file creates the web interface:

```python
import streamlit as st
from main import add, subtract, multiply, divide

st.title("Simple Calculator")

Number1 = st.number_input("Enter the first number:", value=0.0)
Number2 = st.number_input("Enter the second number:", value=0.0)

operation = st.selectbox("Select Operation:", 
    ("Addition(+)", "Subtraction(-)", "Multiplication(*)", "Division(/)"))

if st.button("Calculate"):
    if operation == "Addition(+)":
        result = add(Number1, Number2)
    elif operation == "Subtraction(-)":
        result = subtract(Number1, Number2)
    elif operation == "Multiplication(*)":
        result = multiply(Number1, Number2)
    elif operation == "Division(/)":
        result = divide(Number1, Number2)
    
    st.success(f"Result: {result}")
```

#### UI Components

- **Title**: Displays "Simple Calculator"
- **Number Inputs**: Two input fields for entering numbers
- **Operation Selector**: Dropdown menu with four operations
- **Calculate Button**: Triggers the calculation
- **Result Display**: Shows the result in a success message box

---

## 🖼️ Screenshots

### Calculator Interface

The Streamlit interface includes:
- Clean title header
- Two numeric input fields with default value of 0.0
- Dropdown menu for operation selection
- Calculate button
- Green success box for displaying results

---

## 📖 Examples

### Example 1: Addition

```
Input:
- First Number: 25
- Second Number: 15
- Operation: Addition(+)

Output:
Result: 40
```

### Example 2: Division

```
Input:
- First Number: 100
- Second Number: 4
- Operation: Division(/)

Output:
Result: 25.0
```

### Example 3: Division by Zero

```
Input:
- First Number: 50
- Second Number: 0
- Operation: Division(/)

Output:
Result: Error! Cannot divide by zero.
```

### Example 4: Decimal Numbers

```
Input:
- First Number: 3.14
- Second Number: 2.5
- Operation: Multiplication(*)

Output:
Result: 7.85
```

---

## 🎨 Customization Options

### Modify the UI Theme

You can customize the Streamlit theme by creating a `.streamlit/config.toml` file:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Add More Operations

To add new operations:

1. Add the function to `main.py`:
   ```python
   def power(Number1, Number2):
       return Number1 ** Number2
   ```

2. Import it in `app.py`:
   ```python
   from main import add, subtract, multiply, divide, power
   ```

3. Add to the selectbox:
   ```python
   operation = st.selectbox("Select Operation:", 
       ("Addition(+)", "Subtraction(-)", "Multiplication(*)", 
        "Division(/)", "Power(^)"))
   ```

4. Add the conditional logic:
   ```python
   elif operation == "Power(^)":
       result = power(Number1, Number2)
   ```

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and branch
6. Set `app.py` as the main file
7. Click "Deploy"

### Deploy to Other Platforms

- **Heroku**: Create a `Procfile` and `requirements.txt`
- **AWS**: Use EC2 or Elastic Beanstalk
- **Google Cloud**: Use App Engine or Cloud Run

---

## 🔧 Troubleshooting

### Issue: Module not found error

```bash
# Solution: Install Streamlit
pip install streamlit
```

### Issue: Port already in use

```bash
# Solution: Run on a different port
streamlit run app.py --server.port 8502
```

### Issue: Calculator not loading

- Check that both `main.py` and `app.py` are in the same directory
- Verify Python version is 3.7 or higher
- Ensure all imports are correct

---

## 🎯 Future Enhancements

- [ ] Add scientific calculator functions (sin, cos, tan, log, etc.)
- [ ] Implement calculation history feature
- [ ] Add memory functions (M+, M-, MR, MC)
- [ ] Create dark mode toggle
- [ ] Add keyboard shortcuts
- [ ] Export results to CSV/PDF
- [ ] Add unit conversion features
- [ ] Implement percentage calculations
- [ ] Add graphing capabilities
- [ ] Create mobile-responsive design

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📦 Requirements

Create a `requirements.txt` file for easy installation:

```
streamlit>=1.28.0
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- Python Community - For excellent documentation
- All contributors who help improve this project

---

## 📞 Support

Need help? Here's how to get support:

- 📧 Email: your.email@example.com
- 🐛 Report bugs via [GitHub Issues](https://github.com/yourusername/calculator/issues)
- 💬 Join discussions in [GitHub Discussions](https://github.com/yourusername/calculator/discussions)
- 📖 Check [Streamlit Documentation](https://docs.streamlit.io/)

---

## 📊 Project Stats

- **Version**: 1.0.0
- **Last Updated**: December 15, 2024
- **Python Version**: 3.7+
- **Dependencies**: Streamlit

---

**Made with ❤️ and Python**

*Happy Calculating! 🧮*