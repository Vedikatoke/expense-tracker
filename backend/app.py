# imports
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="build", static_url_path="")

CORS(app)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    amount = db.Column(db.Float)
    category = db.Column(db.String(50), default="General")

with app.app_context():
    db.create_all()

# ✅ API ROUTES FIRST
@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([
        {"id": e.id, "title": e.title, "amount": e.amount, "category": e.category}
        for e in expenses
    ])

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()

    if not data or 'title' not in data or 'amount' not in data:
        return {"error": "Invalid data"}, 400

    if float(data['amount']) <= 0:
        return {"error": "Amount must be > 0"}, 400

    expense = Expense(
        title=data['title'],
        amount=float(data['amount']),
        category="General"
    )

    db.session.add(expense)
    db.session.commit()

    return {"message": "Added"}, 201


# ✅ 🔥 ADD THIS AT THE END (VERY IMPORTANT)

@app.route('/')
def serve_root():
    return send_from_directory('build', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    file_path = os.path.join('build', path)
    if os.path.exists(file_path):
        return send_from_directory('build', path)
    else:
        return send_from_directory('build', 'index.html')


# run app
if __name__ == '__main__':
    app.run(debug=True)