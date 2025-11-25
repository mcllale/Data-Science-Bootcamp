```
# Task Manager - Simple Console-Based Task Management System

A lightweight, file-based task management application written in Python, designed for small teams. It allows users to register, add tasks, assign tasks to team members, track progress, mark tasks as complete, and generate reports — all without requiring a database.

Perfect for learning file handling, user authentication, and basic menu-driven programs in Python.

---

### Features

- User registration (admin only)
- Login system with 3 attempt limit
- Add new tasks
- View all tasks
- View only your assigned tasks
- Mark tasks as complete
- Edit task assignee or due date (only if not completed)
- View completed tasks
- Delete tasks (admin only)
- Generate detailed statistics and reports
- Display statistics (admin only)
- Overdue task tracking
- Color-coded console output using `colorama`

---

### File Structure

```
- task_manager.py       Main program
- user.txt              Stores usernames and passwords
- tasks.txt             Stores all task details
- task_overview.txt     Generated automatically (task stats)
- user_overview.txt     Generated automatically (per-user stats)
- README.md             This file
```

> Note: `user.txt` and `tasks.txt` will be created automatically if they don't exist.

---

### Default Login (First Run)

When you run the program for the first time, it creates a default admin account:

```
Username: admin
Password: adm1n
```

Use these credentials to log in and register other users.

---

### Menu Options

#### Regular User Menu:
- `a`  – Add a task  
- `va` – View all tasks  
- `vm` – View my tasks  
- `e`  – Exit  

#### Admin Menu (extra options):
- `r`   – Register a new user  
- `vc`  – View completed tasks  
- `del` – Delete a task  
- `gr`  – Generate reports  
- `ds`  – Display statistics  

---

### Date Format

All dates must follow this format:  
**`DD Mon YYYY`**  
Example: `25 Oct 2025`, `01 Jan 2025`

---

### Reports Generated

After running `gr` (Generate Reports), two files are created:

1. **`task_overview.txt`**  
   Overall statistics: total tasks, completed, incomplete, overdue, percentages.

2. **`user_overview.txt`**  
   Per-user breakdown: tasks assigned, completion rate, overdue tasks, etc.

These are plain text files and can be viewed anytime.

---

### Requirements

- Python 3.6+
- `colorama` library

Install dependency:
```bash
pip install colorama
```

---

### How to Run

1. Save the code as `task_manager.py`
2. Open terminal/command prompt in the folder
3. Run:
```bash
python task_manager.py
```

4. Login with:
   - Username: `admin`
   - Password: `adm1n`

5. Start managing tasks!

---

### Security Note

This is a **learning project**. Passwords are stored in plain text in `user.txt`.  
Do **not** use this in production or with sensitive data.

---

### Author

Created as part of a Python programming curriculum.

Feel free to modify and improve!

---
```