from flask import Flask, render_template, url_for, redirect, request
from list_manager import ListManager
from list import List
import datetime
import os
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5

load_dotenv()
app = Flask(__name__)
manager = ListManager()
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    if manager.empty():
        manager.add_list(List())
    lists = manager.get_lists()
    if not manager.get_current():
        manager.set_current(lists[0])
    if request.method == "POST":
        redirect(url_for("add_list"))
    current = manager.get_current()
    todos = current.sorting()
    date = datetime.datetime.now().strftime("%B %d, %Y")
    current = manager.get_current()
    return render_template("index.html", lists=lists, date=date, todos=todos, current=current, manager=manager)


@app.route("/get_data", methods=["GET", "POST"])
def get_data():
    global manager  # Access the global manager variable
    if request.method == "POST":
        value = request.form.get("data")
        if value:
            manager = value
        else:
            json_data = request.get_json()
            manager = json_data.get("data") if json_data else None
    return redirect(url_for("home"))


@app.route("/add_list", methods=["GET", "POST"])
def add_list():
    if request.form.get("list"):
        manager.add_list(List(request.form.get("list")))
    else:
        manager.add_list(List())
    return redirect(url_for("home"))


@app.route("/delete_list/<int:position>")
def delete_list(position):
    if manager.size() > 1:
        if manager.get_current() == manager.get_lists()[position] and position != 0:
            display_list(0)
        elif manager.get_current() == manager.get_lists()[position] and position == 0:
            display_list(1)
        manager.remove_list(position)
    return redirect(url_for("home"))


@app.route("/add_todo", methods=["GET", "POST"])
def add_todo():
    if request.method == "POST":
        arr = manager.get_current()
        tags = " " if not request.form.get("tags") else request.form.get("tags")
        message = " " if not request.form.get("message") else request.form.get("message")
        arr.add_todo(
            task=request.form.get("task"),
            start=request.form.get("start"),
            end=request.form.get("end"),
            message=message,
            priority=request.form.get("priority"),
            tags=tags
        )
    return redirect(url_for('home'))


@app.route("/delete_todo<int:num>", methods=["GET", "POST"])
def delete_todo(num):
    arr = manager.get_current()
    obj = arr.get_todos()[num]
    arr.delete_todo(obj)
    return redirect(url_for("home"))


@app.route("/display_list/<int:number>")
def display_list(number):
    arr = manager.get_lists()[number]
    manager.set_current(arr)
    return redirect(url_for("home"))


@app.route("/sort_todos", methods=["GET", "POST"])
def sort_todos():
    value = request.form.get('sorting')
    manager.current.set_sort(value)
    return redirect(url_for("home"))


@app.route("/switch_button/<int:index>")
def switch_button(index):
    todos = manager.get_current().get_todos()
    todos[index].switch_completion()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
