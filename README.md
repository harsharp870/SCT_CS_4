# SCT_CS_4
# Keyboard Activity Logger

## Objective
The objective of this project is to develop a basic Python application that records and logs keyboard inputs. It helps in understanding how keystroke events can be captured and stored for analysis in a controlled and ethical environment.

## Description
This project is a GUI-based Keyboard Activity Logger built using Python. It captures keyboard inputs in real time when logging is enabled and displays them inside the application window.

The application ensures user control and transparency, meaning logging starts only when the user explicitly clicks the Start button.

## Features
- Start and Stop logging functionality
- Real-time display of keystrokes
- Save logs to a text file
- Clear log display
- Simple and user-friendly graphical interface

## Technologies Used
- Python
- Tkinter for graphical user interface
- pynput for keyboard input handling

## Project Structure
```
SCT_CS_4/
│── keylogger.py
│── README.md
```


## Installation and Execution

### Step 1: Clone the Repository
git clone https://github.com/your-username/SCT_CS_4.git
cd SCT_CS_4

### Step 2: Install Dependencies
pip install pynput
### Step 3: Run the Program
python keylogger.py


## Working Principle
1. The application starts in an idle state.
2. When the user clicks Start, logging begins.
3. Each key pressed is displayed in real time.
4. Logging can be stopped using the Stop button.
5. The recorded data can be saved to a file using the Save option.
6. Logs can be cleared using the Clear button.

## Disclaimer
This project is intended only for educational purposes. Do not use this tool without proper authorization or for unethical activities.

## Conclusion
This project demonstrates how keyboard inputs can be captured, displayed, and stored using Python. It provides practical exposure to event handling, GUI development, and file operations.

## Author
Harsha R P
