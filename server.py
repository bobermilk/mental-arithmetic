from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def arithmetic():
    if request.method == "POST":
        return render_template("arithmeticgame.html", data=request.form)
    return render_template("arithmetic.html")