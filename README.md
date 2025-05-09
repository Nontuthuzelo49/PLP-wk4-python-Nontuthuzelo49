# PLP-wk4-python-Nontuthuzelo49
## File Handling and Exception Handling Assignment
## 📌 Overview
This Python project focuses on **reading, modifying, and writing files**, while also **handling errors gracefully** using exception handling.

## 🔧 Features
- **Modify File:** Reads content from a file and converts it to uppercase before saving it.
- **Read File:** Reads a user-specified file and handles common errors.
- **Error Handling:** Prevents crashes when files are missing or inaccessible.

## 🚀 How to Run
1️⃣ **Ensure Python is installed.**  
2️⃣ **Create a text file (input.txt) with some content.**  
3️⃣ **Run the script**:
```sh
python filename.py
```
4️⃣ **Provide a filename when prompted.**  
5️⃣ **Check the modified output file (output.txt).**

## 🔍 Example Usage
```python
modify_file('input.txt', 'output.txt')  # Converts text to uppercase
read_file()  # Prompts user for filename and displays content
```

## 🛡️ Error Handling
- Handles **FileNotFoundError** if the file is missing.
- Prevents **PermissionError** if file access is restricted.
- Catches unexpected exceptions to maintain program stability.

## 📄 License
This project is **free to use** and open-source.
