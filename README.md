# 🗂️ Task Manager — New Day

A task management system built with Django 4.1. This app allows users to create, assign, and track tasks with priority, tags, types, and completion status. Includes user management and analytics dashboard.

---

## 🚀 Features

- ✅ User authentication & roles
- ✅ Create/update/delete tasks
- ✅ Assign/unassign tasks
- ✅ Task types, tags, priorities
- ✅ Filtering & search (by name, tag, status, task type, priority)
- ✅ "Only my tasks" view
- ✅ Dashboard with stats & charts (Chart.js)
- ✅ Admin panel customization
- ✅ Bootstrap 5 styling

---

## 🏗️ Technologies Used

- Python 3.12
- Django 4.1
- SQLite (default)
- Bootstrap 5
- Chart.js
- Crispy Forms (`django-crispy-forms` + `crispy-bootstrap4`)
- Faker (for generating test data)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/task-manager-new-day.git
cd task-manager-new-day
```
### 2. Fill db

```bash
Get-Content .\populate_db.py | python manage.py shell  
```

## Demo
Home page
![demo.png](demo.png)

## Admin Credentials

To access the Django admin panel, use the following credentials:

- **Login**: `admin.user`  
- **Password**: `1qazcde3`

Admin panel is available at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
