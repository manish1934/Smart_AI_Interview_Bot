from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Smart AI Interview Bot is Live 🚀"

if __name__ == "__main__":
    app.run()