# 💰 Expense Tracker with AI

## 🚀 Overview

This is a full-stack Expense Tracker application built using **Flask (Python)** for backend and **React** for frontend.
It allows users to add expenses and automatically categorizes them using a simple AI-based system.

---

## 🏗️ Tech Stack

* **Frontend:** React, Axios
* **Backend:** Flask, Flask-CORS
* **Database:** SQLite (SQLAlchemy ORM)
* **AI Logic:** Rule-based categorization

---

## ✨ Features

* Add new expenses
* View all expenses
* Automatic AI-based categorization
* Total expense calculation
* Simple and clean UI

---

## 🤖 AI Feature

The app uses a rule-based AI system to categorize expenses automatically.

### Examples:

* "Pizza" → Food
* "Uber ride" → Travel
* "Electricity bill" → Bills

👉 The AI module is designed to be modular and can be replaced with advanced models like OpenAI APIs.

---

## 📁 Project Structure

```
expense-tracker/
│
├── backend/
│   ├── app.py
│   ├── ai_service.py
│   └── expenses.db
│
├── frontend/
│   └── React App
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd backend
python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🔌 API Endpoints

### GET /expenses

Fetch all expenses

### POST /expenses

Add a new expense

#### Sample Request:

```json
{
  "title": "Pizza",
  "amount": 200
}
```

---

## ✅ Validation

* Title is required
* Amount must be greater than 0

---

## 🧪 Testing

* Tested via frontend UI
* API tested using browser / Postman

---

## ⚡ Key Technical Decisions

* Used SQLite for simplicity and quick setup
* Implemented rule-based AI for offline functionality
* Separated AI logic into `ai_service.py` for modularity

---

## 🔄 Future Improvements

* Replace rule-based AI with LLM (OpenAI)
* Add authentication (login/signup)
* Add filters and search
* Add charts and analytics
* Deploy to cloud

---

## ⚠️ Limitations

* Basic AI logic
* No authentication
* No pagination

---

## 🎯 Conclusion

This project demonstrates:

* Full-stack development
* REST API design
* Database integration
* AI feature integration

---

## 📹 Walkthrough Video

(Add your video link here)

---
