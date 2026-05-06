# 🧮 Advanced Python Calculator

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A powerful, terminal-based scientific calculator built with Python that supports basic arithmetic, advanced mathematical operations, and trigonometric functions. Perfect for quick calculations, scientific computations, and learning Python programming.

---

## 📋 Table of Contents

- [Features](#-features)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Operations Reference](#-operations-reference)
- [Examples](#-examples)
- [Error Handling](#-error-handling)
- [License](#-license)

---

## ✨ Features

### Basic Operations
- ✅ **Addition** (`+`): Add two numbers
- ✅ **Subtraction** (`-`): Subtract second number from first
- ✅ **Multiplication** (`*`): Multiply two numbers
- ✅ **Division** (`/`): Divide with decimal results
- ✅ **Exponentiation** (`**`): Raise number to a power
- ✅ **Modulus** (`%`): Get remainder of division
- ✅ **Floor Division** (`//`): Divide and round down to nearest integer

### Advanced Mathematical Operations
- 🔬 **Square Root** (`sqrt`): Calculate square root of a number
- 📊 **Logarithm Base 10** (`log`): Common logarithm
- 📈 **Natural Logarithm** (`ln`): Logarithm base e
- 🔢 **Factorial** (`fact`): Calculate n! (factorial)

### Trigonometric Functions
- 📐 **Sine** (`sin`): Trigonometric sine (input in degrees)
- 📐 **Cosine** (`cos`): Trigonometric cosine (input in degrees)
- 📐 **Tangent** (`tan`): Trigonometric tangent (input in degrees)

### Utility Functions
- 🔄 **Absolute Value** (`abs`): Remove negative sign
- 🎯 **Round** (`round`): Round to specified decimal places
- ⬆️ **Maximum** (`max`): Find larger of two numbers
- ⬇️ **Minimum** (`min`): Find smaller of two numbers

### User Experience Features
- 🔁 **Continuous Operation**: Calculate multiple times without restarting
- 🛡️ **Error Prevention**: Division by zero protection
- ✔️ **Input Validation**: Prevents invalid mathematical operations
- 💬 **User-Friendly Interface**: Clear prompts and operation display

---

## 💻 System Requirements

### Required
- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Terminal**: Any terminal with Python support

### Python Modules
All required modules are part of Python's standard library:
- `math` - Mathematical functions (pre-installed)

**No external dependencies required!** ✨

---

## 📦 Installation

### Step 1: Verify Python Installation
```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.6.0` or higher

### Step 2: Download the Calculator
```bash
# Option 1: Clone from GitHub
git clone https://github.com/yourusername/advanced-python-calculator.git
cd advanced-python-calculator

# Option 2: Download directly
# Download advanced-python-calculator.py from the repository
```

### Step 3: Run the Calculator
```bash
python advanced-python-calculator.py
# or
python3 advanced-python-calculator.py
```

That's it! No installation needed. 🎉

---

## 📖 Usage Guide

### Starting the Calculator

1. **Open your terminal**
2. **Navigate to the file location**:
   ```bash
   cd path/to/calculator
   ```
3. **Run the program**:
   ```bash
   python advanced-python-calculator.py
   ```

### Basic Workflow

```
--- Calculator ---
Basic: +  -  *  /  **  %  //
Advanced: sqrt  log  ln  sin  cos  tan  fact
Other: abs  round  max  min

Enter operation: +
Enter first number: 15
Enter second number: 27
Answer: 42.0

Do you want to calculate again? (Y/N): Y
```

### How to Use

1. **Select an operation** by typing the operator (e.g., `+`, `sqrt`, `sin`)
2. **Enter the required number(s)**:
   - Two numbers for: `+`, `-`, `*`, `/`, `**`, `%`, `//`, `max`, `min`
   - One number for: `sqrt`, `log`, `ln`, `sin`, `cos`, `tan`, `fact`, `abs`, `round`
3. **View the result** displayed as "Answer: [result]"
4. **Choose to continue** or exit:
   - Type `Y` to perform another calculation
   - Type `N` to exit the program

### Exiting the Program

- Type `N` when asked "Do you want to calculate again?"
- Or press `Ctrl+C` to force quit

---

## 📚 Operations Reference

### Basic Arithmetic Operations

| Operation | Symbol | Example Input | Example Output | Notes |
|-----------|--------|---------------|----------------|-------|
| Addition | `+` | `5 + 3` | `8.0` | Adds two numbers |
| Subtraction | `-` | `10 - 4` | `6.0` | Subtracts second from first |
| Multiplication | `*` | `6 * 7` | `42.0` | Multiplies two numbers |
| Division | `/` | `15 / 3` | `5.0` | Decimal division |
| Exponentiation | `**` | `2 ** 8` | `256.0` | Raises to power |
| Modulus | `%` | `17 % 5` | `2.0` | Returns remainder |
| Floor Division | `//` | `17 // 5` | `3.0` | Divides and rounds down |

### Advanced Mathematical Operations

| Operation | Symbol | Example Input | Example Output | Valid Range |
|-----------|--------|---------------|----------------|-------------|
| Square Root | `sqrt` | `sqrt(64)` | `8.0` | n ≥ 0 |
| Logarithm (base 10) | `log` | `log(100)` | `2.0` | n > 0 |
| Natural Logarithm | `ln` | `ln(2.718)` | `≈1.0` | n > 0 |
| Factorial | `fact` | `fact(5)` | `120.0` | n ≥ 0, integer only |

### Trigonometric Functions

| Operation | Symbol | Example Input | Example Output | Notes |
|-----------|--------|---------------|----------------|-------|
| Sine | `sin` | `sin(30)` | `0.5` | Input in degrees |
| Cosine | `cos` | `cos(60)` | `0.5` | Input in degrees |
| Tangent | `tan` | `tan(45)` | `≈1.0` | Input in degrees |

**Important**: All trigonometric functions expect input in **degrees**, not radians. The calculator automatically converts degrees to radians internally.

### Utility Functions

| Operation | Symbol | Example Input | Example Output | Notes |
|-----------|--------|---------------|----------------|-------|
| Absolute Value | `abs` | `abs(-15)` | `15.0` | Removes negative sign |
| Round | `round` | `round(3.14159, 2)` | `3.14` | Prompts for decimal places |
| Maximum | `max` | `max(10, 25)` | `25.0` | Returns larger number |
| Minimum | `min` | `min(10, 25)` | `10.0` | Returns smaller number |

---

## 💡 Examples

### Example 1: Basic Addition
```
Enter operation: +
Enter first number: 123
Enter second number: 456
Answer: 579.0
```

### Example 2: Power Calculation
```
Enter operation: **
Enter first number: 2
Enter second number: 10
Answer: 1024.0
```

### Example 3: Square Root
```
Enter operation: sqrt
Enter number: 144
Answer: 12.0
```

### Example 4: Trigonometry
```
Enter operation: sin
Enter number: 90
Answer: 1.0
```

### Example 5: Factorial
```
Enter operation: fact
Enter number: 6
Answer: 720.0
```

### Example 6: Rounding
```
Enter operation: round
Enter number: 3.14159265
Decimal places: 3
Answer: 3.142
```

### Example 7: Finding Maximum
```
Enter operation: max
Enter first number: 42.5
Enter second number: 38.9
Answer: 42.5
```

---

## 🛡️ Error Handling

The calculator includes robust error handling to prevent crashes:

### Division by Zero Protection
```
Enter operation: /
Enter first number: 10
Enter second number: 0
Invalid, cannot divide by 0
```

### Invalid Square Root
```
Enter operation: sqrt
Enter number: -25
Invalid input
```

### Invalid Logarithm
```
Enter operation: log
Enter number: -5
Invalid input
(Logarithm requires positive numbers)
```

### Invalid Factorial
```
Enter operation: fact
Enter number: 5.5
Invalid input
(Factorial requires non-negative integers)
```

### Invalid Operation
```
Enter operation: xyz
Invalid operation
```

---

## 🎯 Use Cases

### For Students
- ✏️ Quick homework calculations
- 📐 Trigonometry problem solving
- 🔬 Science project computations
- 📊 Statistics and data analysis

### For Professionals
- 💼 Business calculations
- 📈 Financial computations
- 🏗️ Engineering calculations
- 🔬 Scientific research

### For Learning
- 🐍 Python programming practice
- 🧮 Understanding mathematical operations
- 💻 Command-line interface development
- 🔧 Error handling implementation

---

## 🔧 Technical Details

### Code Structure
```python
# Main Loop
while running:
    # Display menu
    # Get operation
    # Perform calculation
    # Display result
    # Ask to continue
```

### Built-in Python Modules Used
- **`math`**: Provides mathematical functions
  - `math.sqrt()` - Square root
  - `math.log10()` - Base 10 logarithm
  - `math.log()` - Natural logarithm
  - `math.sin()`, `math.cos()`, `math.tan()` - Trigonometric functions
  - `math.radians()` - Degree to radian conversion
  - `math.factorial()` - Factorial calculation

### Input/Output
- **Input Type**: String (converted to float)
- **Output Type**: Float
- **Precision**: Python's default float precision (~15-17 significant digits)

---

## 🚀 Future Enhancements

### Planned Features
- [ ] Operation history/memory
- [ ] Previous answer recall (ANS button)
- [ ] Support for complex numbers
- [ ] Graphing capabilities
- [ ] Unit conversions
- [ ] Scientific notation display
- [ ] Expression evaluation (e.g., "5 + 3 * 2")
- [ ] Constants (π, e, φ)
- [ ] Save/load calculations
- [ ] GUI version

---

## 🐛 Known Limitations

1. **Single Operation at a Time**: Cannot chain operations (e.g., "5 + 3 * 2")
2. **No Expression Parsing**: Must perform one operation at a time
3. **Degree Mode Only**: Trigonometric functions only work in degrees
4. **No Memory Functions**: Cannot store results for later use
5. **Limited Precision**: Subject to floating-point arithmetic limitations

---

## 💻 Customization

### Changing Trigonometric Units to Radians

To use radians instead of degrees, modify lines 58-63:

**Current (Degrees)**:
```python
elif op == "sin":
    result = math.sin(math.radians(n))
```

**Change to (Radians)**:
```python
elif op == "sin":
    result = math.sin(n)
```

Repeat for `cos` and `tan`.

### Adding New Operations

To add a new operation (example: cube root):

```python
# Add to menu display
print("Advanced: sqrt  cbrt  log  ln  sin  cos  tan  fact")

# Add to operation check
elif op in ["sqrt", "cbrt", "log", ...]:
    n = float(input("Enter number: "))
    
    # Add operation logic
    if op == "cbrt":
        result = n ** (1/3)
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
1. 🐛 **Report Bugs**: Open an issue describing the bug
2. 💡 **Suggest Features**: Share your ideas for improvements
3. 📝 **Improve Documentation**: Fix typos or add examples
4. 🔧 **Submit Code**: Fork, modify, and create a pull request

### Contribution Guidelines
1. Test your changes thoroughly
2. Follow existing code style
3. Add comments for complex logic
4. Update documentation if needed

---

## 📄 License

This project is licensed under the MIT License:

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Support

### Need Help?
- 📖 Check the [Operations Reference](#-operations-reference)
- 💡 Review the [Examples](#-examples)
- 🐛 [Report an Issue](https://github.com/yourusername/advanced-python-calculator/issues)

---

## 🙏 Acknowledgments

- **Python Software Foundation** for the Python programming language
- **Python Math Module** for comprehensive mathematical functions
- All users and contributors who help improve this calculator

---

## 📊 Quick Reference Card

```
╔═══════════════════════════════════════════════════════════╗
║           ADVANCED PYTHON CALCULATOR QUICK REF             ║
╠═══════════════════════════════════════════════════════════╣
║ BASIC                │ ADVANCED        │ TRIG             ║
║ +    Addition        │ sqrt  Sq Root   │ sin   Sine       ║
║ -    Subtraction     │ log   Log10     │ cos   Cosine     ║
║ *    Multiply        │ ln    Ln        │ tan   Tangent    ║
║ /    Divide          │ fact  Factorial │                  ║
║ **   Power           │                 │ UTILITY          ║
║ %    Modulus         │                 │ abs   Absolute   ║
║ //   Floor Div       │                 │ round Round      ║
║                      │                 │ max   Maximum    ║
║                      │                 │ min   Minimum    ║
╚═══════════════════════════════════════════════════════════╝
```

---

<div align="center">

**Built with ❤️ and Python**

*Making calculations simple and accessible for everyone*

[Report Bug](https://github.com/yourusername/advanced-python-calculator/issues) · [Request Feature](https://github.com/yourusername/advanced-python-calculator/issues) · [View Code](https://github.com/yourusername/advanced-python-calculator)

</div>

---

## ⭐ Star This Repository

If you found this calculator helpful, please consider giving it a star! It helps others discover the project.

**Happy Calculating! 🧮**
