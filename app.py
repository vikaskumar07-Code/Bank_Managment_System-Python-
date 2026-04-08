import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank System", layout="centered")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Account", "Deposit", "Withdraw", "Update", "Delete"]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        result = bank.create_account(name, age, email, pin)
        if isinstance(result, dict):
            st.success("Account Created!")
            st.write(result)
        else:
            st.error(result)

# ---------------- DEPOSIT ----------------
elif menu == "Deposit":
    st.header("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        st.success(bank.deposit(acc, pin, amount))

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw":
    st.header("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        st.success(bank.withdraw(acc, pin, amount))

# ---------------- UPDATE ----------------
elif menu == "Update":
    st.header("Update Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        st.success(bank.update_details(acc, pin, name, email, new_pin))

# ---------------- DELETE ----------------
elif menu == "Delete":
    st.header("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        st.warning(bank.delete_account(acc, pin))