# 📒 Contact Book (Python)

A simple command-line Contact Book written in Python.  
It allows you to **add** and **view** contacts, storing them in a JSON file for persistence.

---

## 🚀 Features
- Add new contacts (name + phone number)
- View saved contacts in a numbered list
- Data stored in `contacts.json`
- Lightweight and beginner-friendly

---

## 🛠️ Requirements
- Python 3.x  
- No external libraries required (uses only built-in `json` and `os` modules)

---

## 📂 Project Structure
├── contactBook.py # Main script

├── contacts.json # Auto-created file to store contacts

└── README.md # Project documentation

---

## ▶️ Usage

1. Clone this repository:
```bash
   git clone https://github.com/RynVarkh/contact-book.git
   cd contact-book
```

2. Run the script:
```bash
   python3 contactBook.py
```

3. Choose an option:
```bash
   1. View
   2. Add
```
Option 1 (View): Shows all saved contacts.
Option 2 (Add): Lets you add a new contact (name + phone).
