# 🔐 Password Security Analyzer

A Python-based cybersecurity tool that evaluates password strength and checks whether a password has appeared in known data breaches using a privacy-preserving approach.

---

## 📌 Features
- Analyzes password strength
- Calculates password entropy
- Detects weak and reused passwords
- Checks breached passwords using the Have I Been Pwned API
- Provides security recommendations
- Command-line based tool

---

## 🛠️ Technologies Used
- Python 3
- Requests Library
- SHA-1 Hashing
- Regular Expressions

---

## 🚀 How It Works
1. User enters a password
2. Tool analyzes:
   - Password length
   - Uppercase/lowercase usage
   - Numbers
   - Special characters
3. Password entropy is calculated
4. Password hash is checked against breached-password databases using k-Anonymity
5. Security recommendations are displayed

---

## ▶️ Usage

Run the following command:

```bash
python password_checker.py