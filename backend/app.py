from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="build", static_url_path="")

# ✅ Enable CORS (safe)
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    amount = db.Column(db.Float)
    category = db.Column(db.String(50), default="General")

# ✅ Create DB
with app.app_context():
    db.create_all()

# ✅ API: Get all expenses
@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([
        {
            "id": e.id,
            "title": e.title,
            "amount": e.amount,
            "category": e.category
        } for e in expenses
    ])

# ✅ API: Add expense
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()

    # Validation
    if not data or 'title' not in data or 'amount' not in data:
        return {"error": "Invalid data"}, 400

    if float(data['amount']) <= 0:
        return {"error": "Amount must be > 0"}, 400

    # Simple category logic
    title = data['title'].lower()
    if "pizza" in title or "food" in title:
        category = "Food"
    elif "travel" in title:
        category = "Travel"
    elif "shop" in title:
        category = "Shopping"
    else:
        category = "General"

    expense = Expense(
        title=data['title'],
        amount=float(data['amount']),
        category=category
    )

    db.session.add(expense)
    db.session.commit()

    return {"message": "Added"}, 201

# ✅ Serve React frontend (IMPORTANT)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

# ✅ Run app
if __name__ == '__main__':
    print("🚀 Server starting...")
    app.run(debug=True)