import requests
from flask import Flask, request, render_template, send_file
import subprocess

LOG_PATH = "log.txt" # change way for log dile

def log_event(message: str): # writing logs
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(message + "\n")

app = Flask(__name__)

def run_cpp_script(bong): # starting c++ script
    result = subprocess.run(
        ['/Users/ilya/PycharmProjects/pythonProject28/c++/mm'], # change way for c++ script
        input=bong,
        capture_output=True,
        text=True
    )
    return result.stdout


def read_file_content(): # read file with task list
    try:
        with open("task1.txt", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "File empty or doesn't exist"


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ''
    file_content = read_file_content() # read file forever

    if request.method == "POST":
        user_input = request.form.get('question', '')
        user_input2 = request.form.get('question2', '')
        button_value = request.form.get('button_name')

        if button_value == 'add':
            bong = user_input + "add"
        elif button_value == 'remove':
            bong = user_input2 + "rem"
        else:
            bong = ""

        answer = run_cpp_script(bong)
        file_content = read_file_content()  # update after change

    return render_template('index.html', response=answer, file_content=file_content)
@app.route("/log") # page with logs
def get_log():
    key = request.args.get("key")
    if key != "zK2$N7gP@d8^tXv9!eB4Lm":
        return "Access denied", 403


if __name__ == '__main__': #starting script
    app.run(host="0.0.0.0", port=5001, debug=True)