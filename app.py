from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route("/")
def home():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form["task"]

    if task:
        todos.append(task)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)