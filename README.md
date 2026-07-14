# 🤖 TaskFlowAI

> An AI-Powered Smart Task Management System built with Flask and Google Gemini AI.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📌 Overview

TaskFlowAI is a modern AI-powered productivity web application developed during the **Synent Technologies Python Development Internship**.

It helps users organize tasks, analyze workloads using AI, generate intelligent task plans, and monitor productivity through an interactive dashboard.

---

## ✨ Features

### 🔐 Authentication
- User Registration
- Secure Login
- Logout
- Session Management

### 📋 Task Management
- Create Tasks
- Edit Tasks
- Delete Tasks
- Mark Tasks as Completed
- Search Tasks
- Filter Tasks
- Categories
- Priority Levels
- Due Dates

### 🤖 AI Features
- AI Task Analysis
- AI Planner
- Save AI Plans as Tasks
- AI Coach
- Floating AI Assistant (Gemini)

### 📊 Dashboard
- Task Statistics
- Completion Rate
- Productivity Analytics
- Category Charts
- Upcoming Deadlines
- AI Recommendations

### 🎨 UI Features
- Responsive Design
- Dark Mode
- Modern Dashboard
- Bootstrap 5 UI
- Loading Animation

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- SQLAlchemy
- Flask Login
- Flask WTF
- Flask Migrate

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

## Database

- SQLite

## AI

- Google Gemini API

---

# 📂 Project Structure

```
TaskFlowAI
│
├── app
│   ├── auth
│   ├── ai
│   ├── tasks
│   ├── static
│   │   ├── css
│   │   ├── js
│   │   └── images
│   ├── templates
│   └── models
│
├── migrations
├── instance
├── run.py
├── config.py
├── requirements.txt
├── Procfile
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Harsh746-bit/synent-task9-taskflowai-harshbhanarkar.git

cd synent-task9-taskflowai-harshbhanarkar
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key

GEMINI_MODEL=gemini-3.5-flash
```

---

## Initialize Database

```bash
flask db upgrade
```

---

## Run Project

```bash
python run.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

### Login

<img width="1915" height="885" alt="Screenshot 2026-07-13 135641" src="https://github.com/user-attachments/assets/6fbd2a0e-9f46-48a5-96e6-3cfef88017e1" />


---

### Dashboard

<img width="1918" height="907" alt="Screenshot 2026-07-13 140116" src="https://github.com/user-attachments/assets/d6507a97-1ae5-490c-892d-53035e0bb6b9" />

---



### AI Planner

<img width="1616" height="498" alt="image" src="https://github.com/user-attachments/assets/6213e2e3-e0fe-4b8f-b065-1d69e8751f5f" />


---

### AI Analysis

<img width="1898" height="918" alt="image" src="https://github.com/user-attachments/assets/cb4b4315-761f-43c4-a182-c99cb7c3fedb" />


# 📊 Database

## Users

| Field | Type |
|--------|------|
| id | Integer |
| username | String |
| email | String |
| password | String |

---

## Tasks

| Field | Type |
|--------|------|
| id | Integer |
| title | String |
| description | Text |
| category | String |
| priority | String |
| due_date | Date |
| status | String |
| user_id | Integer |

---

# 🤖 AI Modules

### AI Planner

Generates a complete execution roadmap for any goal.

### AI Task Analysis

Analyzes

- Difficulty
- Estimated Time
- Priority
- Deadline
- Subtasks
- Recommendations

### AI Coach

Provides productivity suggestions based on dashboard statistics.

---

# 📈 Future Enhancements

- Email Notifications
- Calendar Integration
- Team Collaboration
- PostgreSQL Support
- Mobile Application
- Voice Assistant
- Kanban Board
- Export Tasks to PDF

---

# 👨‍💻 Developer

**Harsh Bhanarkar**

GitHub

https://github.com/Harsh746-bit

---

# 🏢 Internship

Developed as part of the

**Synent Technologies Python Development Internship Program**

---

# 📜 License

This project is intended for educational and internship purposes.

---

⭐ If you like this project, consider giving it a star on GitHub!
