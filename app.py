from flask import Flask, jsonify, render_template, request
from recommender import Recommender
app = Flask(__name__)
R = Recommender()

@app.get("/")
def index(): return render_template("index.html")

@app.post("/api/recommend")
def api_recommend():
    spec = (request.get_json(silent=True) or {}).get("spec", "").strip()
    if not spec: return jsonify({"error": "spec required"}), 400
    return jsonify({"results": R.recommend(spec)})

if __name__ == "__main__":
    app.run(port=5003)
