from flask import Flask, request, jsonify, render_template
from agent_service import run_agent
from database import save_chat, init_db
import os

app = Flask(__name__)

# Initialize database
init_db()

# ---------------------------
# 🏠 Home Route
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------
# 🤖 Chat API
# ---------------------------
@app.route("/ask", methods=["POST"])
def ask():

    user_message = request.json["message"]

    answer = run_agent(user_message)

    # Save chat to DB
    save_chat(user_message, answer)

    return jsonify({
        "answer": answer
    })


# ---------------------------
# 📂 Upload File
# ---------------------------
@app.route("/upload", methods=["POST"])
def upload_file():

    file = request.files["file"]

    # Ensure data folder exists
    if not os.path.exists("data"):
        os.makedirs("data")

    filepath = "data/company_docs.txt"
    file.save(filepath)

    return jsonify({
        "message": "File uploaded successfully"
    })


# ---------------------------
# 🚀 Run App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)