import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [expenses, setExpenses] = useState([]);
  const [title, setTitle] = useState("");
  const [amount, setAmount] = useState("");

  // Fetch expenses
  const fetchExpenses = async () => {
    const res = await axios.get("http://127.0.0.1:5000/expenses");
    setExpenses(res.data);
  };

  useEffect(() => {
    fetchExpenses();
  }, []);

  // Add expense
  const addExpense = async () => {
    if (!title || !amount) {
      alert("Enter all fields");
      return;
    }

    await axios.post("http://127.0.0.1:5000/expenses", {
      title,
      amount: parseFloat(amount),
    });

    setTitle("");
    setAmount("");
    fetchExpenses();
  };

  // Total calculation
  const total = expenses.reduce((sum, e) => sum + e.amount, 0);

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>💰 Expense Tracker</h1>
       <h1 style={styles.heading}> By Vedika Toke</h1>

      {/* Input Box */}
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

        <button style={styles.button} onClick={addExpense}>
          Add Expense
        </button>
      </div>

      {/* Total */}
      <h2 style={styles.total}>Total: ₹{total}</h2>

      {/* Expense List */}
      <div style={styles.list}>
        {expenses.map((e) => (
          <div key={e.id} style={styles.item}>
            <span>
              <b>{e.title}</b> ({e.category})
            </span>
            <span>₹{e.amount}</span>
          </div>
        ))}
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