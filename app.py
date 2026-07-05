from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("VERSION", "Version 2")

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure DevOps Canary Demo</title>
        <style>
            body {{
                background-color:#f2f2f2;
                font-family:Arial;
                text-align:center;
                margin-top:80px;
            }}
            .card {{
                width:500px;
                margin:auto;
                background:white;
                padding:30px;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;
            }}
            h1 {{
                color:#0078D4;
            }}
            h2 {{
                color:green;
            }}
        </style>
    </head>
    <body>

        <div class="card">
            <h1>Azure DevOps Deployment Demo</h1>
            <h2>{VERSION}</h2>

            <hr>

            <h3>Deployment Strategy</h3>

            <p>✔ Azure App Service</p>

            <p>✔ Deployment Slots</p>

            <p>✔ Canary Deployment</p>

            <p>✔ Rollback Supported</p>

        </div>

    </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "Healthy",
        "version": VERSION
    }, 200

@app.route("/about")
def about():
    return {
        "application": "Azure DevOps Canary Demo",
        "deployment": VERSION
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
