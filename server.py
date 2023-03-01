from flask import Flask, render_template, request, jsonify
import base64
import json

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def arithmetic():
    game=request.args.get("game")
    if game is None:
        if request.method == "POST":
            # creating a game
            game_dict=request.form.to_dict(flat=False)
            game=base64.urlsafe_b64encode(json.dumps(game_dict).encode()).decode()
            return render_template("arithmeticgame.html", game=game, data=request.form)
        # create a game
        return render_template("arithmetic.html")
    else:
        # join a game
        data=json.loads(base64.urlsafe_b64decode(game.encode()).decode())
        return render_template("arithmeticgame.html", data=data)
