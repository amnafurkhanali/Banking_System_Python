# Banking System — Python (GUI + MySQL)

A desktop banking application built with **Python (Tkinter)** for the GUI and **MySQL** for persistent data storage. Simulates core customer-facing banking operations through a graphical interface.

## Features

- **Login authentication** with password strength validation (requires a mix of uppercase, lowercase, numbers, and special characters)
- **Customer home dashboard** with navigation to account actions
- **New account creation**
- **Deposit and withdrawal** operations with balance updates
- **View current balance**
- **View last transaction / transaction history**
- **Delete account**
- Custom UI styling with hover effects on buttons

## Tech Stack

- **Python 3** — application logic
- **Tkinter** — GUI framework
- **MySQL** — relational database for account and transaction records (`mysql-connector-python`)

## Project Structure

```
Banking System-Python/
├── BANKING SYSTEM.py    # Main application (UI + logic)
├── Sql.txt              # Database schema and sample data
├── login.png, home.png, new.png, deposit.png,
│   withdraw.png, delete.png, last.png,
│   current balance.png  # UI assets
```

## Setup

1. Install dependencies:
   ```bash
   pip install mysql-connector-python
   ```
2. Create the database using the schema in `Sql.txt`:
   ```bash
   mysql -u root -p < Sql.txt
   ```
3. Set your MySQL connection details as environment variables (or update the connection config in the script) — 
4. Run the app:
   ```bash
   python "BANKING SYSTEM.py"
   ```


- This was built as an academic project to practice GUI development and integrating Python applications with a relational database.
- Sample account data in `Sql.txt` is placeholder/test data only.
