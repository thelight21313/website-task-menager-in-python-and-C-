Task Manager Web Application

A Flask-based web application for task management with C++ backend processing. The system provides a web interface to add and remove tasks, storing them persistently in a local file. The frontend is built with Python and Flask templates, while task operations are handled by a high-performance C++ backend. Features include real-time task list display, automatic logging, and simple form-based interaction.

Project Structure

app.py - Main Flask application handling web routes and form processing
templates/index.html - Web interface with task input forms and display
c++/mm.cpp - C++ source code for task processing logic
c++/mm - Compiled C++ executable
task1.txt - Text file storing current tasks
log.txt - Application activity logs
Setup & Usage

Compile the C++ component: g++ -o c++/mm c++/mm.cpp
Start the Flask server: python app.py
Access the web interface at http://localhost:5001
Use the forms to add new tasks or remove existing ones by number
The application runs locally and requires no external dependencies beyond standard C++ compiler and Python Flask. All task operations are processed through the C++ backend for optimal performance while maintaining a simple web-based user interface.
