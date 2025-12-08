#!/usr/bin/env python3
"""
Expense Tracker (improved beginner-friendly version)
 
Features:
- Store expenses in CSV file (expenses.csv)
- Add, view, edit, delete entries (by ID)
- Monthly total, category summary, search by note
- Simple input validation (date format DD-MM-YYYY, numeric amount)
- Pure Python (stdlib only), single-file
 
Usage:
  python expense_tracker.py
"""
 
from __future__ import annotations
import csv
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
 
CSV_FILE = Path("expenses.csv")
FIELDNAMES = ["id", "date", "amount", "category", "note"]
 
# ---------- Helpers ----------
def ensure_csv_exists():
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
            writer.writeheader()
 
def read_all() -> List[Dict[str, str]]:
    ensure_csv_exists()
    with CSV_FILE.open("r", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return list(reader)
 
def write_all(rows: List[Dict[str, str]]):
    with CSV_FILE.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
 
def next_id(rows: List[Dict[str, str]]) -> int:
    if not rows:
        return 1
    return max(int(r["id"]) for r in rows) + 1
 
def valid_date(s: str) -> bool:
    try:
        datetime.strptime(s, "%d-%m-%Y")
        return True
    except Exception:
        return False
 
def input_date(prompt: str = "Enter date (DD-MM-YYYY): ") -> str:
    while True:
        d = input(prompt).strip()
        if valid_date(d):
            return d
        print("  Invalid date format. Use DD-MM-YYYY (e.g., 05-12-2025).")
 
def input_amount(prompt: str = "Enter amount: ") -> str:
    while True:
        a = input(prompt).strip()
        try:
            # allow integers or floats
            float(a)
            return a
        except Exception:
            print("  Invalid amount. Enter number like 120 or 99.50")
 
def input_nonempty(prompt: str) -> str:
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("  Value cannot be empty.")
 
# ---------- Core actions ----------
def add_expense():
    rows = read_all()
    eid = next_id(rows)
    date = input_date()
    amount = input_amount()
    category = input_nonempty("Enter category (Food/Travel/Bill/etc): ")
    note = input("Enter note (optional): ").strip()
 
    rows.append({"id": str(eid), "date": date, "amount": amount, "category": category, "note": note})
    write_all(rows)
    print(f"\n[OK] Expense added with ID {eid}\n")
 
def print_row(r: Dict[str, str]):
    print(f"ID: {r['id']:>3} | Date: {r['date']} | Amount: ₹{r['amount']} | Category: {r['category']} | Note: {r['note']}")
 
def view_expenses():
    rows = read_all()
    if not rows:
        print("\nNo expenses found.\n")
        return
    print("\n--- All Expenses ---")
    for r in rows:
        print_row(r)
    print()
 
def monthly_total():
    rows = read_all()
    month = input("Enter month (MM): ").strip().zfill(2)
    year = input("Enter year (YYYY): ").strip()
    if not (month.isdigit() and len(month) == 2 and year.isdigit() and len(year) == 4):
        print("Invalid month/year format.")
        return
    total = 0.0
    for r in rows:
        try:
            d = datetime.strptime(r["date"], "%d-%m-%Y")
            if d.strftime("%m") == month and d.strftime("%Y") == year:
                total += float(r["amount"])
        except Exception:
            continue
    print(f"\nTotal expenses for {month}-{year}: ₹{total:.2f}\n")
 
def category_summary():
    rows = read_all()
    if not rows:
        print("\nNo expenses found.\n")
        return
    summary: Dict[str, float] = {}
    for r in rows:
        cat = r["category"]
        amt = float(r["amount"])
        summary[cat] = summary.get(cat, 0.0) + amt
    print("\n--- Category Summary ---")
    for cat, amt in sorted(summary.items(), key=lambda x: -x[1]):
        print(f"{cat:20} : ₹{amt:.2f}")
    print()
 
def search_notes():
    q = input("Enter search keyword (searches notes): ").strip().lower()
    if not q:
        print("Empty keyword.")
        return
    rows = read_all()
    found = [r for r in rows if q in r.get("note", "").lower()]
    if not found:
        print("\nNo matching entries found.\n")
        return
    print(f"\nFound {len(found)} entries:")
    for r in found:
        print_row(r)
    print()
 
def delete_entry():
    rows = read_all()
    if not rows:
        print("\nNo expenses to delete.\n")
        return
    eid = input_nonempty("Enter ID to delete: ")
    new = [r for r in rows if r["id"] != eid]
    if len(new) == len(rows):
        print(f"No entry with ID {eid}")
    else:
        write_all(new)
        print(f"Deleted entry ID {eid}\n")
 
def edit_entry():
    rows = read_all()
    if not rows:
        print("\nNo expenses to edit.\n")
        return
    eid = input_nonempty("Enter ID to edit: ")
    for r in rows:
        if r["id"] == eid:
            print("Current entry:")
            print_row(r)
            print("Press Enter to keep current value.")
            d = input(f"Date [{r['date']}]: ").strip()
            if d:
                if valid_date(d):
                    r["date"] = d
                else:
                    print("Invalid date format. Skipping date change.")
            a = input(f"Amount [{r['amount']}]: ").strip()
            if a:
                try:
                    float(a)
                    r["amount"] = a
                except Exception:
                    print("Invalid amount. Skipping amount change.")
            cat = input(f"Category [{r['category']}]: ").strip()
            if cat:
                r["category"] = cat
            note = input(f"Note [{r['note']}]: ").strip()
            if note:
                r["note"] = note
            write_all(rows)
            print(f"Entry ID {eid} updated.\n")
            return
    print(f"No entry with ID {eid}\n")
 
# ---------- CLI ----------
def main():
    ensure_csv_exists()
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Total")
        print("4. Category Summary")
        print("5. Search Notes")
        print("6. Edit Entry (by ID)")
        print("7. Delete Entry (by ID)")
        print("8. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            search_notes()
        elif choice == "6":
            edit_entry()
        elif choice == "7":
            delete_entry()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
 
if __name__ == "__main__":
    main()
 