



 Expense Tracker (Python CLI Application)

A simple **command-line based Expense Tracker** built using **pure Python (standard library only)**.
The application helps users manage daily expenses efficiently by storing data in a CSV file.



 Features

✔ Store expenses in a CSV file (`expenses.csv`)
✔ Add, view, edit, and delete expenses using **unique IDs**
✔ View **monthly expense totals**
✔ Get **category-wise expense summary**
✔ Search expenses by **notes/keywords**
✔ Input validation for:

* Date format (`DD-MM-YYYY`)
* Numeric amount
  ✔ Single-file implementation
  ✔ No external libraries required


 Technologies Used

* **Python 3**
* `csv`
* `datetime`
* `pathlib`
* `typing`
* `os`

> ⚠️ Uses **Python Standard Library only** (No third-party dependencies)

---

## 📁 Project Structure

```
Expense-Tracker/
│
├── expense_tracker.py   # Main application file
├── expenses.csv         # Auto-generated CSV file for storage
└── README.md            # Project documentation
```

---

## 🧾 CSV File Format

The application stores data in the following format:

| ID | Date       | Amount | Category | Note  |
| -- | ---------- | ------ | -------- | ----- |
| 1  | 05-12-2025 | 250.00 | Food     | Lunch |

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Run the Application

```bash
python expense_tracker.py
```

---

## 📌 Menu Options

```
==== Expense Tracker ====
1. Add Expense
2. View All Expenses
3. View Monthly Total
4. Category Summary
5. Search Notes
6. Edit Entry (by ID)
7. Delete Entry (by ID)
8. Exit
```

---

## 🧪 Input Validation

* **Date:** Must be in `DD-MM-YYYY` format
* **Amount:** Accepts integers and floating-point values
* **Category:** Cannot be empty

Invalid inputs are rejected with helpful error messages.

---

## 🎯 Use Cases

* Daily personal expense tracking
* Student budget management
* Learning Python file handling & CLI apps
* Mini-project for academics

---

## 🔮 Future Enhancements (Optional)

* Export monthly reports
* Add income tracking
* Graphical User Interface (GUI)
* Data encryption
* Backup & restore functionality

---

## 👨‍💻 Author

**Rushikesh Gokhe**
Electrical Engineering Student
Python & Embedded Systems Enthusiast

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

⭐ If you found this project useful, **give it a star on GitHub!**

---

If you want, I can also:

* Add **screenshots section**
* Create a **LICENSE file**
* Make this README more **resume-oriented**
* Convert it into a **project report format**

Just tell me 👍
