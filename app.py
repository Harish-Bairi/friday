# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# ❌ Hardcoded credentials (for testing rule violations)
USERNAME = "admin"
PASSWORD = "admin123"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    
    username = data.get("username")
    password = data.get("password")

    # ❌ No input validation
    # ❌ Plain text password comparison
    if username == USERNAME and password == PASSWORD:
        return jsonify({
            "status": "success",
            "message": "Login successful"
        })
    else:
        return jsonify({
            "status": "fail",
            "message": "Invalid credentials"
        })

@app.route('/home')
def home():
    # ❌ No authentication check
    return "Welcome to Home Page!"

if __name__ == "__main__":
    app.run(debug=True)  # ❌ Debug mode ON (security issue)