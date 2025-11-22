# Task Manager Web Application

A Flask-based web application for task management with C++ backend processing.

## Features
- Web interface for task management
- Add/remove tasks through forms  
- Real-time task list display
- C++ backend for fast processing
- Persistent task storage
- Activity logging

## Project Structure
- `app.py` - Main Flask application
- `templates/index.html` - Web interface
- `c++/mm.cpp` - C++ source code
- `c++/mm` - Compiled executable
- `task1.txt` - Task storage file
- `log.txt` - Application logs

## Setup
1. Compile C++: `g++ -o c++/mm c++/mm.cpp`
2. Run Flask: `python app.py`
3. Access: `http://localhost:5001`

## Usage
- Add tasks using the top input field
- Remove tasks by number using the bottom field
- View current tasks in real-time below
