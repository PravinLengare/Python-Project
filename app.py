from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ice_breaker1 import ice_break_with

load_dotenv()
app = Flask(__name__)  # it will going to initialize a new flask application


@app.route("/")  # It going to execute index function
def index():  # it's going to render an HTML template
    return render_template("index.html")


@app.route("/summary", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with(name=name)
    return jsonify({
        "summary_and_facts": summary.to_dict(),
        "photoUrl": profile_pic_url,
    }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
