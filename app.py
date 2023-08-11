from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

response = "This is the AI response."


@app.route("/")
def handle_home():
    return render_template("index.html")

@app.route("/chat", methods = ["POST"])
def handle_chat():
    data = request.json
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=3000)
