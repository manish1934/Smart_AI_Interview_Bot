import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Smart AI Interview Bot</title>
        </head>
        <body style="text-align:center; font-family:Arial;">
            <h1>🚀 Smart AI Interview Bot is Live!</h1>
            <p>Your deployment is successful 🎉</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)