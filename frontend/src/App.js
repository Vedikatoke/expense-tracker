import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [expenses, setExpenses] = useState([]);
  const [title, setTitle] = useState("");
  const [amount, setAmount] = useState("");

  // ✅ If using single deploy (same backend)
  const API_URL = "/expenses";

  // ❗ If using separate backend (Render), use this instead:
  // const API_URL = "https://expense-tracker-rifi.onrender.com/expenses";

  // ✅ Fetch expenses
  const fetchExpenses = async () => {
    try {
      const res = await axios.get(API_URL);
      setExpenses(res.data);
    } catch (error) {
      console.error("Error fetching expenses:", error);
    }
  };

  useEffect(() => {
    fetchExpenses();
  }, []);

  // ✅ Add expense
  const addExpense = async () => {
    try {
      console.log("Button clicked");

      if (!title || !amount) {
        alert("Enter all fields");
        return;
      }

      await axios.post(API_URL, {
        title,
        amount: parseFloat(amount),
      });

      setTitle("");
      setAmount("");
      fetchExpenses();
    } catch (error) {
      console.error("Error adding expense:", error);
      alert("Error adding expense. Check console.");
    }
  };

  // ✅ Total calculation
  const total = expenses.reduce((sum, e) => sum + e.amount, 0);

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>💰 Expense Tracker</h1>
   

      {/* Input Section */}
      <div style={styles.card}>
        <input
          style={styles.input}
          placeholder="Enter Title (e.g. Pizza)"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <input
          style={styles.input}
          type="number"
          placeholder="Enter Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />

        <button
          style={styles.button}
          onClick={(e) => {
            e.preventDefault();
            addExpense();
          }}
        >
          Add Expense
        </button>
      </div>

      {/* Total */}
      <h2 style={styles.total}>Total: ₹{total}</h2>

      {/* Expense List */}
      <div style={styles.list}>
        {expenses.length === 0 ? (
          <p style={{ textAlign: "center" }}>No expenses yet</p>
        ) : (
          expenses.map((e) => (
            <div key={e.id} style={styles.item}>
              <span>
                <b>{e.title}</b> ({e.category})
              </span>
              <span>₹{e.amount}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

// 🎨 Styles
const styles = {
  container: {
    maxWidth: "500px",
    margin: "auto",
    fontFamily: "Arial",
    padding: "20px",
  },
  heading: {
    textAlign: "center",
  },
  card: {
    background: "#f5f5f5",
    padding: "15px",
    borderRadius: "10px",
    marginBottom: "20px",
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },
  input: {
    padding: "10px",
    borderRadius: "5px",
    border: "1px solid #ccc",
  },
  button: {
    padding: "10px",
    background: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  total: {
    textAlign: "center",
  },
  list: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },
  item: {
    display: "flex",
    justifyContent: "space-between",
    background: "#fff",
    padding: "10px",
    borderRadius: "5px",
    boxShadow: "0px 0px 5px rgba(0,0,0,0.1)",
  },
};

export default App;
