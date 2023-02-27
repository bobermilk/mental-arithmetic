from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        return render_template("game.html", data=request.form)
    return render_template("index.html")