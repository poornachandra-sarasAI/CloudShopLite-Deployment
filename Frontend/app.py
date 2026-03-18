from flask import Flask
import requests
import os

app = Flask(__name__)
api_url = os.getenv("API_URL", "http://localhost:5000")

@app.route("/")
def home():
    try:
        res = requests.get(f"{api_url}/count").json()
        return f"""
        <h1>CloudShop Lite</h1>
        <p>Visits: {res['visits']}</p>
        <br>
        <p>Background Jobs: {res['background_jobs']}</p>
        <h1> Happy Deployment!! </h1>
        """
    except:
        return "<h1>Frontend running, API unavailable</h1>"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)