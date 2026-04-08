# 🏦 Bank Management System (Streamlit)

A simple and clean **Bank Management System** built using **Python + Streamlit**.
This project allows users to create accounts, deposit/withdraw money, update details, and manage accounts through a modern UI.

---

## 🚀 Features

* 🆕 Create New Account
* 💰 Deposit Money
* 💸 Withdraw Money
* 📝 Update Account Details
* ❌ Delete Account
* 🔐 PIN-based Authentication
* 💾 Data stored using JSON

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Streamlit** (for UI)
* **JSON** (for data storage)

---

## 📂 Project Structure

```
bank_managment_system/
│
├── app.py              # Streamlit UI
├── bank.py             # Backend logic
├── data.json           # Database (ignored in git)
├── data_sample.json    # Sample empty database
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/vikaskumar07-Code/bank-management-system.git
cd bank_managment_system
```

2. Install dependencies:

```bash
pip install streamlit
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 📌 Usage

* Open browser at: `http://localhost:8501`
* Use sidebar to navigate between features
* Create account → Note your account number
* Use account number + PIN for transactions

---

## 🔒 Security Note

* PIN is used for authentication (basic level)
* Do NOT use real personal data
* `data.json` is excluded using `.gitignore`

---

## 🧪 Sample Data

If `data.json` is empty, initialize it with:

```json
[]
```

---

## 📸 Screenshots
![Bank UI](https://github.com/vikaskumar07-Code/Bank_Managment_System-Python-/raw/main/UI%20Design.png)

---

## 🚀 Future Improvements

* 🔐 Secure PIN hashing
* 👤 Login & session system
* 📊 Dashboard with charts
* 🧾 Transaction history
* 🌐 Database integration (SQLite / MySQL)
* 🎨 Advanced UI styling

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is for learning purposes.

---

## 👨‍💻 Author

**Vikas Kumar**

---

⭐ If you like this project, give it a star!
