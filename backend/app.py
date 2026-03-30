from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Import AI function
from ai_service import categorize_expense

# Create app
app = Flask(__name__)
CORS(app)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------------
# Model
# -------------------------------
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), default="Other")

# -------------------------------
# Create DB
# -------------------------------
with app.app_context():
    db.create_all()

# -------------------------------
# Home Route
# -------------------------------
@app.route('/')
def home():
    return "Backend is running!"

# -------------------------------
# GET Expenses
# -------------------------------
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

# -------------------------------
# POST Expense (AI integrated)
# -------------------------------
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()

    # Validation
    if not data or 'title' not in data or 'amount' not in data:
        return jsonify({"error": "Title and amount required"}), 400

    if data['amount'] <= 0:
        return jsonify({"error": "Amount must be greater than 0"}), 400

    # AI categorization
    category = categorize_expense(data['title'])

    # Create expense
    expense = Expense(
        title=data['title'],
        amount=data['amount'],
        category=category
    )

    db.session.add(expense)
    db.session.commit()

    return jsonify({"message": "Expense added"}), 201

# -------------------------------
# Run App
# -------------------------------
if __name__ == '__main__':
    print("🚀 Server starting...")
    app.run(host="0.0.0.0", port=5000)
